import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/utils/axios'
import { ElMessage } from 'element-plus'
import { useI18n } from 'vue-i18n'
import type { DetectionRecord, DetectionResult } from '@/types'

export const useDetectionStore = defineStore('detection', () => {
  const { t } = useI18n()
  // --- State ---
  const records = ref<DetectionRecord[]>([])
  const currentResults = ref<DetectionResult[]>([])
  const currentImage = ref<string>('')
  const uploading = ref(false)
  const detecting = ref(false)
  const saving = ref(false)

  // Pagination
  const currentPage = ref(1)
  const pageSize = ref(10)
  const total = ref(0)

  // Filter
  const patternFilter = ref<string>('')

  // --- Computed ---
  const filteredRecords = computed(() => {
    if (!patternFilter.value) return records.value
    return records.value.filter(r =>
      r.pattern_type.includes(patternFilter.value)
    )
  })

  const totalPages = computed(() =>
    Math.ceil(total.value / pageSize.value)
  )

  const hasRecords = computed(() => records.value.length > 0)
  const hasCurrentResults = computed(() => currentResults.value.length > 0)

  // --- Actions ---
  async function fetchRecords(page?: number) {
    try {
      const p = page ?? currentPage.value
      const res = await api.get('/api/detection/my-records/', {
        params: { page: p, page_size: pageSize.value }
      })

      const data = res.data
      if (Array.isArray(data)) {
        records.value = data
        total.value = data.length
      } else if (data.results) {
        records.value = data.results
        total.value = data.count ?? data.results.length
      } else {
        records.value = []
        total.value = 0
      }

      currentPage.value = p
    } catch (err: any) {
      console.error('获取检测记录失败:', err)
    }
  }

  async function detectImage(file: File) {
    uploading.value = true
    detecting.value = true
    currentResults.value = []
    currentImage.value = ''

    try {
      const formData = new FormData()
      formData.append('image', file)
      currentImage.value = URL.createObjectURL(file)

      const res = await api.post('/api/detection/detect/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        timeout: 120000,
      })

      const data = res.data
      // 后端返回 detections 和 image_data
      const detections = data.detections || data.results
      if (detections && Array.isArray(detections)) {
        currentResults.value = detections.map((r: any) => ({
          label: r.label || r.pattern_type || '',
          confidence: r.confidence ?? r.score ?? 0,
          era: r.era_estimate || r.era || '',
          region: r.region_type || r.region || '',
          bbox: r.bbox || [],
        }))
      }

      if (data.image_data) {
        currentImage.value = data.image_data
      }

      ElMessage.success(t('detection.detectionComplete'))
      return currentResults.value
    } catch (err: any) {
      throw err
    } finally {
      uploading.value = false
      detecting.value = false
    }
  }

  async function saveRecord(payload: {
    original_image?: string
    annotated_image?: string
    annotated_image_data?: string
    pattern_type: string
    era_estimate: string
    region_type: string
    confidence: number
    remark?: string
  }) {
    saving.value = true
    try {
      const res = await api.post('/api/detection/save-record/', payload)
      ElMessage.success(t('detection.saveSuccess'))
      await fetchRecords(currentPage.value)
      return res.data
    } catch (err: any) {
      throw err
    } finally {
      saving.value = false
    }
  }

  async function deleteRecord(id: number) {
    try {
      await api.delete(`/api/detection/delete-record/${id}/`)
      records.value = records.value.filter(r => r.id !== id)
      total.value -= 1
    } catch (err: any) {
      throw err
    }
  }

  function setCurrentResults(results: DetectionResult[], image?: string) {
    currentResults.value = results
    if (image) currentImage.value = image
  }

  function clearCurrent() {
    if (currentImage.value?.startsWith('blob:')) {
      URL.revokeObjectURL(currentImage.value)
    }
    currentResults.value = []
    currentImage.value = ''
  }

  function setPage(page: number) {
    currentPage.value = page
    fetchRecords(page)
  }
  function setPatternFilter(pattern: string) {
    patternFilter.value = pattern
    currentPage.value = 1
  }

  return {
    records,
    currentResults,
    currentImage,
    uploading,
    detecting,
    saving,
    currentPage,
    pageSize,
    total,
    patternFilter,
    filteredRecords,
    totalPages,
    hasRecords,
    hasCurrentResults,
    fetchRecords,
    detectImage,
    saveRecord,
    deleteRecord,
    setCurrentResults,
    clearCurrent,
    setPage,
    setPatternFilter,
  }
})
