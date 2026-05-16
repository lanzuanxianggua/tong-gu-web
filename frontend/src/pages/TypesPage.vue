<template>
  <div class="types-page">
    <div class="container">
      <!-- 页面标题 -->
      <SectionHeader :title="t('pages.types.title')" :subtitle="t('pages.types.subtitle')" />

      <BronzeDivider />

      <!-- 分型法介绍 -->
      <div class="classification-intro">
        <p class="intro-paragraph">
          {{ t('pages.types.intro') }}
        </p>
      </div>

      <!-- 铜鼓年代表 -->
      <div class="table-section">
        <h3 class="section-title">{{ t('pages.types.chronology') }}</h3>
        <div class="archive-table-wrapper">
          <table class="archive-table">
            <thead>
              <tr>
                <th>{{ t('pages.types.typeName') }}</th>
                <th>{{ t('pages.types.period') }}</th>
                <th>{{ t('pages.types.region') }}</th>
                <th>{{ t('pages.types.feature') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in drumTypes" :key="item.name">
                <td class="type-name">{{ item.name }}</td>
                <td>{{ item.period }}</td>
                <td>{{ item.region }}</td>
                <td>{{ item.feature }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <BronzeDivider decorated />

      <!-- 八大类型详情 -->
      <div class="type-details-section">
        <h3 class="section-title">{{ t('pages.types.details') }}</h3>

        <!-- 药丸标签选择器 -->
        <div class="filter-pills">
          <button
            v-for="(item, index) in drumTypes"
            :key="item.name"
            :class="['pill', { active: selected === index }]"
            @click="selected = index"
          >
            {{ item.name }}
          </button>
        </div>

        <!-- 选中类型内容 -->
        <div class="type-content-area">
          <ArchiveCard hoverable>
            <div class="type-content">
              <div class="type-image-col">
                <img
                  :src="drumTypes[selected].image"
                  :alt="drumTypes[selected].title"
                  class="type-image"
                />
                <p class="image-caption">{{ drumTypes[selected].imageCaption }}</p>
              </div>
              <div class="type-info-col">
                <h4 class="type-title">{{ drumTypes[selected].title }}</h4>
                <div class="info-grid">
                  <div class="info-item">
                    <span class="info-label">{{ t('pages.types.excavationSite') }}:</span>
                    <span class="info-value">{{ drumTypes[selected].location }}</span>
                  </div>
                  <div class="info-item">
                    <span class="info-label">{{ t('pages.types.eraPeriod') }}:</span>
                    <span class="info-value">{{ drumTypes[selected].period }}</span>
                  </div>
                  <div class="info-item">
                    <span class="info-label">{{ t('pages.types.mainFeature') }}:</span>
                    <span class="info-value">{{ drumTypes[selected].feature }}</span>
                  </div>
                </div>
                <p class="type-paragraph">{{ drumTypes[selected].description1 }}</p>
                <p class="type-paragraph">{{ drumTypes[selected].description2 }}</p>
                <div class="cultural-value">
                  <h5 class="value-title">{{ t('pages.types.culturalValue') }}</h5>
                  <p class="type-paragraph">{{ drumTypes[selected].culturalValue }}</p>
                </div>
              </div>
            </div>
          </ArchiveCard>
        </div>
      </div>

      <!-- 铜鼓类型关系示意图 -->
      <div class="relationship-section">
        <h3 class="section-title">{{ t('pages.types.relationship') }}</h3>
        <div class="relationship-container">
          <img :src="tonggu04" :alt="t('pages.types.relationship')" class="relationship-image" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'
import ArchiveCard from '@/components/ArchiveCard.vue'

import tonggu_type01 from '@/assets/tonggu_type01.png'
import tonggu_type02 from '@/assets/tonggu_type02.png'
import tonggu_type03 from '@/assets/tonggu_type03.png'
import tonggu_type04 from '@/assets/tonggu_type04.png'
import tonggu_type05 from '@/assets/tonggu_type05.png'
import tonggu_type06 from '@/assets/tonggu_type06.png'
import tonggu_type07 from '@/assets/tonggu_type07.png'
import tonggu_type08 from '@/assets/tonggu_type08.png'
import tonggu04 from '@/assets/tonggu04.jpg'

const { t, tm, locale } = useI18n()

const selected = ref(0)

const images = [
  tonggu_type01, tonggu_type02, tonggu_type03, tonggu_type04,
  tonggu_type05, tonggu_type06, tonggu_type07, tonggu_type08,
]

const drumTypes = computed(() => {
  const items: any = tm('pages.types.drumTypes')
  if (!Array.isArray(items)) return []
  return items.map((item: any, i: number) => ({
    ...item,
    image: images[i],
  }))
})
</script>

<style scoped>
.types-page {
  min-height: 100vh;
  padding: var(--space-8) 0 var(--space-16);
}

/* 分型法介绍 */
.classification-intro {
  margin-bottom: var(--space-10);
}

.intro-paragraph {
  font-size: var(--text-base);
  line-height: var(--leading-relaxed);
  color: var(--text-secondary);
  text-indent: 2em;
  max-width: 900px;
  margin: 0 auto;
}

/* 小节标题 */
.section-title {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: var(--weight-bold);
  color: var(--text-primary);
  text-align: center;
  margin-bottom: var(--space-6);
  position: relative;
  display: inline-block;
  width: 100%;
}

.section-title::after {
  content: '';
  display: block;
  width: 48px;
  height: 2px;
  background: linear-gradient(90deg, var(--accent-gold), transparent);
  margin: var(--space-2) auto 0;
}

/* 年代表格 */
.table-section {
  margin-bottom: var(--space-10);
}

.archive-table-wrapper {
  overflow-x: auto;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  background: var(--bg-surface);
}

.archive-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

.archive-table th {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  font-weight: var(--weight-semibold);
  color: var(--accent-gold);
  background: var(--bg-elevated);
  border-bottom: 1px solid var(--border-subtle);
  white-space: nowrap;
}

.archive-table td {
  padding: var(--space-3) var(--space-4);
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-subtle);
  line-height: var(--leading-normal);
}

.archive-table tbody tr:last-child td {
  border-bottom: none;
}

.archive-table tbody tr:hover {
  background: var(--bg-hover);
}

.archive-table .type-name {
  color: var(--accent-gold);
  font-weight: var(--weight-semibold);
  font-family: var(--font-display);
  white-space: nowrap;
}

/* 类型详情区 */
.type-details-section {
  margin-bottom: var(--space-12);
}

/* 药丸标签 — 与 DetectionPage 一致 */
.filter-pills {
  display: flex;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
  flex-wrap: wrap;
  justify-content: center;
}

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

.pill:hover {
  border-color: var(--accent-gold);
  color: var(--text-primary);
}

.pill.active {
  border-color: var(--accent-gold);
  color: var(--accent-gold);
  background: rgba(201, 162, 39, 0.08);
}

/* 选中类型内容 */
.type-content-area {
  animation: fadeIn var(--duration-normal) var(--ease-out) both;
}

.type-content {
  display: flex;
  gap: var(--space-8);
  align-items: flex-start;
}

.type-image-col {
  flex: 0 0 280px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.type-image {
  width: 100%;
  max-width: 280px;
  height: auto;
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-card);
  transition: transform var(--duration-normal) var(--ease-out),
              box-shadow var(--duration-normal) var(--ease-out);
}

.type-image:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-elevated);
}

