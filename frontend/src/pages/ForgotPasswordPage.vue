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
            <span class="title-glow">修改密码</span>
          </h1>
        </div>

        <!-- 忘记密码表单 -->
        <el-form
          :model="formData"
          :rules="rules"
          ref="forgotFormRef"
          class="login-form"
          @keyup.enter="handleSubmit"
        >
          <!-- 手机号码输入 -->
          <el-form-item prop="phone">
            <div class="input-group">
              <div class="input-icon">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </div>
              <el-input
                v-model="formData.phone"
                placeholder="请输入注册时的手机号码"
                class="game-input"
              />
            </div>
          </el-form-item>

          <!-- 新密码输入 -->
          <el-form-item prop="new_password">
            <div class="input-group">
              <div class="input-icon">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <el-input
                v-model="formData.new_password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="请输入新密码"
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
          </el-form-item>

          <!-- 确认新密码输入 -->
          <el-form-item prop="confirm_password">
            <div class="input-group">
              <div class="input-icon">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                  <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                </svg>
              </div>
              <el-input
                v-model="formData.confirm_password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="请再次输入新密码"
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
          </el-form-item>

          <!-- 密码要求 -->
          <div class="password-requirements" v-if="formData.new_password.length > 0">
            <div class="requirement invalid" v-if="!isPasswordValid(formData.new_password)">
              <span>✗ 至少8个字符，包含大小写字母和数字</span>
            </div>
            <div class="requirement valid" v-else>
              <span>✓ 密码强度符合要求</span>
            </div>
            <div class="requirement invalid" v-if="formData.confirm_password && formData.new_password !== formData.confirm_password">
              <span>✗ 两次输入的密码不一致</span>
            </div>
          </div>

          <!-- 修改密码按钮 -->
          <div class="btn-glass login-btn" @click="handleSubmit" :class="{ loading: isLoading, success: isSuccess }" :disabled="isLoading">
            <div class="btn-glass-shadow"></div>
            <div class="btn-glass-backdrop"></div>
            <div class="btn-glass-content">
              <span v-if="isSuccess" class="success-icon">✓</span>
              <span v-else-if="isLoading" class="loading-spinner"></span>
              <span v-else>修改密码</span>
            </div>
          </div>
        </el-form>
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
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import api from "../utils/axios";

const router = useRouter();
const forgotFormRef = ref(null);
const isLoading = ref(false);
const isSuccess = ref(false);
const showPassword = ref(false);

const formData = reactive({
  phone: "",
  new_password: "",
  confirm_password: "",
});

const rules = {
  phone: [
    { required: true, message: "手机号码不能为空", trigger: "blur" },
    { pattern: /^1[3-9]\d{9}$/, message: "请输入正确的手机号码", trigger: "blur" }
  ],
  new_password: [{ required: true, message: "新密码不能为空", trigger: "blur" }],
  confirm_password: [{ required: true, message: "请确认新密码", trigger: "blur" }],
};

const isPasswordValid = (password) => {
  return password.length >= 8 && /[A-Z]/.test(password) && /[a-z]/.test(password) && /[0-9]/.test(password);
};

const handleSubmit = async () => {
  if (!forgotFormRef.value) return;

  try {
    const valid = await forgotFormRef.value.validate();
    
    if (!valid) {
      return;
    }
    
    if (!isPasswordValid(formData.new_password)) {
      ElMessage.error("密码强度不符合要求，请至少使用8个字符，包含大小写字母和数字");
      return;
    }

    if (formData.new_password !== formData.confirm_password) {
      ElMessage.error("两次输入的密码不一致");
      return;
    }

    isLoading.value = true;
    
    const response = await api.post("/api/users/forgot-password/", formData);

    if (response.status === 200) {
      isSuccess.value = true;
      ElMessage.success("密码修改成功，即将返回登录页面");
      
      setTimeout(() => {
        router.push("/login");
      }, 1000);
    }
  } catch (error) {
    isSuccess.value = false;
    
    if (error instanceof Error && error.message.includes('validation failed')) {
      return;
    }
    
    const errorMsg = error.response?.data?.message || error.message;
    const errorsObj = error.response?.data?.errors || {};
    
    if (Object.keys(errorsObj).length > 0) {
      Object.entries(errorsObj).forEach(([field, messages]) => {
        if (Array.isArray(messages)) {
          messages.forEach(msg => {
            ElMessage.error(msg);
          });
        } else {
          ElMessage.error(messages);
        }
      });
    } else if (errorMsg) {
      ElMessage.error(errorMsg);
    } else {
      ElMessage.error("修改密码失败：未知错误");
    }
  } finally {
    isLoading.value = false;
  }
};

const handleBackLogin = () => {
  router.push("/login");
};

onMounted(() => {});
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

/* 网格覆盖层 */
.grid-overlay {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 50px 50px;
  pointer-events: none;
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
  width: 100%;
}

/* 确保所有输入框宽度一致 */
:deep(.el-form-item) {
  width: 100%;
  margin-bottom: 32px;
  position: relative;
}

:deep(.el-form-item .el-input) {
  width: 100%;
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
  margin: 16px 0;
  font-size: 12px;
}

.requirement {
  margin-bottom: 4px;
  display: flex;
  align-items: center;
}

.requirement.valid {
  color: #10b981;
}

.requirement.invalid {
  color: #f87171;
}

/* 表单错误信息 */
:deep(.el-form-item__error) {
  font-size: 12px;
  color: #f87171;
  margin-top: 8px;
  margin-left: 0;
  text-align: left;
  position: absolute;
  top: 43px;
  left: 0;
  width: 100%;
  z-index: 10;
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