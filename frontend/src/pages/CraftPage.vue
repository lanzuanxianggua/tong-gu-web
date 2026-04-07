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
          <h1 class="page-title">制作工艺</h1>
          <p class="section-desc text-center">
            铜鼓的制作工艺是中国古代青铜铸造技术的杰出代表，展现了古代工匠的智慧和技艺
          </p>

          <!-- 工艺流程图 -->
          <div class="craft-process">
            <h2 class="section-subtitle">制作流程</h2>
            <div class="process-steps">
              <div class="process-step">
                <div class="step-number">1</div>
                <div class="step-content">
                  <h3>原料准备</h3>
                  <p>选用高质量的铜、锡、铅等金属原料，按照一定比例配制成合金。古代工匠通过长期实践，掌握了最佳的合金配比，确保铜鼓的音质和耐用性。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">2</div>
                <div class="step-content">
                  <h3>制模</h3>
                  <p>使用泥土制作铜鼓的内外模具。内模（芯）和外模（范）分别雕刻出铜鼓的内部和外部形状，包括复杂的纹饰图案。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">3</div>
                <div class="step-content">
                  <h3>合范浇注</h3>
                  <p>将内外模具合在一起，形成浇注空腔。通过浇注口将熔化的青铜合金注入模具中，待冷却后形成铜鼓的雏形。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">4</div>
                <div class="step-content">
                  <h3>脱模与修整</h3>
                  <p>待青铜完全冷却后，打破模具取出铜鼓。对铜鼓进行打磨、修整，去除多余的金属，使表面光滑平整。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">5</div>
                <div class="step-content">
                  <h3>纹饰雕刻</h3>
                  <p>在铜鼓表面雕刻或铸造精美的纹饰，包括太阳纹、云雷纹、蛙纹等。这些纹饰不仅美观，还具有深刻的文化内涵。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">6</div>
                <div class="step-content">
                  <h3>调音</h3>
                  <p>通过调整铜鼓的壁厚和形状，使铜鼓产生优美的音色。古代工匠凭借丰富的经验，能够制作出音质清脆、响亮的铜鼓。</p>
                </div>
              </div>
            </div>
          </div>

          <!-- 工艺特点 -->
          <div class="craft-features">
            <h2 class="section-subtitle">工艺特点</h2>
            <div class="features-grid">

              <div class="feature-card">
                <div class="feature-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                </div>
                <h3>合金配比</h3>
                <p>古代工匠掌握了精确的合金配比技术，使铜鼓具有良好的机械性能和音质。</p>
              </div>
              <div class="feature-card">
                <div class="feature-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                </div>
                <h3>调音技术</h3>
                <p>通过调整铜鼓的壁厚和形状，实现不同音高和音色的要求。</p>
              </div>
              <div class="feature-card">
                <div class="feature-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                </div>
                <h3>纹饰工艺</h3>
                <p>采用浮雕、线刻等多种工艺，在铜鼓表面创作精美的纹饰图案。</p>
              </div>
            </div>
          </div>

          <!-- 制作方法 -->
          <div class="craft-methods">
            <h2 class="section-subtitle">制作方法</h2>
            <div class="methods-grid">
              <!-- 失蜡铸造法 -->
              <div class="method-card">
                <h3>失蜡铸造法</h3>
                <div class="method-content">
                  <p>中国失蜡铸造技术起源于焚失法，最早见于商代中晚期，是一种青铜等金属器物的精密铸造方法。以蜂蜡做成铸件的模型，再用耐火材料填充泥芯和敷成外范。加热烘烤后，蜡模全部熔化流失，使整个铸件模型变成空壳再往内浇注金属溶液铸成器物。有学者认为，早至石寨山型铜鼓流行时期，失蜡法便被用于铜鼓铸造。</p>
                </div>
              </div>
              
              <!-- 泥型合范法 -->
              <div class="method-card">
                <h3>泥型合范法</h3>
                <div class="method-content">
                  <p>以筛选过的陶泥糅合草根、谷糠等为范模原料，以鼓形作内模，外范由2-4块组成，内模与外范之间的空隙为鼓壁厚度。工匠通过预留的浇口浇铸熔融后的铜锡铅合金溶液，浇铸后在鼓身留下明显的合范缝。</p>
                </div>
              </div>
            </div>
          </div>

          <!-- 现代传承 -->
          <div class="modern-heritage">
            <h2 class="section-subtitle">现代传承</h2>
            <div class="heritage-content">
              <p class="paragraph">
                如今，铜鼓制作工艺已被列入非物质文化遗产名录，得到了有效的保护和传承。现代工匠在继承传统工艺的基础上，结合现代技术，不断创新和发展铜鼓制作技艺。
              </p>
              <p class="paragraph">
                一些地区建立了铜鼓制作工坊，培养新一代铜鼓制作艺人，确保这一古老工艺能够继续传承下去。同时，铜鼓文化也通过各种展览和活动，被更多的人所了解和喜爱。
              </p>
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

/* 制作流程 */
.craft-process {
  margin-bottom: 4rem;
}

.section-subtitle {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 2rem;
  color: white;
}

.process-steps {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.process-step {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
  transition: all 0.3s ease;
}

.process-step:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.step-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #d4af37, #f4e4ba);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.step-content {
  flex: 1;
}

.step-content h3 {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: white;
}

.step-content p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #E5E5EA;
}

/* 工艺特点 */
.craft-features {
  margin-bottom: 4rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
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
}

.feature-card p {
  font-size: 1rem;
  line-height: 1.6;
  color: #E5E5EA;
}

/* 制作方法分类 */
.craft-methods {
  margin-bottom: 4rem;
}

.methods-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  gap: 3rem;
}

.method-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2.5rem;
  transition: all 0.3s ease;
}

.method-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  border-color: rgba(255, 255, 255, 0.2);
}

.method-card h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 2rem;
  color: white;
  text-align: center;
  background: linear-gradient(90deg, #d4af37, #f4e4ba, #d4af37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.method-content {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 0.8rem;
  padding: 1.5rem;
  border-left: 4px solid #d4af37;
}

.method-content p {
  font-size: 1rem;
  line-height: 1.6;
  color: #E5E5EA;
  margin: 0;
}

/* 现代传承 */
.modern-heritage {
  margin-bottom: 4rem;
}

.heritage-content {
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
  
  .process-step {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .step-number {
    margin-bottom: 1rem;
  }
  
  .section-subtitle {
    font-size: 1.5rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .methods-grid {
    grid-template-columns: 1fr;
  }
  
  .method-card {
    padding: 1.5rem;
  }
  
  .method-card h3 {
    font-size: 1.3rem;
  }
  
  .method-content {
    padding: 1rem;
  }
  
  .method-content p {
    font-size: 0.9rem;
  }
}
</style>