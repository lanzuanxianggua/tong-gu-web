<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-black p-0 m-0 w-full relative overflow-hidden">
    <!-- 动态背景 -->
    <div class="animated-bg">
      <div class="bg-image"></div>
      <div class="gradient-sphere sphere-1"></div>
      <div class="gradient-sphere sphere-2"></div>
      <div class="gradient-sphere sphere-3"></div>
    </div>
    <!-- 导航栏 -->
    <header class="home-nav">
      <nav
        :data-state="menuState ? 'active' : undefined"
      >
        <div
          :class="['home-nav-container', { scrolled: scrolled }]"
        >
          <div
            :class="['home-nav-content', { scrolled: scrolled }]"
          >
            <div class="home-nav-brand">
              <div
                @click="router.push('/')"
                aria-label="home"
                class="home-logo cursor-pointer"
              >
                <img
                  src="@/assets/tonggu_logo.png"
                  alt="铜鼓智能识别与数字化保护平台"
                  class="logo-image"
                />
                <span class="logo-text">铜鼓智能识别与数字化保护平台</span>
              </div>

              <!-- 移动端菜单切换按钮 -->
              <button
                @click="toggleMenu"
                :aria-label="menuState ? 'Close Menu' : 'Open Menu'"
                class="home-nav-toggle"
              >
                <svg
                  :class="['home-nav-toggle-icon', { active: menuState }]"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <line x1="4" x2="20" y1="12" y2="12"/>
                  <line x1="4" x2="20" y1="6" y2="6"/>
                  <line x1="4" x2="20" y1="18" y2="18"/>
                </svg>
                <svg
                  :class="['home-nav-toggle-close', { active: menuState }]"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M18 6 6 18"/>
                  <path d="m6 6 12 12"/>
                </svg>
              </button>

              <!-- 桌面端导航链接 -->
              <div class="home-nav-links">
                <ul>
                  <li v-for="(item, index) in menuItems" :key="index">
                    <div
                      @click="router.push(item.href)"
                      class="home-nav-link cursor-pointer"
                    >
                      <span>{{ item.name }}</span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <!-- 移动端菜单 / 桌面端按钮区域 -->
            <div
              :class="['home-nav-menu', { active: menuState }]"
            >
              <!-- 移动端导航链接 -->
              <div class="home-nav-mobile">
                <ul>
                  <li v-for="(item, index) in menuItems" :key="index">
                    <div
                      @click="router.push(item.href)"
                      class="home-nav-link cursor-pointer"
                    >
                      <span>{{ item.name }}</span>
                    </div>
                  </li>
                </ul>
              </div>

              <!-- 登录/注册按钮或用户信息 -->
              <div class="home-nav-actions">
                <template v-if="!isLoggedIn">
                  <!-- 登录 -->
                  <div class="btn-glass" @click="router.push('/login')">
                    <div class="btn-glass-shadow"></div>
                    <div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content">
                      <span>登录</span>
                    </div>
                  </div>
                  
                  <!-- 注册 -->
                  <div class="btn-glass" @click="router.push('/register')">
                    <div class="btn-glass-shadow"></div>
                    <div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content">
                      <span>注册</span>
                    </div>
                  </div>
                </template>
                <template v-else>
                  <!-- 用户信息和退出登录 -->
                  <div class="home-user-info">
                    <span class="user-name">{{ userName }}</span>
                    <div class="btn-glass" @click="handleLogout">
                      <div class="btn-glass-shadow"></div>
                      <div class="btn-glass-backdrop"></div>
                      <div class="btn-glass-content">
                        <span>退出登录</span>
                      </div>
                    </div>
                  </div>
                </template>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <!-- 页面内容 -->
    <div class="detection-container">
      <div class="page-header-wrapper">
        <div class="page-header glassmorphism">
          <div class="page-title">铜鼓纹样智能检测与分析</div>
        </div>
      </div>

    <el-row :gutter="24" class="main-content">
      <!-- 左侧：操作与上传 -->
      <el-col :md="8" :sm="24">
        <el-card class="control-card glassmorphism" shadow="never">
          <template #header>
            <div class="card-header">
              <span class="header-title">上传待检测图片</span>
            </div>
          </template>

          <el-upload
            class="upload-area"
            drag
            action="#"
            :auto-upload="false"
            :show-file-list="false"
            :on-change="handleFileChange"
          >
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
              将纹样图片拖到此处，或<em>点击上传</em>
            </div>
          </el-upload>

          <div class="action-btns" v-if="selectedFile">
            <el-button
              size="large"
              :loading="isLoading"
              @click="startDetection"
              class="detect-btn touch-feedback glass-button"
            >
              开始智能检测分析
            </el-button>
          </div>

          <!-- 识别结果结构化展示 -->
          <div class="results-panel" v-if="detections.length > 0">
            <div class="results-header">
              <h3>
                <el-icon><Histogram /></el-icon> 识别结果分析
              </h3>
            </div>
            <div
              v-for="(item, index) in detections"
              :key="index"
              class="detection-item glassmorphism"
            >
              <el-descriptions :column="1" border size="small">
                <el-descriptions-item label="纹样类型">
                  <el-tag type="success" effect="dark">{{ item.label }}</el-tag>
                </el-descriptions-item>
                <el-descriptions-item label="年代推测">
                  <span class="info-text">{{ item.era }}</span>
                </el-descriptions-item>
                <el-descriptions-item label="地域类型">
                  <span class="info-text">{{ item.region }}</span>
                </el-descriptions-item>
                <el-descriptions-item label="置信度">
                  <el-progress
                    :percentage="Math.round(item.confidence * 100)"
                    :color="customColors"
                  />
                </el-descriptions-item>
              </el-descriptions>

              <div class="save-action" v-if="user">
                <el-input
                  v-model="item.remark"
                  placeholder="添加个人备注..."
                  size="small"
                  class="remark-input"
                >
                  <template #append>
                    <el-button @click="saveRecord(item)" class="touch-feedback glass-button">保存记录</el-button>
                  </template>
                </el-input>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>

      <!-- 右侧：可视化展示区域 -->
      <el-col :md="16" :sm="24">
        <el-card class="display-card glassmorphism" shadow="never">
          <template #header>
            <div class="card-header">
              <span class="header-title">可视化标记与关键特征</span>
            </div>
          </template>

          <div class="image-preview-container">
            <template v-if="annotatedImage">
              <el-image
                :src="annotatedImage"
                fit="contain"
                class="preview-img"
                :preview-src-list="[annotatedImage]"
              />
            </template>
            <template v-else-if="previewUrl">
              <el-image :src="previewUrl" fit="contain" class="preview-img" />
            </template>
            <el-empty v-else description="请先在左侧上传铜鼓纹样图片" />
          </div>
        </el-card>

        <!-- 历史记录展示 -->
        <el-card
          class="history-card glassmorphism"
          v-if="user && historyRecords.length > 0"
          shadow="never"
        >
          <template #header>
            <div class="card-header">
              <span class="header-title">识别记录归档</span>
              <el-radio-group v-model="filterType" size="small" class="filter-group">
                <el-radio-button value="all" class="touch-feedback">全部</el-radio-button>
                <el-radio-button value="sun" class="touch-feedback">太阳纹</el-radio-button>
                <el-radio-button value="wa" class="touch-feedback">蛙纹</el-radio-button>
                <el-radio-button value="lei" class="touch-feedback">云雷纹</el-radio-button>
              </el-radio-group>
            </div>
          </template>
          <el-row :gutter="20">
            <el-col
              :span="8"
              v-for="record in filteredRecords"
              :key="record.id"
              class="history-col"
            >
              <el-card
                :body-style="{ padding: '0px' }"
                class="record-card glassmorphism"
                shadow="hover"
              >
                <el-image
                  :src="record.annotated_image_data"
                  fit="cover"
                  class="record-img"
                  :alt="record.pattern_type"
                />
                <div class="record-info">
                  <div class="record-title">
                    <span class="record-label">{{ record.pattern_type }}</span>
                    <span class="record-date">{{
                      formatDate(record.created_at)
                    }}</span>
                  </div>
                  <p class="record-era">{{ record.era_estimate }}</p>
                  <p class="record-remark" v-if="record.remark">
                    {{ record.remark }}
                  </p>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import {
  UploadFilled,
  Histogram,
} from "@element-plus/icons-vue";
import api from "../utils/axios";
// 引入样式
import '@/styles/HomePage.css'

