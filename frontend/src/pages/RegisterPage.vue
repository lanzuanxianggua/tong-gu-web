<template>
  <div class="login-page">
    <!-- 动态背景 -->
    <div class="animated-bg">
      <div class="bg-image"></div>
      <div class="gradient-sphere sphere-1"></div>
      <div class="gradient-sphere sphere-2"></div>
      <div class="gradient-sphere sphere-3"></div>
    </div>

    <!-- 返回登录按钮 -->
    <div class="back-home-btn">
      <div class="btn-glass" @click="handleBackLogin">
        <div class="btn-glass-shadow"></div>
        <div class="btn-glass-backdrop"></div>
        <div class="btn-glass-content">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
          <span>返回登录</span>
        </div>
      </div>
    </div>

    <!-- 主容器 -->
    <div class="login-container">      
      <!-- 内容区 -->
      <div class="content-wrapper">
        <!-- 头部 -->
        <div class="login-header">
          <h1 class="title">
            <span class="title-glow">注册</span>
          </h1>
        </div>

        <!-- 注册表单 -->
        <el-form
          :model="formData"
          :rules="rules"
          ref="registerFormRef"
          class="login-form"
          @keyup.enter="handleSubmit"
        >
          <!-- 用户名输入 -->
          <div class="input-group">
            <div class="input-icon">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <el-input
              v-model="formData.username"
              placeholder="请输入用户名"
              class="game-input"
            />
          </div>

          <!-- 手机号输入 -->
          <div class="input-group">
            <div class="input-icon">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
            </div>
            <el-input
              v-model="formData.phone"
              placeholder="请输入手机号"
              maxlength="11"
              class="game-input"
            />
          </div>

          <!-- 邮箱输入 -->
          <div class="input-group">
            <div class="input-icon">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
            </div>
            <el-input
              v-model="formData.email"
              placeholder="请输入邮箱地址（可选）"
              class="game-input"
            />
          </div>

          <!-- 密码输入 -->
          <div class="input-group">
            <div class="input-icon">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
            </div>
            <el-input
              v-model="formData.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="请输入密码"
              class="game-input"
            />
            <button 
              type="button" 
              class="toggle-password"
              @click="showPassword = !showPassword"
            >
              <svg v-if="!showPassword" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                <circle cx="12" cy="12" r="3"></circle>
              </svg>
              <svg v-else viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                <line x1="1" y1="1" x2="23" y2="23"></line>
              </svg>
            </button>
          </div>

          <!-- 确认密码输入 -->
          <div class="input-group">
            <div class="input-icon">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
            </div>
            <el-input
              v-model="formData.password_confirm"
              :type="showPassword ? 'text' : 'password'"
              placeholder="请再次输入密码"
              class="game-input"
            />
          </div>

          <!-- 密码要求 -->
          <div v-if="formData.password.length > 0" class="password-requirements">
            <p>密码要求：</p>
            <ul>
              <li v-if="passwordStrength.length < 8" class="invalid">✗ 至少 8 个字符</li>
              <li v-if="!hasUppercase" class="invalid">✗ 包含大写字母</li>
              <li v-if="!hasLowercase" class="invalid">✗ 包含小写字母</li>
              <li v-if="!hasNumber" class="invalid">✗ 包含数字</li>
              <li v-if="passwordStrength.length >= 8 && hasUppercase && hasLowercase && hasNumber" class="valid">✓ 密码强度符合要求</li>
            </ul>
          </div>

          <!-- 注册按钮 -->
          <div class="btn-glass login-btn" @click="handleSubmit" :class="{ loading: isLoading, success: isSuccess }" :disabled="isLoading">
            <div class="btn-glass-shadow"></div>
            <div class="btn-glass-backdrop"></div>
            <div class="btn-glass-content">
              <span v-if="isSuccess" class="success-icon">✓</span>
              <span v-else-if="isLoading" class="loading-spinner"></span>
              <span v-else>注册</span>
            </div>
          </div>
        </el-form>

        <!-- 登录链接 -->
        <div class="register-section">
          <span class="register-text">已有账号？</span>
          <button class="register-btn" @click="handleBackLogin">
            立即登录
          </button>
        </div>
      </div>
    </div>
    
    <!-- SVG Filter Definition -->
    <svg class="svg-filters" aria-hidden="true">
      <defs>
        <filter
          id="container-glass"
          x="0%"
          y="0%"
          width="100%"
          height="100%"
          color-interpolation-filters="sRGB"
        >
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.05 0.05"
            numOctaves="1"
            seed="1"
            result="turbulence"
          />
          <feGaussianBlur in="turbulence" stdDeviation="2" result="blurredNoise" />
          <feDisplacementMap
            in="SourceGraphic"
            in2="blurredNoise"
            scale="70"
            xChannelSelector="R"
            yChannelSelector="B"
            result="displaced"
          />
          <feGaussianBlur in="displaced" stdDeviation="4" result="finalBlur" />
          <feComposite in="finalBlur" in2="finalBlur" operator="over" />
        </filter>
      </defs>
    </svg>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from 'element-plus'
