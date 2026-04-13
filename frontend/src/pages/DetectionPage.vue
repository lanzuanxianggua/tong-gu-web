<template>
  <div class="detection-page">
    <!-- 动态背景 -->
    <div class="bg-image"></div>

    <!-- 导航栏 -->
    <header class="home-nav" :class="{ scrolled: scrolled }">
      <nav :data-state="menuState ? 'active' : undefined">
        <div class="home-nav-container">
          <div class="home-nav-content">
            <!-- Logo -->
            <div class="home-nav-brand">
              <div @click="router.push('/')" class="home-logo cursor-pointer">
                <img src="@/assets/tonggu_logo.png" alt="铜鼓智能识别平台" class="logo-image" />
                <span class="logo-text">铜鼓智能识别与数字化保护平台</span>
              </div>

              <!-- 移动端菜单按钮 -->
              <button @click="toggleMenu" class="home-nav-toggle">
                <svg :class="['home-nav-toggle-icon', { active: menuState }]" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>
                </svg>
                <svg :class="['home-nav-toggle-close', { active: menuState }]" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 6 6 18"/><path d="m6 6 12 12"/>
                </svg>
              </button>

              <!-- 桌面导航 -->
              <div class="home-nav-links">
                <ul>
                  <li v-for="(item, index) in menuItems" :key="index">
                    <div @click="router.push(item.href)" class="home-nav-link cursor-pointer">{{ item.name }}</div>
                  </li>
                </ul>
              </div>
            </div>

            <!-- 移动菜单 / 操作按钮 -->
            <div :class="['home-nav-menu', { active: menuState }]">
              <div class="home-nav-mobile">
                <ul>
                  <li v-for="(item, index) in menuItems" :key="index">
                    <div @click="handleMobileNavClick(item.href)" class="home-nav-link cursor-pointer">{{ item.name }}</div>
                  </li>
                </ul>
              </div>

              <div class="home-nav-actions">
                <template v-if="!isLoggedIn">
                  <div class="btn-glass" @click="router.push('/login')">
                    <div class="btn-glass-shadow"></div><div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content"><span>登录</span></div>
                  </div>
                  <div class="btn-glass" @click="router.push('/register')">
                    <div class="btn-glass-shadow"></div><div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content"><span>注册</span></div>
                  </div>
                </template>
                <template v-else>
                  <div class="home-user-info">
                    <span 
                      class="user-name" 
                      @click="router.push('/profile')"
                      role="button"
                      tabindex="0"
                      aria-label="查看个人资料"
                    >
                      {{ userName }}
                    </span>
                    <div class="btn-glass" @click="handleLogout">
                      <div class="btn-glass-shadow"></div><div class="btn-glass-backdrop"></div>
                      <div class="btn-glass-content"><span>退出登录</span></div>
                    </div>
                  </div>
                </template>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <!-- 主要内容区域 -->
    <main class="main-content">
      <section class="content-section">
        <div class="section-container">
          <h1 class="page-title gradient-text">铜鼓纹样智能检测与分析</h1>
          <el-tabs v-model="activeTab" class="custom-tabs">
            <!-- Tab 1: 智能检测 -->
            <el-tab-pane label="智能检测" name="detect">
              <div class="detect-grid">
                <!-- 左侧：上传与控制 -->
                <div class="control-panel glass-card">
                  <div class="panel-header">
                    <h3 class="panel-title">上传待检测图片</h3>
                  </div>

                  <!-- 上传区域 -->
                  <el-upload
                    class="upload-zone"
                    drag
                    action="#"
                    :auto-upload="false"
                    :show-file-list="false"
                    :on-change="handleFileChange"
                  >
                    <div class="upload-content">
                      <div class="upload-icon"></div>
                      <p class="upload-text">将纹样图片拖到此处，或<em>点击上传</em></p>
                      <p class="upload-hint">支持 JPG、PNG 格式，建议尺寸 ≥ 512px</p>
                    </div>
                  </el-upload>

                  <!-- 检测按钮 -->
                  <div class="button-wrapper">
                    <button
                      v-if="selectedFile"
                      class="detect-button"
                      :class="{ loading: isLoading }"
                      @click="startDetection"
                      :disabled="isLoading"
                    >
                      <span v-if="!isLoading">开始检测</span>
                      <span v-else class="loading-text">
                        <span class="spinner"></span>
                        检测中...
                      </span>
                    </button>
                  </div>

                  <!-- 示例图片链接 -->
                  <div class="sample-link" v-if="!selectedFile">
                    <p class="link-text">没有铜鼓照片？</p>
                    <router-link to="/samples" class="link-btn">
                      前往示例图片库选择
                      <span class="arrow">→</span>
                    </router-link>
                  </div>

                  <!-- 识别结果 - 分页显示 -->
                  <div class="results-section" v-if="detections.length > 0">
                    <div class="results-header">
                      <h3 class="results-title">
                        识别结果分析
                        <span class="result-count">(共 {{ detections.length }} 条)</span>
                      </h3>
                      
                      <!-- 结果分页器 -->
                      <div class="results-pagination" v-if="totalResultPages > 1">
                        <button 
                          class="page-btn" 
                          :disabled="currentResultPage === 1"
                          @click="currentResultPage--"
                        >
                          ‹
                        </button>
                        <span class="page-info">{{ currentResultPage }} / {{ totalResultPages }}</span>
                        <button 
                          class="page-btn"
                          :disabled="currentResultPage === totalResultPages"
                          @click="currentResultPage++"
                        >
                          ›
                        </button>
                      </div>
                    </div>

                    <!-- 分页后的结果列表 -->
                    <transition-group name="list" tag="div" class="results-list">
                      <div
                        v-for="(item, index) in paginatedDetections"
                        :key="'det-' + index"
                        class="detection-result-card"
                      >
                        <div class="result-main">
                          <div class="result-label">
                            <el-tag type="success" effect="dark" size="large">{{ item.label }}</el-tag>
                            <span class="confidence-badge" :style="{ width: Math.round(item.confidence * 100) + '%' }">
                              {{ Math.round(item.confidence * 100) }}%
                            </span>
                          </div>
                          
                          <div class="result-details">
                            <div class="detail-item">
                              <span class="detail-label">年代推测</span>
                              <span class="detail-value">{{ item.era }}</span>
                            </div>
                            <div class="detail-item">
                              <span class="detail-label">地域类型</span>
                              <span class="detail-value">{{ item.region }}</span>
                            </div>
                          </div>
                        </div>

                        <!-- 保存操作 -->
                        <div class="save-action" v-if="user">
                          <input
                            type="text"
                            v-model="item.remark"
                            placeholder="添加个人备注..."
                            class="remark-input"
                          />
                          <button class="save-btn" @click="saveRecord(item)">保存</button>
                        </div>
                      </div>
                    </transition-group>
                  </div>
                </div>

                <!-- 右侧：图像预览 -->
                <div class="preview-panel glass-card">
                  <div class="panel-header">
                    <h3 class="panel-title">可视化标记与关键特征</h3>
                  </div>

                  <div class="preview-container">
                    <template v-if="annotatedImage">
                      <el-image
                        :src="annotatedImage"
                        fit="contain"
                        class="preview-image"
                        :preview-src-list="[annotatedImage]"
                      />
                    </template>
                    <template v-else-if="previewUrl">
                      <el-image :src="previewUrl" fit="contain" class="preview-image" />
                    </template>
                    <div v-else class="empty-state">
                      <p class="empty-text">请先在左侧上传铜鼓纹样图片</p>
                    </div>
                  </div>
                </div>
              </div>
            </el-tab-pane>

            <!-- Tab 2: 归档记录 -->
            <el-tab-pane label="识别归档" name="archive" :disabled="!user">
              <div class="archive-panel glass-card">
                <div class="panel-header">
                  <h3 class="panel-title">识别记录归档</h3>
                  
                  <!-- 筛选器 -->
                  <div class="filter-bar">
                    <el-radio-group v-model="filterType" size="small" class="filter-group">
                      <el-radio-button value="all">全部</el-radio-button>
                      <el-radio-button value="sun">太阳纹</el-radio-button>
                      <el-radio-button value="wa">蛙纹</el-radio-button>
                      <el-radio-button value="lei">云雷纹</el-radio-button>
                    </el-radio-group>
                    
                    <span class="record-stats">
                      共 {{ filteredRecords.length }} 条记录
                    </span>
                  </div>
                </div>

                <!-- 记录网格 -->
                <template v-if="filteredRecords.length > 0">
                  <div class="records-grid">
                    <transition-group name="grid" tag="div" class="grid-container">
                      <div
                        v-for="record in paginatedRecords"
                        :key="record.id"
                        class="record-card"
                      >
                        <div class="record-image-wrapper">
                          <el-image
                            :src="record.annotated_image_data"
                            fit="cover"
                            class="record-image"
                            :alt="record.pattern_type"
                          />
                          <div class="record-overlay">
                            <span class="overlay-label">{{ record.pattern_type }}</span>
                          </div>
                        </div>
                        
                        <div class="record-body">
                          <div class="record-meta">
                            <span class="record-type">{{ record.pattern_type }}</span>
                            <span class="record-date">{{ formatDate(record.created_at) }}</span>
                          </div>
                          
                          <p class="record-era">{{ record.era_estimate }}</p>
                          
                          <p class="record-remark" v-if="record.remark">
                            {{ record.remark }}
                          </p>
                          
                          <button
                            class="delete-btn"
                            @click="deleteRecord(record.id)"
                            v-if="user"
                          >
                            删除
                          </button>
                        </div>
                      </div>
                    </transition-group>
                  </div>

                  <!-- 分页器 -->
                  <div class="archive-pagination" v-if="totalPages > 1">
                    <el-pagination
                      :current-page="currentPage"
                      :page-size="pageSize"
                      :total="filteredRecords.length"
                      layout="prev, pager, next"
                      :background="true"
                      class="custom-pagination"
                      @update:current-page="(val) => currentPage = val"
                    />
                  </div>
                </template>

                <!-- 空状态 -->
                <div v-else class="empty-archive">
                  <p class="empty-text">暂无识别记录</p>
                  <p class="empty-hint">完成检测后可在此查看历史记录</p>
                  <button v-if="!user" class="login-prompt-btn" @click="router.push('/login')">
                    登录后查看归档
                  </button>
                </div>
              </div>
            </el-tab-pane>
          </el-tabs>
        </div>
      </section>
    </main>
    
    <!-- 回到顶部按钮 -->
    <BackToTop />
    
    <!-- 页脚 -->
    <Footer />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import api from '../utils/axios'