const router = useRouter();
const user = ref(null);
const isLoading = ref(false);
const selectedFile = ref(null);
const previewUrl = ref("");
const annotatedImage = ref("");
const detections = ref([]);
const historyRecords = ref([]);
const filterType = ref("all");

// 导航栏相关状态
const menuState = ref(false);
const scrolled = ref(false);
const isLoggedIn = ref(false);
const userName = ref("");

// 导航菜单
const menuItems = ref([
  { name: "前言", href: "/preface" },
  { name: "起源与发展", href: "/origin" },
  { name: "制作工艺", href: "/craft" },
  { name: "铜鼓类型", href: "/types" },
  { name: "艺术特色", href: "/art" },
  { name: "文化功能", href: "/culture" },
  { name: "现状", href: "/status" },
  { name: "检测", href: "/detection" },
]);

// 切换菜单
const toggleMenu = () => {
  menuState.value = !menuState.value;
};

// 处理滚动
const handleScroll = () => {
  scrolled.value = window.scrollY > 50;
};

// 处理登出
const handleLogout = () => {
  localStorage.removeItem("user");
  localStorage.removeItem("token");
  isLoggedIn.value = false;
  userName.value = "";
  user.value = null;
  ElMessage.success("退出登录成功");
  router.push("/");
};

// 监听滚动事件
onMounted(() => {
  window.addEventListener("scroll", handleScroll);
  
  const userData = localStorage.getItem("user");
  if (userData) {
    user.value = JSON.parse(userData);
    isLoggedIn.value = true;
    userName.value = user.value.username || "用户";
    fetchHistory();
  }
});

