<template>
  <div class="detection-page">
    <div class="detection-container">
      <SectionHeader :title="t('detection.title')" :subtitle="t('detection.subtitle')" />

      <el-tabs v-model="activeTab" class="detection-tabs">
        <!-- Tab 1: Smart Detection -->
        <el-tab-pane :label="t('detection.smartDetection')" name="detect">
          <!-- 状态1：未选择图片 → 上传区 -->
          <div v-if="!det.currentImage && !det.detecting" class="upload-standalone">
            <div
              class="upload-zone"
              :class="{ 'upload-zone--active': isDragOver }"
              @click="triggerFileInput"
            >
              <input ref="fileInput" type="file" accept="image/*" @change="handleFileSelect" style="display:none" />
              <div class="upload-zone__empty" @dragover.prevent="isDragOver = true" @dragleave="isDragOver = false" @drop="handleDrop">
                <div class="upload-zone__deco">
                  <span class="upload-zone__corner upload-zone__corner--tl"></span>
                  <span class="upload-zone__corner upload-zone__corner--tr"></span>
                  <span class="upload-zone__corner upload-zone__corner--bl"></span>
                  <span class="upload-zone__corner upload-zone__corner--br"></span>
                  <div class="upload-zone__icon-wrap">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                  </div>
                </div>
                <p class="upload-zone__text">{{ t('detection.uploadHint') }}</p>
                <p class="upload-zone__hint">{{ t('detection.uploadFormatHint') }}</p>
              </div>
            </div>
            <div v-if="!selectedFile" class="sample-link">
              <router-link to="/samples" class="sample-link__btn">
                {{ t('detection.goToSampleGallery') }} <span class="sample-link__arrow">&rarr;</span>
              </router-link>
            </div>
          </div>

          <!-- 状态2：已选图片，待检测 → 预览 + 按钮 -->
          <div v-else-if="selectedFile && !det.detecting && !det.hasCurrentResults" class="preview-state">
            <div class="preview-frame">
              <img :src="det.currentImage" alt="预览" class="preview-image" />
            </div>
            <div class="preview-actions">
              <ArchiveButton variant="primary" @click="runDetection">
                {{ t('detection.startDetection') }}
              </ArchiveButton>
              <ArchiveButton variant="ghost" size="sm" @click="triggerFileInput">
                {{ t('detection.uploadHint') }}
              </ArchiveButton>
              <ArchiveButton variant="ghost" size="sm" @click="clearUpload">
                {{ t('detection.clearImage') }}
              </ArchiveButton>
            </div>
          </div>

          <!-- 状态3：检测中 -->
          <div v-else-if="det.detecting" class="detecting-state">
            <div class="detecting-orb">
              <div class="detecting-orb__ring"></div>
              <div class="detecting-orb__ring detecting-orb__ring--outer"></div>
              <div class="detecting-orb__core"></div>
            </div>
            <p class="detecting-state__text">{{ t('detection.analyzingPatterns') }}</p>
            <p class="detecting-state__sub">YOLOv11</p>
          </div>

          <!-- 状态4：检测结果 → 图片 + 侧边栏 -->
          <div v-else class="result-workspace">
            <!-- 左侧：标注图片 -->
            <div class="result-image-panel">
              <div class="result-image-frame">
                <img :src="det.currentImage" alt="检测结果" class="result-image" />
              </div>
              <div class="result-image-actions">
                <ArchiveButton variant="ghost" size="sm" @click="clearUpload">
                  {{ t('detection.clearImage') }}
                </ArchiveButton>
                <span class="result-image-badge" v-if="det.hasCurrentResults">
                  {{ det.currentResults.length }} {{ t('detection.patternsFound') || '个纹样' }}
                </span>
              </div>
            </div>

            <!-- 右侧：纹样列表（可滚动） -->
            <div class="result-sidebar">
              <div class="result-sidebar__header">
                <span class="result-sidebar__title">{{ t('detection.patternsDetected') || '纹样识别结果' }}</span>
              </div>

              <div class="result-list">
                <div
                  v-for="(result, idx) in det.currentResults"
                  :key="idx"
                  class="result-item"
                  :class="{ 'result-item--active': activeResult === idx }"
                  @click="activeResult = idx"
                >
                  <div class="result-item__row">
                    <span class="result-item__index">{{ idx + 1 }}</span>
                    <span class="result-item__label">{{ result.label }}</span>
                    <span class="result-item__conf">{{ (result.confidence * 100).toFixed(1) }}%</span>
                  </div>
                  <div class="result-item__bar">
                    <div class="result-item__bar-fill" :style="{ width: `${result.confidence * 100}%` }"></div>
                  </div>
                </div>
              </div>

              <!-- 选中纹样的详情面板 -->
              <div v-if="det.hasCurrentResults && activeResult >= 0" class="result-detail">
                <div class="result-detail__header">
                  <span class="result-detail__label">{{ det.currentResults[activeResult]?.label }}</span>
                  <span class="result-detail__conf">{{ (det.currentResults[activeResult]?.confidence * 100).toFixed(1) }}%</span>
                </div>
                <div class="result-detail__info" v-if="det.currentResults[activeResult]?.era || det.currentResults[activeResult]?.region">
                  <div class="result-detail__row" v-if="det.currentResults[activeResult]?.era">
                    <span class="result-detail__key">{{ t('detection.era') || '年代' }}</span>
                    <span class="result-detail__val">{{ det.currentResults[activeResult].era }}</span>
                  </div>
                  <div class="result-detail__row" v-if="det.currentResults[activeResult]?.region">
                    <span class="result-detail__key">{{ t('detection.region') || '地域' }}</span>
                    <span class="result-detail__val">{{ det.currentResults[activeResult].region }}</span>
                  </div>
                </div>
                <div class="result-detail__remark">
                  <ArchiveInput
                    v-model="remarks[activeResult]"
                    :placeholder="t('detection.remarkPlaceholder')"
                  />
                </div>
                <ArchiveButton variant="primary" size="sm" @click="saveSingle(activeResult)">
                  {{ t('detection.saveToArchive') }}
                </ArchiveButton>
              </div>

              <!-- 全部保存 -->
              <div class="result-sidebar__footer" v-if="det.hasCurrentResults">
                <ArchiveButton variant="ghost" size="sm" fullWidth @click="clearUpload">
                  {{ t('detection.clearImage') }}
                </ArchiveButton>
              </div>
            </div>
          </div>
        </el-tab-pane>

        <!-- Tab 2: Detection Records -->
        <el-tab-pane :label="t('detection.detectionRecords')" name="records">
          <div class="records-section">
            <!-- 过滤器 -->
            <div class="records-toolbar">
              <div class="filter-pills">
                <button
                  :class="['pill', { active: det.patternFilter === '' }]"
                  @click="det.setPatternFilter('')"
                >{{ t('detection.all') }}</button>
                <button
                  v-for="pt in patternTypes"
                  :key="pt.key"
                  :class="['pill', { active: det.patternFilter === pt.key }]"
                  @click="det.setPatternFilter(pt.key)"
                >{{ pt.label }}</button>
              </div>
              <div class="records-count" v-if="det.hasRecords">
                {{ det.total }} {{ t('detection.recordsTotal') || '条记录' }}
              </div>
            </div>

            <!-- 空状态 -->
            <div v-if="!det.hasRecords" class="empty-state">
              <div class="empty-state__frame">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
              </div>
              <p class="empty-state__text">{{ t('detection.noRecords') }}</p>
              <p class="empty-state__hint">{{ t('detection.noRecordsHint') }}</p>
            </div>

            <!-- 记录列表 -->
            <div v-else class="records-list">
              <div
                v-for="record in det.filteredRecords"
                :key="record.id"
                class="record-item"
              >
                <div class="record-item__img" v-if="record.annotated_image_url || record.original_image">
                  <img :src="record.annotated_image_url || record.original_image" :alt="record.pattern_type" />
                </div>
                <div class="record-item__body">
                  <div class="record-item__top">
                    <span class="record-item__type">{{ record.pattern_type }}</span>
                    <span class="record-item__conf">{{ (record.confidence * 100).toFixed(1) }}%</span>
                  </div>
                  <div class="record-item__meta">
                    <span v-if="record.era_estimate">{{ record.era_estimate }}</span>
                    <span v-if="record.region_type">{{ record.region_type }}</span>
                  </div>
                  <p v-if="record.remark" class="record-item__remark">{{ record.remark }}</p>
                  <div class="record-item__bottom">
                    <span class="record-item__date">{{ formatDate(record.created_at) }}</span>
                    <button class="record-item__delete" @click="confirmDelete(record.id)">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>
                      {{ t('detection.delete') }}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <div v-if="det.totalPages > 1" class="records-pagination">
              <el-pagination
                :current-page="det.currentPage"
                :page-size="det.pageSize"
                :total="det.total"
                layout="prev, pager, next"
                @current-change="det.setPage"
              />
            </div>
          </div>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useDetectionStore } from '@/stores/detection'