import '@/styles/HomePage.css'
import BackToTop from '@/components/BackToTop.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()
const route = useRoute()

const menuState = ref(false)
const scrolled = ref(false)
const isLoggedIn = ref(false)
const userName = ref('')
const user = ref(null)

const menuItems = [
  { name: '前言', href: '/preface' },
  { name: '起源与发展', href: '/origin' },
  { name: '制作工艺', href: '/craft' },
  { name: '铜鼓类型', href: '/types' },
  { name: '艺术特色', href: '/art' },
  { name: '文化功能', href: '/culture' },
  { name: '现状', href: '/status' },
  { name: '检测', href: '/detection' },
]

const activeTab = ref('detect')

const isLoading = ref(false)
const selectedFile = ref(null)
const previewUrl = ref('')
const annotatedImage = ref('')
const detections = ref([])

const currentResultPage = ref(1)
const resultPageSize = ref(3)

const sampleImages = ref([
  {
    name: '太阳纹样',
    thumb: new URL('@/assets/tonggu06.png', import.meta.url).href,
    full: new URL('@/assets/tonggu06.png', import.meta.url).href
  },
  {
    name: '蛙纹样',
    thumb: new URL('@/assets/tonggu07.png', import.meta.url).href,
    full: new URL('@/assets/tonggu07.png', import.meta.url).href
  },
  {
    name: '云雷纹',
    thumb: new URL('@/assets/tonggu04.png', import.meta.url).href,
    full: new URL('@/assets/tonggu04.png', import.meta.url).href
  }
])

