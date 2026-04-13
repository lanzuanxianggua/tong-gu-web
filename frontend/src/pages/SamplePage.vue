<template>
  <div class="sample-page">
    <!-- 背景图片 -->
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
                    <span class="user-name" @click="router.push('/profile')">{{ userName }}</span>
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

    <!-- 主要内容 -->
    <main class="main-content">
      <section class="content-section">
        <div class="section-container">
          <h1 class="page-title gradient-text">示例图片库</h1>
          
          <p class="page-description">
            这里提供了一些铜鼓纹样的示例图片，您可以点击任意图片自动加载到检测页面进行体验。
            后续会持续添加更多不同类型的铜鼓纹样图片。
          </p>

          <!-- 示例图片网格 -->
          <div class="sample-grid">
            <div 
              v-for="(sample, index) in paginatedSampleList" 
              :key="index"
              class="sample-card"
              @click="useSample(sample)"
            >
              <div class="sample-image-wrapper">
                <img :src="sample.image" :alt="sample.name" class="sample-image" />
                <div class="sample-overlay">
                  <span class="use-btn">使用此图片</span>
                </div>
              </div>
              
              <div class="sample-info">
                <h3 class="sample-name">{{ sample.name }}</h3>
                <p class="sample-type">{{ sample.type }}</p>
                <p class="sample-desc">{{ sample.description }}</p>
              </div>
            </div>
          </div>

          <!-- 空状态提示 -->
          <div v-if="sampleList.length === 0" class="empty-state">
            <p class="empty-text">暂无示例图片</p>
            <p class="empty-hint">管理员正在添加中，请稍后再来...</p>
          </div>

          <!-- 分页控件 -->
          <div v-if="totalPages > 1" class="sample-pagination">
            <div class="pagination-info">
              显示 {{ (currentPage - 1) * pageSize + 1 }} - {{ Math.min(currentPage * pageSize, sampleList.length) }} 张图片，共 {{ sampleList.length }} 张
            </div>
            <div class="pagination-controls">
              <button 
                class="page-btn" 
                :disabled="currentPage === 1"
                @click="currentPage--"
              >
                ‹
              </button>
              <button 
                v-for="page in visiblePages"
                :key="page"
                class="page-btn"
                :class="{ active: page === currentPage, ellipsis: page === '...' }"
                :disabled="page === '...'"
                @click="page !== '...' && (currentPage = page)"
              >
                {{ page }}
              </button>
              <button 
                class="page-btn"
                :disabled="currentPage === totalPages"
                @click="currentPage++"
              >
                ›
              </button>
            </div>
          </div>
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
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

import '@/styles/HomePage.css'
import BackToTop from '@/components/BackToTop.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()

const menuState = ref(false)
const scrolled = ref(false)
const isLoggedIn = ref(false)
const userName = ref('')

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

const sampleList = ref([])

const currentPage = ref(1)
const pageSize = 9

const totalPages = computed(() => {
  return Math.ceil(sampleList.value.length / pageSize)
})

const paginatedSampleList = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  const end = start + pageSize
  return sampleList.value.slice(start, end)
})

const visiblePages = computed(() => {
  const total = totalPages.value
  const current = currentPage.value
  
  if (total <= 7) {
    return Array.from({ length: total }, (_, i) => i + 1)
  }
  
  const pages = []
  
  if (current <= 4) {
    pages.push(1, 2, 3, 4, 5, '...', total)
  } else if (current >= total - 3) {
    pages.push(1, '...', total - 4, total - 3, total - 2, total - 1, total)
  } else {
    pages.push(1, '...', current - 1, current, current + 1, '...', total)
  }
  
  return pages
})

const loadSampleList = async () => {
  try {
    const response = await fetch('/samples/samples.json')
    const data = await response.json()
    
    sampleList.value = data.samples.map(sample => ({
      ...sample,
      image: `/samples/${sample.image}`
    }))
  } catch (error) {
    console.error('加载示例图片失败:', error)
    sampleList.value = []
  }
}

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
  ElMessage.success('退出登录成功')
  router.push('/')
}

const useSample = (sample) => {
  sessionStorage.setItem('selectedSample', JSON.stringify(sample))
  
  router.push({
    path: '/detection',
    query: { useSample: 'true' }
  })
  
  ElMessage.success(`已选择：${sample.name}，正在跳转到检测页面...`)
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()

  const userData = localStorage.getItem('user')
  if (userData) {
    const user = JSON.parse(userData)
    isLoggedIn.value = true
    userName.value = user.username || '用户'
  }
  
  loadSampleList()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Background */
.sample-page {
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

/* Main Content */
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

/* Page Title */
.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 2rem;
  color: white;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-description {
  text-align: center;
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.7);
  max-width: 800px;
  margin: 0 auto 3rem;
  line-height: 1.7;
}

/* Sample Grid */
.sample-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

@media (max-width: 768px) {
  .sample-grid {
    grid-template-columns: 1fr;
  }
}

/* Sample Card */
.sample-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  overflow: hidden;
  transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
  cursor: pointer;
  will-change: transform;
}

.sample-card:hover {
  border-color: rgba(212, 175, 55, 0.5);
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(212, 175, 55, 0.2);
}

.sample-image-wrapper {
  position: relative;
  width: 100%;
  height: 240px;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.3);
}

.sample-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
  will-change: transform;
}

.sample-card:hover .sample-image {
  transform: scale(1.05);
}

.sample-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8) 0%, transparent 60%);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 1.5rem;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.sample-card:hover .sample-overlay {
  opacity: 1;
}

.use-btn {
  padding: 10px 24px;
  background: linear-gradient(90deg, #d4af37, #f4e4ba);
  color: #000;
  font-weight: 600;
  font-size: 0.9rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.use-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(212, 175, 55, 0.4);
}

.sample-info {
  padding: 1.5rem;
}

.sample-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #d4af37;
  margin-bottom: 0.5rem;
}

.sample-type {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 0.75rem;
  padding: 4px 12px;
  background: rgba(212, 175, 55, 0.15);
  border-radius: 20px;
  display: inline-block;
}

.sample-desc {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
}

.empty-text {
  font-size: 1.5rem;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 1rem;
}

.empty-hint {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.5);
}

/* Pagination - 全透明样式 */
.sample-pagination {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  margin-top: 3rem;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.02);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.pagination-info {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 500;
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.page-btn {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent !important;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 10px;
  color: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.page-btn:hover:not(:disabled):not(.ellipsis) {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: rgba(212, 175, 55, 0.4);
  color: #d4af37;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2), 0 0 12px rgba(212, 175, 55, 0.1);
  transform: translateY(-2px);
}

.page-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  background: transparent !important;
}

.page-btn.active {
  background: rgba(212, 175, 55, 0.2) !important;
  border-color: rgba(212, 175, 55, 0.5) !important;
  color: #d4af37 !important;
  font-weight: 600;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2), 0 0 16px rgba(212, 175, 55, 0.15);
}

.page-btn.ellipsis {
  background: transparent !important;
  border: none;
  cursor: default;
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.5);
}

/* Responsive */
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

  .sample-image-wrapper {
    height: 200px;
  }

  .sample-pagination {
    padding: 1.5rem;
  }

  .page-btn {
    width: 36px;
    height: 36px;
    font-size: 0.9rem;
  }
}
</style>
