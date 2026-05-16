<template>
  <div class="status-page">
    <div class="container-narrow">
      <SectionHeader :title="t('pages.status.title')" :subtitle="t('pages.status.subtitle')" />

      <div class="grid-3col stats-grid">
        <StatCard :value="t('home.statsValues.collection')" :label="t('pages.status.collectionCount')" />
        <StatCard :value="t('home.statsValues.years')" :label="t('pages.status.culturalHistory')" />
        <StatCard :value="t('home.statsValues.types')" :label="t('pages.status.mainTypes')" />
      </div>

      <BronzeDivider />

      <div class="content-prose">
        <h2>{{ t('pages.status.protectionStatus') }}</h2>
        <p>{{ t('pages.status.protectionP1') }}</p>
        <p>{{ t('pages.status.protectionP2') }}</p>

        <h2>{{ t('pages.status.challenges') }}</h2>
        <p>{{ t('pages.status.challengeP1') }}</p>

        <h2>{{ t('pages.status.future') }}</h2>
        <p>{{ t('pages.status.futureP1') }}</p>
        <p>{{ t('pages.status.futureP2') }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'
import StatCard from '@/components/StatCard.vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<style scoped>
.status-page {
  padding: var(--space-8) 0 var(--space-16);
}

.stats-grid {
  gap: var(--space-6);
  margin-bottom: var(--space-4);
}

.content-prose h2 {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 600;
  color: var(--text-primary);
  margin-top: var(--space-8);
  margin-bottom: var(--space-4);
  position: relative;
  padding-left: var(--space-4);
}

.content-prose h2::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--accent-gold);
}

.content-prose p {
  text-indent: 2em;
  margin-bottom: var(--space-4);
  line-height: var(--leading-relaxed);
  color: var(--text-secondary);
}

@media (max-width: 768px) {
  .status-page {
    padding: var(--space-6) 0 var(--space-10);
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: var(--space-4);
  }

  .content-prose h2 {
    font-size: var(--text-xl);
    margin-top: var(--space-6);
  }
}
</style>
