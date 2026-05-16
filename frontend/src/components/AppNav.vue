<template>
  <header class="app-nav" :class="{ scrolled }" role="banner">
    <nav class="app-nav__inner" aria-label="主导航">
      <div class="app-nav__brand" @click="router.push('/')" role="link" tabindex="0" aria-label="返回首页">
        <img src="@/assets/tonggu_logo.png" alt="铜鼓" class="app-nav__logo" />
        <span class="app-nav__title" :class="{ 'app-nav__title--wrap': currentLang === 'en' }">{{ t('nav.brand') }}</span>
      </div>

      <ul class="app-nav__links" role="menubar">
        <li v-for="item in menuItems" :key="item.href" role="none">
          <router-link :to="item.href" class="app-nav__link" role="menuitem" @click="menuOpen = false">
            {{ item.name }}
          </router-link>
        </li>
      </ul>

      <div class="app-nav__actions">
        <button class="app-nav__lang" @click="toggleLang" :aria-label="currentLang === 'zh' ? 'Switch to English' : '切换至中文'">
          {{ currentLang === 'zh' ? 'EN' : '中' }}
        </button>
        <template v-if="!auth.isLoggedIn">
          <ArchiveButton variant="ghost" size="sm" @click="router.push('/login')">{{ t('nav.login') }}</ArchiveButton>
          <ArchiveButton variant="primary" size="sm" @click="router.push('/register')">{{ t('nav.register') }}</ArchiveButton>
        </template>
        <template v-else>
          <span class="app-nav__user" @click="router.push('/profile')">{{ auth.userName }}</span>
          <ArchiveButton variant="ghost" size="sm" @click="handleLogout">{{ t('nav.logout') }}</ArchiveButton>
        </template>
      </div>

      <button class="app-nav__hamburger" :class="{ active: menuOpen }" @click="menuOpen = !menuOpen" :aria-label="menuOpen ? '关闭菜单' : '打开菜单'" :aria-expanded="menuOpen" type="button">
        <span></span><span></span><span></span>
      </button>
    </nav>

    <transition name="nav-slide">
      <div v-if="menuOpen" class="app-nav__mobile" role="navigation" aria-label="移动端导航">
        <ul role="menu">
          <li v-for="item in menuItems" :key="item.href" role="none">
            <router-link :to="item.href" class="app-nav__mobile-link" role="menuitem" @click="menuOpen = false">
              {{ item.name }}
            </router-link>
          </li>
        </ul>
        <div class="app-nav__mobile-actions">
          <button class="app-nav__lang" @click="toggleLang" :aria-label="currentLang === 'zh' ? 'Switch to English' : '切换至中文'">
            {{ currentLang === 'zh' ? 'EN' : '中' }}
          </button>
          <template v-if="!auth.isLoggedIn">
            <ArchiveButton variant="ghost" fullWidth @click="router.push('/login'); menuOpen = false">{{ t('nav.login') }}</ArchiveButton>
            <ArchiveButton variant="primary" fullWidth @click="router.push('/register'); menuOpen = false">{{ t('nav.register') }}</ArchiveButton>
          </template>
          <template v-else>
            <span class="app-nav__user" @click="router.push('/profile'); menuOpen = false">{{ auth.userName }}</span>
            <ArchiveButton variant="ghost" fullWidth @click="auth.logout()">{{ t('nav.logoutConfirm') }}</ArchiveButton>
          </template>
        </div>
      </div>
    </transition>
  </header>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { ElMessageBox } from 'element-plus'
import { useAuthStore } from '@/stores/auth'
import ArchiveButton from '@/components/ArchiveButton.vue'

const router = useRouter()
const auth = useAuthStore()
const { locale, t } = useI18n()

const currentLang = computed(() => locale.value)
function toggleLang() {
  const next = locale.value === 'zh' ? 'en' : 'zh'
  locale.value = next
  localStorage.setItem('lang', next)
}

const menuItems = computed(() => [
  { name: t('nav.preface'), href: '/preface' },
  { name: t('nav.origin'), href: '/origin' },
  { name: t('nav.craft'), href: '/craft' },
  { name: t('nav.types'), href: '/types' },
  { name: t('nav.art'), href: '/art' },
  { name: t('nav.culture'), href: '/culture' },
  { name: t('nav.status'), href: '/status' },
  { name: t('nav.detection'), href: '/detection' },
])

const scrolled = ref(false)
const menuOpen = ref(false)