const historyRecords = ref([])
const filterType = ref('all')
const currentPage = ref(1)
const pageSize = ref(9)

const totalResultPages = computed(() => {
  return Math.ceil(detections.value.length / resultPageSize.value)
})

const paginatedDetections = computed(() => {
  const start = (currentResultPage.value - 1) * resultPageSize.value
  const end = start + resultPageSize.value
  return detections.value.slice(start, end)
})

const filteredRecords = computed(() => {
  if (filterType.value === 'all') return historyRecords.value
  const typeMap = { sun: '太阳纹', wa: '蛙纹', lei: '云雷纹' }
  return historyRecords.value.filter(r => r.pattern_type === typeMap[filterType.value])
})

const totalPages = computed(() => {
  return Math.ceil(filteredRecords.value.length / pageSize.value)
})

const paginatedRecords = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  const end = start + pageSize.value
  return filteredRecords.value.slice(start, end)
})

const toggleMenu = () => {
  menuState.value = !menuState.value
}

const handleMobileNavClick = (href) => {
  router.push(href)
  menuState.value = false
}

const handleScroll = () => {
  scrolled.value = window.scrollY > window.innerHeight * 0.05
}

const handleLogout = () => {
  localStorage.removeItem('user')
  localStorage.removeItem('token')
  isLoggedIn.value = false
  userName.value = ''
  user.value = null
  ElMessage.success('退出登录成功')
  router.push('/')
}

