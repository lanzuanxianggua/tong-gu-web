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

    <!-- 主要内容 -->
    <main class="main-content">
      <section class="content-section">
        <div class="section-container">
          <h1 class="page-title">铜鼓纹样智能检测与分析</h1>
          <p class="section-desc text-center">
            基于深度学习的铜鼓纹样智能识别与数字化分析系统
          </p>
          
          <div class="detection-container">
            <el-row :gutter="24">
              <!-- 左侧：操作与上传 -->
              <el-col :md="8" :sm="24">
                <el-card class="control-card" shadow="never">
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
                      class="detect-btn"
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
                      class="detection-item"
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
                            <el-button @click="saveRecord(item)" class="save-btn">保存记录</el-button>
                          </template>
                        </el-input>
                      </div>
                    </div>
                  </div>
                </el-card>
              </el-col>

              <!-- 右侧：可视化展示区域 -->
              <el-col :md="16" :sm="24">
                <el-card class="display-card" shadow="never">
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
                  class="history-card"
                  v-if="user && historyRecords.length > 0"
                  shadow="never"
                >
                  <template #header>
                    <div class="card-header">
                      <span class="header-title">识别记录归档</span>
                      <el-radio-group v-model="filterType" size="small" class="filter-group">
                        <el-radio-button value="all">全部</el-radio-button>
                        <el-radio-button value="sun">太阳纹</el-radio-button>
                        <el-radio-button value="wa">蛙纹</el-radio-button>
                        <el-radio-button value="lei">云雷纹</el-radio-button>
                      </el-radio-group>
                    </div>
                  </template>
                  <el-row :gutter="20">
                    <el-col
                      :span="8"
                      v-for="record in paginatedRecords"
                      :key="record.id"
                      class="history-col"
                    >
                      <el-card
                        :body-style="{ padding: '0px' }"
                        class="record-card"
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
                          <div class="record-actions" v-if="user">
                            <el-button
                              type="danger"
                              size="small"
                              @click="deleteRecord(record.id)"
                              class="delete-btn"
                            >
                              <el-icon><Delete /></el-icon> 删除
                            </el-button>
                          </div>
                        </div>
                      </el-card>
                    </el-col>
                  </el-row>
                  
                  <!-- 分页器 -->
                  <div class="pagination-container" v-if="totalPages > 1">
                    <el-pagination
                      v-model="currentPage"
                      :page-size="pageSize"
                      :total="filteredRecords.length"
                      layout="prev, pager, next"
                      :background="false"
                      class="custom-pagination"
                    />
                  </div>
                </el-card>
              </el-col>
            </el-row>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from "vue";
import { useRouter } from "vue-router";
import { ElMessage, ElMessageBox } from "element-plus";
import { Delete } from "@element-plus/icons-vue";
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
const currentPage = ref(1);
const pageSize = ref(6); // 每页显示 9 条记录

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

const deleteRecord = async (id) => {
  try {
    await ElMessageBox.confirm(
      '确定要删除这条识别记录吗？此操作无法撤销。',
      '确认删除',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );
    
    const response = await api.delete(`/api/detection/delete-record/${id}/`);
    
    if (response.status === 200 || response.status === 204) {
      ElMessage.success('记录已删除');
      fetchHistory();
    }
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败：' + (error.response?.data?.detail || error.message));
    }
  }
};

const filteredRecords = computed(() => {
  if (filterType.value === "all") return historyRecords.value;
  const typeMap = { sun: "太阳纹", wa: "蛙纹", lei: "云雷纹" };
  return historyRecords.value.filter(
    (r) => r.pattern_type === typeMap[filterType.value]
  );
});

const totalPages = computed(() => {
  return Math.ceil(filteredRecords.value.length / pageSize.value);
});

const paginatedRecords = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  return filteredRecords.value.slice(start, end);
});

