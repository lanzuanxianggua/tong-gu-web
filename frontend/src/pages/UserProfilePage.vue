<template>
  <div class="profile-page">
    <!-- 动态背景 -->
    <div class="animated-bg">
      <div class="bg-image"></div>
      <div class="gradient-sphere sphere-1"></div>
      <div class="gradient-sphere sphere-2"></div>
      <div class="gradient-sphere sphere-3"></div>
    </div>

    <!-- 返回按钮 -->
    <div class="back-btn">
      <div class="btn-glass" @click="handleBackHome">
        <div class="btn-glass-shadow"></div>
        <div class="btn-glass-backdrop"></div>
        <div class="btn-glass-content">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M15 18l-6-6 6-6"/>
          </svg>
          <span>返回</span>
        </div>
      </div>
    </div>

    <!-- 主容器 -->
    <div class="profile-container">
      <div class="content-wrapper">
        <!-- 头部 -->
        <div class="profile-header">
          <h1 class="title">
            <span class="title-glow">个人信息</span>
          </h1>
        </div>

        <!-- 信息列表 -->
        <div class="info-list">
          <div class="info-item">
            <div class="info-label">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
              <span>用户名</span>
            </div>
            <div class="info-value">{{ userInfo.username || '未设置' }}</div>
          </div>

          <div class="info-item">
            <div class="info-label">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
              <span>手机号码</span>
            </div>
            <div class="info-value">{{ userInfo.phone || '未绑定' }}</div>
          </div>

          <div class="info-item">
            <div class="info-label">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
              <span>邮箱</span>
            </div>
            <div class="info-value email-value">
              <span>{{ userInfo.email || '未绑定' }}</span>
              <span v-if="!userInfo.email" class="bind-btn" @click="showBindEmailDialog">立即绑定</span>
            </div>
          </div>

          <div class="info-item">
            <div class="info-label">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
              <span>注册时间</span>
            </div>
            <div class="info-value">{{ formatDate(userInfo.created_at) || '未知' }}</div>
          </div>
        </div>

        <!-- 操作按钮 -->
        <div class="action-buttons">
          <div class="btn-glass action-btn" @click="handleChangePassword">
            <div class="btn-glass-shadow"></div>
            <div class="btn-glass-backdrop"></div>
            <div class="btn-glass-content">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
              <span>修改密码</span>
            </div>
          </div>

          <div class="btn-glass logout-btn" @click="handleLogout">
            <div class="btn-glass-shadow"></div>
            <div class="btn-glass-backdrop"></div>
            <div class="btn-glass-content">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                <polyline points="16 17 21 12 16 7"></polyline>
                <line x1="21" y1="12" x2="9" y2="12"></line>
              </svg>
              <span>退出登录</span>
            </div>
          </div>
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

    <!-- 邮箱绑定对话框 -->
    <div v-if="showEmailDialog" class="dialog-overlay" @click.self="closeEmailDialog">
      <div class="email-dialog">
        <h3 class="dialog-title">绑定邮箱</h3>
        <div class="dialog-content">
          <div class="form-item">
            <label>邮箱地址</label>
            <input
              v-model="emailForm.email"
              type="email"
              placeholder="请输入邮箱地址"
              class="dialog-input"
            />
          </div>
          <div class="form-item">
            <label>验证码</label>
            <div class="code-input-wrapper">
              <input
                v-model="emailForm.code"
                type="text"
                placeholder="请输入验证码"
                class="dialog-input code-input"
              />
              <button
                class="send-code-btn"
                :disabled="codeCooldown > 0"
                @click="sendVerificationCode"
              >
                {{ codeCooldown > 0 ? `${codeCooldown}s` : '发送验证码' }}
              </button>
            </div>
          </div>
        </div>
        <div class="dialog-actions">
          <button class="dialog-btn cancel-btn" @click="closeEmailDialog">取消</button>
          <button class="dialog-btn confirm-btn" @click="bindEmail">确认绑定</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { ElMessage, ElMessageBox } from "element-plus";
import api from "../utils/axios";

const router = useRouter();

const userInfo = reactive({
  username: "",
  phone: "",
  email: "",
  created_at: ""
});

const showEmailDialog = ref(false);
const emailForm = reactive({
  email: "",
  code: ""
});
const codeCooldown = ref(0);
let codeTimer = null;

const formatDate = (dateStr) => {
  if (!dateStr) return "";
  const date = new Date(dateStr);
  return date.toLocaleDateString("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  });
};

const fetchUserInfo = async () => {
  try {
    const response = await api.get("/api/users/profile/");
    if (response.status === 200) {
      Object.assign(userInfo, response.data.user || response.data);
    }
  } catch (error) {
    console.error("获取用户信息失败:", error);
    ElMessage.error("获取用户信息失败");
  }
};

const handleChangePassword = () => {
  router.push("/change-password");
};

const handleLogout = async () => {
  try {
    await ElMessageBox.confirm("确定要退出登录吗？", "提示", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning"
    });

    localStorage.removeItem("user");
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("token");

    ElMessage.success("已退出登录");
    router.push("/login");
  } catch (error) {
    if (error !== "cancel") {
      console.error("退出登录失败:", error);
    }
  }
};

const handleBackHome = () => {
  router.push("/");
};

const showBindEmailDialog = () => {
  emailForm.email = "";
  emailForm.code = "";
  showEmailDialog.value = true;
};

const closeEmailDialog = () => {
  showEmailDialog.value = false;
  if (codeTimer) {
    clearInterval(codeTimer);
    codeTimer = null;
  }
  codeCooldown.value = 0;
};

