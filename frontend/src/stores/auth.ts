import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/utils/axios'
import router from '@/router'
import { ElMessage } from 'element-plus'
import { useI18n } from 'vue-i18n'
import type { UserInfo } from '@/types'

export const useAuthStore = defineStore('auth', () => {
  const { t } = useI18n()
  // --- State ---
  const user = ref<UserInfo | null>(null)
  const accessToken = ref<string | null>(localStorage.getItem('access_token'))
  const refreshToken = ref<string | null>(localStorage.getItem('refresh_token'))
  const loading = ref(false)

  // --- Computed ---
  const isLoggedIn = computed(() => !!accessToken.value && !!user.value)
  const userName = computed(() => user.value?.username ?? '')
  const userRole = computed(() => user.value?.role ?? 'user')

  // --- Actions ---
  function setTokens(access: string, refresh: string) {
    accessToken.value = access
    refreshToken.value = refresh
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)
  }

  function setUser(info: UserInfo) {
    user.value = info
    localStorage.setItem('user', JSON.stringify(info))
  }

  async function login(username: string, password: string) {
    loading.value = true
    try {
      const res = await api.post('/api/users/login/', { username, password })
      const data = res.data

      if (data.access && data.refresh) {
        setTokens(data.access, data.refresh)
        if (data.user) {
          setUser(data.user)
        }
        ElMessage.success(t('errors.loginSuccess'))
        return true
      }
      return false
    } catch (err: any) {
        const msg = err.response?.data?.message || err.response?.data?.detail
        if (msg) ElMessage.error(msg)
        return false
    } finally {
      loading.value = false
    }
  }

  async function fetchUserInfo() {
    try {
      const res = await api.get('/api/users/info/')
      if (res.data) {
        setUser(res.data)
      }
    } catch {
      // Token may be invalid; let interceptor handle it
    }
  }

  async function refreshTokenAction() {
    if (!refreshToken.value) return false

    try {
      const res = await api.post('/api/users/token/refresh/', {
        refresh: refreshToken.value
      })
      if (res.status === 200 && res.data.access) {
        accessToken.value = res.data.access
        localStorage.setItem('access_token', res.data.access)
        return true
      }
      return false
    } catch {
      return false
    }
  }

  function logout() {
    api.post('/api/users/logout/').catch(() => {})

    user.value = null
    accessToken.value = null
    refreshToken.value = null

    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')

    router.push('/login')
    ElMessage.success(t('errors.logoutSuccess'))
  }

  /** Initialize auth state from localStorage on app startup */
  function initFromStorage() {
    const storedUser = localStorage.getItem('user')
    if (storedUser) {
      try {
        user.value = JSON.parse(storedUser)
      } catch {
        localStorage.removeItem('user')
      }
    }
  }

  return {
    user,
    accessToken,
    refreshToken,
    loading,
    isLoggedIn,
    userName,
    userRole,
    login,
    logout,
    fetchUserInfo,
    refreshTokenAction,
    initFromStorage,
    setTokens,
    setUser,
  }
})