// 监听筛选类型变化，重置页码
watch(filterType, () => {
  currentPage.value = 1;
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
    transform: translate(0, 0);
  }
  25% {
    transform: translate(30px, -30px);
  }
  50% {
    transform: translate(-20px, 20px);
  }
  75% {
    transform: translate(20px, 30px);
  }
}

/* 检测页面容器 */
.detection-container {
  position: relative;
  z-index: 1;
  width: 100%;
}

/* 页面标题样式 */
.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1.5rem;
  color: white;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-desc {
  font-size: 1.1rem;
  color: #E5E5EA;
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

/* 主内容区域 */
.main-content {
  position: relative;
  z-index: 10;
  flex: 1;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 8rem 0 4rem;
}

.content-section {
  padding: 2rem 0;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* 卡片通用样式 - 全透明背景 */
.control-card,
.display-card,
.history-card {
  background: transparent !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  box-shadow: none !important;
  border-radius: 1rem !important;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}

.control-card :deep(.el-card__header),
.display-card :deep(.el-card__header),
.history-card :deep(.el-card__header) {
  background: transparent !important;
  border-bottom-color: rgba(255, 255, 255, 0.1) !important;
}

.control-card :deep(.el-card__body),
.display-card :deep(.el-card__body),
.history-card :deep(.el-card__body) {
  background: transparent !important;
}

.control-card:hover,
.display-card:hover,
.history-card:hover {
  border-color: rgba(255, 255, 255, 0.2) !important;
}

/* 卡片头部样式 */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  background: transparent;
}

.header-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #d4af37;
  background: linear-gradient(90deg, #d4af37, #f4e4ba);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* 上传区域样式 */
.upload-area {
  width: 100%;
  padding: 2rem;
  background: transparent;
  border: 2px dashed rgba(212, 175, 55, 0.3);
  border-radius: 0.75rem;
  transition: all 0.3s ease;
}

.upload-area:hover {
  border-color: rgba(212, 175, 55, 0.6);
  background: transparent;
}

.upload-area :deep(.el-icon--upload) {
  font-size: 3rem;
  color: #d4af37;
  margin-bottom: 1rem;
}

.upload-area :deep(.el-upload__text) {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.95rem;
}

.upload-area :deep(.el-upload__text em) {
  color: #d4af37;
  font-style: normal;
}

.upload-area :deep(.el-upload) {
  background: transparent !important;
}

.upload-area :deep(.el-upload-dragger) {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}

/* 操作按钮区域 */
.action-btns {
  margin-top: 1.5rem;
  display: flex;
  justify-content: center;
}

.detect-btn {
  width: 100%;
  background: linear-gradient(135deg, #d4af37, #f4e4ba);
  color: #000;
  font-weight: 600;
  font-size: 1rem;
  padding: 1.25rem 2rem;
  border: none;
  border-radius: 0.75rem;
  transition: all 0.3s ease;
}

.detect-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(212, 175, 55, 0.4);
}

.detect-btn:active {
  transform: translateY(0);
}

/* 结果展示面板 */
.results-panel {
  margin-top: 1.5rem;
}

.results-header {
  margin-bottom: 1rem;
}

.results-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #d4af37;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* 检测项样式 */
.detection-item {
  margin-bottom: 1rem;
}

.detection-item :deep(.el-descriptions) {
  background: transparent;
  border-color: rgba(255, 255, 255, 0.1);
}

.detection-item :deep(.el-descriptions__header) {
  background: transparent;
}

.detection-item :deep(.el-descriptions__label) {
  background: rgba(212, 175, 55, 0.05);
  color: #d4af37;
  border-color: rgba(255, 255, 255, 0.1);
}

.detection-item :deep(.el-descriptions__content) {
  color: rgba(255, 255, 255, 0.9);
  border-color: rgba(255, 255, 255, 0.1);
}

.detection-item :deep(.el-descriptions__body) {
  background: transparent;
}

.info-text {
  color: rgba(255, 255, 255, 0.9);
}

/* 备注输入框 */
.remark-input {
  margin-top: 0.75rem;
}

.remark-input :deep(.el-input__wrapper) {
  background: rgba(255, 255, 255, 0.02);
  border-color: rgba(255, 255, 255, 0.1);
}

.remark-input :deep(.el-input__inner) {
  color: rgba(255, 255, 255, 0.9);
}

.save-btn {
  background: rgba(212, 175, 55, 0.2);
  color: #d4af37;
  border: 1px solid rgba(212, 175, 55, 0.5);
  font-weight: 600;
  backdrop-filter: blur(10px);
}

.save-btn:hover {
  background: rgba(212, 175, 55, 0.3);
  border-color: rgba(212, 175, 55, 0.8);
}

/* 图片预览容器 */
.image-preview-container {
  width: 100%;
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border-radius: 0.75rem;
  padding: 1.5rem;
}

.preview-img {
  width: 100%;
  max-height: 600px;
  border-radius: 0.5rem;
}

/* 历史记录卡片 */
.record-card {
  transition: all 0.3s ease;
  overflow: hidden;
  background: transparent !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  box-shadow: none !important;
}

.record-card :deep(.el-card__body) {
  background: transparent !important;
}

.record-card:hover {
  transform: translateY(-4px);
  border-color: rgba(255, 255, 255, 0.2) !important;
}

.record-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.record-info {
  padding: 1rem;
  background: transparent;
}

.record-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.record-label {
  font-size: 1rem;
  font-weight: 600;
  color: #d4af37;
}

.record-date {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
}

.record-era {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0.5rem;
}

.record-remark {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
  background: rgba(255, 255, 255, 0.03);
  padding: 0.5rem;
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
}

.record-actions {
  margin-top: 0.75rem;
  display: flex;
  justify-content: flex-end;
}

.delete-btn {
  background: rgba(244, 67, 54, 0.2);
  border-color: rgba(244, 67, 54, 0.3);
  color: #f44336;
  padding: 2px 10px;
  font-size: 11px;
  height: 24px;
  line-height: 1;
  transition: all 0.3s ease;
}

.delete-btn .el-icon {
  font-size: 12px;
  margin-right: 2px;
}

.delete-btn:hover {
  background: rgba(244, 67, 54, 0.3);
  border-color: rgba(244, 67, 54, 0.5);
  color: #fff;
}

/* 筛选器样式 */
.filter-group {
  background: rgba(255, 255, 255, 0.02);
  padding: 0.25rem;
  border-radius: 0.5rem;
}

.filter-group :deep(.el-radio-button__inner) {
  background: transparent;
  border-color: rgba(255, 255, 255, 0.2);
  color: rgba(255, 255, 255, 0.8);
}

.filter-group :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
  background: linear-gradient(135deg, #d4af37, #f4e4ba);
  border-color: #d4af37;
  color: #000;
}

/* 分页器样式 */
.pagination-container {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
  padding: 1rem;
}

.custom-pagination :deep(.el-pagination) {
  background: transparent;
}

.custom-pagination :deep(.el-pager li) {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  min-width: 36px;
  height: 36px;
  line-height: 36px;
  margin: 0 4px;
  transition: all 0.3s ease;
}

.custom-pagination :deep(.el-pager li:hover) {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.3);
}

.custom-pagination :deep(.el-pager li.is-active) {
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.3), rgba(244, 228, 186, 0.2));
  border-color: rgba(212, 175, 55, 0.6);
  color: #d4af37;
  font-weight: 600;
}

.custom-pagination :deep(.btn-prev),
.custom-pagination :deep(.btn-next) {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  min-width: 36px;
  height: 36px;
  line-height: 36px;
  margin: 0 4px;
  transition: all 0.3s ease;
}

.custom-pagination :deep(.btn-prev:hover),
.custom-pagination :deep(.btn-next:hover) {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.3);
  color: #fff;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .detection-container {
    padding: 1rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .image-preview-container {
    min-height: 300px;
  }
}
</style>
