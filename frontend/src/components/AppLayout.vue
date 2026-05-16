<template>
  <div class="archive-layout">
    <AppNav />
    <main class="archive-main">
      <router-view v-slot="{ Component }">
        <transition name="page-fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
    <Footer />
    <BackToTop />
  </div>
</template>

<script setup lang="ts">
import AppNav from '@/components/AppNav.vue'
import Footer from '@/components/Footer.vue'
import BackToTop from '@/components/BackToTop.vue'
</script>

<style scoped>
.archive-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.archive-main {
  flex: 1;
  padding-top: 64px;
}

.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity var(--duration-normal);
}

.page-fade-enter-from,
.page-fade-leave-to {
  opacity: 0;
}
</style>
