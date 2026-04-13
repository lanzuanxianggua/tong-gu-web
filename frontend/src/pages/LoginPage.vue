<template>
  <div class="login-page">
    <!-- 动态背景 -->
    <div class="animated-bg">
      <div class="bg-image"></div>
      <div class="gradient-sphere sphere-1"></div>
      <div class="gradient-sphere sphere-2"></div>
      <div class="gradient-sphere sphere-3"></div>
    </div>

    <!-- 返回首页按钮 -->
    <div class="back-home-btn">
      <div class="btn-glass" @click="handleBackHome">
        <div class="btn-glass-shadow"></div>
        <div class="btn-glass-backdrop"></div>
        <div class="btn-glass-content">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
          <span>返回首页</span>
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
            <span class="title-glow">登录</span>
          </h1>
        </div>

        <!-- 登录表单 -->
        <el-form
          :model="formData"
          :rules="rules"
          ref="loginFormRef"
          class="login-form"
          @keyup.enter="handleSubmit"
        >
          <!-- 用户名/邮箱输入 -->
          <div class="input-group">
            <div class="input-icon">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <el-input
              v-model="formData.username"
              placeholder="请输入用户名或邮箱"
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

          <!-- 记住我和忘记密码 -->
          <div class="options-row">
            <div class="remember-me" @click="rememberMe = !rememberMe">
              <div class="toggle-switch" :class="{ active: rememberMe }">
                <div class="toggle-thumb"></div>
              </div>
              <span class="remember-text">记住我</span>
            </div>
            <div class="forgot-link cursor-pointer" @click="router.push('/forgot-password')">忘记密码？</div>
          </div>

          <!-- 登录按钮 -->
          <div class="btn-glass login-btn" @click="handleSubmit" :class="{ loading: isLoading, success: isSuccess }" :disabled="isLoading">
            <div class="btn-glass-shadow"></div>
            <div class="btn-glass-backdrop"></div>
            <div class="btn-glass-content">
              <span v-if="isSuccess" class="success-icon">✓</span>
              <span v-else-if="isLoading" class="loading-spinner"></span>
              <span v-else>进入平台</span>
            </div>
          </div>
        </el-form>

        <!-- 注册链接 -->
        <div class="register-section">
          <span class="register-text">还没有账号？</span>
          <button class="register-btn" @click="router.push('/register')">
            立即注册
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
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { User } from '@element-plus/icons-vue';
import api from "../utils/axios";

const router = useRouter();
const loginFormRef = ref(null);
const videoRef = ref(null);
const isLoading = ref(false);
const isSuccess = ref(false);
const showPassword = ref(false);
const rememberMe = ref(false);


const formData = reactive({
  username: "",
  password: "",
});

const rules = {
  username: [{ required: true, message: "用户名不能为空", trigger: "blur" }],
  password: [{ required: true, message: "密码不能为空", trigger: "blur" }],
};

const handleSubmit = async () => {
  if (!loginFormRef.value) return;

  await loginFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        isLoading.value = true;
        
        await new Promise(resolve => setTimeout(resolve, 800));
        
        const response = await api.post("/api/users/login/", formData);

        if (response.status === 200) {
          localStorage.setItem("user", JSON.stringify(response.data.user));

          localStorage.setItem("access_token", response.data.access);
          localStorage.setItem("refresh_token", response.data.refresh);

          if (rememberMe.value) {
            localStorage.setItem("remembered_username", formData.username);
          } else {
            localStorage.removeItem("remembered_username");
          }

          isSuccess.value = true;
          ElMessage.success("登录成功，欢迎回来！");
          
          setTimeout(() => {
            router.push("/");
          }, 1000);
        }
      } catch (error) {
        isSuccess.value = false;
        const errorMsg = error.response?.data?.message || error.message;
        const errorsObj = error.response?.data?.errors || {};
        const errorDetails = Object.values(errorsObj).join(" ");
        const allErrorInfo = (errorMsg + " " + errorDetails).toLowerCase();

        if (
          allErrorInfo.includes("用户名或密码错误") ||
          allErrorInfo.includes("用户不存在")
        ) {
          ElMessage.error("该账号尚未注册，请先注册后再登录！");
        } else {
          ElMessage.error("登录失败：" + errorMsg);
        }
      } finally {
        isLoading.value = false;
      }
    }
  });
};

const handleBackHome = () => {
  router.push("/");
};

onMounted(() => {
  const remembered = localStorage.getItem("remembered_username");
  if (remembered) {
    formData.username = remembered;
    rememberMe.value = true;
  }
  
  if (videoRef.value) {
    videoRef.value.play().catch(() => {});
  }
});
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

.subtitle {
  display: flex;
  flex-direction: column;
  gap: 8px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
}

.pulse-text {
  animation: textPulse 2s ease-in-out infinite;
}

@keyframes textPulse {
  0%, 100% { opacity: 0.7; }
  50% { opacity: 1; }
}

.hint-text {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
  font-family: monospace;
}

.emoji-row {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-top: 12px;
}

.emoji {
  font-size: 20px;
  display: inline-block;
}

.emoji.pulse {
  animation: emojiPulse 2s ease-in-out infinite;
}

.emoji.bounce {
  animation: bounce 1.5s ease-in-out infinite;
}

@keyframes emojiPulse {
  0%, 100% { transform: scale(1); opacity: 0.7; }
  50% { transform: scale(1.2); opacity: 1; }
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
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

/* 选项行 */
.options-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px 0;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.toggle-switch {
  width: 44px;
  height: 24px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  position: relative;
  transition: background 0.3s;
}

.toggle-switch.active {
  background: #9333ea;
}

.toggle-thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  background: white;
  border-radius: 50%;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-switch.active .toggle-thumb {
  transform: translateX(20px);
}

.remember-text {
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
}

.forgot-link {
  color: rgba(255, 255, 255, 0.6);
  font-size: 14px;
  text-decoration: none;
  transition: color 0.2s;
}

.forgot-link:hover {
  color: #ec4899;
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
  
  .social-buttons {
    gap: 8px;
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