const sendVerificationCode = async () => {
  if (!emailForm.email) {
    ElMessage.error("请输入邮箱地址");
    return;
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailForm.email)) {
    ElMessage.error("请输入有效的邮箱地址");
    return;
  }

  try {
    await api.post("/api/users/send-code/", { email: emailForm.email, type: "bind" });
    ElMessage.success("验证码已发送到邮箱");
    codeCooldown.value = 60;
    codeTimer = setInterval(() => {
      codeCooldown.value--;
      if (codeCooldown.value <= 0) {
        clearInterval(codeTimer);
        codeTimer = null;
      }
    }, 1000);
  } catch (error) {
    ElMessage.error("发送验证码失败");
  }
};

const bindEmail = async () => {
  if (!emailForm.email) {
    ElMessage.error("请输入邮箱地址");
    return;
  }
  if (!emailForm.code) {
    ElMessage.error("请输入验证码");
    return;
  }

  try {
    const response = await api.post("/api/users/bind-email/", {
      email: emailForm.email,
      code: emailForm.code
    });
    if (response.status === 200) {
      ElMessage.success("邮箱绑定成功");
      userInfo.email = emailForm.email;
      closeEmailDialog();
    }
  } catch (error) {
    ElMessage.error("邮箱绑定失败");
  }
};

onMounted(() => {
  fetchUserInfo();
});
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.profile-page {
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

.animated-bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

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
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(30px, -30px) scale(1.1); }
  66% { transform: translate(-20px, 20px) scale(0.9); }
}

.profile-container {
  position: relative;
  width: 100%;
  max-width: 480px;
  z-index: 10;
}

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

.profile-header {
  text-align: center;
  margin-bottom: 32px;
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

.info-list {
  margin-bottom: 32px;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.info-item:last-child {
  border-bottom: none;
}

.info-label {
  display: flex;
  align-items: center;
  gap: 10px;
  color: rgba(255, 255, 255, 0.5);
  font-size: 14px;
}

.info-label svg {
  flex-shrink: 0;
}

.info-value {
  color: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  font-weight: 500;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

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
  padding: 0.75rem 1.5rem;
  height: auto;
  overflow: hidden;
  text-decoration: none;
}

.btn-glass:hover {
  transform: scale(1.02);
  text-decoration: none;
}

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

.btn-glass-content {
  pointer-events: none;
  z-index: 10;
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.action-btn {
  width: 100%;
}

.logout-btn .btn-glass-shadow {
  box-shadow:
    0 0 6px rgba(0, 0, 0, 0.03),
    0 2px 6px rgba(0, 0, 0, 0.08),
    inset 3px 3px 0.5px -3px rgba(0, 0, 0, 0.9),
    inset -3px -3px 0.5px -3px rgba(0, 0, 0, 0.85),
    inset 1px 1px 1px -0.5px rgba(0, 0, 0, 0.6),
    inset -1px -1px 1px -0.5px rgba(0, 0, 0, 0.6),
    inset 0 0 6px 6px rgba(0, 0, 0, 0.12),
    inset 0 0 2px 2px rgba(0, 0, 0, 0.06),
    0 0 12px rgba(239, 68, 68, 0.25);
}

.logout-btn:hover {
  transform: scale(1.02);
}

.back-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 20;
}

.back-btn .btn-glass {
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  height: auto;
  align-items: center;
}

.back-btn .btn-glass-content {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.back-btn .btn-glass-content svg {
  flex-shrink: 0;
}

.svg-filters {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.email-value {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.bind-btn {
  font-size: 0.75rem;
  padding: 0.25rem 0.5rem;
  background: rgba(212, 175, 55, 0.15);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 4px;
  color: #d4af37;
  cursor: pointer;
  transition: all 0.3s ease;
}

.bind-btn:hover {
  background: rgba(212, 175, 55, 0.25);
  border-color: rgba(212, 175, 55, 0.5);
}

.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.email-dialog {
  background: linear-gradient(135deg, rgba(30, 30, 40, 0.95), rgba(20, 20, 30, 0.95));
  border: 1px solid rgba(212, 175, 55, 0.2);
  border-radius: 16px;
  padding: 24px;
  width: 90%;
  max-width: 400px;
  backdrop-filter: blur(20px);
}

.dialog-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 1.5rem;
  text-align: center;
}

.dialog-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-item label {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
}

.dialog-input {
  padding: 0.75rem 1rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #fff;
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.3s ease;
}

.dialog-input:focus {
  border-color: rgba(212, 175, 55, 0.5);
}

.code-input-wrapper {
  display: flex;
  gap: 0.5rem;
}

.code-input {
  flex: 1;
}

.send-code-btn {
  padding: 0.75rem 1rem;
  background: rgba(212, 175, 55, 0.15);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 8px;
  color: #d4af37;
  font-size: 0.8rem;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.3s ease;
}

.send-code-btn:hover:not(:disabled) {
  background: rgba(212, 175, 55, 0.25);
}

.send-code-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.dialog-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.dialog-btn {
  flex: 1;
  padding: 0.75rem;
  border-radius: 8px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.cancel-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.7);
}

.cancel-btn:hover {
  background: rgba(255, 255, 255, 0.1);
}

.confirm-btn {
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.8), rgba(180, 140, 30, 0.9));
  border: none;
  color: #000;
  font-weight: 600;
}

.confirm-btn:hover {
  background: linear-gradient(135deg, rgba(212, 175, 55, 1), rgba(180, 140, 30, 1));
}

@media (max-width: 480px) {
  .content-wrapper {
    padding: 32px 24px;
  }

  .title {
    font-size: 28px;
  }
}
</style>
