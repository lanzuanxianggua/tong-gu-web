<template>
  <div class="auth-page">
    <div class="auth-card">
      <!-- Decorative top line -->
      <div class="auth-card__deco"></div>

      <h1 class="auth-card__title">{{ t('auth.login') }}</h1>
      <div class="auth-card__deco-line"></div>

      <el-form
        :model="formData"
        :rules="rules"
        ref="loginFormRef"
        class="auth-form"
        @keyup.enter="handleSubmit"
      >
        <el-form-item prop="username">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.username') }}</label>
            <input
              v-model="formData.username"
              type="text"
              class="auth-field__input"
              :placeholder="t('auth.placeholders.username')"
            />
          </div>
        </el-form-item>

        <el-form-item prop="password">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.password') }}</label>
            <div class="auth-field__password">
              <input
                v-model="formData.password"
                :type="showPassword ? 'text' : 'password'"
                class="auth-field__input"
                :placeholder="t('auth.placeholders.password')"
              />
              <button type="button" class="auth-field__toggle" @click="showPassword = !showPassword">
                {{ showPassword ? t('auth.hide') : t('auth.show') }}
              </button>
            </div>
          </div>
        </el-form-item>

        <div class="auth-options">
          <label class="auth-remember" @click="rememberMe = !rememberMe">
            <span class="auth-remember__box" :class="{ active: rememberMe }"></span>
            <span>{{ t('auth.rememberMe') }}</span>
          </label>
          <router-link to="/forgot-password" class="auth-forgot">{{ t('auth.forgotPasswordLink') }}</router-link>
        </div>

        <div class="auth-terms">
          <label class="auth-terms__label" @click.prevent="toggleTermsAgree">
            <span class="auth-terms__checkbox" :class="{ checked: agreedToTerms }">
              <span v-if="agreedToTerms" class="auth-terms__check">&#10003;</span>
            </span>
            <span class="auth-terms__text">
              {{ t('auth.agreeTerms') }}
              <a class="auth-terms__link" @click.stop="showTermsDialog">{{ t('auth.userTerms') }}</a>
            </span>
          </label>
          <p v-if="termsWarning" class="auth-terms__warning">{{ t('auth.agreeTerms') }}</p>
        </div>

        <ArchiveButton
          variant="primary"
          fullWidth
          :loading="loading"
          @click="handleSubmit"
        >
          {{ t('auth.enterPlatform') }}
        </ArchiveButton>
      </el-form>

      <div class="auth-footer">
        <span>{{ t('auth.noAccount') }}</span>
        <router-link to="/register" class="auth-footer__link">{{ t('auth.registerNow') }}</router-link>
      </div>

      <!-- Decorative bottom line -->
      <div class="auth-card__deco"></div>
    </div>

    <TermsDialog ref="termsDialogRef" @confirm="onTermsConfirm" />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { ElMessage } from 'element-plus'
import { useAuthStore } from '@/stores/auth'
import ArchiveButton from '@/components/ArchiveButton.vue'
import TermsDialog from '@/components/TermsDialog.vue'

const { t } = useI18n()
const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const loginFormRef = ref()
const termsDialogRef = ref()
const showPassword = ref(false)
const rememberMe = ref(false)
const agreedToTerms = ref(false)
const termsWarning = ref(false)
const loading = ref(false)

const formData = reactive({
  username: '',
  password: '',
})

const rules = {
  username: [{ required: true, message: () => t('auth.placeholders.username'), trigger: 'blur' }],
  password: [{ required: true, message: () => t('auth.placeholders.password'), trigger: 'blur' }],
}

function toggleTermsAgree() {
  agreedToTerms.value = !agreedToTerms.value
  if (agreedToTerms.value) termsWarning.value = false
}

function showTermsDialog() {
  termsDialogRef.value?.open()
}

function onTermsConfirm() {
  agreedToTerms.value = true
}

