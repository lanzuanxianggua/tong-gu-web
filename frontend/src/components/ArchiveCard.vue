<template>
  <div class="archive-card" :class="{ 'archive-card--hoverable': hoverable }">
    <slot />
  </div>
</template>

<script setup lang="ts">
defineProps<{
  hoverable?: boolean
}>()
</script>

<style scoped>
.archive-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: var(--space-6);
  box-shadow: var(--shadow-inset);
  transition: border-color var(--duration-normal) var(--ease-out),
              box-shadow var(--duration-normal) var(--ease-out);
}

.archive-card--hoverable:hover {
  border-color: rgba(201, 162, 39, 0.4);
  box-shadow: var(--shadow-card), var(--shadow-inset);
}

@media (max-width: 768px) {
  .archive-card {
    padding: var(--space-4);
  }
}

@media (max-width: 480px) {
  .archive-card {
    padding: var(--space-3);
  }
}
</style>
