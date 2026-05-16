<template>
  <div class="auth-page">
    <div class="auth-card">
      <div class="auth-card__deco"></div>

      <h1 class="auth-card__title">{{ t('auth.register') }}</h1>
      <div class="auth-card__deco-line"></div>

      <el-form
        :model="formData"
        :rules="rules"
        ref="registerFormRef"
        class="auth-form"
        @keyup.enter="handleSubmit"
      >
        <el-form-item prop="username">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.username') }}</label>
            <input v-model="formData.username" type="text" class="auth-field__input" :placeholder="t('auth.placeholders.username')" />
          </div>
        </el-form-item>

        <el-form-item prop="phone">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.phone') }}</label>
            <input v-model="formData.phone" type="tel" class="auth-field__input" :placeholder="t('auth.placeholders.phone')" maxlength="11" />
          </div>
        </el-form-item>

        <el-form-item prop="email">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.placeholders.emailOptional') }}</label>
            <input v-model="formData.email" type="email" class="auth-field__input" :placeholder="t('auth.placeholders.email')" />
          </div>
        </el-form-item>

        <el-form-item prop="password">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.password') }}</label>
            <input v-model="formData.password" :type="showPassword ? 'text' : 'password'" class="auth-field__input" :placeholder="t('auth.placeholders.password')" />
          </div>
        </el-form-item>

        <el-form-item prop="password_confirm">
          <div class="auth-field">
            <label class="auth-field__label">{{ t('auth.confirmPassword') }}</label>
            <input v-model="formData.password_confirm" :type="showPassword ? 'text' : 'password'" class="auth-field__input" :placeholder="t('auth.placeholders.confirmPassword')" />
          </div>
        </el-form-item>

        <!-- Password strength -->
        <div v-if="formData.password.length > 0" class="password-strength">
          <div class="password-strength__bar">
            <div class="password-strength__fill" :style="{ width: strengthPercent + '%' }" :class="strengthClass"></div>
          </div>
          <div class="password-strength__checks">
            <span :class="{ met: formData.password.length >= 8 }">{{ formData.password.length >= 8 ? '✓' : '✗' }} {{ t('auth.passwordStrength.atLeast8') }}</span>
            <span :class="{ met: hasUpper }">{{ hasUpper ? '✓' : '✗' }} {{ t('auth.passwordStrength.uppercase') }}</span>
            <span :class="{ met: hasLower }">{{ hasLower ? '✓' : '✗' }} {{ t('auth.passwordStrength.lowercase') }}</span>
            <span :class="{ met: hasDigit }">{{ hasDigit ? '✓' : '✗' }} {{ t('auth.passwordStrength.digit') }}</span>
          </div>
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

        <ArchiveButton variant="primary" fullWidth :loading="loading" @click="handleSubmit">
          {{ t('auth.register') }}
        </ArchiveButton>
      </el-form>

      <div class="auth-footer">
        <span>{{ t('auth.hasAccount') }}</span>
        <router-link to="/login" class="auth-footer__link">{{ t('auth.loginNow') }}</router-link>
      </div>

      <div class="auth-card__deco"></div>
    </div>

    <TermsDialog ref="termsDialogRef" @confirm="onTermsConfirm" />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { ElMessage } from 'element-plus'
import api from '@/utils/axios'
import ArchiveButton from '@/components/ArchiveButton.vue'
import TermsDialog from '@/components/TermsDialog.vue'

const { t } = useI18n()
const router = useRouter()
const registerFormRef = ref()
const termsDialogRef = ref()
const showPassword = ref(false)
const agreedToTerms = ref(false)
const termsWarning = ref(false)
const loading = ref(false)

const formData = reactive({
  username: '',
  email: '',
  phone: '',
  password: '',
  password_confirm: '',
})

