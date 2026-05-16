import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../pages/HomePage.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../pages/LoginPage.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../pages/RegisterPage.vue')
    },
    {
      path: '/forgot-password',
      name: 'forgot-password',
      component: () => import('../pages/ForgotPasswordPage.vue')
    },
    {
      path: '/preface',
      name: 'preface',
      component: () => import('../pages/PrefacePage.vue')
    },
    {
      path: '/origin',
      name: 'origin',
      component: () => import('../pages/OriginPage.vue')
    },
    {
      path: '/craft',
      name: 'craft',
      component: () => import('../pages/CraftPage.vue')
    },
    {
      path: '/types',
      name: 'types',
      component: () => import('../pages/TypesPage.vue')
    },
    {
      path: '/culture',
      name: 'culture',
      component: () => import('../pages/CulturePage.vue')
    },
    {
      path: '/art',
      name: 'art',
      component: () => import('../pages/ArtPage.vue')
    },
    {
      path: '/status',
      name: 'status',
      component: () => import('../pages/StatusPage.vue')
    },
    {
      path: '/detection',
      name: 'detection',
      component: () => import('../pages/DetectionPage.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/samples',
      name: 'samples',
      component: () => import('../pages/SamplePage.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../pages/UserProfilePage.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/change-password',
      name: 'change-password',
      component: () => import('../pages/ChangePasswordPage.vue'),
      meta: { requiresAuth: true }
    }
  ]
})

// Auth guard — 使用 auth store 的 isLoggedIn 状态
router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  const loggedIn = auth.isLoggedIn

  if (to.meta.requiresAuth && !loggedIn) {
    next({ name: 'login', query: { redirect: to.fullPath } })
  } else if (loggedIn && (to.name === 'login' || to.name === 'register' || to.name === 'forgot-password')) {
    next({ name: 'home' })
  } else {
    next()
  }
})

export default router