import api from "../utils/axios";

const router = useRouter();
const registerFormRef = ref(null);
const isLoading = ref(false);
const isSuccess = ref(false);
const showPassword = ref(false);

const formData = reactive({
  username: "",
  email: "",
  phone: "",
  password: "",
  password_confirm: "",
});

// 密码强度检查
const passwordStrength = computed(() => formData.password);
const hasUppercase = computed(() => /[A-Z]/.test(formData.password));
const hasLowercase = computed(() => /[a-z]/.test(formData.password));
const hasNumber = computed(() => /\d/.test(formData.password));

const validatePass2 = (rule, value, callback) => {
  if (value !== formData.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

const validatePassword = (rule, value, callback) => {
  if (!value) {
    callback(new Error('密码不能为空'))
    return
  }
  
  if (value.length < 8) {
    callback(new Error('密码长度至少为 8 位'))
    return
  }
  
  if (!/[A-Z]/.test(value)) {
    callback(new Error('密码必须包含至少一个大写字母'))
    return
  }
  
  if (!/[a-z]/.test(value)) {
    callback(new Error('密码必须包含至少一个小写字母'))
    return
  }
  
  if (!/\d/.test(value)) {
    callback(new Error('密码必须包含至少一个数字'))
    return
  }
  
  // 检查是否与用户名太相似
  if (formData.username && (value.toLowerCase().includes(formData.username.toLowerCase()) || formData.username.toLowerCase().includes(value.toLowerCase()))) {
    callback(new Error('密码不能与用户名太相似'))
    return
  }
  
  callback()
}

const rules = {
  username: [
    { required: true, message: '用户名不能为空', trigger: 'blur' },
    { min: 3, message: '用户名至少需要 3 个字符', trigger: 'blur' }
  ],
  phone: [
    { required: true, message: '手机号不能为空', trigger: 'blur' },
    { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
  ],
  email: [
    { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '密码不能为空', trigger: 'blur' },
    { validator: validatePassword, trigger: 'blur' }
  ],
  password_confirm: [
    { required: true, message: '请确认密码', trigger: 'blur' },
    { validator: validatePass2, trigger: 'blur' }
  ]
}

const handleSubmit = async () => {
  if (!registerFormRef.value) return

  await registerFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        isLoading.value = true;
        
        // 模拟加载动画
        await new Promise(resolve => setTimeout(resolve, 800));
        
        const response = await api.post("/api/users/register/", formData);

        if (response.status === 201) {
          // 显示成功动画
          isSuccess.value = true;
          ElMessage.success("注册成功，请登录！");
          
          // 延迟跳转
          setTimeout(() => {
            router.push("/login");
          }, 1000);
        }
      } catch (error) {
        isSuccess.value = false;
        const errorMsg = error.response?.data?.message || error.message;
        const errorsObj = error.response?.data?.errors || {};
        const errorDetails = Object.values(errorsObj).join(" ");
        ElMessage.error("注册失败：" + errorMsg + " " + errorDetails);
      } finally {
        isLoading.value = false;
      }
    }
  })
}

// 返回登录
const handleBackLogin = () => {
  router.push("/login");
};
</script>

<style scoped>
/* 基础重置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 页面容器 */
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  position: relative;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #0a0a0f;
}

/* 动态背景 */
.animated-bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

/* 背景图片 */
.bg-image {
  position: fixed;
  inset: 0;
  background-image: url('@/assets/tonggu07.png');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0;
  opacity: 0.5;
}

.gradient-sphere {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.5;
  animation: float 20s infinite ease-in-out;
}

.sphere-1 {
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(147, 51, 234, 0.4) 0%, transparent 70%);
  top: -200px;
  left: -200px;
  animation-delay: 0s;
}

.sphere-2 {
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(236, 72, 153, 0.4) 0%, transparent 70%);
  bottom: -150px;
  right: -150px;
  animation-delay: -5s;
}

.sphere-3 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(59, 130, 246, 0.3) 0%, transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation-delay: -10s;
}

@keyframes float {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(30px, -30px) scale(1.1);
  }
  66% {
    transform: translate(-20px, 20px) scale(0.9);
  }
}

