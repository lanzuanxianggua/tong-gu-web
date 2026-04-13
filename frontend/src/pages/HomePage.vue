<template>
  <div class="home-page-container">
    <!-- Ambient Background Layer -->
    <div class="ambient-bg"></div>
    
    <!-- Navigation System -->
    <header 
      class="home-nav" 
      :class="{ scrolled: scrolled }"
      role="banner"
    >
      <nav
        :data-state="menuState ? 'active' : undefined"
        aria-label="Main navigation"
      >
        <div class="home-nav-container">
          <div class="home-nav-content">
            <!-- Logo & Brand -->
            <div class="home-nav-brand">
              <div
                @click="router.push('/')"
                class="home-logo"
                role="link"
                tabindex="0"
                aria-label="返回首页"
              >
                <img
                  src="@/assets/tonggu_logo.png"
                  alt="铜鼓智能识别与数字化保护平台"
                  class="logo-image"
                  loading="eager"
                />
                <span class="logo-text">铜鼓智能识别与数字化保护平台</span>
              </div>

              <!-- Mobile Menu Toggle -->
              <button
                @click="toggleMenu"
                :aria-label="menuState ? '关闭菜单' : '打开菜单'"
                :aria-expanded="menuState"
                class="home-nav-toggle"
                type="button"
              >
                <svg
                  :class="['home-nav-toggle-icon', { active: menuState }]"
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <line x1="4" x2="20" y1="12" y2="12"/>
                  <line x1="4" x2="20" y1="6" y2="6"/>
                  <line x1="4" x2="20" y1="18" y2="18"/>
                </svg>
                <svg
                  :class="['home-nav-toggle-close', { active: menuState }]"
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <path d="M18 6 6 18"/>
                  <path d="m6 6 12 12"/>
                </svg>
              </button>

              <!-- Desktop Navigation Links -->
              <div class="home-nav-links">
                <ul role="menubar">
                  <li v-for="(item, index) in menuItems" :key="index" role="none">
                    <div
                      @click="router.push(item.href)"
                      @keydown.enter="router.push(item.href)"
                      class="home-nav-link cursor-pointer"
                      role="menuitem"
                      tabindex="0"
                    >
                      {{ item.name }}
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <!-- Mobile Menu / Actions Area -->
            <div
              :class="['home-nav-menu', { active: menuState }]"
              role="navigation"
              aria-label="Mobile navigation"
            >
              <!-- Mobile Navigation Links -->
              <div class="home-nav-mobile">
                <ul role="menu">
                  <li v-for="(item, index) in menuItems" :key="index" role="none">
                    <div
                      @click="handleMobileNavClick(item.href)"
                      class="home-nav-link cursor-pointer"
                      role="menuitem"
                      tabindex="0"
                    >
                      {{ item.name }}
                    </div>
                  </li>
                </ul>
              </div>

              <!-- Authentication Actions -->
              <div class="home-nav-actions">
                <template v-if="!isLoggedIn">
                  <div 
                    class="btn-glass" 
                    @click="router.push('/login')"
                    role="button"
                    tabindex="0"
                    aria-label="登录账户"
                  >
                    <div class="btn-glass-shadow"></div>
                    <div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content">
                      <span>登录</span>
                    </div>
                  </div>
                  
                  <div 
                    class="btn-glass" 
                    @click="router.push('/register')"
                    role="button"
                    tabindex="0"
                    aria-label="注册新账户"
                  >
                    <div class="btn-glass-shadow"></div>
                    <div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content">
                      <span>注册</span>
                    </div>
                  </div>
                </template>
                
                <template v-else>
                  <div class="home-user-info">
                    <span 
                      class="user-name" 
                      @click="handleProfileClick"
                      :title="userName"
                      role="button"
                      tabindex="0"
                      aria-label="查看个人资料"
                    >
                      {{ userName }}
                    </span>
                    
                    <div 
                      class="btn-glass" 
                      @click="handleLogout"
                      role="button"
                      tabindex="0"
                      aria-label="退出登录"
                    >
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
    
    <!-- Particle Animation Canvas -->
    <canvas
      ref="canvasRef"
      class="particle-canvas"
      @mousedown="handleMouseDown"
      @mouseup="handleMouseUp"
      @mousemove="handleMouseMove"
      @mouseleave="handleMouseLeave"
      @contextmenu.prevent
      aria-hidden="true"
    />
    
    <!-- SVG Filter Definitions -->
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
export const DEFAULT_WORDS = ["你好", "欢迎", "了解", "铜鼓"]
</script>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

import '@/styles/HomePage.css'

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

interface Vector2D {
  x: number
  y: number
}

