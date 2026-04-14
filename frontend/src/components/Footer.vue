<template>
  <footer class="site-footer">
    <div class="footer-content">
      <div class="footer-main">
        <div class="footer-brand">
          <img src="@/assets/tonggu_logo.png" alt="铜鼓智能识别平台" class="footer-logo" />
          <div class="footer-info">
            <span class="footer-title">铜鼓智能识别与数字化保护平台</span>
            <span class="footer-subtitle">AI-Powered Bronze Drum Pattern Recognition</span>
          </div>
        </div>
      </div>

      <div class="footer-divider"></div>

      <div class="footer-bottom">
        <p class="copyright">&copy; {{ currentYear }} 铜鼓智能识别与数字化保护平台</p>
        <p class="beian">
          <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">桂 ICP 备 2026006185 号</a>
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script>

<style scoped>
.site-footer {
  width: 100%;
  background: rgba(0, 0, 0, 0.4);
  border-top: 1px solid rgba(212, 175, 55, 0.15);
  padding: 3rem 0 2rem;
  margin-top: auto;
}

.footer-content {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 2rem;
}

.footer-main {
  text-align: center;
  margin-bottom: 2rem;
}

.footer-brand {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
}

.footer-logo {
  height: 36px;
  width: auto;
  opacity: 0.85;
}

.footer-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 2px;
}

.footer-title {
  font-size: 1rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
}

.footer-subtitle {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 0.5px;
}

.footer-divider {
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(212, 175, 55, 0.25),
    transparent
  );
  margin: 1.5rem 0;
}

.footer-bottom {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.copyright {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.4);
}

.beian {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.3);
}

.beian a {
  color: rgba(255, 255, 255, 0.4);
  text-decoration: none;
  transition: color 0.2s ease;
}

.beian a:hover {
  color: #d4af37;
}

@media (max-width: 768px) {
  .site-footer {
    padding: 2rem 0 1.5rem;
  }

  .footer-content {
    padding: 0 1rem;
  }

  .footer-brand {
    flex-direction: column;
    gap: 0.75rem;
    text-align: center;
  }

  .footer-info {
    align-items: center;
  }

  .footer-title {
    font-size: 0.9rem;
  }

  .footer-subtitle {
    font-size: 0.7rem;
  }
}

@media (max-width: 480px) {
  .site-footer {
    padding: 1.5rem 0 1rem;
  }

  .footer-logo {
    height: 28px;
  }

  .footer-title {
    font-size: 0.85rem;
  }

  .footer-subtitle {
    font-size: 0.65rem;
  }

  .copyright,
  .beian {
    font-size: 0.7rem;
  }
}

@supports (padding: env(safe-area-inset-bottom)) {
  .site-footer {
    padding-bottom: calc(2rem + env(safe-area-inset-bottom));
  }
}
</style>