.image-caption {
  margin-top: var(--space-3);
  font-size: var(--text-sm);
  color: var(--text-muted);
  text-align: center;
}

.type-info-col {
  flex: 1;
  min-width: 0;
}

.type-title {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: var(--weight-bold);
  color: var(--accent-gold);
  margin-bottom: var(--space-4);
}

.info-grid {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-bottom: var(--space-4);
  padding: var(--space-4);
  background: rgba(201, 162, 39, 0.04);
  border-left: 3px solid var(--accent-gold);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
}

.info-item {
  display: flex;
  align-items: baseline;
  gap: var(--space-2);
}

.info-label {
  font-weight: var(--weight-semibold);
  color: var(--accent-gold);
  font-size: var(--text-sm);
  white-space: nowrap;
}

.info-value {
  color: var(--text-primary);
  font-size: var(--text-sm);
  line-height: var(--leading-normal);
}

.type-paragraph {
  font-size: var(--text-base);
  line-height: var(--leading-relaxed);
  color: var(--text-secondary);
  margin-bottom: var(--space-3);
  text-indent: 2em;
}

.type-paragraph:last-child {
  margin-bottom: 0;
}

.cultural-value {
  margin-top: var(--space-4);
  padding: var(--space-4);
  background: rgba(201, 162, 39, 0.04);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-sm);
}

.value-title {
  font-family: var(--font-display);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--accent-gold);
  margin-bottom: var(--space-2);
}

/* 关系示意图 */
.relationship-section {
  margin-top: var(--space-12);
}

.relationship-container {
  border: 2px solid var(--border-gold);
  border-radius: var(--radius-sm);
  padding: var(--space-6);
  background: var(--bg-surface);
  text-align: center;
}

.relationship-image {
  max-width: 100%;
  height: auto;
  margin: 0 auto;
}

/* 动画 */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* 响应式 */
@media (max-width: 768px) {
  .type-content {
    flex-direction: column;
    align-items: center;
  }

  .type-image-col {
    flex: 0 0 auto;
    width: 100%;
    max-width: 260px;
  }

  .archive-table th,
  .archive-table td {
    padding: var(--space-2) var(--space-3);
    font-size: var(--text-xs);
  }
}
</style>