interface RGBColor {
  r: number
  g: number
  b: number
}

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

  startColor: RGBColor = { r: 0, g: 0, b: 0 }
  targetColor: RGBColor = { r: 0, g: 0, b: 0 }
  colorWeight = 0
  colorBlendRate = 0.01

  move(): void {
    let proximityMult = 1
    const distance = Math.sqrt(
      Math.pow(this.pos.x - this.target.x, 2) + 
      Math.pow(this.pos.y - this.target.y, 2)
    )

    if (distance < this.closeEnoughTarget) {
      proximityMult = distance / this.closeEnoughTarget
    }

    const towardsTarget: Vector2D = {
      x: this.target.x - this.pos.x,
      y: this.target.y - this.pos.y,
    }

    const magnitude = Math.sqrt(towardsTarget.x * towardsTarget.x + towardsTarget.y * towardsTarget.y)
    
    if (magnitude > 0) {
      towardsTarget.x = (towardsTarget.x / magnitude) * this.maxSpeed * proximityMult
      towardsTarget.y = (towardsTarget.y / magnitude) * this.maxSpeed * proximityMult
    }

    const steer: Vector2D = {
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

  draw(ctx: CanvasRenderingContext2D, drawAsPoints: boolean): void {
    if (this.colorWeight < 1.0) {
      this.colorWeight = Math.min(this.colorWeight + this.colorBlendRate, 1.0)
    }

    const currentColor: RGBColor = {
      r: Math.round(this.startColor.r + (this.targetColor.r - this.startColor.r) * this.colorWeight),
      g: Math.round(this.startColor.g + (this.targetColor.g - this.startColor.g) * this.colorWeight),
      b: Math.round(this.startColor.b + (this.targetColor.b - this.startColor.b) * this.colorWeight),
    }

    ctx.fillStyle = `rgb(${currentColor.r}, ${currentColor.g}, ${currentColor.b})`

    if (drawAsPoints) {
      ctx.fillRect(this.pos.x, this.pos.y, 2, 2)
    } else {
      ctx.beginPath()
      ctx.arc(this.pos.x, this.pos.y, this.particleSize / 2, 0, Math.PI * 2)
      ctx.fill()
    }
  }

  kill(width: number, height: number): void {
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

interface Props {
  words?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  words: () => DEFAULT_WORDS
})

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

const generateRandomPos = (x: number, y: number, mag: number): Vector2D => {
  const randomX = Math.random() * 1000
  const randomY = Math.random() * 500

  const direction: Vector2D = {
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

const nextWord = (word: string, canvas: HTMLCanvasElement): void => {
  const offscreenCanvas = document.createElement("canvas")
  offscreenCanvas.width = canvas.width
  offscreenCanvas.height = canvas.height
  
  const offscreenCtx = offscreenCanvas.getContext("2d")!

  offscreenCtx.fillStyle = "#ffffff"
  offscreenCtx.font = "bold 150px 'Noto Sans SC', 'Inter', sans-serif"
  offscreenCtx.textAlign = "center"
  offscreenCtx.textBaseline = "middle"
  offscreenCtx.fillText(word, canvas.width / 2, canvas.height / 2)

  const imageData = offscreenCtx.getImageData(0, 0, canvas.width, canvas.height)
  const pixels = imageData.data

  const newColor: RGBColor = {
    r: Math.floor(Math.random() * 100) + 155,
    g: Math.floor(Math.random() * 100) + 155,
    b: Math.floor(Math.random() * 100) + 155,
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

const animate = (): void => {
  const canvas = canvasRef.value
  if (!canvas) return

  const ctx = canvas.getContext("2d")!
  const particles = particlesRef.value

  ctx.fillStyle = "rgba(0, 0, 0, 0.12)"
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

const handleMouseDown = (e: MouseEvent): void => {
  mouseRef.value.isPressed = true
  mouseRef.value.isRightClick = e.button === 2
  
  const rect = (e.target as HTMLCanvasElement).getBoundingClientRect()
  mouseRef.value.x = e.clientX - rect.left
  mouseRef.value.y = e.clientY - rect.top
}

const handleMouseUp = (): void => {
  mouseRef.value.isPressed = false
  mouseRef.value.isRightClick = false
}

const handleMouseMove = (e: MouseEvent): void => {
  const rect = (e.target as HTMLCanvasElement).getBoundingClientRect()
  mouseRef.value.x = e.clientX - rect.left
  mouseRef.value.y = e.clientY - rect.top
}

const handleMouseLeave = (): void => {
  mouseRef.value.isPressed = false
  mouseRef.value.isRightClick = false
}

const resizeCanvas = (): void => {
  const canvas = canvasRef.value
  if (!canvas) return

  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
  
  nextWord(props.words[wordIndexRef.value], canvas)
}

const toggleMenu = (): void => {
  menuState.value = !menuState.value
}

const handleMobileNavClick = (href: string): void => {
  router.push(href)
  menuState.value = false
}

const checkLoginStatus = (): void => {
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

const handleLogout = (): void => {
  localStorage.removeItem('user')
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  
  isLoggedIn.value = false
  userName.value = ''
  
  router.push('/')
}

const handleProfileClick = (): void => {
  router.push('/profile')
}

const handleScroll = (): void => {
  scrolled.value = window.scrollY > window.innerHeight * 0.05
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()
  
  checkLoginStatus()
  
  const canvas = canvasRef.value
  if (!canvas) return

  canvas.width = window.innerWidth
  canvas.height = window.innerHeight

  window.addEventListener('resize', resizeCanvas)

  nextWord(props.words[0], canvas)
  animate()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', resizeCanvas)
  
  if (animationRef.value) {
    cancelAnimationFrame(animationRef.value)
  }
})
</script>
