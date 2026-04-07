<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-black p-0 m-0 w-full relative overflow-hidden">
    <!-- 背景图片 -->
    <div class="bg-image"></div>
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

    <main class="main-content">
      <section class="content-section ios-section">
        <div class="section-container">
          <h1 class="page-title">现状与传承</h1>
          <p class="section-desc text-center">
            铜鼓文化在现代社会的传承与发展，以及面临的挑战和机遇
          </p>
          <div class="heritage-stats">
            <div class="features-grid">
              <div class="feature-card animate-scale-in">
                <div class="feature-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                </div>
                <h3>1500+</h3>
                <p>馆藏铜鼓数量</p>
              </div>
              <div class="feature-card animate-scale-in">
                <div class="feature-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                </div>
                <h3>2700</h3>
                <p>文化流传历史 (年)</p>
              </div>
              <div class="feature-card animate-scale-in">
                <div class="feature-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                </div>
                <h3>8</h3>
                <p>主要铜鼓类型</p>
              </div>
            </div>
          </div>
          <div class="heritage-content">
            <h2 class="section-subtitle">保护现状</h2>
            <p class="paragraph">
              广西作为"铜鼓之乡"，不仅拥有世界之最的铜鼓藏量，更在非物质文化遗产保护上走在前端。河池市被誉为"世界铜鼓之乡"，这里的民间铸造技艺正迎来新生，让铜鼓这一"活化石"继续在现代生活中敲响时代的强音。
            </p>
            <p class="paragraph">
              近年来，各级政府和文化部门加大了对铜鼓文化的保护力度，建立了铜鼓博物馆，开展了铜鼓铸造技艺的传承培训，同时通过数字化手段对铜鼓进行保护和研究。这些举措为铜鼓文化的传承和发展提供了有力的支持。
            </p>
            <h2 class="section-subtitle">传承挑战</h2>
            <p class="paragraph">
              尽管铜鼓文化得到了一定的保护和传承，但仍然面临着诸多挑战。随着现代化进程的加速，年轻一代对传统铜鼓文化的了解和兴趣逐渐减少，铜鼓铸造技艺面临失传的危险。此外，铜鼓的保护和研究需要大量的资金和专业人才，这也是当前面临的重要挑战。
            </p>
            <h2 class="section-subtitle">未来展望</h2>
            <p class="paragraph">
              面对挑战，我们需要采取更加积极有效的措施来保护和传承铜鼓文化。通过教育普及、文化活动、数字化保护等多种方式，让更多的人了解和关注铜鼓文化。同时，加强国际交流与合作，让铜鼓文化走向世界，成为人类共同的文化遗产。
            </p>
            <p class="paragraph">
              本平台的建立，正是为了通过数字化手段，保护和传承铜鼓文化，让更多人了解这一珍贵的民族文化遗产。我们相信，在大家的共同努力下，铜鼓文化一定能够在现代社会焕发出新的生机和活力。
            </p>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer glass-footer">
      <div class="footer-content">
        <p>&copy; 铜鼓纹文化门户 - 探索民族瑰宝</p>
        <div class="footer-links">
          <span>中华优秀传统文化传承项目</span>
        </div>
      </div>
    </footer>

    <el-backtop :right="40" :bottom="40" class="backtop-btn" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from "element-plus";
// 引入样式
import '@/styles/HomePage.css'

const router = useRouter()
const user = ref(null);

// 菜单项配置
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

// 响应式状态
const menuState = ref(false)
const scrolled = ref(false)
const isLoggedIn = ref(false)
const userName = ref('')

// 检查登录状态
const checkLoginStatus = () => {
  const userStr = localStorage.getItem('user')
  if (userStr) {
    try {
      const userData = JSON.parse(userStr)
      isLoggedIn.value = true
      user.value = userData
      // 尝试获取用户名，根据实际数据结构调整
      userName.value = userData.username || userData.name || '用户'
    } catch (e) {
      console.error('解析用户信息失败:', e)
      isLoggedIn.value = false
      userName.value = ''
    }
  } else {
    isLoggedIn.value = false
    userName.value = ''
  }
}

// 退出登录
const handleLogout = () => {
  // 清除本地存储的用户信息和token
  localStorage.removeItem('user')
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  
  // 更新登录状态
  isLoggedIn.value = false
  userName.value = ''
  user.value = null
  
  ElMessage.success("退出登录成功");
  
  // 跳转到首页
  router.push('/')
}

// 切换菜单状态
const toggleMenu = () => {
  menuState.value = !menuState.value
}

// 滚动监听
const handleScroll = () => {
  scrolled.value = window.scrollY > window.innerHeight * 0.05
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()
  checkLoginStatus()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
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

/* 页面内容样式 */
.main-content {
  position: relative;
  z-index: 10;
  flex: 1;
  padding: 8rem 0 var(--ios-spacing-2xl);
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  overflow-y: auto;
}

.content-section {
  padding: var(--ios-spacing-2xl) 0;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--ios-spacing-lg);
}

.page-title {
  font-size: 28px;
  font-weight: 700;
  text-align: center;
  margin-bottom: var(--ios-spacing-lg);
  color: #fff;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-desc {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: var(--ios-spacing-xl);
  text-align: center;
}

.heritage-stats {
  margin-bottom: var(--ios-spacing-2xl);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.feature-icon {
  margin-bottom: 1.5rem;
  color: #d4af37;
}

.feature-card h3 {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
  text-align: center;
}

.feature-card p {
  font-size: 1rem;
  line-height: 1.6;
  color: #E5E5EA;
  text-align: center;
}

.heritage-content {
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
}

.section-subtitle {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: var(--ios-spacing-lg);
  color: #fff;
}

.paragraph {
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: var(--ios-spacing-lg);
  color: rgba(255, 255, 255, 0.8);
}

.footer {
  padding: var(--ios-spacing-xl) 0;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.05);
  width: 100%;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--ios-spacing-lg);
}

.footer-content p {
  color: rgba(255, 255, 255, 0.8);
}

.footer-links {
  margin-top: var(--ios-spacing-md);
  font-size: 14px;
  color: rgba(255, 255, 255, 0.6);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .heritage-stats .el-col {
    flex: 100%;
    max-width: 100%;
    margin-bottom: var(--ios-spacing-lg);
  }
  
  .section-container {
    padding: 0 var(--ios-spacing-md);
  }
  
  .page-title {
    font-size: 24px;
  }
  
  .section-subtitle {
    font-size: 18px;
  }
  
  .paragraph {
    font-size: 14px;
  }
}
</style>