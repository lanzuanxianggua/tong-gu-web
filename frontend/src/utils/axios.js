import axios from 'axios'
import { ElMessage } from 'element-plus'
import router from '../router'

// 创建 axios 实例
const api = axios.create({
  // 使用环境变量配置 API 地址
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 30000, // 增加超时时间到 30 秒
})

// 请求拦截器：添加 JWT Token
api.interceptors.request.use(
  (config) => {
    // 优先使用 access_token
    let token = localStorage.getItem('access_token')
    
    // 如果没有 access_token，尝试使用旧的 token 字段（兼容旧版本）
    if (!token) {
      token = localStorage.getItem('token')
    }
    
    if (token) {
      // JWT token 使用 Bearer 认证
      config.headers.Authorization = `Bearer ${token}`
    }
    
    return config
  },
  (error) => {
    console.error('请求拦截器错误:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器：处理 token 过期和自动刷新
api.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    const originalRequest = error.config
    
    // 如果是 401 错误且没有重试过
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      
      const refreshToken = localStorage.getItem('refresh_token')
      
      if (refreshToken) {
        try {
          // 尝试刷新 token
          const refreshResponse = await axios.post(
            `${import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'}/api/users/token/refresh/`,
            { refresh: refreshToken }
          )
          
          if (refreshResponse.status === 200) {
            const newAccessToken = refreshResponse.data.access
            
            // 保存新的 access token
            localStorage.setItem('access_token', newAccessToken)
            
            // 重试原始请求
            originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
            return api(originalRequest)
          }
        } catch (refreshError) {
          // 刷新失败，清除所有 token 并跳转到登录页
          console.error('Token 刷新失败:', refreshError)
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          localStorage.removeItem('token')
          localStorage.removeItem('user')
          
          ElMessage.error('登录已过期，请重新登录')
          router.push('/login')
          return Promise.reject(refreshError)
        }
      } else {
        // 没有 refresh token，直接跳转到登录页
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        
        ElMessage.error('请先登录')
        router.push('/login')
      }
    }
    
    return Promise.reject(error)
  }
)

export default api