// 移除滚动事件监听
onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});

const customColors = [
  { color: "#f56c6c", percentage: 20 },
  { color: "#e6a23c", percentage: 40 },
  { color: "#5cb87a", percentage: 60 },
  { color: "#1989fa", percentage: 80 },
  { color: "#6f7ad3", percentage: 100 },
];

onMounted(() => {
  const userData = localStorage.getItem("user");
  if (userData) {
    user.value = JSON.parse(userData);
    fetchHistory();
  }
});

const handleFileChange = (file) => {
  selectedFile.value = file.raw;
  previewUrl.value = URL.createObjectURL(file.raw);
  annotatedImage.value = "";
  detections.value = [];
};

const startDetection = async () => {
  if (!selectedFile.value) return;

  const formData = new FormData();
  formData.append("image", selectedFile.value);

  try {
    isLoading.value = true;
    const response = await api.post("/api/detection/detect/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    if (response.status === 200) {
      detections.value = response.data.detections.map((d) => ({
        ...d,
        remark: "",
      }));
      annotatedImage.value = response.data.image_data;
      ElMessage.success("检测并分析完成");
    }
  } catch (error) {
    ElMessage.error(
      "检测失败：" + (error.response?.data?.message || error.message)
    );
  } finally {
    isLoading.value = false;
  }
};

const saveRecord = async (item) => {
  try {
    const formData = new FormData();
    // 不发送原始图片，只发送标注图片的 base64 数据
    formData.append("annotated_image_data", annotatedImage.value);
    formData.append("pattern_type", item.label);
    formData.append("era_estimate", item.era);
    formData.append("region_type", item.region);
    formData.append("confidence", item.confidence);
    formData.append("remark", item.remark);

    const response = await api.post("/api/detection/save-record/", formData);

    if (response.status === 201) {
      ElMessage.success("记录已存入档案");
      fetchHistory();
    }
  } catch (error) {
    ElMessage.error("保存失败：" + (error.response?.data?.detail || error.message));
  }
};

const fetchHistory = async () => {
  try {
    const response = await api.get("/api/detection/my-records/");
    historyRecords.value = response.data;
  } catch (error) {
    console.error("无法获取历史记录", error);
  }
};

const filteredRecords = computed(() => {
  if (filterType.value === "all") return historyRecords.value;
  const typeMap = { sun: "太阳纹", wa: "蛙纹", lei: "云雷纹" };
  return historyRecords.value.filter(
    (r) => r.pattern_type === typeMap[filterType.value]
  );
});

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString();
};
</script>

<style scoped>
/* 动态背景 */
.animated-bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: 0;
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

.detection-container {
  position: relative;
  z-index: 10;
  padding: var(--ios-spacing-lg) var(--ios-spacing-xl);
  min-height: calc(100vh - 88px);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
}



.page-header-wrapper {
  margin-bottom: var(--ios-spacing-lg);
}

