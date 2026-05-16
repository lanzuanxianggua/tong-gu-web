<template>
  <button
    class="btn-archive"
    :class="[
      `btn-archive--${variant}`,
      { 'btn-archive--full': fullWidth, 'btn-archive--sm': size === 'sm', 'btn-archive--lg': size === 'lg' }
    ]"
    :disabled="disabled || loading"
    @click="$emit('click', $event)"
  >
    <span v-if="loading" class="btn-archive__spinner"></span>
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps<{
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  fullWidth?: boolean
  disabled?: boolean
  loading?: boolean
}>()

defineEmits<{
  click: [e: MouseEvent]
}>()
</script>

<style scoped>
.btn-archive {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  font-family: var(--font-body);
  font-weight: 600;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
  border: none;
  position: relative;
  white-space: nowrap;
  user-select: none;
}

.btn-archive:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Sizes */
.btn-archive--sm {
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-sm);
}

.btn-archive--lg {
  padding: var(--space-3) var(--space-8);
  font-size: var(--text-lg);
}

/* Default (md) */
.btn-archive:not(.btn-archive--sm):not(.btn-archive--lg) {
  padding: var(--space-2) var(--space-5);
  font-size: var(--text-base);
}

/* Primary — gold filled with bottom accent */
.btn-archive--primary {
  background: var(--accent-gold);
  color: var(--text-on-accent);
  border-bottom: 2px solid #a68520;
}

.btn-archive--primary:hover:not(:disabled) {
  background: var(--accent-gold-light);
}

/* Secondary — outlined gold */
.btn-archive--secondary {
  background: transparent;
  color: var(--accent-gold);
  border: 1px solid var(--accent-gold);
  border-bottom: 2px solid var(--accent-gold);
}

.btn-archive--secondary:hover:not(:disabled) {
  background: rgba(201, 162, 39, 0.08);
}

/* Ghost — text only */
.btn-archive--ghost {
  background: transparent;
  color: var(--text-secondary);
  border: none;
}

.btn-archive--ghost:hover:not(:disabled) {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.04);
}

/* Danger — rust red */
.btn-archive--danger {
  background: transparent;
  color: var(--accent-red);
  border: 1px solid var(--accent-red);
}

.btn-archive--danger:hover:not(:disabled) {
  background: rgba(160, 64, 64, 0.12);
}

/* Full width */
.btn-archive--full {
  width: 100%;
}

@media (max-width: 480px) {
  .btn-archive {
    min-height: 44px;
  }

  .btn-archive--sm {
    min-height: 36px;
  }
}

/* Spinner */
.btn-archive__spinner {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: btn-spin 0.6s linear infinite;
}

@keyframes btn-spin {
  to { transform: rotate(360deg); }
}
</style>