const handleFileChange = (file) => {
  selectedFile.value = file.raw
  previewUrl.value = URL.createObjectURL(file.raw)
  annotatedImage.value = ''
  detections.value = []
  currentResultPage.value = 1
}

const downloadSample = async (sample) => {
  try {
    const response = await fetch(sample.full)
    const blob = await response.blob()
    const file = new File([blob], `${sample.name}.png`, { type: 'image/png' })
    
    selectedFile.value = file
    previewUrl.value = URL.createObjectURL(file)
    annotatedImage.value = ''
    detections.value = []
    currentResultPage.value = 1
    
    ElMessage.success(`已加载示例图片：${sample.name}`)
  } catch (error) {
    ElMessage.error('加载示例图片失败')
  }
}

const loadSampleImage = async (sample) => {
  try {
    const response = await fetch(sample.image)
    const blob = await response.blob()
    const file = new File([blob], `${sample.name}.png`, { type: 'image/png' })
    
    selectedFile.value = file
    previewUrl.value = URL.createObjectURL(file)
    annotatedImage.value = ''
    detections.value = []
    currentResultPage.value = 1
    
    ElMessage.success(`已加载示例图片：${sample.name}，可以直接开始检测`)
  } catch (error) {
    ElMessage.error('加载示例图片失败')
  }
}

