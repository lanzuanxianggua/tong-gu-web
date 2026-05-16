<template>
  <div class="culture-page">
    <SectionHeader
      :title="t('pages.culture.title')"
      :subtitle="t('pages.culture.subtitle')"
    />

    <!-- 主要功能 -->
    <section class="section">
      <div class="container-narrow">
        <h2 class="section-label">{{ t('pages.culture.mainFunctions') }}</h2>
        <div class="grid-3col">
          <ArchiveCard
            v-for="(item, index) in functionList"
            :key="index"
            hoverable
            class="function-card animate-fade-in-up"
            :class="`delay-${index + 1}`"
          >
            <div class="function-card__icon" v-html="item.icon"></div>
            <h3 class="function-card__title">{{ item.title }}</h3>
            <p class="function-card__desc">{{ item.desc }}</p>
          </ArchiveCard>
        </div>
      </div>
    </section>

    <div class="container-narrow">
      <BronzeDivider decorated />
    </div>

    <!-- 文化意义 -->
    <section class="section">
      <div class="container-narrow">
        <h2 class="section-label">{{ t('pages.culture.culturalSignificance') }}</h2>
        <div class="significance-block content-prose">
          <p>{{ t('pages.culture.significanceP1') }}</p>
          <p>{{ t('pages.culture.significanceP2') }}</p>
        </div>
      </div>
    </section>

    <div class="container-narrow">
      <BronzeDivider decorated />
    </div>

    <!-- 铜鼓与民族节日 -->
    <section class="section">
      <div class="container-narrow">
        <h2 class="section-label">{{ t('pages.culture.festivals') }}</h2>
        <div class="grid-3col">
          <ArchiveCard
            v-for="(item, index) in festivalList"
            :key="index"
            hoverable
            class="festival-card animate-fade-in-up"
            :class="`delay-${index + 1}`"
          >
            <h3 class="festival-card__title">{{ item.title }}</h3>
            <p class="festival-card__desc">{{ item.desc }}</p>
          </ArchiveCard>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'
import ArchiveCard from '@/components/ArchiveCard.vue'
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

interface FunctionItem {
  title: string
  desc: string
  icon: string
}

interface FestivalItem {
  title: string
  desc: string
}

const functionIcons = [
  '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>',
  '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
  '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
  '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>',
  '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
  '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>',
]

const functionList = computed<FunctionItem[]>(() => {
  const items = tm('pages.culture.functionList') as unknown as { title: string; desc: string }[]
  return Array.isArray(items) ? items.map((item, i) => ({ ...item, icon: functionIcons[i] || '' })) : []
})

const festivalList = computed<FestivalItem[]>(() => {
  const items = tm('pages.culture.festivalList') as unknown as FestivalItem[]
  return Array.isArray(items) ? items : []
})
</script>

<style scoped>
.culture-page {
  padding-top: var(--space-12);
  padding-bottom: var(--space-16);
  animation: fadeIn var(--duration-normal) var(--ease-out) both;
}

/* 区域标签 */
.section-label {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: var(--weight-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-8);
  position: relative;
  padding-left: var(--space-4);
}

.section-label::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, var(--accent-gold), var(--accent-copper));
  border-radius: 2px;
}

/* 功能卡片 */
.function-card {
  text-align: center;
}

.function-card__icon {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: var(--space-4);
  color: var(--accent-gold);
  filter: drop-shadow(0 0 6px rgba(201, 162, 39, 0.25));
  transition: all var(--duration-normal) var(--ease-out);
}

.function-card:hover .function-card__icon {
  transform: scale(1.1);
  filter: drop-shadow(0 0 12px rgba(201, 162, 39, 0.5));
}

.function-card__title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
  margin-bottom: var(--space-3);
}

.function-card__desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin: 0;
}

/* 文化意义 */
.significance-block {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: var(--space-8);
  position: relative;
  overflow: hidden;
}

.significance-block::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
  opacity: 0.4;
}

.significance-block p {
  font-size: var(--text-base);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  text-align: justify;
}

/* 节日卡片 */
.festival-card {
  display: flex;
  flex-direction: column;
}

.festival-card__title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  color: var(--accent-gold-light);
  margin-bottom: var(--space-3);
  position: relative;
  padding-bottom: var(--space-3);
}

.festival-card__title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 2px;
  background: linear-gradient(90deg, var(--accent-gold), transparent);
}

.festival-card__desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin: 0;
}

/* 响应式 */
@media (max-width: 768px) {
  .culture-page {
    padding-top: var(--space-8);
    padding-bottom: var(--space-10);
  }

  .grid-3col {
    grid-template-columns: 1fr;
  }

  .significance-block {
    padding: var(--space-6);
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .grid-3col {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
