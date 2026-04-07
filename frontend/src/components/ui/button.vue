<script setup lang="ts">
interface Props {
  type?: 'button' | 'submit' | 'reset'
  disabled?: boolean
  className?: string
}

const props = withDefaults(defineProps<Props>(), {
  type: 'button',
  disabled: false,
  className: ''
})

const emit = defineEmits<{
  click: [e: MouseEvent]
}>()
</script>

<template>
  <button
    :type="type"
    :class="className"
    :disabled="disabled"
    @click="emit('click', $event)"
  >
    <slot>Button</slot>
  </button>
</template>