const hasUpper = computed(() => /[A-Z]/.test(formData.password))
const hasLower = computed(() => /[a-z]/.test(formData.password))
const hasDigit = computed(() => /\d/.test(formData.password))
const strengthPercent = computed(() => {
  let s = 0
  if (formData.password.length >= 8) s += 25
  if (hasUpper.value) s += 25
  if (hasLower.value) s += 25
  if (hasDigit.value) s += 25
  return s
})
const strengthClass = computed(() => {
  if (strengthPercent.value <= 25) return 'weak'
  if (strengthPercent.value <= 50) return 'fair'
  if (strengthPercent.value <= 75) return 'good'
  return 'strong'
})

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

const validatePass = (_rule: any, value: string, callback: Function) => {
  if (!value) { callback(new Error(t('auth.passwordStrength.atLeast8'))); return }
  if (value.length < 8) { callback(new Error(t('auth.passwordStrength.atLeast8'))); return }
  if (!/[A-Z]/.test(value)) { callback(new Error(t('auth.passwordStrength.uppercase'))); return }
  if (!/[a-z]/.test(value)) { callback(new Error(t('auth.passwordStrength.lowercase'))); return }
  if (!/\d/.test(value)) { callback(new Error(t('auth.passwordStrength.digit'))); return }
  callback()
}

const validatePass2 = (_rule: any, value: string, callback: Function) => {
  if (value !== formData.password) { callback(new Error(t('auth.passwordMismatch'))); return }
  callback()
}

const rules = {
  username: [
    { required: true, message: () => t('auth.username'), trigger: 'blur' },
    { min: 3, message: () => t('auth.placeholders.username'), trigger: 'blur' },
  ],
  phone: [
    { required: true, message: () => t('auth.phone'), trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: () => t('auth.placeholders.phone'), trigger: 'blur' },
  ],
  email: [{ type: 'email' as const, message: () => t('auth.placeholders.email'), trigger: 'blur' }],
  password: [
    { required: true, message: () => t('auth.password'), trigger: 'blur' },
    { validator: validatePass, trigger: 'blur' },
  ],
  password_confirm: [
    { required: true, message: () => t('auth.confirmPassword'), trigger: 'blur' },
    { validator: validatePass2, trigger: 'blur' },
  ],
}

async function handleSubmit() {
  if (!registerFormRef.value) return

  if (!agreedToTerms.value) {
    termsWarning.value = true
    return
  }

  try {
    await registerFormRef.value.validate()
  } catch {
    return
  }

  loading.value = true
  try {
    await api.post('/api/users/register/', formData)
    ElMessage.success(t('auth.registerSuccess'))
    router.push('/login')
  } catch (err: any) {
    // error handled by interceptor
  } finally {
    loading.value = false
  }
}
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
  padding: var(--space-8) var(--space-8);
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
  letter-spacing: 0.5em;
}

.auth-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
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

.auth-field__input:focus {
  border-bottom-color: var(--accent-gold);
  border-bottom-width: 2px;
}

/* Password strength */
.password-strength {
  margin: var(--space-3) 0 var(--space-4);
}

.password-strength__bar {
  height: 3px;
  background: var(--bg-hover);
  border-radius: 2px;
  overflow: hidden;
}

.password-strength__fill {
  height: 100%;
  border-radius: 2px;
  transition: width var(--duration-normal), background var(--duration-normal);
}

.password-strength__fill.weak { background: var(--accent-red); }
.password-strength__fill.fair { background: var(--accent-copper); }
.password-strength__fill.good { background: var(--accent-gold); }
.password-strength__fill.strong { background: var(--accent-verdigris); }

.password-strength__checks {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2) var(--space-4);
  margin-top: var(--space-2);
  font-size: var(--text-xs);
  color: var(--accent-red);
}

.password-strength__checks .met {
  color: var(--accent-verdigris);
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

.auth-footer {
  margin-top: var(--space-6);
  text-align: center;
  font-size: var(--text-sm);
  color: var(--text-muted);
}

.auth-footer__link {
  color: var(--accent-copper);
  text-decoration: none;
  font-weight: 600;
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
