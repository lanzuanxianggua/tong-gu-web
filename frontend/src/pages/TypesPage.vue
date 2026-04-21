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
              <div @click="router.push('/')" aria-label="home" class="home-logo cursor-pointer">
                <img src="@/assets/tonggu_logo.png" alt="铜鼓智能识别与数字化保护平台" class="logo-image" />
                <span class="logo-text">铜鼓智能识别与数字化保护平台</span>
              </div>

              <!-- 移动端菜单切换按钮 -->
              <button @click="toggleMenu" :aria-label="menuState ? 'Close Menu' : 'Open Menu'" class="home-nav-toggle">
                <svg :class="['home-nav-toggle-icon', { active: menuState }]" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="4" x2="20" y1="12" y2="12"/>
                  <line x1="4" x2="20" y1="6" y2="6"/>
                  <line x1="4" x2="20" y1="18" y2="18"/>
                </svg>
                <svg :class="['home-nav-toggle-close', { active: menuState }]" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 6 6 18"/>
                  <path d="m6 6 12 12"/>
                </svg>
              </button>

              <!-- 桌面端导航链接 -->
              <div class="home-nav-links">
                <ul>
                  <li v-for="(item, index) in menuItems" :key="index">
                    <div @click="router.push(item.href)" class="home-nav-link cursor-pointer">
                      <span>{{ item.name }}</span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <!-- 移动端菜单 / 桌面端按钮区域 -->
            <div :class="['home-nav-menu', { active: menuState }]">
              <div class="home-nav-mobile">
                <ul>
                  <li v-for="(item, index) in menuItems" :key="index">
                    <div @click="router.push(item.href)" class="home-nav-link cursor-pointer">
                      <span>{{ item.name }}</span>
                    </div>
                  </li>
                </ul>
              </div>

              <div class="home-nav-actions">
                <template v-if="!isLoggedIn">
                  <div class="btn-glass" @click="router.push('/login')">
                    <div class="btn-glass-shadow"></div>
                    <div class="btn-glass-backdrop"></div>
                    <div class="btn-glass-content"><span>登录</span></div>
                  </div>
                  <div class="btn-glass" @click="router.push('/register')">
                    <div class="btn-glass-shadow"></div>
                    <div class="btn-glass-backdrop"></div>
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
                      <div class="btn-glass-shadow"></div>
                      <div class="btn-glass-backdrop"></div>
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
          <h1 class="page-title gradient-text">铜鼓类型</h1>
          <p class="section-desc text-center">
            我国学者按标准器出土地命名原则，将铜鼓分为八大类型，其中三型以广西地名命名
          </p>
          
          <!-- 铜鼓分型法介绍 -->
          <div class="classification-intro">
            <h2 class="section-subtitle">铜鼓分型法</h2>
            <div class="intro-content">
              <p class="paragraph">
                我国学者按标准器出土地命名原则，将铜鼓分为万家坝、石寨山、冷水冲、北流、灵山、遵义、西盟、麻江八大类型。其中，以广西地名命名的铜鼓类型有冷水冲、北流、灵山三型。此三型鼓的共同特点是体型硕大、通体纹饰。
              </p>
              <p class="paragraph">
                八型法已得到国内外学界越来越广泛的认可。此外，国外一些学者采用黑格尔四型法对铜鼓进行分类。
              </p>
            </div>
          </div>
          
          <!-- 铜鼓年代表 -->
          <div class="timeline-section">
            <h2 class="section-subtitle">中国古代铜鼓年代表</h2>
            <div class="timeline-container">
              <div class="copper-drum-table">
                <table>
                  <thead>
                    <tr>
                      <th>类型名称</th>
                      <th>流行年代</th>
                      <th>主要特征</th>
                      <th>分布地区</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>万家坝型</td>
                      <td>春秋中期至战国晚期（约公元前8世纪-公元前3世纪）</td>
                      <td>鼓面较小，胸部膨胀，胸径大于面径，腰部上端最小，往下逐渐展开呈梯形；花纹简单，鼓面一般有太阳纹</td>
                      <td>云南中部，广西西部、越南西北部和泰国北部</td>
                    </tr>
                    <tr>
                      <td>石寨山型</td>
                      <td>战国晚期至西汉晚期（约公元前4世纪-公元前1世纪）</td>
                      <td>铸工精良，整鼓遍布花纹，鼓面径大于腰径，胸部膨胀较小，腰部呈梯形；装饰花纹有几何形花纹和写实花纹</td>
                      <td>云南晋宁、四川会理、贵州赫章、广西玉林等</td>
                    </tr>
                    <tr>
                      <td>冷水冲型</td>
                      <td>西汉中期至南朝时期（约公元前1世纪-公元6世纪）</td>
                      <td>体型高大，鼓面不出沿或略出沿，鼓胸微胀，胸径略大于面径或者等于面径；鼓面开始出现立体的青蛙或乘骑、马、水禽、龟等立体雕塑</td>
                      <td>广西藤县冷水冲为代表，主要分布在广西地区</td>
                    </tr>
                    <tr>
                      <td>北流型</td>
                      <td>西汉至唐代（约公元前1世纪-公元9世纪）</td>
                      <td>体形硕大，鼓面大于胸径而出沿，有的鼓还形成垂檐，胸腰收缩不明显，以1圈浅凹槽分界，腰和足则以1圈凸棱分界；鼓面一般有4只立体雕塑青蛙</td>
                      <td>广西北流为代表，主要分布在广西、广东地区</td>
                    </tr>
                    <tr>
                      <td>灵山型</td>
                      <td>东汉至唐代（约公元1世纪-公元9世纪）</td>
                      <td>鼓面大于胸而出沿，鼓胸圆而凸。鼓面一般装饰6只立体雕塑青蛙，有的青蛙大、小背负而成“累蛙”，青蛙的后面2足并拢相连，看上去是“三足蛙”</td>
                      <td>广西灵山为代表，主要分布在广西地区</td>
                    </tr>
                    <tr>
                      <td>遵义型</td>
                      <td>唐、宋时期（约公元7世纪-13世纪）</td>
                      <td>鼓面基本无立体青蛙装饰，胸腰逐渐收缩，没有转折和明显分界线；纹饰简单，除新出现的一圈乳钉纹外，还有同心圆圈纹、复线角形纹、树叶纹、游旗纹等</td>
                      <td>贵州遵义为代表，主要分布在贵州、广西、云南、四川等地</td>
                    </tr>
                    <tr>
                      <td>西盟型</td>
                      <td>唐代至现代（约公元7世纪-至今）</td>
                      <td>鼓形瘦高，上大下小，胸、腰、足无分界，整鼓形状似桶；装饰在鼓面的有立雕青蛙或累蛙，鼓身花纹有云、雷、米粒、团花、翎眼、同心圆圈、羽毛、栉、鹭、定胜、变形羽人等纹饰</td>
                      <td>云南西盟为代表，主要分布在云南西南部和东南亚地区</td>
                    </tr>
                    <tr>
                      <td>麻江型</td>
                      <td>南宋至晚清（约公元12世纪-19世纪）</td>
                      <td>体型小而扁矮，胸、腰、足转折柔和，已无明显分界，鼓腰中部有1圈凸棱；鼓面没有立体动物装饰，花纹有游旗、翎眼、生肖、八卦、云雷、栉纹等</td>
                      <td>贵州麻江为代表，广泛分布于两广、滇、黔、川、湘、海南等省区</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          <!-- 铜鼓类型关系示意图 -->
          <div class="relationship-section">
            <h2 class="section-subtitle">中国古代铜鼓类型关系示意图</h2>
            <div class="relationship-container">
              <img src="../assets/tonggu04.png" alt="中国古代铜鼓类型关系示意图" class="relationship-image rounded-img shadow-lg" />
            </div>
          </div>
          
          <!-- 八大类型详情 - 滑动标签页 -->
          <div class="type-details">
            <h2 class="section-subtitle">八大类型详情</h2>
            
            <!-- 滑动标签导航 -->
            <div class="slide-tabs-container">
              <div class="slide-tabs-wrapper">
                <ul
                  class="slide-tabs-list"
                >
                  <li
                    v-for="(tab, i) in tabs"
                    :key="tab.id"
                    :ref="(el) => setTabRef(el, i)"
                    @click="() => { selected = i; updateCursorPosition(i); }"
                    class="slide-tab-item"
                    :class="{ active: selected === i }"
                  >
                    {{ tab.name }}
                  </li>
                  <!-- 滑动光标 -->
                  <li 
                    class="slide-cursor"
                    :style="cursorStyle"
                  />
                </ul>
              </div>
            </div>

            <!-- 内容展示区 -->
            <div class="tab-content-area">
              <TransitionGroup name="fade">
                <div 
                  v-for="(tab, i) in tabs" 
                  :key="tab.id"
                  v-show="selected === i" 
                  class="content-wrapper"
                >
                  <div class="type-content">
                    <div style="flex: 0 0 300px; display: flex; flex-direction: column; align-items: center;">
                      <img 
                        :src="tab.image" 
                        :alt="tab.title" 
                        class="type-image rounded-img shadow-lg hover-lift" 
                        style="width: 100%; max-width: 300px; height: auto;"
                      />
                      <p class="image-caption" style="text-align: center; margin-top: 1rem; width: 100%;">{{ tab.imageCaption }}</p>
                    </div>
                    <div class="text-content">
                      <h3 class="tab-title">{{ tab.title }}</h3>
                      <div class="info-grid">
                        <div class="info-item">
                          <span class="info-label">出土地点：</span>
                          <span class="info-value">{{ tab.location }}</span>
                        </div>
                        <div class="info-item">
                          <span class="info-label">年代时期：</span>
                          <span class="info-value">{{ tab.period }}</span>
                        </div>
                        <div class="info-item">
                          <span class="info-label">主要特征：</span>
                          <span class="info-value">{{ tab.features }}</span>
                        </div>
                      </div>
                      <p class="paragraph">{{ tab.description1 }}</p>
                      <p class="paragraph">{{ tab.description2 }}</p>
                      <div class="cultural-value">
                        <h4 class="value-title">文化价值</h4>
                        <p class="paragraph">{{ tab.culturalValue }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </TransitionGroup>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- SVG Filter Definition -->
    <svg class="svg-filters" aria-hidden="true">
      <defs>
        <filter id="container-glass" x="0%" y="0%" width="100%" height="100%" color-interpolation-filters="sRGB">
          <feTurbulence type="fractalNoise" baseFrequency="0.05 0.05" numOctaves="1" seed="1" result="turbulence" />
          <feGaussianBlur in="turbulence" stdDeviation="2" result="blurredNoise" />
          <feDisplacementMap in="SourceGraphic" in2="blurredNoise" scale="70" xChannelSelector="R" yChannelSelector="B" result="displaced" />
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

<script setup>
import { ref, reactive, watch, nextTick, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import '@/styles/HomePage.css'
import BackToTop from '@/components/BackToTop.vue'
import Footer from '@/components/Footer.vue'
import tonggu_type01 from '@/assets/tonggu_type01.png'
import tonggu_type02 from '@/assets/tonggu_type02.png'
import tonggu_type03 from '@/assets/tonggu_type03.png'
import tonggu_type04 from '@/assets/tonggu_type04.png'
import tonggu_type05 from '@/assets/tonggu_type05.png'
import tonggu_type06 from '@/assets/tonggu_type06.png'
import tonggu_type07 from '@/assets/tonggu_type07.png'
import tonggu_type08 from '@/assets/tonggu_type08.png'

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

const selected = ref(0)
const tabRefs = ref([])
const cursorPosition = reactive({
  left: 0,
  width: 0,
  opacity: 0,
})

const cursorStyle = computed(() => ({
  left: `${cursorPosition.left}px`,
  width: `${cursorPosition.width}px`,
  opacity: cursorPosition.opacity,
}))

const setTabRef = (el, index) => {
  if (el) {
    tabRefs.value[index] = el
  }
}

const updateCursorPosition = (index) => {
  const selectedTab = tabRefs.value[index]
  if (selectedTab) {
    const { width } = selectedTab.getBoundingClientRect()
    cursorPosition.left = selectedTab.offsetLeft
    cursorPosition.width = width
    cursorPosition.opacity = 1
  }
}

watch(selected, (newVal) => {
  nextTick(() => {
    updateCursorPosition(newVal)
  })
}, { immediate: true })

const handleMouseEnter = (index) => {}

const handleMouseLeave = () => {}

// 八大铜鼓类型数据
const tabs = [
  {
    id: 'wanjiaba',
    name: '万家坝型',
    title: '万家坝型铜鼓',
    location: '云南楚雄万家坝',
    period: '春秋早期（约公元前8世纪）',
    features: '器壁较厚，器形高大，鼓面较小，无花纹或仅有简单几何纹',
    description1: '万家坝型铜鼓是目前发现的最早类型的铜鼓，代表了铜鼓艺术的萌芽时期。生活在我国云南省中西部地区的濮人从炊具铜釜中创造了这种打击乐器，开启了铜鼓文化的先河。',
    description2: '此型铜鼓是铜鼓的原始形态，反映了铜鼓从炊具向乐器演变的早期阶段。它的发现对于研究铜鼓的起源和发展具有重要意义，被誉为"铜鼓之祖"。',
    culturalValue: '万家坝型铜鼓是铜鼓文化的源头，见证了古代濮人的智慧创造，为研究中国南方古代民族的历史、文化、冶金技术提供了珍贵的实物资料。',
    image: tonggu_type01,
    imageCaption: '万家坝型铜鼓示意图'
  },
  {
    id: 'shizhaishan',
    name: '石寨山型',
    title: '石寨山型铜鼓',
    location: '云南晋宁石寨山',
    period: '战国至汉代（公元前475年-公元220年）',
    features: '器形较矮胖，鼓面较大，纹饰丰富精美',
    description1: '石寨山型铜鼓以云南晋宁石寨山出土的铜鼓为代表，是铜鼓发展的鼎盛时期的代表。其纹饰生动地反映了古代滇人的社会生活和文化信仰，常见翔鹭纹、羽人舞蹈纹、龙舟竞渡纹等。',
    description2: '此型铜鼓工艺精湛，纹饰繁缛，内容丰富，是古滇国青铜文化的重要组成部分。它不仅是一种乐器，更是权力和财富的象征，在祭祀、战争、宴乐等重要场合使用。',
    culturalValue: '石寨山型铜鼓是滇国文化的标志性器物，其丰富的纹饰为研究古代滇国的社会结构、宗教信仰、生产生活提供了直观的图像资料，具有极高的历史和艺术价值。',
    image: tonggu_type02,
    imageCaption: '石寨山型铜鼓示意图'
  },
  {
    id: 'lengshuichong',
    name: '冷水冲型',
    title: '冷水冲型铜鼓',
    location: '广西藤县冷水冲',
    period: '汉代至唐代（公元前221年-公元960年）',
    features: '器形高大，鼓面直径大于鼓胸，纹饰精美繁复',
    description1: '冷水冲型铜鼓以广西藤县冷水冲出土的铜鼓为代表，是广西地区最具代表性的铜鼓类型之一。其特点是体型硕大、通体纹饰，常见云雷纹、变形羽人纹、乘骑纹等。',
    description2: '此型铜鼓的出现标志着铜鼓文化在广西的繁荣发展，是骆越文化的重要遗存。它的分布范围广泛，影响深远，对研究岭南地区古代民族的历史文化具有重要价值。',
    culturalValue: '冷水冲型铜鼓是广西铜鼓文化的典型代表，体现了古代骆越民族高超的青铜铸造技艺和独特的审美观念，是研究岭南地区民族史、艺术史的重要实物资料。',
    image: tonggu_type03,
    imageCaption: '冷水冲型铜鼓示意图'
  },
  {
    id: 'beiliu',
    name: '北流型',
    title: '北流型铜鼓',
    location: '广西北流',
    period: '汉代至唐代（公元前221年-公元960年）',
    features: '体型硕大雄浑，鼓面宽大，纹饰华丽精美',
    description1: '北流型铜鼓以广西北流出土的铜鼓为代表，是广西地区重要的铜鼓类型之一。其特点是体型硕大、纹饰华丽，常见太阳纹、云雷纹、夔纹等，工艺精湛，气势恢宏。',
    description2: '此型铜鼓以其雄浑的体型和精美的纹饰著称，是岭南地区铜鼓文化繁荣发展的见证。它不仅是乐器，更是权力的象征，在古代社会中具有崇高的地位。',
    culturalValue: '北流型铜鼓是广西铜鼓文化的瑰宝，其宏大的体量和精美的纹饰展现了古代岭南民族的强盛与繁荣，对于研究中国古代南方民族的历史文化具有重要价值。',
    image: tonggu_type04,
    imageCaption: '北流型铜鼓示意图'
  },
  {
    id: 'lingshan',
    name: '灵山型',
    title: '灵山型铜鼓',
    location: '广西灵山',
    period: '唐代至宋代（公元618年-公元1279年）',
    features: '器形小巧玲珑，鼓面饰有复杂精细的花纹',
    description1: '灵山型铜鼓以广西灵山出土的铜鼓为代表，是铜鼓发展后期的代表。其特点是器形小巧玲珑，纹饰更加精细，常见花卉纹、鸟兽纹、人物纹等，工艺精湛。',
    description2: '此型铜鼓反映了铜鼓文化在唐宋时期的演变，纹饰更加世俗化和精细化，体现了当时高超的工艺水平和独特的审美趣味。它既是乐器，也是精美的艺术品。',
    culturalValue: '灵山型铜鼓是铜鼓文化后期的精品，其精细的纹饰和小巧的形制反映了铜鼓功能的转变和审美观念的变化，对于研究唐宋时期南方民族文化具有重要价值。',
    image: tonggu_type05,
    imageCaption: '灵山型铜鼓示意图'
  },
  {
    id: 'zunyi',
    name: '遵义型',
    title: '遵义型铜鼓',
    location: '贵州遵义',
    period: '宋代至明清（公元960年-公元1644年）',
    features: '器形中等，鼓面较平，纹饰简化',
    description1: '遵义型铜鼓以贵州遵义出土的铜鼓为代表，是铜鼓发展后期的一种类型。其特点是器形中等，鼓面较平，纹饰简化，常见几何纹和动物纹，风格朴实。',
    description2: '此型铜鼓主要分布在贵州地区，反映了铜鼓文化在贵州的发展演变。虽然纹饰简化，但仍保留了铜鼓的基本特征和文化内涵，是研究贵州少数民族历史的重要资料。',
    culturalValue: '遵义型铜鼓是贵州地区铜鼓文化的代表，体现了铜鼓文化在西南山区的传播与演变，对于研究贵州苗族、布依族等少数民族的历史文化具有重要价值。',
    image: tonggu_type06,
    imageCaption: '遵义型铜鼓示意图'
  },
  {
    id: 'ximeng',
    name: '西盟型',
    title: '西盟型铜鼓',
    location: '云南西盟',
    period: '明清时期（公元1368年-公元1912年）',
    features: '器形高大，鼓面较小，纹饰简单古朴',
    description1: '西盟型铜鼓以云南西盟出土的铜鼓为代表，主要分布在云南西南部和东南亚地区。其特点是器形高大，鼓面较小，纹饰简单，常见几何纹和动物纹。',
    description2: '此型铜鼓是铜鼓文化在边疆地区的延续和发展，也是铜鼓文化向东南亚传播的重要见证。它在当地民族的社会生活中仍占有重要地位，至今仍在使用。',
    culturalValue: '西盟型铜鼓是铜鼓文化跨境传播的重要证据，对于研究中国与东南亚国家的文化交流、民族迁徙以及铜鼓文化的传播路径具有重要价值。',
    image: tonggu_type07,
    imageCaption: '西盟型铜鼓示意图'
  },
  {
    id: 'majiang',
    name: '麻江型',
    title: '麻江型铜鼓',
    location: '贵州麻江',
    period: '明清时期（公元1368年-公元1912年）',
    features: '器形小巧，鼓面较平，纹饰简化，常见吉祥图案',
    description1: '麻江型铜鼓以贵州麻江出土的铜鼓为代表，是铜鼓发展的最后阶段的代表。其特点是器形小巧，鼓面较平，纹饰简化，常见几何纹和吉祥图案，风格朴实。',
    description2: '此型铜鼓主要分布在贵州、广西等地，是铜鼓文化的延续和演变。虽然形制简化，但仍承载着丰富的文化内涵，至今仍在一些少数民族地区使用。',
    culturalValue: '麻江型铜鼓是铜鼓文化的活态遗存，至今仍在苗族、布依族等民族的重要节庆中使用，是研究铜鼓文化传承与保护的珍贵资料，具有活态文化遗产价值。',
    image: tonggu_type08,
    imageCaption: '麻江型铜鼓示意图'
  }
]



// 生命周期
onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  handleScroll()
  checkLoginStatus()
  nextTick(() => {
    updateCursorPosition(selected.value)
  })
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

/* 基础样式 */
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

.section-subtitle {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 2rem;
  color: white;
  background: linear-gradient(90deg, #d4af37, #f4e4ba);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-align: center;
}

.classification-intro {
  margin-bottom: 4rem;
}

.intro-content {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
}

.timeline-section {
  margin-bottom: 4rem;
}

.timeline-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
}

.timeline-image {
  max-width: 100%;
  height: auto;
}

/* 铜鼓年代表表格样式 */
.copper-drum-table {
  width: 100%;
  overflow-x: auto;
}

.copper-drum-table table {
  width: 100%;
  border-collapse: collapse;
  color: white;
}

.copper-drum-table th,
.copper-drum-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.copper-drum-table th {
  background-color: rgba(212, 175, 55, 0.1);
  font-weight: 600;
  color: #d4af37;
}

.copper-drum-table tr:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

.copper-drum-table td {
  background-color: rgba(0, 0, 0, 0.3);
}

/* 响应式表格 */
@media (max-width: 768px) {
  .copper-drum-table {
    font-size: 0.875rem;
  }
  
  .copper-drum-table th,
  .copper-drum-table td {
    padding: 0.75rem;
  }
  
  .copper-drum-table th {
    font-size: 0.875rem;
  }
}

.relationship-section {
  margin-bottom: 4rem;
}

.relationship-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
}

.relationship-image {
  max-width: 100%;
  height: auto;
}

.type-details {
  margin-bottom: 4rem;
}

/* 滑动标签页样式 */
.slide-tabs-container {
  margin-bottom: 2rem;
  display: flex;
  justify-content: center;
}

.slide-tabs-wrapper {
  position: relative;
}

.slide-tabs-list {
  position: relative;
  display: flex;
  width: fit-content;
  border-radius: 9999px;
  border: 2px solid white;
  background: black;
  padding: 0.25rem;
  list-style: none;
  margin: 0;
  overflow: hidden;
}

.slide-tab-item {
  position: relative;
  z-index: 10;
  display: block;
  cursor: pointer;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: white;
  transition: color 0.3s ease;
  white-space: nowrap;
  border-radius: 9999px;
  user-select: none;
}

.slide-tab-item:hover {
  color: white;
}

.slide-tab-item.active {
  color: black;
}

.slide-cursor {
  position: absolute;
  z-index: 0;
  top: 0.25rem;
  height: calc(100% - 0.5rem);
  border-radius: 9999px;
  background: white;
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
  transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1), width 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease;
  pointer-events: none;
}