const startDetection = async () => {
  if (!selectedFile.value) return

  const formData = new FormData()
  formData.append('image', selectedFile.value)

  try {
    isLoading.value = true
    const response = await api.post('/api/detection/detect/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })

    if (response.status === 200) {
      detections.value = response.data.detections.map(d => ({ ...d, remark: '' }))
      annotatedImage.value = response.data.image_data
      currentResultPage.value = 1
      ElMessage.success('检测并分析完成')
      activeTab.value = 'detect'
    }
  } catch (error) {
    ElMessage.error('检测失败：' + (error.response?.data?.message || error.message))
  } finally {
    isLoading.value = false
  }
}

const saveRecord = async (item) => {
  try {
    const formData = new FormData()
    formData.append('annotated_image_data', annotatedImage.value)
    formData.append('pattern_type', item.label)
    formData.append('era_estimate', item.era)
    formData.append('region_type', item.region)
    formData.append('confidence', item.confidence)
    formData.append('remark', item.remark)

    const response = await api.post('/api/detection/save-record/', formData)

    if (response.status === 201) {
      ElMessage.success('记录已存入档案')
      fetchHistory()
    }
  } catch (error) {
    ElMessage.error('保存失败：' + (error.response?.data?.detail || error.message))
  }
}

const fetchHistory = async () => {
  try {
    const response = await api.get('/api/detection/my-records/')
    historyRecords.value = response.data
  } catch (error) {
    console.error('无法获取历史记录', error)
  }
}

const deleteRecord = async (id) => {
  try {
    const confirmed = window.confirm('确定要删除这条识别记录吗？此操作无法撤销。')
    if (!confirmed) return

    const response = await api.delete(`/api/detection/delete-record/${id}/`)

    if (response.status === 200 || response.status === 204) {
      ElMessage.success('记录已删除')
      fetchHistory()
    }
  } catch (error) {
    ElMessage.error('删除失败：' + (error.response?.data?.detail || error.message))
  }
}

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  })
}

watch(filterType, () => {
  currentPage.value = 1
})

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()

  const userData = localStorage.getItem('user')
  if (userData) {
    user.value = JSON.parse(userData)
    isLoggedIn.value = true
    userName.value = user.value.username || '用户'
    fetchHistory()
  }

  if (route.query.useSample === 'true') {
    const sampleData = sessionStorage.getItem('selectedSample')
    if (sampleData) {
      const sample = JSON.parse(sampleData)
      loadSampleImage(sample)
      sessionStorage.removeItem('selectedSample')
    }
  }
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>

.detection-page {
  position: relative;
  min-height: 100vh;
  background: #000000;
  overflow-x: hidden;
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

.main-content {
  position: relative;
  z-index: 10;
  flex: 1;
  width: 100%;
  padding: 8rem 0 4rem;
  overflow-y: auto;
}

.content-section {
  padding: 2rem 0;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
  color: white;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.custom-tabs {
  --el-color-primary: #d4af37;
}

.custom-tabs :deep(.el-tabs__header) {
  margin-bottom: 2rem;
  border-bottom: 1px solid rgba(212, 175, 55, 0.2);
}

.custom-tabs :deep(.el-tabs__nav-wrap::after) {
  display: none;
}

.custom-tabs :deep(.el-tabs__item) {
  color: rgba(255, 255, 255, 0.6);
  font-weight: 500;
  font-size: 1rem;
  padding: 12px 24px;
  transition: all 0.3s ease;
  border-bottom: 2px solid transparent;
}

.custom-tabs :deep(.el-tabs__item:hover) {
  color: rgba(255, 255, 255, 0.9);
}

.custom-tabs :deep(.el-tabs__item.is-active) {
  color: #d4af37;
  border-bottom-color: #d4af37;
}

.custom-tabs :deep(.el-tabs__active-bar) {
  display: none;
}

.custom-tabs :deep(.el-tabs__content) {
  padding: 0;
}

.glass-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  transition: all 0.3s ease;
}

.glass-card:hover {
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

/* Detect Grid Layout */
.detect-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-8);
  align-items: start;
}

@media (min-width: 1024px) {
  .detect-grid {
    grid-template-columns: 420px 1fr;
    align-items: start;
  }
}