async function handleSubmit() {
  if (!loginFormRef.value) return

  if (!agreedToTerms.value) {
    termsWarning.value = true
    return
  }

  try {
    await loginFormRef.value.validate()
  } catch {
    return
  }

  loading.value = true
  try {
    const ok = await auth.login(formData.username, formData.password)
    if (ok) {
      if (rememberMe.value) {
        localStorage.setItem('remembered_username', formData.username)
      } else {
        localStorage.removeItem('remembered_username')
      }
      const redirect = (route.query.redirect as string) || '/'
      router.push(redirect)
    }
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  const remembered = localStorage.getItem('remembered_username')
  if (remembered) {
    formData.username = remembered
    rememberMe.value = true
  }
})
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-6);
}

.auth-card {
  width: 100%;
  max-width: 420px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: var(--space-8) var(--space-6);
  box-shadow: var(--shadow-elevated);
}

.auth-card__title {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--text-primary);
  text-align: center;
  margin-bottom: var(--space-2);
}

.auth-card__deco {
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--border-gold), transparent);
  margin: var(--space-4) 0;
}

.auth-card__deco-line {
  width: 48px;
  height: 2px;
  background: var(--accent-gold);
  margin: 0 auto var(--space-6);
}

/* Fields */
.auth-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  width: 100%;
}

.auth-field__label {
  font-size: var(--text-sm);
  color: var(--text-muted);
  font-weight: 500;
}

.auth-field__input {
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: var(--text-base);
  padding: var(--space-2) 0;
  outline: none;
  width: 100%;
  transition: border-color var(--duration-fast);
}

.auth-field__input::placeholder {
  color: var(--text-muted);
}

.auth-field__input:focus {
  border-bottom-color: var(--accent-gold);
  border-bottom-width: 2px;
}

.auth-field__password {
  position: relative;
}

.auth-field__password .auth-field__input {
  width: 100%;
  padding-right: 48px;
}

.auth-field__toggle {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: var(--text-xs);
  cursor: pointer;
  padding: var(--space-1);
}

.auth-field__toggle:hover {
  color: var(--accent-gold);
}

/* Options */
.auth-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: var(--space-4) 0 var(--space-3);
}

.auth-remember {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  cursor: pointer;
}

.auth-remember__box {
  width: 16px;
  height: 16px;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  transition: all var(--duration-fast);
}

.auth-remember__box.active {
  border-color: var(--accent-gold);
  background: var(--accent-gold);
}

.auth-forgot {
  font-size: var(--text-sm);
  color: var(--accent-copper);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.auth-forgot:hover {
  color: var(--accent-gold);
}

/* Terms */
.auth-terms {
  margin-bottom: var(--space-5);
}

.auth-terms__label {
  display: flex;
  align-items: flex-start;
  gap: var(--space-2);
  cursor: pointer;
  user-select: none;
}

.auth-terms__checkbox {
  width: 16px;
  height: 16px;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--duration-fast);
  flex-shrink: 0;
  margin-top: 2px;
}

.auth-terms__checkbox.checked {
  border-color: var(--accent-gold);
  background: var(--accent-gold);
}

.auth-terms__check {
  font-size: 10px;
  color: var(--text-on-accent);
  font-weight: 700;
}

.auth-terms__text {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.4;
}

.auth-terms__link {
  color: var(--accent-gold);
  text-decoration: none;
  font-weight: 600;
  cursor: pointer;
}

.auth-terms__link:hover {
  color: var(--accent-gold-light);
  text-decoration: underline;
}

.auth-terms__warning {
  margin-top: var(--space-1);
  font-size: var(--text-xs);
  color: var(--accent-red);
  padding-left: calc(16px + var(--space-2));
}

/* Footer */
.auth-footer {
  margin-top: var(--space-6);
  text-align: center;
  font-size: var(--text-sm);
  color: var(--text-muted);
}

.auth-footer__link {
  color: var(--accent-gold);
  text-decoration: none;
  font-weight: 600;
  margin-left: var(--space-1);
}

.auth-footer__link:hover {
  color: var(--accent-gold-light);
}

/* Element Plus overrides */
:deep(.el-form-item) {
  margin-bottom: var(--space-4);
}

:deep(.el-form-item__error) {
  color: var(--accent-red);
  font-size: var(--text-xs);
  padding-top: var(--space-1);
}

@media (max-width: 480px) {
  .auth-card {
    padding: var(--space-6) var(--space-4);
  }

  .auth-card__title {
    font-size: var(--text-2xl);
  }
}
</style>
