<template>
  <div class="sample-page">
    <div class="container">
      <SectionHeader :title="t('sample.title')" :subtitle="t('sample.subtitle')" />

      <div class="sample-back">
        <router-link to="/detection" class="sample-back__link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
          {{ t('common.back') }}
        </router-link>
      </div>

      <div v-if="loading" class="sample-loading">
        <div class="detecting-spinner"></div>
        <p>{{ t('sample.loadingSamples') }}</p>
      </div>

      <div v-else-if="samples.length === 0" class="empty-state">
        <div class="empty-state__icon">🖼</div>
        <p class="empty-state__text">{{ t('sample.noSamples') }}</p>
      </div>

      <div v-else class="sample-grid">
        <ArchiveCard v-for="sample in paginatedSamples" :key="sample.name" hoverable>
          <div class="sample-card">
            <div class="sample-card__img">
              <img :src="sample.image" :alt="sample.name" />
              <div class="sample-card__overlay" @click="useSample(sample)">
                <span class="sample-card__cta">{{ t('sample.useThisImage') }}</span>
              </div>
            </div>
            <div class="sample-card__info">
              <h3 class="sample-card__name">{{ sample.name }}</h3>
              <span v-if="sample.type" class="sample-card__type">{{ sample.type }}</span>
              <p v-if="sample.description" class="sample-card__desc">{{ sample.description }}</p>
            </div>
          </div>
        </ArchiveCard>
      </div>

      <div v-if="totalPages > 1" class="sample-pagination">
        <el-pagination
          :current-page="currentPage"
          :page-size="pageSize"
          :total="samples.length"
          layout="prev, pager, next"
          @current-change="currentPage = $event"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { ElMessage } from 'element-plus'
import SectionHeader from '@/components/SectionHeader.vue'
import ArchiveCard from '@/components/ArchiveCard.vue'

const router = useRouter()
const { t } = useI18n()
const loading = ref(true)
const samples = ref<any[]>([])
const currentPage = ref(1)
const pageSize = 9

const totalPages = computed(() => Math.ceil(samples.value.length / pageSize))

const paginatedSamples = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  return samples.value.slice(start, start + pageSize)
})

function useSample(sample: any) {
  sessionStorage.setItem('selectedSample', JSON.stringify(sample))
  router.push('/detection?useSample=true')
  ElMessage.success(`${t('sample.selected')}: ${sample.name}`)
}

onMounted(async () => {
  try {
    const res = await fetch('/samples/samples.json')
    if (res.ok) {
      const json = await res.json()
      const list = Array.isArray(json) ? json : (json.samples || [])
      samples.value = list.map((s: any) => ({
        ...s,
        image: `/samples/${s.image}`,
      }))
    }
  } catch {
    // samples list is optional
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.sample-page {
  padding: var(--space-8) 0 var(--space-16);
}

.sample-back {
  margin-bottom: var(--space-4);
}

.sample-back__link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.sample-back__link:hover {
  color: var(--accent-gold);
}

.sample-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

.sample-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.sample-card__img {
  position: relative;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: var(--radius-sm);
}

.sample-card__img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--duration-slow);
}

.sample-card:hover .sample-card__img img {
  transform: scale(1.05);
}

.sample-card__overlay {
  position: absolute;
  inset: 0;
  background: rgba(26, 22, 18, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity var(--duration-normal);
  cursor: pointer;
}

.sample-card:hover .sample-card__overlay {
  opacity: 1;
}

/* 触摸屏设备始终显示操作按钮 */
@media (hover: none) {
  .sample-card__overlay {
    opacity: 1;
    background: rgba(26, 22, 18, 0.5);
  }
}

.sample-card__cta {
  padding: var(--space-2) var(--space-4);
  border: 1px solid var(--accent-gold);
  border-radius: var(--radius-sm);
  color: var(--accent-gold);
  font-size: var(--text-sm);
  font-weight: 600;
}

.sample-card__name {
  font-family: var(--font-display);
  font-size: var(--text-base);
  font-weight: 600;
  color: var(--text-primary);
}

.sample-card__type {
  display: inline-block;
  font-size: var(--text-xs);
  color: var(--accent-gold);
  border: 1px solid var(--border-gold);
  border-radius: 999px;
  padding: 1px var(--space-2);
}

.sample-card__desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
}

.sample-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-16);
  color: var(--text-secondary);
}

.detecting-spinner {
  width: 36px;
  height: 36px;
  border: 3px solid var(--border-subtle);
  border-top-color: var(--accent-gold);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

.sample-pagination {
  display: flex;
  justify-content: center;
  padding-top: var(--space-8);
}

.sample-pagination :deep(.el-pagination) {
  --el-pagination-bg-color: transparent;
  --el-pagination-button-bg-color: var(--bg-surface);
  --el-pagination-hover-color: var(--accent-gold);
  --el-pagination-text-color: var(--text-muted);
  --el-pagination-button-color: var(--text-secondary);
}

.sample-pagination :deep(.el-pager li) {
  background: transparent;
  color: var(--text-muted);
  font-family: var(--font-mono);
  border-radius: var(--radius-sm);
}

.sample-pagination :deep(.el-pager li:hover),
.sample-pagination :deep(.el-pager li.is-active) {
  color: var(--accent-gold);
}

.sample-pagination :deep(.el-pager li.is-active) {
  background: rgba(201, 162, 39, 0.08);
}

.sample-pagination :deep(.btn-prev),
.sample-pagination :deep(.btn-next) {
  background: var(--bg-surface) !important;
  color: var(--text-secondary) !important;
  border-radius: var(--radius-sm);
}

.sample-pagination :deep(.btn-prev:hover),
.sample-pagination :deep(.btn-next:hover) {
  color: var(--accent-gold) !important;
}

@media (max-width: 768px) {
  .sample-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-4);
  }
}

@media (max-width: 480px) {
  .sample-grid {
    grid-template-columns: 1fr;
  }
}
</style>