/* Panel Header */
.panel-header {
  padding: var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.panel-title {
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
  color: var(--color-accent-gold-light);
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

/* Control Panel */
.control-panel {
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* Upload Zone */
.upload-zone {
  padding: var(--space-6);
  margin: var(--space-6) 0;
}

.upload-zone :deep(.el-upload-dragger) {
  background: transparent;
  border: 2px dashed rgba(212, 175, 55, 0.3);
  border-radius: var(--radius-lg);
  padding: var(--space-10) var(--space-6);
  transition: all var(--transition-base);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.upload-zone :deep(.el-upload-dragger:hover) {
  border-color: rgba(212, 175, 55, 0.6);
  background: rgba(212, 175, 55, 0.05);
}

.upload-content {
  text-align: center;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.upload-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto var(--space-4);
  border: 3px dashed rgba(212, 175, 55, 0.4);
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.upload-icon::before {
  content: '+';
  font-size: 2.5rem;
  color: rgba(212, 175, 55, 0.6);
  font-weight: 300;
}

.upload-text {
  color: var(--color-text-secondary);
  font-size: var(--text-base);
  margin-bottom: var(--space-2);
}

.upload-text em {
  color: var(--color-accent-gold);
  font-style: normal;
  font-weight: var(--font-semibold);
}

.upload-hint {
  color: var(--color-text-muted);
  font-size: var(--text-sm);
  margin-top: var(--space-2);
}

/* Sample Link - 替代示例图片 */
.sample-link {
  margin-top: -1.5rem;
  margin-bottom: 1.5rem;
  padding: 1.75rem 2rem;
  background: rgba(212, 175, 55, 0.08);
  border: 1px solid rgba(212, 175, 55, 0.25);
  border-radius: 16px;
  text-align: center;
  max-width: 360px;
  margin-left: auto;
  margin-right: auto;
}

.link-text {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 1.25rem;
  font-weight: 500;
}

.link-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 32px;
  font-size: 1rem;
  font-weight: 600;
  color: #d4af37;
  text-decoration: none;
  background: rgba(212, 175, 55, 0.12);
  border: 1px solid rgba(212, 175, 55, 0.35);
  border-radius: 10px;
  transition: all 0.3s ease;
}

.link-btn:hover {
  background: rgba(212, 175, 55, 0.2);
  border-color: rgba(212, 175, 55, 0.6);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(212, 175, 55, 0.25);
}

.arrow {
  transition: transform 0.3s ease;
  font-size: 1.1rem;
}

.link-btn:hover .arrow {
  transform: translateX(4px);
}

/* Button Wrapper - 居中 */
.button-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
  margin-bottom: 1.5rem;
}

/* Detect Button */
.detect-button {
  width: auto;
  padding: 12px 32px;
  font-size: 0.95rem;
  font-weight: 600;
  color: #000;
  background: linear-gradient(90deg, #d4af37, #f4e4ba);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.detect-button:hover:not(:disabled):not(.loading) {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(212, 175, 55, 0.4);
}

.detect-button:active:not(:disabled) {
  transform: translateY(0);
}

.detect-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.detect-button.loading {
  pointer-events: none;
}

.loading-text {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-3);
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(0, 0, 0, 0.2);
  border-top-color: #000;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Results Section */
.results-section {
  margin-top: 2.5rem;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.02);
  border-radius: var(--radius-lg);
  max-height: 600px;
  overflow-y: auto;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-6);
  flex-wrap: wrap;
  gap: var(--space-4);
}

.results-title {
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
  color: var(--color-accent-gold-light);
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.result-count {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  font-weight: var(--font-normal);
}

/* Results Pagination (Mini) - 全透明样式 */
.results-pagination {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.page-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent !important;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-md);
  color: rgba(255, 255, 255, 0.9);
  font-size: var(--text-lg);
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.page-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: rgba(212, 175, 55, 0.4);
  color: #d4af37;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2), 0 0 12px rgba(212, 175, 55, 0.1);
  transform: translateY(-1px);
}

.page-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  background: transparent !important;
}

.page-info {
  font-size: var(--text-sm);
  color: rgba(255, 255, 255, 0.7);
  min-width: 60px;
  text-align: center;
  font-weight: 500;
}

/* Results List */
.results-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.detection-result-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-5);
  transition: all var(--transition-fast);
}

