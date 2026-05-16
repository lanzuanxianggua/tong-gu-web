<template>
  <div class="bronze-divider" :class="`bronze-divider--${variant}`">
    <span v-if="decorated" class="bronze-divider__ornament">◆</span>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  variant?: 'default' | 'thick' | 'gold'
  decorated?: boolean
}>()
</script>

<style scoped>
.bronze-divider {
  border-top: 1px solid var(--decor-line);
  border-bottom: 1px solid var(--decor-line);
  height: 0;
  margin: var(--space-8) 0;
  position: relative;
}

.bronze-divider--thick {
  border-top-width: 1px;
  border-bottom-width: 1px;
  border-top-color: var(--border-subtle);
  border-bottom-color: var(--border-subtle);
  margin: var(--space-10) 0;
}

.bronze-divider--gold {
  border-top-color: var(--border-gold);
  border-bottom-color: var(--border-gold);
}

.bronze-divider__ornament {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: var(--bg-primary);
  padding: 0 var(--space-4);
  color: var(--accent-gold);
  font-size: 10px;
  letter-spacing: 4px;
  opacity: 0.6;
}
</style>
