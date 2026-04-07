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

    <!-- 主要内容 -->
    <main class="main-content">
      <section class="content-section">
        <div class="section-container">
          <h1 class="page-title gradient-text animate-fade-in">起源与发展</h1>
          <p class="section-desc text-center animate-fade-in" style="animation-delay: 200ms;">
            铜鼓的发展历程跨越了2700多年，从最初的炊具演变为重要的礼乐器和权力象征
          </p>
          <div class="custom-timeline">
            <div class="timeline-item">
              <div class="timeline-node"></div>
              <div class="timeline-timestamp">公元前8世纪 (春秋早期)</div>
              <div class="timeline-content animate-fade-in-up" style="animation-delay: 200ms;">
                <div class="timeline-card interactive-card hover-lift">
                  <div class="timeline-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                  </div>
                  <h4 class="timeline-title">诞生：炊具的蜕变</h4>
                  <p class="timeline-text">
                    最早由居住在云南中西部礼社江流域的濮人创造。最初作为炊具"铜釜"，后逐渐演变为打击乐器。以"万家坝型"为代表，器壁浑厚，纹饰简朴。
                  </p>
                </div>
              </div>
            </div>
            
            <div class="timeline-item">
              <div class="timeline-node"></div>
              <div class="timeline-timestamp">战国至汉代</div>
              <div class="timeline-content animate-fade-in-up" style="animation-delay: 300ms;">
                <div class="timeline-card interactive-card hover-lift">
                  <div class="timeline-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  </div>
                  <h4 class="timeline-title">鼎盛：权力与艺术的结合</h4>
                  <p class="timeline-text">
                    滇人对铜鼓造型进一步美化，石寨山型铜鼓出现。此时铜鼓已成为用于祭祀、节日庆典和军事号令的礼器，是酋长权力的象征。
                  </p>
                </div>
              </div>
            </div>
            
            <div class="timeline-item">
              <div class="timeline-node"></div>
              <div class="timeline-timestamp">魏晋南北朝</div>
              <div class="timeline-content animate-fade-in-up" style="animation-delay: 400ms;">
                <div class="timeline-card interactive-card hover-lift">
                  <div class="timeline-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><path d="M9.59 4.59A2 2 0 1 1 11 8H2"/><path d="M14.42 15.41A2 2 0 1 0 13 19H2"/><path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.71 2.71"/></svg>
                  </div>
                  <h4 class="timeline-title">传播：文化的扩散</h4>
                  <p class="timeline-text">
                    铜鼓制作技术向东、向北传播，进入广西、广东、湖南等地。冷水冲型铜鼓兴起，纹饰更加精美，出现了翔鹭、羽人等图案。
                  </p>
                </div>
              </div>
            </div>
            
            <div class="timeline-item">
              <div class="timeline-node"></div>
              <div class="timeline-timestamp">唐宋时期</div>
              <div class="timeline-content animate-fade-in-up" style="animation-delay: 500ms;">
                <div class="timeline-card interactive-card hover-lift">
                  <div class="timeline-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  </div>
                  <h4 class="timeline-title">演变：风格的融合</h4>
                  <p class="timeline-text">
                    铜鼓制作达到新的高峰，出现了灵山型、西盟型等新类型。铜鼓的社会功能更加多样化，成为民族文化的重要载体。
                  </p>
                </div>
              </div>
            </div>
            
            <div class="timeline-item">
              <div class="timeline-node"></div>
              <div class="timeline-timestamp">明清至今</div>
              <div class="timeline-content animate-fade-in-up" style="animation-delay: 600ms;">
                <div class="timeline-card interactive-card hover-lift">
                  <div class="timeline-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-large"><path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/></svg>
                  </div>
                  <h4 class="timeline-title">传承：文化的延续</h4>
                  <p class="timeline-text">
                    铜鼓文化在西南少数民族地区继续传承，成为民族认同的重要标志。现代铜鼓制作工艺得到保护和发展，铜鼓文化被列入非物质文化遗产名录。
                  </p>
                </div>
              </div>
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
  margin-bottom: 1.5rem;
  color: white;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-desc {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

/* 时间线样式 */
.custom-timeline {
  margin-top: 3rem;
  position: relative;
}

.custom-timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, #d4af37, #f4e4ba, #ffffff);
}

.timeline-item {
  position: relative;
  margin-bottom: 3rem;
  padding-left: 2rem;
}

.timeline-node {
  position: absolute;
  left: -9px;
  top: 0.5rem;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: white;
  border: 3px solid #d4af37;
  box-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
}

.timeline-timestamp {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 600;
  margin-bottom: 1rem;
}

.timeline-content {
  padding-top: 0.5rem;
}

.timeline-card {
  padding: 2rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
  cursor: pointer;
}

.timeline-icon {
  display: inline-block;
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #d4af37, #f4e4ba);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.icon-large {
  font-size: 28px;
  color: white;
}

.timeline-title {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
}

.timeline-text {
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
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
  border-color: rgba(255, 255, 255, 0.2);
}

/* 动画效果 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.8s ease-out forwards;
}

.animate-fade-in-up {
  animation: fadeInUp 0.8s ease-out forwards;
}

/* 响应式设计 */
@media (max-width: 768px) {
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
    width: 48px;
    height: 48px;
  }
  
  .icon-large {
    font-size: 24px;
  }
}
</style>