.detection-result-card:hover {
  border-color: var(--color-border-hover);
  background: var(--color-surface-hover);
  transform: translateX(4px);
}

.result-main {
  margin-bottom: var(--space-4);
}

.result-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-4);
  gap: var(--space-4);
}

.confidence-badge {
  height: 8px;
  background: linear-gradient(90deg, #ef4444, #f59e0b, #10b981);
  border-radius: var(--radius-full);
  position: relative;
  min-width: 80px;
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: white;
  text-align: center;
  line-height: 8px;
  padding: 0 var(--space-2);
}

.result-details {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-3);
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.detail-label {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.detail-value {
  font-size: var(--text-sm);
  color: var(--color-text-primary);
  font-weight: var(--font-medium);
}

/* Save Action */
.save-action {
  display: flex;
  gap: var(--space-3);
  padding-top: var(--space-4);
  border-top: 1px solid var(--color-border);
}

.remark-input {
  flex: 1;
  padding: var(--space-2) var(--space-3);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  color: var(--color-text-primary);
  font-size: var(--text-sm);
  transition: all var(--transition-fast);
}

.remark-input:focus {
  outline: none;
  border-color: var(--color-accent-gold);
  background: rgba(255, 255, 255, 0.05);
}

.remark-input::placeholder {
  color: var(--color-text-muted);
}

.save-btn {
  padding: var(--space-2) var(--space-4);
  background: rgba(212, 175, 55, 0.15);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: var(--radius-md);
  color: var(--color-accent-gold);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
}

.save-btn:hover {
  background: rgba(212, 175, 55, 0.25);
  border-color: rgba(212, 175, 55, 0.5);
  transform: translateY(-1px);
}

/* Preview Panel */
.preview-panel {
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 700px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
}

.preview-container {
  flex: 1;
  padding: var(--space-6);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  margin: var(--space-6);
  overflow: hidden;
}

.preview-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: var(--radius-md);
  background: transparent;
}

.preview-image :deep(img) {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  background: transparent;
}

.preview-image :deep(.el-image__inner) {
  background: transparent;
}

.preview-image :deep(.el-image__placeholder),
.preview-image :deep(.el-image__error) {
  background: transparent;
}

.preview-container :deep(.el-image) {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preview-container :deep(.el-image__inner) {
  position: relative !important;
  width: auto !important;
  height: auto !important;
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  background: transparent !important;
}

.preview-container :deep(.el-image__placeholder),
.preview-container :deep(.el-image__error) {
  background: transparent !important;
}

.empty-state {
  text-align: center;
  padding: var(--space-12) var(--space-6);
}

.empty-text {
  color: var(--color-text-muted);
  font-size: var(--text-base);
}

/* Archive Panel */
.archive-panel {
  padding: var(--space-6);
}

.filter-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
  flex-wrap: wrap;
  padding: var(--space-4) 0;
  border-bottom: 1px solid var(--color-border);
  margin-bottom: var(--space-6);
}

.filter-group {
  background: transparent;
}

.filter-group :deep(.el-radio-button__inner) {
  background: var(--color-surface);
  border-color: var(--color-border);
  color: var(--color-text-secondary);
  padding: var(--space-2) var(--space-4);
}

.filter-group :deep(.el-radio-button__original-radio:checked + .el-radio-button__inner) {
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.3), rgba(244, 228, 186, 0.2));
  border-color: rgba(212, 175, 55, 0.5);
  color: var(--color-accent-gold-light);
}

.record-stats {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

/* Records Grid */
.records-grid {
  margin-bottom: var(--space-8);
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--space-6);
}

@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}

.record-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all var(--transition-base);
}

.record-card:hover {
  border-color: var(--color-border-hover);
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.record-image-wrapper {
  position: relative;
  overflow: hidden;
}

.record-image {
  width: 100%;
  height: 220px;
  object-fit: cover;
  transition: transform var(--transition-slow);
}

.record-card:hover .record-image {
  transform: scale(1.05);
}

.record-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7) 0%, transparent 100%);
  display: flex;
  align-items: flex-end;
  padding: var(--space-4);
  opacity: 0;
  transition: opacity var(--transition-base);
}