import { useAuthStore } from '@/stores/auth'
import { ElMessageBox, ElMessage } from 'element-plus'
import ArchiveButton from '@/components/ArchiveButton.vue'
import ArchiveInput from '@/components/ArchiveInput.vue'
import SectionHeader from '@/components/SectionHeader.vue'

const { t } = useI18n()
const router = useRouter()
const route = useRoute()
const det = useDetectionStore()
const auth = useAuthStore()

const activeTab = ref('detect')
const activeResult = ref(0)
const selectedFile = ref<File | null>(null)
const isDragOver = ref(false)
const remarks = ref<string[]>([])
const patternTypes = computed(() => [
  { key: '太阳纹', label: t('detection.sunPattern') },
  { key: '蛙纹', label: t('detection.frogPattern') },
  { key: '云雷纹', label: t('detection.cloudThunderPattern') },
])
const fileInput = ref<HTMLInputElement | null>(null)

let authPromptShown = false

function checkAuth() {
  if (auth.isLoggedIn || authPromptShown) return
  authPromptShown = true
  ElMessageBox.confirm(
    t('detection.detectionLoginPrompt'),
    t('detection.detectionRequiresLogin'),
    {
      confirmButtonText: t('detection.loginNow'),
      cancelButtonText: t('common.cancel'),
      type: 'warning',
    }
  ).then(() => {
    router.push({ name: 'login', query: { redirect: route.fullPath } })
  }).catch(() => {
    router.back()
  })
}

