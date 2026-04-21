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

    <!-- 主要内容 -->
    <main class="main-content">
      <section class="content-section">
        <div class="section-container">
          <h1 class="page-title gradient-text">前言</h1>
          <div class="content-wrapper">
            <div class="text-content">
              <p class="paragraph">
                铜鼓，是流行于我国南方及东南亚地区长达2700多年的一种青铜礼乐器。自古以来，铜鼓与当地各民族的社会、经济、文化、生活紧密地联系在一起，形成了独特的铜鼓文化。广西被称为"铜鼓之乡"，铜鼓文化在这里世代流传并发扬光大。
              </p>
              <p class="paragraph">
                它既是权势和财富的象征，也是祭祀、集众、战阵、庆典的重器。其独特的造型和丰富的纹饰，反映了使用民族当时的经济状况与文化面貌，堪称一部民族历史的百科全书。
              </p>
              <div class="cta-buttons">
                <div class="btn-glass" @click="router.push('/origin')">
                  <div class="btn-glass-shadow"></div>
                  <div class="btn-glass-backdrop"></div>
                  <div class="btn-glass-content">
                    <span>了解更多</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="image-content" style="flex: 1; max-width: 500px; display: flex; flex-direction: column; align-items: center;">
              <img
                src="@/assets/tonggu06.png"
                alt="铜鼓文化"
                class="rounded-img shadow-lg hover-lift interactive-card"
                style="width: 100%; aspect-ratio: 1;"
              />
              <div class="image-caption" style="margin-top: 1rem; text-align: center; width: 100%;">铜鼓王 —— 北流云雷纹大铜鼓</div>
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

.content-wrapper {
  display: flex;
  gap: 3rem;
  align-items: flex-start;
  margin-top: 2rem;
}

.text-content {
  flex: 1;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
}

.image-content {
  flex: 1;
  max-width: 500px;
  aspect-ratio: 1;
  position: relative;
  align-self: flex-start;
}

.paragraph {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  color: rgba(255, 255, 255, 0.8);
}

.cta-buttons {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
}

.rounded-img {
  border-radius: 50%;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: all 0.3s ease;
}

.image-caption {
  margin-top: 1rem;
  text-align: center;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.6);
  font-style: italic;
  animation: fadeInUp 0.8s ease-out forwards;
  animation-delay: 0.5s;
  opacity: 0;
}

.shadow-lg {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.hover-lift {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-lift:hover {
  transform: translateY(-10px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
}

.interactive-card {
  transition: all 0.3s ease;
}

.interactive-card:hover {
  transform: scale(1.02);
}

/* Responsive Design */
@media (max-width: 768px) {
  .content-wrapper {
    flex-direction: column;
  }
  
  .image-content {
    max-width: 100%;
    margin-top: 0;
  }
  
  .text-content {
    padding: 1.5rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .section-container {
    padding: 0 1rem;
  }
}

@media (min-width: 769px) {
  .image-content {
    margin-top: -70px;
  }
}
</style>