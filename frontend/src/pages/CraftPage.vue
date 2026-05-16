<template>
  <div class="container-narrow section">
    <SectionHeader
      :title="t('pages.craft.title')"
      :subtitle="t('pages.craft.subtitle')"
    />

    <BronzeDivider />

    <!-- 制作流程 -->
    <section class="craft-section">
      <h3 class="section-label">{{ t('pages.craft.process') }}</h3>
      <div class="steps-flow">
        <div
          v-for="(step, index) in steps"
          :key="index"
          class="step-item animate-fade-in-up"
          :class="`delay-${index + 1}`"
        >
          <div class="step-number">{{ step.num }}</div>
          <div class="step-label">{{ step.label }}</div>
        </div>
      </div>
    </section>

    <BronzeDivider decorated />

    <!-- 工艺特点 -->
    <section class="craft-section">
      <h3 class="section-label">{{ t('pages.craft.features') }}</h3>
      <div class="features-grid">
        <ArchiveCard
          v-for="(feature, index) in features"
          :key="index"
          hoverable
          class="animate-fade-in-up"
          :class="`delay-${index + 1}`"
        >
          <h4 class="feature-title">{{ feature.title }}</h4>
          <p class="feature-desc">{{ feature.desc }}</p>
        </ArchiveCard>
      </div>
    </section>

    <BronzeDivider decorated />

    <!-- 铸造方法 -->
    <section class="craft-section">
      <h3 class="section-label">{{ t('pages.craft.methods') }}</h3>
      <div class="methods-grid">
        <div
          v-for="(method, index) in methods"
          :key="index"
          class="method-card animate-fade-in-up"
          :class="`delay-${index + 1}`"
        >
          <h4 class="method-title">{{ method.title }}</h4>
          <p class="method-desc">{{ method.desc }}</p>
        </div>
      </div>
    </section>

    <BronzeDivider variant="thick" />

    <!-- 非遗传承 -->
    <section class="craft-section ich-section">
      <h3 class="section-label">{{ t('pages.craft.ichHeritage') }}</h3>
      <div class="ich-content">
        <p>{{ t('pages.craft.ichP1') }}</p>
        <p>{{ t('pages.craft.ichP2') }}</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'
import ArchiveCard from '@/components/ArchiveCard.vue'

const { t, tm } = useI18n()

interface Step {
  num: number
  label: string
}

interface Feature {
  title: string
  desc: string
}

interface Method {
  title: string
  desc: string
}

const steps = computed<Step[]>(() => {
  const items = tm('pages.craft.steps') as unknown as { label: string }[]
  return Array.isArray(items) ? items.map((item, i) => ({ num: i + 1, label: item.label })) : []
})

const features = computed<Feature[]>(() => {
  const items = tm('pages.craft.featureList') as unknown as Feature[]
  return Array.isArray(items) ? items : []
})

const methods = computed<Method[]>(() => {
  const items = tm('pages.craft.methodList') as unknown as Method[]
  return Array.isArray(items) ? items : []
})
</script>

<style scoped>
/* --- Section Label --- */
.section-label {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: var(--weight-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-6);
  position: relative;
  display: inline-block;
}

.section-label::after {
  content: '';
  display: block;
  width: 32px;
  height: 2px;
  background: linear-gradient(90deg, var(--accent-gold), transparent);
  margin-top: var(--space-2);
}

/* --- Section Spacing --- */
.craft-section {
  margin-bottom: var(--space-10);
}

.craft-section:last-child {
  margin-bottom: 0;
}

/* --- Steps Horizontal Flow --- */
.steps-flow {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: var(--space-4);
}

.step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-6) var(--space-3);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-inset);
  transition: border-color var(--duration-normal) var(--ease-out),
              box-shadow var(--duration-normal) var(--ease-out),
              transform var(--duration-normal) var(--ease-out);
}

.step-item:hover {
  border-color: rgba(201, 162, 39, 0.4);
  box-shadow: var(--shadow-card), var(--shadow-inset);
  transform: translateY(-2px);
}

.step-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display);
  font-size: var(--text-lg);
  font-weight: var(--weight-bold);
  color: var(--bg-primary);
  background: linear-gradient(135deg, var(--accent-gold-light), var(--accent-gold));
  flex-shrink: 0;
}

.step-label {
  font-family: var(--font-display);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  color: var(--text-primary);
  text-align: center;
  white-space: nowrap;
}

/* --- Features Grid --- */
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

.feature-title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--accent-gold);
  margin-bottom: var(--space-3);
  line-height: var(--leading-tight);
}

.feature-desc {
  font-size: var(--text-base);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin: 0;
}

/* --- Methods Grid --- */
.methods-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-6);
}

.method-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-left: 3px solid var(--accent-gold);
  border-radius: var(--radius-sm);
  padding: var(--space-6);
  box-shadow: var(--shadow-inset);
  transition: border-color var(--duration-normal) var(--ease-out),
              box-shadow var(--duration-normal) var(--ease-out);
}

.method-card:hover {
  border-color: rgba(201, 162, 39, 0.4);
  border-left-color: var(--accent-gold);
  box-shadow: var(--shadow-card), var(--shadow-inset);
}

.method-title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--text-primary);
  margin-bottom: var(--space-3);
  line-height: var(--leading-tight);
}

.method-desc {
  font-size: var(--text-base);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin: 0;
}

/* --- ICH Section --- */
.ich-content p {
  text-indent: 2em;
  font-size: var(--text-base);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-4);
}

.ich-content p:last-child {
  margin-bottom: 0;
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .steps-flow {
    grid-template-columns: repeat(3, 1fr);
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .methods-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .steps-flow {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