.page-header {
  padding: var(--ios-spacing-md) var(--ios-spacing-lg);
  border-radius: var(--ios-radius-lg);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  border: none;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.page-title {
  font-weight: 700;
  color: #fff;
  font-size: 20px;
  line-height: 1.2;
  text-align: center;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.control-card,
.display-card,
.history-card {
  border-radius: var(--ios-radius-lg);
  border: none;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  margin-bottom: var(--ios-spacing-lg);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.control-card:hover,
.display-card:hover,
.history-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.15);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title {
  font-weight: 600;
  color: #fff;
  font-size: 16px;
}

.upload-area {
  margin-bottom: var(--ios-spacing-md);
}

.upload-area .el-upload {
  border: 2px dashed #00bfff !important;
  border-radius: var(--ios-radius-lg);
  background: rgba(255, 255, 255, 0.1);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
}

.upload-area .el-upload:hover {
  border-color: #0099cc !important;
  background: rgba(0, 191, 255, 0.1);
  transform: scale(1.02);
}

.upload-area .el-icon--upload {
  color: #00bfff !important;
  font-size: 48px;
}

.upload-area .el-upload__text {
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
}

.upload-area .el-upload__text em {
  color: #00bfff;
  font-style: normal;
  font-weight: 600;
}

.detect-btn {
  width: 100%;
  height: 50px;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 1px;
  background: rgba(0, 191, 255, 0.2) !important;
  border: 1px solid rgba(0, 191, 255, 0.4) !important;
  border-radius: var(--ios-radius-full) !important;
  box-shadow: 0 4px 12px rgba(0, 191, 255, 0.3) !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
  color: #00bfff !important;
}

.detect-btn:hover {
  background: rgba(0, 191, 255, 0.3) !important;
  box-shadow: 0 6px 16px rgba(0, 191, 255, 0.4) !important;
  transform: translateY(-2px) !important;
}

.results-panel {
  margin-top: var(--ios-spacing-lg);
  border-top: 2px solid rgba(255, 255, 255, 0.1);
  padding-top: var(--ios-spacing-md);
}

.results-header h3 {
  color: #fff;
  display: flex;
  align-items: center;
  gap: var(--ios-spacing-xs);
  margin-bottom: var(--ios-spacing-md);
  font-weight: 600;
  font-size: 18px;
}

.results-header .el-icon {
  color: #00bfff;
  font-size: 20px;
}

.detection-item {
  margin-bottom: var(--ios-spacing-md);
  padding: var(--ios-spacing-md);
  border-radius: var(--ios-radius-lg);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.detection-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  background: rgba(255, 255, 255, 0.15);
}

.info-text {
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.save-action {
  margin-top: var(--ios-spacing-sm);
}

.remark-input :deep(.el-input__wrapper) {
  border-radius: var(--ios-radius-md) 0 0 var(--ios-radius-md) !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  background: rgba(255, 255, 255, 0.1) !important;
}

.remark-input :deep(.el-input__wrapper input) {
  color: #fff !important;
}

.remark-input :deep(.el-button) {
  border-radius: 0 var(--ios-radius-md) var(--ios-radius-md) 0 !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* 非毛玻璃按钮保持蓝色 */
.remark-input :deep(.el-button:not(.glass-button)) {
  background: rgba(0, 191, 255, 0.2) !important;
  border: 1px solid rgba(0, 191, 255, 0.4) !important;
  color: #00bfff !important;
}

.remark-input :deep(.el-button:not(.glass-button):hover) {
  background: rgba(0, 191, 255, 0.3) !important;
}

.image-preview-container {
  min-height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: var(--ios-radius-lg);
  padding: var(--ios-spacing-lg);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.preview-img {
  max-width: 100%;
  max-height: 750px;
  border-radius: var(--ios-radius-lg);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.preview-img:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  transform: scale(1.02);
}

.filter-group :deep(.el-radio-button__inner) {
  border-radius: var(--ios-radius-md) !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  background: rgba(255, 255, 255, 0.1) !important;
  color: rgba(255, 255, 255, 0.8) !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.filter-group :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
  background: rgba(0, 191, 255, 0.2) !important;
  border-color: rgba(0, 191, 255, 0.4) !important;
  color: #00bfff !important;
}

.history-col {
  margin-bottom: var(--ios-spacing-md);
}

.record-card {
  border-radius: var(--ios-radius-lg);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.record-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
  transform: translateY(-4px);
  background: rgba(255, 255, 255, 0.15);
}

.record-img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.record-card:hover .record-img {
  transform: scale(1.05);
}

.record-info {
  padding: var(--ios-spacing-sm);
  background: rgba(255, 255, 255, 0.1);
}

.record-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--ios-spacing-xs);
}

.record-label {
  font-weight: 600;
  color: #00bfff;
}

.record-date {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
}

.record-era {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: var(--ios-spacing-xs);
}

.record-remark {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.8);
  font-style: italic;
  line-height: 1.5;
}

.glassmorphism {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.touch-feedback {
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.touch-feedback:active {
  transform: scale(0.97);
  opacity: 0.8;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .detection-container {
    padding: var(--ios-spacing-sm);
  }
  
  .page-header {
    padding: var(--ios-spacing-sm) var(--ios-spacing-md);
  }
  
  .page-title {
    font-size: 16px;
  }
  
  .card-header {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--ios-spacing-sm);
  }
  
  .filter-group {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }
  
  .image-preview-container {
    min-height: 400px;
    padding: var(--ios-spacing-md);
  }
}
</style>
