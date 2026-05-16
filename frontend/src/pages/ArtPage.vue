<template>
  <div class="art-page">
    <div class="container-narrow">
      <SectionHeader :title="t('pages.art.title')" :subtitle="t('pages.art.subtitle')" />

      <div class="grid-2col art-grid">
        <ArchiveCard v-for="art in arts" :key="art.title" hoverable>
          <div class="art-card">
            <div class="art-card__icon">{{ art.icon }}</div>
            <h3 class="art-card__title">{{ art.title }}</h3>
            <p class="art-card__desc">{{ art.desc }}</p>
          </div>
        </ArchiveCard>
      </div>

      <BronzeDivider />

      <div class="content-prose">
        <h2 class="section-header__title">{{ t('pages.art.culturalSignificance') }}</h2>
        <p>{{ t('pages.art.culturalP1') }}</p>
        <p>{{ t('pages.art.culturalP2') }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'
import ArchiveCard from '@/components/ArchiveCard.vue'
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

const arts = computed(() => {
  const items = tm('pages.art.artItems') as unknown as { icon: string; title: string; desc: string }[]
  return Array.isArray(items) ? items : []
})
</script>

<style scoped>
.art-page {
  padding: var(--space-8) 0 var(--space-16);
}

.art-grid {
  gap: var(--space-6);
}

.art-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  text-align: center;
}

.art-card__icon {
  font-size: var(--text-4xl);
  line-height: 1;
  opacity: 0.7;
}

.art-card__title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 600;
  color: var(--accent-gold);
}

.art-card__desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
}

.content-prose {
  padding-top: var(--space-4);
}

.content-prose h2 {
  margin-bottom: var(--space-4);
}

.content-prose p {
  text-indent: 2em;
  margin-bottom: var(--space-4);
  line-height: var(--leading-relaxed);
  color: var(--text-secondary);
}

@media (max-width: 768px) {
  .art-page {
    padding: var(--space-6) 0 var(--space-10);
  }

  .art-grid {
    grid-template-columns: 1fr;
    gap: var(--space-4);
  }

  .art-card__icon {
    font-size: var(--text-3xl);
  }
}
</style>
