<template>
  <div class="stat-card">
    <div v-if="icon" class="stat-card__icon">{{ icon }}</div>
    <div class="stat-card__body">
      <span class="stat-card__number">{{ value }}</span>
      <span class="stat-card__label">{{ label }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  value: string | number
  label: string
  icon?: string
}>()
</script>

<style scoped>
.stat-card {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-6);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-inset);
}

.stat-card__icon {
  font-size: var(--text-3xl);
  opacity: 0.6;
  line-height: 1;
}

.stat-card__body {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.stat-card__number {
  font-family: var(--font-mono);
  font-size: var(--text-4xl);
  font-weight: 700;
  color: var(--accent-gold);
  line-height: 1;
}

.stat-card__label {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

@media (max-width: 768px) {
  .stat-card {
    padding: var(--space-4);
  }

  .stat-card__number {
    font-size: var(--text-3xl);
  }
}

@media (max-width: 480px) {
  .stat-card {
    padding: var(--space-3);
  }

  .stat-card__number {
    font-size: var(--text-2xl);
  }
}
</style>
