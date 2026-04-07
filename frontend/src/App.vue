<template>
  <router-view />
</template>

<script setup>
import './assets/theme.css'
// 导入滚动动画工具
import './utils/scrollAnimation.js'
</script>

<style>
#app {
  font-family: "Noto Sans SC", "思源黑体", Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 100%;
  min-height: 100%;
}

body {
  margin: 0;
  padding: 0;
  width: 100%;
  min-height: 100%;
}

html {
  width: 100%;
  min-height: 100%;
}
</style>