/* 登录容器 */
.login-container {
  position: relative;
  width: 100%;
  max-width: 420px;
  z-index: 10;
}

@keyframes glowRotate {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* 内容包装器 */
.content-wrapper {
  background: rgba(0, 0, 0, 0.01);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 22px;
  padding: 40px 32px;
  box-shadow: 
    0 25px 50px -12px rgba(0, 0, 0, 0.5),
    0 0 0 1px rgba(255, 255, 255, 0.05) inset;
}

/* 头部样式 */
.login-header {
  text-align: center;
  margin-bottom: 32px;
}

.back-home-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 20;
}

.back-home-btn .btn-glass {
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  height: auto;
}

.title {
  font-size: 36px;
  font-weight: 800;
  margin-bottom: 12px;
  position: relative;
  display: inline-block;
}

.title-glow {
  background: linear-gradient(135deg, #fff 0%, #e0e0e0 50%, #fff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  position: relative;
  display: inline-block;
}

.title::before {
  content: '';
  position: absolute;
  inset: -10px -20px;
  background: radial-gradient(ellipse at center, rgba(147, 51, 234, 0.3) 0%, transparent 70%);
  z-index: -1;
  animation: pulse 3s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50% { opacity: 0.8; transform: scale(1.05); }
}

/* 输入组 */
.input-group {
  position: relative;
  margin-bottom: 16px;
}

.input-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255, 255, 255, 0.5);
  z-index: 10;
  pointer-events: none;
}

.toggle-password {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  padding: 4px;
  transition: color 0.2s;
  z-index: 10;
}

.toggle-password:hover {
  color: rgba(255, 255, 255, 0.9);
}

/* 游戏风格输入框 */
:deep(.game-input .el-input__wrapper) {
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  border-radius: 12px !important;
  box-shadow: none !important;
  padding: 0 16px 0 44px !important;
  height: 52px !important;
  transition: all 0.3s ease !important;
}

:deep(.game-input .el-input__wrapper:hover) {
  background: rgba(255, 255, 255, 0.08) !important;
  border-color: rgba(147, 51, 234, 0.3) !important;
}

:deep(.game-input .el-input__wrapper.is-focus) {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: #9333ea !important;
  box-shadow: 0 0 0 3px rgba(147, 51, 234, 0.1) !important;
}

:deep(.game-input .el-input__inner) {
  color: white !important;
  font-size: 15px !important;
}

:deep(.game-input .el-input__inner::placeholder) {
  color: rgba(255, 255, 255, 0.4) !important;
}

/* 密码要求 */
.password-requirements {
  margin: 20px 0;
  padding: 16px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  font-size: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.password-requirements p {
  margin: 0 0 8px 0;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 600;
  font-size: 13px;
}

.password-requirements ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.password-requirements li {
  color: rgba(255, 255, 255, 0.6);
  margin: 8px 0;
  padding-left: 24px;
  position: relative;
  font-size: 12px;
  line-height: 1.5;
  transition: all 0.2s ease;
}

.password-requirements li::before {
  content: '○';
  position: absolute;
  left: 0;
  color: rgba(255, 255, 255, 0.6);
  font-size: 14px;
  transition: all 0.2s ease;
}

.password-requirements li.valid {
  color: #10b981;
  font-weight: 500;
}

.password-requirements li.valid::before {
  content: '✓';
  color: #10b981;
  font-weight: bold;
}

.password-requirements li.invalid {
  color: #f87171;
  font-weight: 500;
}

.password-requirements li.invalid::before {
  content: '✗';
  color: #f87171;
  font-weight: bold;
}

/* 玻璃态按钮样式 */
.btn-glass {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  white-space: nowrap;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  background: transparent;
  color: white;
  padding: 0.5rem 1rem;
  height: auto;
  overflow: hidden;
  text-decoration: none;
}

.btn-glass:hover {
  transform: scale(1.05);
  text-decoration: none;
}

.btn-glass:disabled {
  pointer-events: none;
  opacity: 0.5;
}

/* 玻璃态阴影层 */
.btn-glass-shadow {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
  width: 100%;
  height: 100%;
  border-radius: 9999px;
  transition: all 0.3s ease;
  box-shadow:
    0 0 6px rgba(0, 0, 0, 0.03),
    0 2px 6px rgba(0, 0, 0, 0.08),
    inset 3px 3px 0.5px -3px rgba(0, 0, 0, 0.9),
    inset -3px -3px 0.5px -3px rgba(0, 0, 0, 0.85),
    inset 1px 1px 1px -0.5px rgba(0, 0, 0, 0.6),
    inset -1px -1px 1px -0.5px rgba(0, 0, 0, 0.6),
    inset 0 0 6px 6px rgba(0, 0, 0, 0.12),
    inset 0 0 2px 2px rgba(0, 0, 0, 0.06),
    0 0 12px rgba(255, 255, 255, 0.15);
}

@media (prefers-color-scheme: dark) {
  .btn-glass-shadow {
    box-shadow:
      0 0 1px rgba(0, 0, 0, 0.03),
      0 1px 1px rgba(0, 0, 0, 0.08),
      inset 3px 3px 0.5px -3.5px rgba(255, 255, 255, 0.09),
      inset -3px -3px 0.5px -3.5px rgba(255, 255, 255, 0.85),
      inset 1px 1px 1px -0.5px rgba(255, 255, 255, 0.6),
      inset -1px -1px 1px -0.5px rgba(255, 255, 255, 0.6),
      inset 0 0 6px 6px rgba(255, 255, 255, 0.12),
      inset 0 0 2px 2px rgba(255, 255, 255, 0.06),
      0 0 1px rgba(0, 0, 0, 0.15);
  }
}

/* 玻璃态滤镜背景 */
.btn-glass-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  isolation: isolate;
  z-index: -10;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 9999px;
  backdrop-filter: url('#container-glass');
  -webkit-backdrop-filter: url('#container-glass');
}

