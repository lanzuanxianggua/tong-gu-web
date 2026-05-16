<template>
  <div class="section-header">
    <div v-if="title" class="section-header__title-wrap">
      <span class="section-header__deco" aria-hidden="true">◇</span>
      <h2 class="section-header__title">{{ title }}</h2>
      <span class="section-header__deco" aria-hidden="true">◇</span>
    </div>
    <p v-if="subtitle" class="section-header__subtitle">{{ subtitle }}</p>
    <slot />
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title?: string
  subtitle?: string
}>()
</script>

<style scoped>
.section-header {
  margin-bottom: var(--space-8);
}

.section-header__title-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-3);
}

.section-header__title {
  font-family: var(--font-display);
  font-size: var(--text-4xl);
  font-weight: 700;
  color: var(--text-primary);
  line-height: var(--leading-tight);
  position: relative;
  display: inline-block;
}

.section-header__title::after {
  content: '';
  display: block;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
  margin-top: var(--space-3);
  animation: line-expand 0.8s var(--ease-out) both;
}

@keyframes line-expand {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}

.section-header__deco {
  color: var(--accent-gold);
  opacity: 0.3;
  font-size: var(--text-sm);
}

.section-header__subtitle {
  font-size: var(--text-lg);
  color: var(--text-secondary);
  margin-top: var(--space-3);
  line-height: var(--leading-relaxed);
  text-align: center;
}

@media (max-width: 768px) {
  .section-header__title {
    font-size: var(--text-3xl);
  }

  .section-header__subtitle {
    font-size: var(--text-base);
  }

  .section-header {
    margin-bottom: var(--space-6);
  }
}

@media (max-width: 480px) {
  .section-header__title {
    font-size: var(--text-2xl);
  }

  .section-header__subtitle {
    font-size: var(--text-sm);
  }
}
</style>
