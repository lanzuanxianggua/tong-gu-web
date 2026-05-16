<template>
  <div class="container-narrow section">
    <SectionHeader
      :title="t('pages.origin.title')"
      :subtitle="t('pages.origin.subtitle')"
    />

    <BronzeDivider />

    <div class="timeline">
      <div
        v-for="(entry, index) in timelineData"
        :key="index"
        class="timeline-item"
        :class="`animate-fade-in-up delay-${index + 1}`"
      >
        <div class="timeline-item__year">{{ entry.year }}</div>
        <div class="timeline-item__card archive-card">
          <h3 class="timeline-item__title">{{ entry.title }}</h3>
          <p class="timeline-item__text">{{ entry.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'

interface TimelineEntry {
  year: string
  title: string
  description: string
}

const { t, tm } = useI18n()

const timelineData = computed<TimelineEntry[]>(() => {
  const items = tm('pages.origin.timeline') as unknown as TimelineEntry[]
  return Array.isArray(items) ? items : []
})
</script>

<style scoped>
/* --- Timeline Layout --- */
.timeline {
  position: relative;
  padding-left: var(--space-12);
}

.timeline::before {
  content: '';
  position: absolute;
  left: 11px;
  top: 0;
  bottom: 0;
  width: 1px;
  background: linear-gradient(
    to bottom,
    var(--accent-gold),
    var(--accent-gold-light),
    var(--decor-line)
  );
}

.timeline-item {
  position: relative;
  padding-bottom: var(--space-10);
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: calc(-1 * var(--space-12) + 5px);
  top: 6px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--bg-primary);
  border: 2px solid var(--accent-gold);
  box-shadow: 0 0 8px rgba(201, 162, 39, 0.3);
  z-index: 1;
}

.timeline-item:last-child {
  padding-bottom: 0;
}

/* --- Year Label --- */
.timeline-item__year {
  font-family: var(--font-display);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  color: var(--accent-gold);
  letter-spacing: 0.05em;
  margin-bottom: var(--space-3);
}

/* --- Content Card --- */
.timeline-item__card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: var(--space-6);
  box-shadow: var(--shadow-inset);
  transition: border-color var(--duration-normal) var(--ease-out),
              box-shadow var(--duration-normal) var(--ease-out);
}

.timeline-item__card:hover {
  border-color: rgba(201, 162, 39, 0.4);
  box-shadow: var(--shadow-card), var(--shadow-inset);
}

.timeline-item__title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-3);
  line-height: var(--leading-tight);
}

.timeline-item__text {
  font-size: var(--text-base);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin: 0;
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .timeline {
    padding-left: var(--space-10);
  }

  .timeline-item {
    padding-bottom: var(--space-8);
  }

  .timeline-item::before {
    left: calc(-1 * var(--space-10) + 5px);
    width: 10px;
    height: 10px;
    top: 4px;
  }

  .timeline-item__card {
    padding: var(--space-5);
  }
}

@media (max-width: 640px) {
  .timeline {
    padding-left: var(--space-8);
  }

  .timeline-item::before {
    left: calc(-1 * var(--space-8) + 5px);
    width: 10px;
    height: 10px;
  }

  .timeline-item__card {
    padding: var(--space-4);
  }

  .timeline-item__title {
    font-size: var(--text-lg);
  }
}
</style>