/* 内容展示区 */
.tab-content-area {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  padding: 2rem;
  min-height: 500px;
  position: relative;
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.type-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 3rem;
  width: 100%;
  max-width: 1000px;
  min-height: 400px;
}

.image-content {
  flex: 0 0 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.type-image {
  width: 100%;
  max-width: 300px;
  height: auto;
  border-radius: 1rem;
  border: 2px solid rgba(212, 175, 55, 0.3);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.type-image:hover {
  transform: scale(1.05);
  box-shadow: 0 15px 40px rgba(212, 175, 55, 0.2);
}

.image-caption {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
  text-align: center;
}

.text-content {
  flex: 1;
  min-width: 0;
}



.tab-title {
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: #d4af37;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  background: rgba(212, 175, 55, 0.05);
  border-radius: 0.75rem;
  border-left: 3px solid #d4af37;
}

.info-item {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
}

.info-label {
  font-weight: 600;
  color: #d4af37;
  font-size: 0.95rem;
  min-width: 5rem;
}

.info-value {
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.95rem;
  line-height: 1.5;
}

.paragraph {
  font-size: 1.05rem;
  line-height: 1.8;
  margin-bottom: 1.25rem;
  color: rgba(255, 255, 255, 0.8);
  text-align: justify;
}

.cultural-value {
  margin-top: 2rem;
  padding: 1.5rem;
  background: rgba(212, 175, 55, 0.08);
  border-radius: 0.75rem;
  border: 1px solid rgba(212, 175, 55, 0.2);
}

.value-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #d4af37;
  margin-bottom: 0.75rem;
}



.rounded-img {
  border-radius: 1rem;
  width: 100%;
  height: auto;
  transition: all 0.3s ease;
  border: 1px solid rgba(212, 175, 55, 0.2);
}

.shadow-lg {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}

.hover-lift {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-lift:hover {
  transform: translateY(-10px);
  box-shadow: 0 25px 50px rgba(212, 175, 55, 0.2);
}

.interactive-card {
  transition: all 0.3s ease;
}

.interactive-card:hover {
  transform: scale(1.02);
  border-color: rgba(212, 175, 55, 0.5);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .slide-tabs-list {
    flex-wrap: wrap;
    max-width: 100%;
    border-radius: 1rem;
    gap: 0.25rem;
  }
  
  .slide-tab-item {
    padding: 0.6rem 1rem;
    font-size: 0.8rem;
  }
  
  .slide-cursor {
    display: none;
  }
  
  .slide-tab-item.active {
    background: white;
    color: black;
  }
}

@media (max-width: 768px) {
  .section-container {
    padding: 0 1rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .section-subtitle {
    font-size: 1.5rem;
  }
  
  .intro-content {
    padding: 1.5rem;
  }
  
  .timeline-container,
  .relationship-container {
    padding: 1rem;
  }
  
  .type-content {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }
  
  .image-content {
    flex: 0 0 auto;
    max-width: 100%;
    order: -1;
  }
  
  .type-image {
    max-width: 250px;
  }
  
  .tab-content-area {
    padding: 1.5rem;
  }
  
  .tab-title {
    font-size: 1.5rem;
  }
  
  .info-grid {
    padding: 1rem;
  }
  
  .paragraph {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .slide-tabs-list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.5rem;
    padding: 0.5rem;
  }
  
  .slide-tab-item {
    text-align: center;
    padding: 0.5rem;
    font-size: 0.7rem;
  }
}
</style>