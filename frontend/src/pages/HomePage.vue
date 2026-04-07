<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-black p-0 m-0 w-full">
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
    
    <!-- 粒子效果 -->
    <canvas
      ref="canvasRef"
      class="particle-canvas"
      @mousedown="handleMouseDown"
      @mouseup="handleMouseUp"
      @mousemove="handleMouseMove"
      @contextmenu.prevent
    />
    
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

<script lang="ts">
export const DEFAULT_WORDS = ["Hello", "Welcome", "Learn","Tong Gu"]
</script>

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

// 类型定义
interface Vector2D {
  x: number
  y: number
}

// Particle 类（保持不变）
class Particle {
  pos: Vector2D = { x: 0, y: 0 }
  vel: Vector2D = { x: 0, y: 0 }
  acc: Vector2D = { x: 0, y: 0 }
  target: Vector2D = { x: 0, y: 0 }

  closeEnoughTarget = 100
  maxSpeed = 1.0
  maxForce = 0.1
  particleSize = 10
  isKilled = false

  startColor = { r: 0, g: 0, b: 0 }
  targetColor = { r: 0, g: 0, b: 0 }
  colorWeight = 0
  colorBlendRate = 0.01

  move() {
    let proximityMult = 1
    const distance = Math.sqrt(
      Math.pow(this.pos.x - this.target.x, 2) + 
      Math.pow(this.pos.y - this.target.y, 2)
    )

    if (distance < this.closeEnoughTarget) {
      proximityMult = distance / this.closeEnoughTarget
    }

    const towardsTarget = {
      x: this.target.x - this.pos.x,
      y: this.target.y - this.pos.y,
    }

    const magnitude = Math.sqrt(towardsTarget.x * towardsTarget.x + towardsTarget.y * towardsTarget.y)
    if (magnitude > 0) {
      towardsTarget.x = (towardsTarget.x / magnitude) * this.maxSpeed * proximityMult
      towardsTarget.y = (towardsTarget.y / magnitude) * this.maxSpeed * proximityMult
    }

    const steer = {
      x: towardsTarget.x - this.vel.x,
      y: towardsTarget.y - this.vel.y,
    }

    const steerMagnitude = Math.sqrt(steer.x * steer.x + steer.y * steer.y)
    if (steerMagnitude > 0) {
      steer.x = (steer.x / steerMagnitude) * this.maxForce
      steer.y = (steer.y / steerMagnitude) * this.maxForce
    }

    this.acc.x += steer.x
    this.acc.y += steer.y

    this.vel.x += this.acc.x
    this.vel.y += this.acc.y
    this.pos.x += this.vel.x
    this.pos.y += this.vel.y
    this.acc.x = 0
    this.acc.y = 0
  }

  draw(ctx: CanvasRenderingContext2D, drawAsPoints: boolean) {
    if (this.colorWeight < 1.0) {
      this.colorWeight = Math.min(this.colorWeight + this.colorBlendRate, 1.0)
    }

    const currentColor = {
      r: Math.round(this.startColor.r + (this.targetColor.r - this.startColor.r) * this.colorWeight),
      g: Math.round(this.startColor.g + (this.targetColor.g - this.startColor.g) * this.colorWeight),
      b: Math.round(this.startColor.b + (this.targetColor.b - this.startColor.b) * this.colorWeight),
    }

    if (drawAsPoints) {
      ctx.fillStyle = `rgb(${currentColor.r}, ${currentColor.g}, ${currentColor.b})`
      ctx.fillRect(this.pos.x, this.pos.y, 2, 2)
    } else {
      ctx.fillStyle = `rgb(${currentColor.r}, ${currentColor.g}, ${currentColor.b})`
      ctx.beginPath()
      ctx.arc(this.pos.x, this.pos.y, this.particleSize / 2, 0, Math.PI * 2)
      ctx.fill()
    }
  }

  kill(width: number, height: number) {
    if (!this.isKilled) {
      const randomPos = generateRandomPos(width / 2, height / 2, (width + height) / 2)
      this.target.x = randomPos.x
      this.target.y = randomPos.y

      this.startColor = {
        r: this.startColor.r + (this.targetColor.r - this.startColor.r) * this.colorWeight,
        g: this.startColor.g + (this.targetColor.g - this.startColor.g) * this.colorWeight,
        b: this.startColor.b + (this.targetColor.b - this.startColor.b) * this.colorWeight,
      }
      this.targetColor = { r: 0, g: 0, b: 0 }
      this.colorWeight = 0

      this.isKilled = true
    }
  }
}

// Props 定义
interface Props {
  words?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  words: () => DEFAULT_WORDS
})

// 响应式 Refs
const canvasRef = ref<HTMLCanvasElement | null>(null)
const animationRef = ref<number | null>(null)
const particlesRef = ref<Particle[]>([])
const frameCountRef = ref(0)
const wordIndexRef = ref(0)
const mouseRef = ref({
  x: 0,
  y: 0,
  isPressed: false,
  isRightClick: false
})

const pixelSteps = 6
const drawAsPoints = true

// 工具函数
const generateRandomPos = (x: number, y: number, mag: number): Vector2D => {
  const randomX = Math.random() * 1000
  const randomY = Math.random() * 500

  const direction = {
    x: randomX - x,
    y: randomY - y,
  }

  const magnitude = Math.sqrt(direction.x * direction.x + direction.y * direction.y)
  if (magnitude > 0) {
    direction.x = (direction.x / magnitude) * mag
    direction.y = (direction.y / magnitude) * mag
  }

  return {
    x: x + direction.x,
    y: y + direction.y,
  }
}

