<template>
  <Teleport to="body">
    <transition name="terms-fade">
      <div v-if="visible" class="terms-overlay" @click.self="close">
        <div class="terms-dialog">
          <div class="terms-dialog__header">
            <h2 class="terms-dialog__title">{{ t('terms.title') }}</h2>
            <button class="terms-dialog__close" @click="close" aria-label="Close">&times;</button>
          </div>

          <div class="terms-dialog__deco"></div>

          <div ref="contentRef" class="terms-dialog__content" @scroll="checkScroll">
            <p v-for="(para, i) in tm('terms.content')" :key="i" class="terms-dialog__para">{{ para }}</p>
          </div>

          <div class="terms-dialog__deco"></div>

          <div class="terms-dialog__footer">
            <label class="terms-dialog__agree" @click.prevent="toggleAgree">
              <span class="terms-dialog__checkbox" :class="{ checked: agreed }">
                <span v-if="agreed" class="terms-dialog__check">&#10003;</span>
              </span>
              <span>{{ t('auth.agreeTerms') }}</span>
            </label>
            <button class="terms-dialog__btn" :disabled="!agreed" @click="confirm">
              {{ t('common.confirm') }}
            </button>
          </div>
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

const visible = ref(false)
const agreed = ref(false)
const scrolledToBottom = ref(false)
const contentRef = ref<HTMLElement | null>(null)

const emit = defineEmits<{
  (e: 'confirm'): void
}>()

function open() {
  visible.value = true
  agreed.value = false
  scrolledToBottom.value = false
}

function close() {
  visible.value = false
}

function toggleAgree() {
  if (scrolledToBottom.value) {
    agreed.value = !agreed.value
  }
}

function checkScroll() {
  if (!contentRef.value) return
  const el = contentRef.value
  const atBottom = el.scrollTop + el.clientHeight >= el.scrollHeight - 20
  if (atBottom) scrolledToBottom.value = true
}

function confirm() {
  if (agreed.value) {
    visible.value = false
    emit('confirm')
  }
}

defineExpose({ open, close })
</script>

<style scoped>
.terms-overlay {
  position: fixed;
  inset: 0;
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
}

.terms-dialog {
  width: 90%;
  max-width: 520px;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-elevated);
}

.terms-dialog__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--decor-line);
}

.terms-dialog__title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--text-primary);
}

.terms-dialog__close {
  font-size: var(--text-2xl);
  color: var(--text-muted);
  background: none;
  border: none;
  cursor: pointer;
  line-height: 1;
  transition: color var(--duration-fast);
}

.terms-dialog__close:hover {
  color: var(--text-primary);
}

.terms-dialog__deco {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
  opacity: 0.2;
}

.terms-dialog__content {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-5);
  max-height: 50vh;
}

.terms-dialog__para {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-4);
  text-indent: 2em;
}

.terms-dialog__para:last-child {
  margin-bottom: 0;
}

.terms-dialog__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  border-top: 1px solid var(--decor-line);
}

.terms-dialog__agree {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  cursor: pointer;
  user-select: none;
}

.terms-dialog__checkbox {
  width: 16px;
  height: 16px;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--duration-fast);
  flex-shrink: 0;
}

.terms-dialog__checkbox.checked {
  border-color: var(--accent-gold);
  background: var(--accent-gold);
}

.terms-dialog__check {
  font-size: 10px;
  color: var(--text-on-accent);
  font-weight: 700;
}

.terms-dialog__btn {
  padding: var(--space-2) var(--space-5);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--text-on-accent);
  background: var(--accent-gold);
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: background var(--duration-fast);
}

.terms-dialog__btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.terms-dialog__btn:not(:disabled):hover {
  background: var(--accent-gold-light);
}

.terms-fade-enter-active,
.terms-fade-leave-active {
  transition: opacity var(--duration-normal);
}

.terms-fade-enter-from,
.terms-fade-leave-to {
  opacity: 0;
}
</style>