const MAX_FILE_SIZE = 50 * 1024 * 1024

function revokeCurrentImage() {
  if (det.currentImage?.startsWith('blob:')) {
    URL.revokeObjectURL(det.currentImage)
  }
}

function triggerFileInput() {
  fileInput.value?.click()
}

function handleFileSelect(e: Event) {
  const input = e.target as HTMLInputElement
  if (input.files?.[0]) {
    const file = input.files[0]
    if (file.size > MAX_FILE_SIZE) {
      ElMessage.warning(t('detection.fileSizeExceed') || '文件大小不能超过50MB')
      return
    }
    revokeCurrentImage()
    selectedFile.value = file
    det.currentImage = URL.createObjectURL(file)
  }
}

function handleDrop(e: DragEvent) {
  isDragOver.value = false
  const file = e.dataTransfer?.files[0]
  if (file && file.type.startsWith('image/')) {
    if (file.size > MAX_FILE_SIZE) {
      ElMessage.warning(t('detection.fileSizeExceed') || '文件大小不能超过50MB')
      return
    }
    revokeCurrentImage()
    selectedFile.value = file
    det.currentImage = URL.createObjectURL(file)
  }
}

function clearUpload() {
  revokeCurrentImage()
  selectedFile.value = null
  det.clearCurrent()
  remarks.value = []
}

