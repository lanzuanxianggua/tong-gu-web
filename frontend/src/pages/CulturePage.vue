<template>
  <div class="flex flex-col min-h-screen bg-black text-white relative overflow-hidden">
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
      <section class="content-section">
        <div class="section-container">
          <h1 class="page-title">文化功能</h1>
          <p class="section-desc text-center">
            铜鼓不仅是一种乐器，更是西南少数民族文化的重要象征，具有多种文化功能
          </p>

          <!-- 功能分类 -->
          <div class="culture-functions">
            <h2 class="section-subtitle">主要功能</h2>
            <div class="functions-grid">
              <div class="function-card">
                <div class="function-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 0 1-9 9c-4.97 0-9-4.03-9-9s4.03-9 9-9 9 4.03 9 9z"></path><polyline points="9 10 12 13 22 4"></polyline></svg>
                </div>
                <h3>祭祀仪式</h3>
                <p>铜鼓是祭祀活动中的重要礼器，用于祈求神灵保佑、驱邪避灾。在重大节日和宗教仪式中，人们会敲击铜鼓，表达对神灵的敬意。</p>
              </div>
              <div class="function-card">
                <div class="function-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                </div>
                <h3>音乐艺术</h3>
                <p>铜鼓是一种打击乐器，具有独特的音色和演奏方式。在民族音乐中，铜鼓是重要的伴奏乐器，能够营造出热烈、庄重的氛围。</p>
              </div>
              <div class="function-card">
                <div class="function-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                </div>
                <h3>社会象征</h3>
                <p>铜鼓是权力和财富的象征，在古代社会中，拥有铜鼓的多少往往代表着地位的高低。铜鼓也是民族认同的重要标志。</p>
              </div>
              <div class="function-card">
                <div class="function-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
                </div>
                <h3>文化传承</h3>
                <p>铜鼓上的纹饰和图案记录了民族的历史、神话和生活场景，是研究民族文化的重要资料，承载着丰富的文化信息。</p>
              </div>
              <div class="function-card">
                <div class="function-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                </div>
                <h3>军事用途</h3>
                <p>铜鼓在古代被用作军事信号，用于指挥作战和传递信息。在战争中，铜鼓的声音可以鼓舞士气，震慑敌人。</p>
              </div>
              <div class="function-card">
                <div class="function-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                </div>
                <h3>贸易交换</h3>
                <p>铜鼓在古代西南地区的贸易中扮演着重要角色，是一种贵重的交换媒介。拥有铜鼓的多少往往代表着财富的多少。</p>
              </div>
            </div>
          </div>

          <!-- 文化意义 -->
          <div class="cultural-significance">
            <h2 class="section-subtitle">文化意义</h2>
            <div class="significance-content">
              <p class="paragraph">
                铜鼓文化是西南少数民族文化的重要组成部分，它不仅体现了古代工匠的精湛技艺，也反映了各民族的历史、宗教、艺术和社会生活。铜鼓的存在，为我们了解古代西南地区的文化交流和民族融合提供了宝贵的实物资料。
              </p>
              <p class="paragraph">
                在现代社会，铜鼓文化依然发挥着重要作用。它是民族文化认同的象征，也是民族团结的纽带。通过铜鼓文化的传承和发展，我们可以更好地保护和弘扬中华民族的优秀传统文化，增强民族凝聚力和文化自信。
              </p>
            </div>
          </div>

          <!-- 铜鼓与民族节日 -->
          <div class="festival-connection">
            <h2 class="section-subtitle">铜鼓与民族节日</h2>
            <div class="festival-grid">
              <div class="festival-card">
                <h3>壮族三月三（歌圩节）</h3>
                <p>壮族最重要的传统节日，又称"歌圩节"。节日期间人们身着民族盛装，敲击铜鼓、载歌载舞庆祝。铜鼓是节日庆典的核心乐器，用于祭祀祖先、庆祝丰收，体现了壮族深厚的铜鼓文化底蕴。</p>
              </div>
              <div class="festival-card">
                <h3>瑶族盘王节（祝著节）</h3>
                <p>瑶族传统重要节日，纪念祖先盘王。在节日庆典中使用铜鼓进行祭祀和庆祝活动。铜鼓作为宗教仪式和节庆活动的重要组成部分，承载着瑶族对祖先的敬仰。</p>
              </div>
              <div class="festival-card">
                <h3>水族铜鼓节</h3>
                <p>水族的传统节日，通常在清明节后举行。铜鼓被视为权力、财富和图腾崇拜的象征，在节庆活动中广泛使用。体现了水族独特的铜鼓文化传统和民族特色。</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- 底部 -->
    <footer class="footer">
      <div class="footer-content">
        <p>&copy; 2024 铜鼓智能识别与数字化保护平台. 版权所有.</p>
      </div>
    </footer>

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

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
// 引入样式
import '@/styles/HomePage.css'

const router = useRouter()

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
      const user = JSON.parse(userStr)
      isLoggedIn.value = true
      // 尝试获取用户名，根据实际数据结构调整
      userName.value = user.username || user.name || '用户'
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

/* 主内容区域 */
.main-content {
  position: relative;
  z-index: 10;
  flex: 1;
  padding: 8rem 0 4rem;
  width: 100%;
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

.section-desc {
  font-size: 1.1rem;
  color: #E5E5EA;
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

/* 功能分类 */
.culture-functions {
  margin-bottom: 4rem;
}

.section-subtitle {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 2rem;
  color: white;
}

.functions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.function-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
  text-align: center;
  transition: all 0.3s ease;
}

.function-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.function-icon {
  margin-bottom: 1.5rem;
  color: #d4af37;
}

.function-card h3 {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
}

.function-card p {
  font-size: 1rem;
  line-height: 1.6;
  color: #E5E5EA;
}

/* 文化意义 */
.cultural-significance {
  margin-bottom: 4rem;
}

.significance-content {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
}

.paragraph {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 1.5rem;
  color: #E5E5EA;
}

/* 铜鼓与民族节日 */
.festival-connection {
  margin-bottom: 4rem;
}

.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.festival-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
  transition: all 0.3s ease;
}

.festival-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.festival-card h3 {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
}

.festival-card p {
  font-size: 1rem;
  line-height: 1.6;
  color: #E5E5EA;
}

/* 底部样式 */
.footer {
  padding: 3rem 0;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.footer p {
  color: #8E8E93;
  font-size: 0.9rem;
  margin: 0;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .main-content {
    padding: 6rem 0 3rem;
  }
  
  .section-container {
    padding: 0 1rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .section-subtitle {
    font-size: 1.5rem;
  }
  
  .functions-grid,
  .festival-grid {
    grid-template-columns: 1fr;
  }
}
</style>