<template>
  <footer class="site-footer">
    <div class="footer-content">
      <div class="footer-brand">
        <img src="@/assets/tonggu_logo.png" :alt="t('footer.brand')" class="footer-logo" />
        <span class="footer-title">{{ t('footer.brand') }}</span>
        <span class="footer-divider-dot">·</span>
        <span class="footer-subtitle">{{ t('footer.brandEn') }}</span>
      </div>
      <div class="footer-bottom">
        <span class="copyright">&copy; {{ currentYear }} {{ t('footer.copyright') }}</span>
        <span class="footer-divider-dot">|</span>
        <a :href="t('footer.beianUrl')" target="_blank" rel="noopener noreferrer" class="beian">{{ t('footer.beian') }}</a>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const currentYear = computed(() => new Date().getFullYear())
</script>

<style scoped>
.site-footer {
  width: 100%;
  background: var(--bg-elevated);
  border-top: 1px solid transparent;
  border-image: linear-gradient(90deg, transparent, rgba(201,162,39,0.2), transparent) 1;
  padding: var(--space-5) 0;
  margin-top: auto;
  position: relative;
}

.footer-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 var(--space-6);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.footer-brand {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
}

.footer-logo {
  height: 24px;
  width: auto;
  opacity: 0.8;
}

.footer-title {
  font-family: var(--font-display);
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--text-primary);
}

.footer-subtitle {
  font-size: var(--text-xs);
  color: var(--text-muted);
  letter-spacing: 0.3px;
}

.footer-divider-dot {
  color: var(--text-muted);
  opacity: 0.4;
  font-size: var(--text-xs);
}

.footer-bottom {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
}

.copyright {
  font-size: var(--text-xs);
  color: var(--text-muted);
}

.beian {
  font-size: var(--text-xs);
  color: var(--text-muted);
  text-decoration: none;
  transition: color var(--duration-fast);
}

.beian:hover {
  color: var(--accent-gold);
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
    gap: var(--space-3);
    padding: 0 var(--space-4);
  }

  .footer-brand {
    flex-wrap: wrap;
    justify-content: center;
  }
}

@supports (padding: env(safe-area-inset-bottom)) {
  .site-footer {
    padding-bottom: calc(var(--space-4) + env(safe-area-inset-bottom));
  }
}
</style>