async function runDetection() {
  if (!selectedFile.value) return
  if (!auth.isLoggedIn) {
    try {
      await ElMessageBox.confirm(
        t('detection.detectionLoginPrompt'),
        t('detection.detectionRequiresLogin'),
        {
          confirmButtonText: t('detection.loginNow'),
          cancelButtonText: t('common.cancel'),
          type: 'warning',
        }
      )
      router.push({ name: 'login', query: { redirect: route.fullPath } })
    } catch {}
    return
  }
  try {
    await det.detectImage(selectedFile.value)
    remarks.value = det.currentResults.map(() => '')
  } catch {}
}

async function saveSingle(idx: number) {
  const r = det.currentResults[idx]
  try {
    await det.saveRecord({
      pattern_type: r.label,
      era_estimate: r.era,
      region_type: r.region,
      confidence: r.confidence,
      remark: remarks.value[idx] || undefined,
      annotated_image_data: det.currentImage.startsWith('data:' ) ? det.currentImage : undefined,
    })
  } catch { ElMessage.error(t('errors.saveFailed')) }
}

async function confirmDelete(id: number) {
  try {
    await ElMessageBox.confirm(t('detection.confirmDeleteRecord'), t('detection.confirmDelete'), {
      confirmButtonText: t('detection.delete'),
      cancelButtonText: t('common.cancel'),
      type: 'warning',
    })
    await det.deleteRecord(id)
    ElMessage.success(t('errors.deleteSuccess'))
  } catch {}
}

function formatDate(dateStr: string): string {
  const d = new Date(dateStr)
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
}

onMounted(() => {
  auth.initFromStorage()
  if (auth.isLoggedIn) {
    det.fetchRecords()
  } else {
    checkAuth()
  }

  if (route.query.useSample === 'true') {
    const sampleData = sessionStorage.getItem('selectedSample')
    if (sampleData) {
      try {
        const sample = JSON.parse(sampleData)
        if (sample.image) {
          fetch(sample.image)
            .then(r => r.blob())
            .then(blob => {
              const file = new File([blob], `${sample.name || 'sample'}.png`, { type: 'image/png' })
              revokeCurrentImage()
              selectedFile.value = file
              det.currentImage = URL.createObjectURL(file)
            })
        }
      } catch {}
      sessionStorage.removeItem('selectedSample')
    }
  }
})

onUnmounted(() => {
  revokeCurrentImage()
})

watch(activeTab, (tab) => {
  if (tab === 'records' && auth.isLoggedIn) {
    det.fetchRecords(1)
  }
})
</script>

<style scoped>
.detection-page { min-height: 100vh; }

.detection-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: var(--space-8) var(--space-6);
}

/* ===== Standalone Upload (no image yet) ===== */
.upload-standalone {
  max-width: 520px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-5);
}

.upload-zone {
  position: relative;
  border: 2px dashed var(--border-gold);
  border-radius: var(--radius-md);
  width: 100%;
  min-height: 260px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: rgba(201, 162, 39, 0.015);
  transition: all var(--duration-normal);
}

.upload-zone:hover { border-color: var(--accent-gold); background: rgba(201, 162, 39, 0.03); }
.upload-zone--active { border-color: var(--accent-gold); background: rgba(201, 162, 39, 0.05); }

.upload-zone__deco {
  position: relative;
  width: 64px;
  height: 64px;
  margin-bottom: var(--space-4);
}

.upload-zone__corner {
  position: absolute;
  width: 12px;
  height: 12px;
  border-color: var(--accent-gold);
  opacity: 0.4;
}
.upload-zone__corner--tl { top: 0; left: 0; border-top: 2px solid; border-left: 2px solid; }
.upload-zone__corner--tr { top: 0; right: 0; border-top: 2px solid; border-right: 2px solid; }
.upload-zone__corner--bl { bottom: 0; left: 0; border-bottom: 2px solid; border-left: 2px solid; }
.upload-zone__corner--br { bottom: 0; right: 0; border-bottom: 2px solid; border-right: 2px solid; }

