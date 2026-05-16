<template>
  <div class="profile-page">
    <div class="container-narrow">
      <div class="profile-header">
        <div class="profile-avatar">{{ (auth.userName || '?')[0] }}</div>
        <div>
          <h1 class="profile-header__title">{{ auth.userName || t('profile.user') }}</h1>
          <span class="profile-header__role">{{ auth.userRole === 'admin' ? t('profile.admin') : t('profile.normalUser') }}</span>
        </div>
      </div>

      <BronzeDivider />

      <div class="info-dl">
        <template v-for="item in infoItems" :key="item.label">
          <dt>{{ item.label }}</dt>
          <dd>
            <span v-if="item.value">{{ item.value }}</span>
            <span v-else class="info-dl__empty">
              {{ t('profile.notSet') }}
              <button v-if="item.action" class="info-dl__action" @click="item.action">{{ item.actionText }}</button>
            </span>
          </dd>
        </template>
      </div>

      <BronzeDivider />

      <div class="profile-actions">
        <ArchiveButton variant="secondary" @click="$router.push('/change-password')">{{ t('profile.changePassword') }}</ArchiveButton>
        <ArchiveButton variant="danger" @click="handleLogout">{{ t('profile.logout') }}</ArchiveButton>
      </div>

      <!-- Email binding dialog -->
      <el-dialog v-model="showEmailDialog" :title="t('profile.bindEmail')" width="90%" style="max-width:400px" :append-to-body="true">
        <el-form :model="emailForm" label-position="top">
          <el-form-item :label="t('profile.emailAddress')">
            <el-input v-model="emailForm.email" :placeholder="t('profile.enterEmail')" />
          </el-form-item>
          <el-form-item :label="t('profile.verificationCode')">
            <div style="display:flex;gap:8px">
              <el-input v-model="emailForm.code" :placeholder="t('profile.enterCode')" />
              <el-button @click="sendCode" :disabled="codeCooldown > 0">
                {{ codeCooldown > 0 ? `${codeCooldown}s` : t('profile.sendVerificationCode') }}
              </el-button>
            </div>
          </el-form-item>
        </el-form>
        <template #footer>
          <ArchiveButton variant="ghost" @click="showEmailDialog = false">{{ t('common.cancel') }}</ArchiveButton>
          <ArchiveButton variant="primary" @click="bindEmail">{{ t('profile.confirmBind') }}</ArchiveButton>
        </template>
      </el-dialog>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '@/stores/auth'
import { ElMessage } from 'element-plus'
import api from '@/utils/axios'
import ArchiveButton from '@/components/ArchiveButton.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'

const router = useRouter()
const auth = useAuthStore()
const { t, locale } = useI18n()

const showEmailDialog = ref(false)
const codeCooldown = ref(0)
let cooldownTimer: ReturnType<typeof setInterval> | null = null

const emailForm = reactive({ email: '', code: '' })

const infoItems = computed(() => [
  { label: t('profile.username'), value: auth.user?.username },
  { label: t('profile.phone'), value: auth.user?.phone },
  { label: t('profile.email'), value: auth.user?.email, action: !auth.user?.email ? openEmailDialog : undefined, actionText: t('profile.bindNow') },
  { label: t('profile.registrationDate'), value: auth.user?.date_joined ? new Date(auth.user.date_joined).toLocaleDateString(locale.value === 'zh' ? 'zh-CN' : 'en-US') : undefined },
])

function openEmailDialog() {
  showEmailDialog.value = true
}

async function sendCode() {
  if (!emailForm.email) { ElMessage.warning(t('profile.enterEmail')); return }
  try {
    await api.post('/api/users/send-code/', { email: emailForm.email })
    ElMessage.success(t('profile.verificationCodeSent'))
    codeCooldown.value = 60
    cooldownTimer = setInterval(() => {
      codeCooldown.value--
      if (codeCooldown.value <= 0 && cooldownTimer) { clearInterval(cooldownTimer); cooldownTimer = null }
    }, 1000)
  } catch (err: any) {
    ElMessage.error(err.response?.data?.message || t('errors.serverError'))
  }
}

async function bindEmail() {
  try {
    await api.post('/api/users/bind-email/', emailForm)
    ElMessage.success(t('profile.emailBindSuccess'))
    showEmailDialog.value = false
    await auth.fetchUserInfo()
  } catch (err: any) {
    ElMessage.error(err.response?.data?.message || t('errors.failed'))
  }
}

function handleLogout() {
  auth.logout()
}

onMounted(() => {
  auth.initFromStorage()
  auth.fetchUserInfo()
})
</script>

<style scoped>
.profile-page {
  padding: var(--space-8) 0 var(--space-16);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  margin-bottom: var(--space-4);
}

.profile-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  border: 2px solid var(--accent-gold);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 700;
  color: var(--accent-gold);
  background: var(--bg-surface);
}

.profile-header__title {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 700;
  color: var(--text-primary);
}

.profile-header__role {
  font-size: var(--text-sm);
  color: var(--text-muted);
}

.info-dl {
  display: grid;
  grid-template-columns: 100px 1fr;
  gap: var(--space-3) var(--space-6);
  padding: var(--space-4) 0;
}

.info-dl dt {
  font-size: var(--text-sm);
  color: var(--text-muted);
  white-space: nowrap;
}

.info-dl dd {
  font-size: var(--text-base);
  color: var(--text-primary);
}

.info-dl__empty {
  color: var(--text-muted);
  font-style: italic;
}

.info-dl__action {
  background: none;
  border: none;
  color: var(--accent-gold);
  font-size: var(--text-sm);
  cursor: pointer;
  margin-left: var(--space-2);
}

.info-dl__action:hover {
  color: var(--accent-gold-light);
}

.profile-actions {
  display: flex;
  gap: var(--space-4);
}

@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
  }

  .profile-actions {
    flex-direction: column;
  }

  .info-dl {
    grid-template-columns: 1fr;
    gap: var(--space-2);
  }
}
</style>
