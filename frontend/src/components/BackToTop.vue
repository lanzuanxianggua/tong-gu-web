<template>
  <transition name="fade-up">
    <div
      v-if="visible"
      class="back-to-top"
      @click="scrollToTop"
      title="回到顶部"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M18 15l-6-6-6 6"/>
      </svg>
    </div>
  </transition>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const visible = ref(false)

function handleScroll() {
  visible.value = window.scrollY > window.innerHeight * 0.3
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.back-to-top {
  position: fixed;
  bottom: var(--space-8);
  right: var(--space-8);
  z-index: 9999;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  border-radius: 50%;
  color: var(--accent-gold);
  cursor: pointer;
  transition: all var(--duration-normal);
  box-shadow: var(--shadow-elevated);
}

.back-to-top:hover {
  background: var(--bg-hover);
  border-color: var(--accent-gold);
  transform: translateY(-3px);
}

.fade-up-enter-active,
.fade-up-leave-active {
  transition: all 0.3s ease-out;
}

.fade-up-enter-from {
  opacity: 0;
  transform: translateY(16px);
}

.fade-up-leave-to {
  opacity: 0;
  transform: translateY(8px);
}

@media (max-width: 768px) {
  .back-to-top {
    bottom: var(--space-4);
    right: var(--space-4);
  }
}
</style>