/* 按钮内容 */
.btn-glass-content {
  pointer-events: none;
  z-index: 10;
  position: relative;
}

.btn-glass-content svg {
  vertical-align: text-top;
  margin-top: 2px;
}

/* 登录按钮特定样式 */
.login-btn {
  width: 100%;
  height: auto;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 9999px;
  padding: 0.75rem 1.5rem;
  gap: 0.5rem;
  margin-top: 16px;
}

.login-btn.loading .btn-glass-shadow {
  box-shadow:
    0 0 6px rgba(0, 0, 0, 0.03),
    0 2px 6px rgba(0, 0, 0, 0.08),
    inset 3px 3px 0.5px -3px rgba(255, 255, 255, 0.9),
    inset -3px -3px 0.5px -3px rgba(255, 255, 255, 0.85),
    inset 1px 1px 1px -0.5px rgba(255, 255, 255, 0.6),
    inset -1px -1px 1px -0.5px rgba(255, 255, 255, 0.6),
    inset 0 0 6px 6px rgba(255, 255, 255, 0.12),
    inset 0 0 2px 2px rgba(255, 255, 255, 0.06),
    0 0 12px rgba(124, 58, 237, 0.3);
}

.login-btn.success .btn-glass-shadow {
  box-shadow:
    0 0 6px rgba(0, 0, 0, 0.03),
    0 2px 6px rgba(0, 0, 0, 0.08),
    inset 3px 3px 0.5px -3px rgba(255, 255, 255, 0.9),
    inset -3px -3px 0.5px -3px rgba(255, 255, 255, 0.85),
    inset 1px 1px 1px -0.5px rgba(255, 255, 255, 0.6),
    inset -1px -1px 1px -0.5px rgba(255, 255, 255, 0.6),
    inset 0 0 6px 6px rgba(255, 255, 255, 0.12),
    inset 0 0 2px 2px rgba(255, 255, 255, 0.06),
    0 0 12px rgba(16, 185, 129, 0.3);
  animation: successPulse 0.5s ease;
}

.loading-spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@keyframes successPulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.success-icon {
  font-size: 24px;
  animation: checkmark 0.5s ease;
}

@keyframes checkmark {
  0% { transform: scale(0) rotate(-45deg); opacity: 0; }
  50% { transform: scale(1.2) rotate(0deg); }
  100% { transform: scale(1) rotate(0deg); opacity: 1; }
}

/* SVG 滤镜（隐藏但功能存在） */
.svg-filters {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

/* 注册区域 */
.register-section {
  margin-top: 24px;
  text-align: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}

.register-text {
  margin-right: 8px;
}

.register-btn {
  background: none;
  border: none;
  color: #ec4899;
  font-weight: 600;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
  position: relative;
}

.register-btn::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #ec4899, #9333ea);
  transition: width 0.3s;
}

.register-btn:hover {
  color: #f472b6;
}

.register-btn:hover::after {
  width: 100%;
}

/* 响应式 */
@media (max-width: 480px) {
  .content-wrapper {
    padding: 32px 24px;
  }
  
  .title {
    font-size: 28px;
  }
}

/* Element Plus 表单样式覆盖 */
:deep(.el-form-item) {
  margin-bottom: 0;
}

:deep(.el-form-item__error) {
  color: #f87171;
  font-size: 12px;
  padding-top: 4px;
}
</style>
