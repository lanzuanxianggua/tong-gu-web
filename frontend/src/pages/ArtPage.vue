<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-black p-0 m-0 w-full relative overflow-hidden">
    <!-- 背景图片 -->
    <div class="bg-image"></div>
    <!-- 导航栏 -->
    <header class="home-nav" :class="{ scrolled: scrolled }">
      <nav :data-state="menuState ? 'active' : undefined">
        <div class="home-nav-container">
          <div class="home-nav-content">
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
                </template>
                <template v-else>
                  <!-- 用户信息和退出登录 -->
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
          <h1 class="page-title">独特的艺术魅力</h1>
          <p class="section-desc text-center">
            铜鼓不仅是实用的乐器，更是精美的艺术品，其纹饰蕴含着丰富的文化内涵
          </p>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 justify-items-center">
            <div v-for="art in arts" :key="art.title" class="timeline-card interactive-card hover-lift">
              <div class="timeline-icon">
                <svg v-if="art.icon === 'Sunny'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                <svg v-else-if="art.icon === 'Compass'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                <svg v-else-if="art.icon === 'Brush'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><path d="M9.59 4.59A2 2 0 1 1 11 8H2"></path><path d="M14.42 15.41A2 2 0 1 0 13 19H2"></path><path d="M17.73 6.27A2.5 2.5 0 1 1 20 8H8"></path><path d="M15.58 18.41A2 2 0 1 0 17 14H8"></path></svg>
                <svg v-else-if="art.icon === 'Cloudy'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"></path></svg>
              </div>
              <h3 class="timeline-title">{{ art.title }}</h3>
              <p class="timeline-text">{{ art.desc }}</p>
            </div>
          </div>
          
          <div class="art-highlights">
            <h2 class="section-subtitle">纹饰的文化意义</h2>
            <div class="highlight-content">
              <p class="paragraph">
                铜鼓的纹饰不仅是装饰，更是古代民族文化的重要载体。太阳纹象征对太阳神的崇拜，反映了农业社会对阳光的依赖；蛙立饰则与稻作文化密切相关，青蛙是雨神的使者，象征着丰收和吉祥。
              </p>
              <p class="paragraph">
                翔鹭纹、羽人舞蹈纹、龙舟竞渡纹等写实纹饰，生动地记录了古代民族的生产生活场景，为研究古代社会提供了宝贵的实物资料。这些纹饰不仅具有艺术价值，更是研究古代民族历史、宗教信仰和社会生活的重要依据。
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>

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
    
    <!-- 回到顶部按钮 -->
    <BackToTop />
    
    <!-- 页脚 -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import '@/styles/HomePage.css'
import BackToTop from '@/components/BackToTop.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()

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

const menuState = ref(false)
const scrolled = ref(false)
const isLoggedIn = ref(false)
const userName = ref('')

const arts = [
  {
    title: "太阳纹",
    icon: "Sunny",
    desc: "位于鼓面中心，象征着对太阳的崇拜。十二道光芒常代表一年中的十二个月，寓意祈求风调雨顺。"
  },
  {
    title: "蛙立饰",
    icon: "Compass",
    desc: "铜鼓边缘最常见的立体装饰。青蛙在壮族文化中是雨神的使者，反映了古老的稻作信仰。"
  },
  {
    title: "写实纹饰",
    icon: "Brush",
    desc: "包含翔鹭纹、羽人舞蹈纹、龙舟竞渡纹等，生动记录了先民狩猎、祭祀、劳作的生活场景。"
  },
  {
    title: "云雷纹",
    icon: "Cloudy",
    desc: "以连续的云纹和雷纹构成，象征着对自然力量的崇拜。云纹代表雨水，雷纹象征天鼓，共同祈求风调雨顺。"
  }
];

const checkLoginStatus = () => {
  const userStr = localStorage.getItem('user')
  if (userStr) {
    try {
      const user = JSON.parse(userStr)
      isLoggedIn.value = true
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

const handleLogout = () => {
  localStorage.removeItem('user')
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  
  isLoggedIn.value = false
  userName.value = ''
  
  router.push('/')
}

const toggleMenu = () => {
  menuState.value = !menuState.value
}

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

.section-desc {
  font-size: 1.1rem;
  color: #E5E5EA;
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.art-highlights {
  margin-top: 4rem;
  padding-top: 3rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.section-subtitle {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 2rem;
  color: white;
  text-align: center;
}

.highlight-content {
  max-width: 800px;
  margin: 0 auto;
}

.paragraph {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 1.5rem;
  color: #E5E5EA;
  text-align: center;
}

/* 卡片样式 */
.timeline-card {
  background: rgba(255, 255, 255, 0.01);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 1.5rem;
  transition: all 0.3s ease;
  text-align: center;
  width: 100%;
  max-width: 320px;
  margin-left: auto;
  margin-right: auto;
}

.timeline-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.timeline-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  margin-bottom: 1.5rem;
  color: #d4af37;
}

.timeline-title {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
}

.timeline-text {
  font-size: 1rem;
  color: #E5E5EA;
  line-height: 1.6;
  text-align: center;

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
  
  .timeline-card {
    padding: 1.5rem;
  }
  
  .timeline-icon {
    font-size: 2.5rem;
  }
}
</style>