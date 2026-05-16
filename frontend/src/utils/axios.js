import axios from 'axios'
import { ElMessage } from 'element-plus'
import router from '../router'
import i18n from '../i18n'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 30000,
})

function getErrorMessage(error) {
  const t = i18n.global.t
  if (!error.response) {
    if (error.code === 'ECONNABORTED') return t('errors.timeout') || '请求超时，请重试'
    return t('errors.networkError') || '网络连接失败，请检查网络'
  }

  const { status, data } = error.response
  const serverMsg = data?.message || data?.detail || data?.error

  switch (status) {
    case 400: return serverMsg || t('errors.badRequest') || '请求参数错误'
    case 401: return t('errors.tokenExpired') || '登录已过期，请重新登录'
    case 403: return t('errors.forbidden') || '您没有权限执行此操作'
    case 404: return t('errors.notFound') || '请求的资源不存在'
    case 429: return t('errors.tooManyRequests') || '操作过于频繁，请稍后再试'
    default:
      if (status >= 500) return t('errors.serverError') || '服务器繁忙，请稍后再试'
      return serverMsg || t('errors.requestFailed') || '请求失败，请重试'
  }
}

api.interceptors.request.use(
  (config) => {
    let token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    console.error('请求拦截器错误:', error)
    return Promise.reject(error)
  }
)

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      // Login/register/forgot-password/captcha requests should handle 401 themselves
      const url = originalRequest.url || ''
      const isAuthEndpoint = url.includes('/login/') || url.includes('/register/') ||
        url.includes('/forgot-password/') || url.includes('/captcha/') ||
        url.includes('/token/refresh/')

      if (isAuthEndpoint) {
        return Promise.reject(error)
      }

      originalRequest._retry = true

      const refreshToken = localStorage.getItem('refresh_token')

      if (refreshToken) {
        try {
          const refreshResponse = await axios.post(
            `${import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'}/api/users/token/refresh/`,
            { refresh: refreshToken }
          )

          if (refreshResponse.status === 200) {
            const newAccessToken = refreshResponse.data.access
            localStorage.setItem('access_token', newAccessToken)
            originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
            return api(originalRequest)
          }
        } catch (refreshError) {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          localStorage.removeItem('token')
          localStorage.removeItem('user')

          ElMessage.error('登录已过期，请重新登录')
          router.push('/login')
          return Promise.reject(refreshError)
        }
      } else {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('token')
        localStorage.removeItem('user')

        router.push('/login')
      }
    } else if (error.response?.status !== 401) {
      const msg = getErrorMessage(error)
      ElMessage.error(msg)
    }

    return Promise.reject(error)
  }
)

export default api