function handleScroll() {
  scrolled.value = window.scrollY > 50
}

function handleLogout() {
  ElMessageBox.confirm(t('nav.logoutConfirm'), t('nav.logout'), {
    confirmButtonText: t('common.confirm') || t('nav.logout'),
    cancelButtonText: t('common.cancel'),
    type: 'warning',
  }).then(() => {
    auth.logout()
  }).catch(() => {})
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  auth.initFromStorage()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.app-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: transparent;
  transition: background var(--duration-normal), box-shadow var(--duration-normal);
}

.app-nav.scrolled {
  background: rgba(18, 16, 13, 0.92);
  box-shadow: 0 1px 0 rgba(201,162,39,0.1);
  backdrop-filter: blur(16px);
}

.app-nav.scrolled::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 10%;
  right: 10%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(201,162,39,0.25), transparent);
}

.app-nav__inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-6);
  height: 64px;
  display: flex;
  align-items: center;
  gap: var(--space-6);
}

.app-nav__brand {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  cursor: pointer;
  flex-shrink: 0;
}

.app-nav__logo {
  height: 32px;
  width: auto;
  opacity: 0.9;
}

.app-nav__title {
  font-family: var(--font-display);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--accent-gold);
  white-space: nowrap;
}

.app-nav__title--wrap {
  white-space: normal;
  max-width: 180px;
  line-height: 1.3;
}

.app-nav__links {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  list-style: none;
  margin: 0;
  padding: 0;
  flex: 1;
  justify-content: center;
}

.app-nav__link {
  display: block;
  padding: var(--space-2) var(--space-3);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast);
  white-space: nowrap;
  border-radius: var(--radius-sm);
  position: relative;
}

.app-nav__link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--accent-gold);
  transition: width var(--duration-normal) var(--ease-out), left var(--duration-normal) var(--ease-out);
}

.app-nav__link:hover,
.app-nav__link.router-link-active {
  color: var(--text-primary);
}

.app-nav__link:hover::after,
.app-nav__link.router-link-active::after {
  width: 60%;
  left: 20%;
}

.app-nav__actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-shrink: 0;
}

.app-nav__lang {
  background: none;
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  font-size: var(--text-xs);
  font-weight: 600;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: color var(--duration-fast), border-color var(--duration-fast);
  letter-spacing: 0.5px;
}

.app-nav__lang:hover {
  color: var(--accent-gold);
  border-color: var(--accent-gold);
}

.app-nav__user {
  font-size: var(--text-sm);
  color: var(--accent-gold);
  cursor: pointer;
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  transition: background var(--duration-fast);
}

.app-nav__user:hover {
  background: var(--bg-hover);
}

.app-nav__hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--space-2);
  width: 36px;
  height: 36px;
}

.app-nav__hamburger span {
  display: block;
  width: 20px;
  height: 2px;
  background: var(--text-primary);
  transition: transform var(--duration-fast), opacity var(--duration-fast);
}

.app-nav__hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.app-nav__hamburger.active span:nth-child(2) {
  opacity: 0;
}

.app-nav__hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

.app-nav__mobile {
  position: fixed;
  top: 64px;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--bg-elevated);
  padding: var(--space-6);
  overflow-y: auto;
  z-index: 999;
}

.app-nav__mobile ul {
  list-style: none;
  padding: 0;
  margin: 0 0 var(--space-6);
}

.app-nav__mobile-link {
  display: block;
  padding: var(--space-3) 0;
  font-size: var(--text-lg);
  color: var(--text-secondary);
  text-decoration: none;
  border-bottom: 1px solid var(--border-subtle);
  transition: color var(--duration-fast);
}

.app-nav__mobile-link:hover,
.app-nav__mobile-link.router-link-active {
  color: var(--accent-gold);
}

.app-nav__mobile-actions {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.nav-slide-enter-active,
.nav-slide-leave-active {
  transition: opacity var(--duration-normal), transform var(--duration-normal);
}

.nav-slide-enter-from,
.nav-slide-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}

@media (max-width: 1024px) {
  .app-nav__links,
  .app-nav__actions {
    display: none;
  }

  .app-nav__hamburger {
    display: flex;
    margin-left: auto;
  }

  .app-nav__title {
    font-size: var(--text-xs);
  }
}

@media (max-width: 480px) {
  .app-nav__inner {
    padding: 0 var(--space-4);
  }

  .app-nav__title {
    display: none;
  }
}
</style>