.upload-zone__icon-wrap {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: var(--accent-gold);
  opacity: 0.6;
}

.upload-zone__empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-6);
}

.upload-zone__text { font-size: var(--text-base); color: var(--text-secondary); }
.upload-zone__hint { font-size: var(--text-xs); color: var(--text-muted); }

.upload-actions-center {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
}

.sample-link { text-align: center; }
.sample-link__btn { font-size: var(--text-sm); color: var(--accent-gold); text-decoration: none; transition: color var(--duration-fast); }
.sample-link__btn:hover { color: var(--accent-gold-light); }
.sample-link__arrow { display: inline-block; transition: transform var(--duration-fast); }
.sample-link__btn:hover .sample-link__arrow { transform: translateX(4px); }

/* ===== Preview State (image selected, not yet detected) ===== */
.preview-state {
  max-width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-5);
}

.preview-frame {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preview-image {
  width: 100%;
  max-height: 420px;
  object-fit: contain;
  display: block;
  border-radius: var(--radius-sm);
}

.preview-actions {
  display: flex;
  gap: var(--space-3);
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
}

/* ===== Detecting State ===== */
.detecting-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-20) var(--space-6);
  gap: var(--space-4);
}

.detecting-orb { position: relative; width: 56px; height: 56px; }

.detecting-orb__ring {
  position: absolute;
  inset: 0;
  border: 2px solid transparent;
  border-top-color: var(--accent-gold);
  border-radius: 50%;
  animation: orb-spin 1s linear infinite;
}

.detecting-orb__ring--outer {
  inset: -6px;
  border-top-color: var(--accent-copper);
  animation-duration: 1.6s;
  animation-direction: reverse;
  opacity: 0.5;
}

.detecting-orb__core {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 8px;
  height: 8px;
  transform: translate(-50%, -50%);
  background: var(--accent-gold);
  border-radius: 50%;
  animation: orb-pulse 1.5s ease-in-out infinite;
}

@keyframes orb-spin { to { transform: rotate(360deg); } }
@keyframes orb-pulse { 0%,100% { opacity: 0.4; transform: translate(-50%, -50%) scale(1); } 50% { opacity: 1; transform: translate(-50%, -50%) scale(1.3); } }

.detecting-state__text { color: var(--text-secondary); }
.detecting-state__sub { color: var(--text-muted); font-size: var(--text-xs); font-family: var(--font-mono); letter-spacing: 1px; }

/* ===== Result Workspace: Image + Sidebar ===== */
.result-workspace {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: var(--space-6);
  align-items: start;
  min-height: 500px;
}

/* Image Panel */
.result-image-panel {
  position: relative;
}

.result-image-frame {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-image {
  width: 100%;
  max-height: 560px;
  object-fit: contain;
  display: block;
  border-radius: var(--radius-sm);
}

.result-image-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: var(--space-3);
}

.result-image-badge {
  font-size: var(--text-xs);
  color: var(--accent-gold);
  font-family: var(--font-mono);
  padding: 2px 8px;
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-sm);
}

/* Sidebar */
.result-sidebar {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  display: flex;
  flex-direction: column;
  max-height: 680px;
  overflow: hidden;
}

.result-sidebar__header {
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--border-subtle);
}

.result-sidebar__title {
  font-family: var(--font-display);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--accent-gold);
  letter-spacing: 0.5px;
}

/* Result list - scrollable */
.result-list {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-2) 0;
}

.result-list::-webkit-scrollbar { width: 4px; }
.result-list::-webkit-scrollbar-track { background: transparent; }
.result-list::-webkit-scrollbar-thumb { background: var(--border-subtle); border-radius: 2px; }

.result-item {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-5);
  cursor: pointer;
  transition: background var(--duration-fast);
  border-left: 2px solid transparent;
}

.result-item:hover { background: var(--bg-hover); }
.result-item--active {
  background: rgba(201, 162, 39, 0.06);
  border-left-color: var(--accent-gold);
}