// 切换文字
const nextWord = (word: string, canvas: HTMLCanvasElement) => {
  const offscreenCanvas = document.createElement("canvas")
  offscreenCanvas.width = canvas.width
  offscreenCanvas.height = canvas.height
  const offscreenCtx = offscreenCanvas.getContext("2d")!

  offscreenCtx.fillStyle = "white"
  offscreenCtx.font = "bold 150px Arial"
  offscreenCtx.textAlign = "center"
  offscreenCtx.textBaseline = "middle"
  offscreenCtx.fillText(word, canvas.width / 2, canvas.height / 2)

  const imageData = offscreenCtx.getImageData(0, 0, canvas.width, canvas.height)
  const pixels = imageData.data

  const newColor = {
    r: Math.random() * 255,
    g: Math.random() * 255,
    b: Math.random() * 255,
  }

  const particles = particlesRef.value
  let particleIndex = 0

  const coordsIndexes: number[] = []
  for (let i = 0; i < pixels.length; i += pixelSteps * 4) {
    coordsIndexes.push(i)
  }

  for (let i = coordsIndexes.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[coordsIndexes[i], coordsIndexes[j]] = [coordsIndexes[j], coordsIndexes[i]]
  }

  for (const coordIndex of coordsIndexes) {
    const pixelIndex = coordIndex
    const alpha = pixels[pixelIndex + 3]

    if (alpha > 0) {
      const x = (pixelIndex / 4) % canvas.width
      const y = Math.floor(pixelIndex / 4 / canvas.width)

      let particle: Particle

      if (particleIndex < particles.length) {
        particle = particles[particleIndex]
        particle.isKilled = false
        particleIndex++
      } else {
        particle = new Particle()
        const randomPos = generateRandomPos(canvas.width / 2, canvas.height / 2, (canvas.width + canvas.height) / 2)
        particle.pos.x = randomPos.x
        particle.pos.y = randomPos.y

        particle.maxSpeed = Math.random() * 6 + 4
        particle.maxForce = particle.maxSpeed * 0.05
        particle.particleSize = Math.random() * 6 + 6
        particle.colorBlendRate = Math.random() * 0.0275 + 0.0025

        particles.push(particle)
      }

      particle.startColor = {
        r: particle.startColor.r + (particle.targetColor.r - particle.startColor.r) * particle.colorWeight,
        g: particle.startColor.g + (particle.targetColor.g - particle.startColor.g) * particle.colorWeight,
        b: particle.startColor.b + (particle.targetColor.b - particle.startColor.b) * particle.colorWeight,
      }
      particle.targetColor = newColor
      particle.colorWeight = 0

      particle.target.x = x
      particle.target.y = y
    }
  }

  for (let i = particleIndex; i < particles.length; i++) {
    particles[i].kill(canvas.width, canvas.height)
  }
}

// 动画循环
const animate = () => {
  const canvas = canvasRef.value
  if (!canvas) return

  const ctx = canvas.getContext("2d")!
  const particles = particlesRef.value

  ctx.fillStyle = "rgba(0, 0, 0, 0.1)"
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  for (let i = particles.length - 1; i >= 0; i--) {
    const particle = particles[i]
    particle.move()
    particle.draw(ctx, drawAsPoints)

    if (particle.isKilled) {
      if (
        particle.pos.x < 0 ||
        particle.pos.x > canvas.width ||
        particle.pos.y < 0 ||
        particle.pos.y > canvas.height
      ) {
        particles.splice(i, 1)
      }
    }
  }

  if (mouseRef.value.isPressed && mouseRef.value.isRightClick) {
    particles.forEach((particle) => {
      const distance = Math.sqrt(
        Math.pow(particle.pos.x - mouseRef.value.x, 2) + 
        Math.pow(particle.pos.y - mouseRef.value.y, 2),
      )
      if (distance < 50) {
        particle.kill(canvas.width, canvas.height)
      }
    })
  }

  frameCountRef.value++
  if (frameCountRef.value % 240 === 0) {
    wordIndexRef.value = (wordIndexRef.value + 1) % props.words.length
    nextWord(props.words[wordIndexRef.value], canvas)
  }

  animationRef.value = requestAnimationFrame(animate)
}

// 鼠标事件处理
const handleMouseDown = (e: MouseEvent) => {
  mouseRef.value.isPressed = true
  mouseRef.value.isRightClick = e.button === 2
  const rect = (e.target as HTMLCanvasElement).getBoundingClientRect()
  mouseRef.value.x = e.clientX - rect.left
  mouseRef.value.y = e.clientY - rect.top
}

const handleMouseUp = () => {
  mouseRef.value.isPressed = false
  mouseRef.value.isRightClick = false
}

const handleMouseMove = (e: MouseEvent) => {
  const rect = (e.target as HTMLCanvasElement).getBoundingClientRect()
  mouseRef.value.x = e.clientX - rect.left
  mouseRef.value.y = e.clientY - rect.top
}

// 工具函数
const resizeCanvas = () => {
  const canvas = canvasRef.value
  if (!canvas) return

  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
  
  nextWord(props.words[wordIndexRef.value], canvas)
}

// 生命周期
onMounted(() => {
  const canvas = canvasRef.value
  if (!canvas) return

  canvas.width = window.innerWidth
  canvas.height = window.innerHeight

  window.addEventListener('resize', resizeCanvas)

  nextWord(props.words[0], canvas)
  animate()
})

onUnmounted(() => {
  if (animationRef.value) {
    cancelAnimationFrame(animationRef.value)
  }
  window.removeEventListener('resize', resizeCanvas)
})
</script>