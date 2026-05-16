<template>
  <div class="auth-page">
    <div class="auth-card">
      <div class="auth-card__deco"></div>

      <h1 class="auth-card__title">{{ t('auth.forgotPassword') }}</h1>
      <div class="auth-card__deco-line"></div>

      <el-form
        :model="formData"
        :rules="rules"
        ref="forgotFormRef"
        class="auth-form"
        @keyup.enter="handleSubmit"
      >
        <el-form-item prop="phone">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.phone') }}</label>
            <input v-model="formData.phone" type="tel" class="auth-field__input" :placeholder="t('auth.placeholders.phone')" maxlength="11" />
          </div>
        </el-form-item>

        <el-form-item prop="captcha_code">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('profile.verificationCode') }}</label>
            <div class="captcha-row">
              <input v-model="formData.captcha_code" type="text" class="auth-field__input captcha-input" :placeholder="t('profile.enterCode')" maxlength="4" />
              <div class="captcha-image" @click="fetchCaptcha" :title="t('common.retry')">
                <img v-if="captchaImage" :src="captchaImage" alt="captcha" />
                <span v-else class="captcha-loading">...</span>
              </div>
            </div>
          </div>
        </el-form-item>

        <el-form-item prop="new_password">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.newPassword') }}</label>
            <input v-model="formData.new_password" :type="showPassword ? 'text' : 'password'" class="auth-field__input" :placeholder="t('auth.placeholders.newPassword')" />
            <button type="button" class="auth-field__toggle" @click="showPassword = !showPassword">
              {{ showPassword ? t('auth.hide') : t('auth.show') }}
            </button>
          </div>
        </el-form-item>

        <el-form-item prop="confirm_password">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.confirmPassword') }}</label>
            <input v-model="formData.confirm_password" :type="showPassword ? 'text' : 'password'" class="auth-field__input" :placeholder="t('auth.placeholders.confirmPassword')" />
          </div>
        </el-form-item>

        <div v-if="formData.new_password.length > 0" class="password-hint">
          <span v-if="isPasswordValid(formData.new_password)" class="password-hint--valid">✓ {{ t('auth.passwordValid') }}</span>
          <span v-else class="password-hint--invalid">✗ {{ t('auth.passwordHint') }}</span>
          <span v-if="formData.confirm_password && formData.new_password !== formData.confirm_password" class="password-hint--invalid">✗ {{ t('auth.passwordMismatch') }}</span>
        </div>

        <ArchiveButton variant="primary" fullWidth :loading="loading" @click="handleSubmit">
          {{ t('common.submit') }}
        </ArchiveButton>
      </el-form>

      <div class="auth-footer">
        <router-link to="/login" class="auth-footer__link">← {{ t('nav.login') }}</router-link>
      </div>

      <div class="auth-card__deco"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { ElMessage } from 'element-plus'
import api from '@/utils/axios'
import ArchiveButton from '@/components/ArchiveButton.vue'

const { t } = useI18n()
const router = useRouter()
const forgotFormRef = ref()
const showPassword = ref(false)
const loading = ref(false)
const captchaImage = ref('')
const captchaKey = ref('')

const formData = reactive({
  phone: '',
  captcha_code: '',
  new_password: '',
  confirm_password: '',
})

const rules = {
  phone: [
    { required: true, message: () => t('auth.placeholders.phone'), trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: () => t('auth.placeholders.phone'), trigger: 'blur' },
  ],
  captcha_code: [{ required: true, message: () => t('profile.enterCode'), trigger: 'blur' }],
  new_password: [{ required: true, message: () => t('auth.placeholders.newPassword'), trigger: 'blur' }],
  confirm_password: [{ required: true, message: () => t('auth.placeholders.confirmPassword'), trigger: 'blur' }],
}

function isPasswordValid(p: string): boolean {
  return p.length >= 8 && /[A-Z]/.test(p) && /[a-z]/.test(p) && /[0-9]/.test(p)
}

async function fetchCaptcha() {
  try {
    const res = await api.get('/api/users/captcha/')
    captchaImage.value = res.data.captcha_image
    captchaKey.value = res.data.captcha_key
  } catch {
    // handled by interceptor
  }
}

async function handleSubmit() {
  if (!forgotFormRef.value) return
  try {
    await forgotFormRef.value.validate()
    if (!isPasswordValid(formData.new_password)) {
      ElMessage.error(t('auth.passwordHint'))
      return
    }
    if (formData.new_password !== formData.confirm_password) {
      ElMessage.error(t('auth.passwordMismatch'))
      return
    }

    loading.value = true
    await api.post('/api/users/forgot-password/', {
      phone: formData.phone,
      captcha_key: captchaKey.value,
      captcha_code: formData.captcha_code,
      new_password: formData.new_password,
      confirm_password: formData.confirm_password,
    })
    ElMessage.success(t('errors.passwordChangeSuccess'))
    setTimeout(() => router.push('/login'), 1000)
  } catch (err: any) {
    if (err.message?.includes('validation failed')) return
    fetchCaptcha()
    const msg = err.response?.data?.message
    if (msg) ElMessage.error(msg)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchCaptcha()
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
  padding: var(--space-8);
  box-shadow: var(--shadow-inset);
}

.auth-card__deco {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
  opacity: 0.3;
}

.auth-card__deco-line {
  width: 48px;
  height: 2px;
  background: var(--accent-gold);
  margin: 0 auto var(--space-6);
}

.auth-card__title {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--text-primary);
  text-align: center;
  margin: var(--space-4) 0 var(--space-2);
}

.auth-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  position: relative;
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

.auth-field__input::placeholder { color: var(--text-muted); }
.auth-field__input:focus { border-bottom-color: var(--accent-gold); border-bottom-width: 2px; }

.auth-field__toggle {
  position: absolute;
  right: 0;
  bottom: var(--space-2);
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: var(--text-xs);
  cursor: pointer;
}

.auth-field__toggle:hover { color: var(--accent-gold); }

/* Captcha */
.captcha-row {
  display: flex;
  align-items: flex-end;
  gap: var(--space-3);
}

.captcha-input {
  flex: 1;
}

.captcha-image {
  flex-shrink: 0;
  height: 36px;
  cursor: pointer;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  overflow: hidden;
  transition: border-color var(--duration-fast);
}

.captcha-image:hover {
  border-color: var(--accent-gold);
}

.captcha-image img {
  height: 100%;
  width: auto;
  display: block;
}

.captcha-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 36px;
  font-size: var(--text-sm);
  color: var(--text-muted);
}

.password-hint {
  margin: var(--space-3) 0 var(--space-4);
  font-size: var(--text-xs);
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.password-hint--valid { color: var(--accent-verdigris); }
.password-hint--invalid { color: var(--accent-red); }

.auth-footer {
  margin-top: var(--space-6);
  text-align: center;
}

.auth-footer__link {
  font-size: var(--text-sm);
  color: var(--accent-copper);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.auth-footer__link:hover { color: var(--accent-gold); }

:deep(.el-form-item) { margin-bottom: var(--space-4); }
:deep(.el-form-item__error) { color: var(--accent-red); font-size: var(--text-xs); padding-top: var(--space-1); }

@media (max-width: 480px) {
  .auth-card { padding: var(--space-6) var(--space-4); }
  .auth-card__title { font-size: var(--text-2xl); }
}
</style>