.result-item__row {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.result-item__index {
  width: 20px;
  height: 20px;
  border: 1px solid var(--border-subtle);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
  flex-shrink: 0;
}

.result-item--active .result-item__index {
  border-color: var(--accent-gold);
  color: var(--accent-gold);
}

.result-item__label {
  flex: 1;
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-primary);
}

.result-item__conf {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-secondary);
}

.result-item__bar {
  height: 2px;
  background: var(--bg-hover);
  border-radius: 1px;
  overflow: hidden;
  margin-left: 32px;
}

.result-item__bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-copper), var(--accent-gold));
  border-radius: 1px;
  transition: width 0.6s var(--ease-out);
}

/* Detail panel for selected result */
.result-detail {
  padding: var(--space-4) var(--space-5);
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  background: rgba(201, 162, 39, 0.02);
}

.result-detail__header {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
}

.result-detail__label {
  font-family: var(--font-display);
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--accent-gold);
}

.result-detail__conf {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.result-detail__info {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.result-detail__row {
  display: flex;
  align-items: baseline;
  gap: var(--space-2);
}

.result-detail__key {
  font-size: var(--text-xs);
  color: var(--text-muted);
  white-space: nowrap;
  min-width: 36px;
}

.result-detail__val {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.result-sidebar__footer {
  padding: var(--space-3) var(--space-5);
  border-top: 1px solid var(--border-subtle);
}

/* ===== Records Section ===== */
.records-section { padding-top: var(--space-4); }

.records-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-6);
  flex-wrap: wrap;
  gap: var(--space-3);
}

.records-count { font-size: var(--text-sm); color: var(--text-muted); font-family: var(--font-mono); }

.filter-pills { display: flex; gap: var(--space-2); flex-wrap: wrap; }

.pill {
  padding: var(--space-1) var(--space-4);
  border: 1px solid var(--border-subtle);
  border-radius: 999px;
  font-size: var(--text-sm);
  color: var(--text-secondary);
  background: transparent;
  cursor: pointer;
  transition: all var(--duration-fast);
}
.pill:hover { border-color: var(--accent-gold); color: var(--text-primary); }
.pill.active { border-color: var(--accent-gold); color: var(--accent-gold); background: rgba(201, 162, 39, 0.08); }

/* Empty state */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--space-16) var(--space-6);
  text-align: center;
}

.empty-state__frame {
  width: 80px;
  height: 80px;
  border: 1px solid var(--border-subtle);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  margin-bottom: var(--space-4);
  opacity: 0.5;
}

.empty-state__text { color: var(--text-secondary); margin-bottom: var(--space-1); }
.empty-state__hint { color: var(--text-muted); font-size: var(--text-sm); }

/* Records list */
.records-list { display: flex; flex-direction: column; gap: var(--space-3); }

.record-item {
  display: flex;
  gap: var(--space-4);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: var(--space-4);
  height: 140px;
  overflow: hidden;
  transition: border-color var(--duration-fast), box-shadow var(--duration-fast);
}

.record-item:hover { border-color: rgba(201, 162, 39, 0.35); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }

.record-item__img {
  flex: 0 0 140px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  background: var(--bg-elevated);
}

.record-item__img img { width: 100%; height: 100%; object-fit: cover; }

.record-item__body {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  overflow: hidden;
}

.record-item__top { display: flex; align-items: center; gap: var(--space-3); }
.record-item__type { font-family: var(--font-display); font-size: var(--text-base); font-weight: 600; color: var(--accent-gold); }
.record-item__conf { font-family: var(--font-mono); font-size: var(--text-sm); color: var(--text-secondary); }

.record-item__meta { display: flex; gap: var(--space-3); font-size: var(--text-sm); color: var(--text-muted); }
.record-item__meta span + span::before { content: '·'; margin-right: var(--space-3); }

