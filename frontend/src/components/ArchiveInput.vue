<template>
  <div class="archive-input" :class="{ 'archive-input--focused': focused }">
    <label v-if="label" class="archive-input__label">{{ label }}</label>
    <input
      ref="inputRef"
      class="archive-input__field"
      :type="type"
      :value="modelValue"
      :placeholder="placeholder"
      :disabled="disabled"
      :readonly="readonly"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      @focus="focused = true"
      @blur="focused = false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  modelValue?: string | number
  label?: string
  type?: string
  placeholder?: string
  disabled?: boolean
  readonly?: boolean
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()

const focused = ref(false)
</script>

<style scoped>
.archive-input {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.archive-input__label {
  font-size: var(--text-sm);
  color: var(--text-muted);
  font-weight: 500;
}

.archive-input__field {
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: var(--text-base);
  padding: var(--space-2) 0;
  outline: none;
  transition: border-color var(--duration-fast) var(--ease-out),
              border-width var(--duration-fast) var(--ease-out);
}

.archive-input__field::placeholder {
  color: var(--text-muted);
}

.archive-input--focused .archive-input__field,
.archive-input__field:focus {
  border-bottom-color: var(--accent-gold);
  border-bottom-width: 2px;
}

.archive-input__field:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

@media (max-width: 480px) {
  .archive-input__field {
    min-height: 44px;
  }
}
</style>