.record-card:hover .record-overlay {
  opacity: 1;
}

.overlay-label {
  color: white;
  font-weight: var(--font-semibold);
  font-size: var(--text-base);
}

.record-body {
  padding: var(--space-5);
}

.record-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-3);
}

.record-type {
  font-weight: var(--font-semibold);
  color: var(--color-accent-gold-light);
  font-size: var(--text-base);
}

.record-date {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

.record-era {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-3);
}

.record-remark {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  background: var(--color-surface);
  padding: var(--space-3);
  border-radius: var(--radius-md);
  margin-bottom: var(--space-4);
  line-height: var(--leading-relaxed);
}

.delete-btn {
  width: 100%;
  padding: var(--space-2) var(--space-4);
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: var(--radius-md);
  color: #ef4444;
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.delete-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  border-color: rgba(239, 68, 68, 0.4);
}

/* Archive Pagination - 全透明样式 */
.archive-pagination {
  display: flex;
  justify-content: center;
  padding: var(--space-6) 0;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.custom-pagination :deep(.el-pagination) {
  --el-pagination-button-bg-color: transparent;
  --el-pagination-hover-color: #d4af37;
  background: transparent;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.custom-pagination :deep(.btn-next),
.custom-pagination :deep(.btn-prev) {
  background: transparent !important;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  color: rgba(255, 255, 255, 0.9);
  transition: all 0.3s ease;
}

.custom-pagination :deep(.btn-next:hover),
.custom-pagination :deep(.btn-prev:hover) {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: rgba(212, 175, 55, 0.4) !important;
  color: #d4af37;
}

.custom-pagination :deep(.el-pager li) {
  background: transparent !important;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.9);
  margin: 0 4px;
  transition: all 0.3s ease;
}

.custom-pagination :deep(.el-pager li:hover) {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: rgba(212, 175, 55, 0.4);
  color: #d4af37;
}

.custom-pagination :deep(.is-active) {
  background: rgba(212, 175, 55, 0.2) !important;
  border-color: rgba(212, 175, 55, 0.5) !important;
  color: #d4af37 !important;
  font-weight: 600;
}

/* Empty Archive State */
.empty-archive {
  text-align: center;
  padding: var(--space-16) var(--space-6);
}

.empty-archive .empty-text {
  font-size: var(--text-xl);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-3);
}

.empty-archive .empty-hint {
  color: var(--color-text-muted);
  margin-bottom: var(--space-8);
}

.login-prompt-btn {
  padding: var(--space-3) var(--space-8);
  background: var(--gradient-gold);
  color: #000;
  font-weight: var(--font-semibold);
  border: none;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--transition-base);
}

.login-prompt-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--glow-gold);
}

/* List Animations */
.list-enter-active,
.list-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.list-enter-from {
  opacity: 0;
  transform: translateX(-20px);
}

.list-leave-to {
  opacity: 0;
  transform: translateX(20px);
}

.grid-enter-active,
.grid-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.grid-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}

.grid-leave-to {
  opacity: 0;
  transform: scale(0.9) translateY(-20px);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .detect-grid {
    grid-template-columns: 1fr;
  }

  .preview-panel {
    position: static;
  }

  .preview-container {
    min-height: 350px;
  }

  .results-section {
    max-height: none;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 6rem 0 2rem;
  }

  .page-title {
    font-size: 2rem;
  }

  .section-container {
    padding: 0 1rem;
  }

  .result-details {
    grid-template-columns: 1fr;
  }

  .save-action {
    flex-direction: column;
  }

  .filter-bar {
    flex-direction: column;
    align-items: stretch;
  }

  .grid-container {
    grid-template-columns: 1fr;
  }
}
</style>
