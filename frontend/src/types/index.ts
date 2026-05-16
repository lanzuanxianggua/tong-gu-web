/**
 * 青铜档案馆 — 全局类型定义
 * Bronze Drum Pattern Detection System
 */

export interface UserInfo {
  id: number
  username: string
  phone?: string
  email?: string
  role: 'admin' | 'user'
  date_joined?: string
}

export interface DetectionResult {
  label: string          // '太阳纹' | '蛙纹' | '云雷纹'
  confidence: number     // 0-1
  era: string            // 年代推测
  region: string         // 地域类型
  bbox: number[]         // [x1, y1, x2, y2]
}

export interface DetectionRecord {
  id: number
  user: number
  original_image?: string
  annotated_image?: string
  annotated_image_url?: string
  pattern_type: string
  era_estimate: string
  region_type: string
  confidence: number
  remark?: string
  created_at: string
}

export interface MenuItem {
  name: string
  href: string
}

export interface NavState {
  scrolled: boolean
  menuOpen: boolean
}