.record-item__remark {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  font-style: italic;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.record-item__bottom { display: flex; align-items: center; justify-content: space-between; margin-top: auto; }
.record-item__date { font-size: var(--text-xs); color: var(--text-muted); font-family: var(--font-mono); }

.record-item__delete {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: var(--text-xs);
  cursor: pointer;
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-sm);
  transition: color var(--duration-fast), background var(--duration-fast);
}
.record-item__delete:hover { color: #e74c3c; background: rgba(231, 76, 60, 0.08); }

.records-pagination { display: flex; justify-content: center; padding-top: var(--space-8); }

.records-pagination :deep(.el-pagination) {
  --el-pagination-bg-color: transparent;
  --el-pagination-button-bg-color: var(--bg-surface);
  --el-pagination-hover-color: var(--accent-gold);
  --el-pagination-text-color: var(--text-muted);
  --el-pagination-button-color: var(--text-secondary);
}

.records-pagination :deep(.el-pager li) {
  background: transparent;
  color: var(--text-muted);
  font-family: var(--font-mono);
  border-radius: var(--radius-sm);
}

.records-pagination :deep(.el-pager li:hover),
.records-pagination :deep(.el-pager li.is-active) {
  color: var(--accent-gold);
}

.records-pagination :deep(.el-pager li.is-active) {
  background: rgba(201, 162, 39, 0.08);
}

.records-pagination :deep(.btn-prev),
.records-pagination :deep(.btn-next) {
  background: var(--bg-surface) !important;
  color: var(--text-secondary) !important;
  border-radius: var(--radius-sm);
}

.records-pagination :deep(.btn-prev:hover),
.records-pagination :deep(.btn-next:hover) {
  color: var(--accent-gold) !important;
}

/* ===== Element Plus Tab Overrides ===== */
.detection-tabs :deep(.el-tabs__header) {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm) var(--radius-sm) 0 0;
  padding: 0 var(--space-4);
}
.detection-tabs :deep(.el-tabs__nav-wrap::after) { display: none; }
.detection-tabs :deep(.el-tabs__item) { color: var(--text-secondary); font-size: var(--text-sm); padding: 0 var(--space-5); }
.detection-tabs :deep(.el-tabs__item.is-active) { color: var(--accent-gold); }
.detection-tabs :deep(.el-tabs__active-bar) { background: var(--accent-gold); }

/* ===== Responsive ===== */
@media (max-width: 900px) {
  .result-workspace {
    grid-template-columns: 1fr;
  }

  .result-sidebar {
    max-height: none;
  }

  .result-image-frame {
    padding: var(--space-2);
  }

  .result-image {
    max-height: 360px;
  }

  .preview-state {
    max-width: 100%;
  }

  .preview-image {
    max-height: 300px;
  }

  .preview-actions {
    flex-wrap: wrap;
  }
}

@media (max-width: 768px) {
  .detection-container {
    padding: var(--space-6) var(--space-4);
  }

  .upload-zone {
    min-height: 200px;
  }

  .record-item {
    flex-direction: column;
    height: auto;
    min-height: 0;
    padding: var(--space-3);
  }

  .record-item__img {
    flex: none;
    width: 100%;
    max-width: 200px;
    align-self: center;
    aspect-ratio: auto;
  }

  .filter-pills {
    justify-content: flex-start;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    flex-wrap: nowrap;
    scrollbar-width: none;
    padding-bottom: var(--space-1);
  }

  .filter-pills::-webkit-scrollbar { display: none; }

  .pill {
    flex-shrink: 0;
  }

  .result-detail__remark :deep(.archive-input) {
    min-height: 44px;
  }

  .records-toolbar {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .detection-container {
    padding: var(--space-4) var(--space-3);
  }

  .upload-zone {
    min-height: 180px;
  }

  .preview-frame {
    padding: var(--space-2);
  }

  .preview-image {
    max-height: 240px;
  }

  .preview-actions {
    flex-direction: column;
  }

  .preview-actions :deep(.archive-button) {
    width: 100%;
  }

  .result-image {
    max-height: 280px;
  }

  .result-item__row {
    gap: var(--space-2);
  }
}
</style>
