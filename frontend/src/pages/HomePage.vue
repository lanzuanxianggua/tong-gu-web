<template>
  <div class="home-page">
    <!-- Hero Section — Full viewport immersive -->
    <section class="hero">
      <div class="hero__drum" aria-hidden="true">
        <div class="hero__drum-ring hero__drum-ring--1"></div>
        <div class="hero__drum-ring hero__drum-ring--2"></div>
        <div class="hero__drum-ring hero__drum-ring--3"></div>
        <div class="hero__drum-ring hero__drum-ring--4"></div>
        <div class="hero__drum-ring hero__drum-ring--5"></div>
        <div class="hero__drum-core"></div>
      </div>
      <div class="hero__content">
        <h1 class="hero__title text-shimmer">{{ t('home.heroTitle') }}</h1>
        <p class="hero__subtitle">{{ t('home.heroSubtitle') }}</p>
        <div class="hero__cta">
          <ArchiveButton variant="primary" size="lg" @click="$router.push('/detection')">{{ t('home.ctaDetect') }}</ArchiveButton>
          <ArchiveButton variant="secondary" size="lg" @click="$router.push('/preface')">{{ t('home.ctaLearnMore') }}</ArchiveButton>
        </div>
      </div>
    </section>

    <div class="container">
      <BronzeDivider decorated />

      <!-- Feature Cards -->
      <section class="features">
        <div class="features__grid">
          <ArchiveCard
            v-for="(feature, i) in features"
            :key="feature.title()"
            class="features__card animate-fade-in-up"
            :style="{ animationDelay: `${(i + 1) * 120}ms` }"
          >
            <div class="feature-card__icon" v-html="feature.icon"></div>
            <h3 class="feature-card__title">{{ feature.title() }}</h3>
            <p class="feature-card__desc">{{ feature.desc() }}</p>
            <router-link :to="feature.href" class="feature-card__link">
              {{ feature.cta() }} <span class="feature-card__arrow">&rarr;</span>
            </router-link>
          </ArchiveCard>
        </div>
      </section>

      <BronzeDivider decorated />

      <!-- Stats Section -->
      <section class="stats">
        <div class="stats__grid">
          <div
            v-for="(stat, i) in stats"
            :key="stat.label()"
            class="stat-block animate-fade-in-up"
            :style="{ animationDelay: `${(i + 1) * 150}ms` }"
          >
            <span class="stat-block__icon">{{ stat.icon }}</span>
            <span class="stat-block__value">{{ stat.value() }}</span>
            <span class="stat-block__label">{{ stat.label() }}</span>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import ArchiveCard from '@/components/ArchiveCard.vue'
import ArchiveButton from '@/components/ArchiveButton.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'

const { t } = useI18n()

const features = [
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>',
    title: () => t('home.featureAI.title'),
    desc: () => t('home.featureAI.desc'),
    href: '/detection',
    cta: () => t('home.featureAI.cta'),
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
    title: () => t('home.featureEncyclopedia.title'),
    desc: () => t('home.featureEncyclopedia.desc'),
    href: '/types',
    cta: () => t('home.featureEncyclopedia.cta'),
  },
  {
    icon: '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>',
    title: () => t('home.featureGallery.title'),
    desc: () => t('home.featureGallery.desc'),
    href: '/samples',
    cta: () => t('home.featureGallery.cta'),
  },
]

const stats = [
  { icon: '🏛️', value: () => t('home.statsValues.collection'), label: () => t('home.stats.collection') },
  { icon: '⏳', value: () => t('home.statsValues.years'), label: () => t('home.stats.years') },
  { icon: '📖', value: () => t('home.statsValues.types'), label: () => t('home.stats.types') },
]
</script>

<style scoped>
.home-page {
  padding-bottom: var(--space-16);
}

/* ===== Hero — Full Viewport ===== */
.hero {
  position: relative;
  min-height: 92vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: var(--space-16) var(--space-6);
}

.hero__drum {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(600px, 80vw);
  height: min(600px, 80vw);
  pointer-events: none;
}

.hero__drum-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid var(--decor-pattern);
  animation: drum-pulse 8s ease-in-out infinite;
}

.hero__drum-ring--1 { inset: 0; animation-delay: 0s; }
.hero__drum-ring--2 { inset: 8%; border-color: rgba(201,162,39,0.08); animation-delay: 1.6s; }
.hero__drum-ring--3 { inset: 16%; border-color: rgba(201,162,39,0.1); animation-delay: 3.2s; }
.hero__drum-ring--4 { inset: 26%; border-color: rgba(201,162,39,0.06); animation-delay: 4.8s; }
.hero__drum-ring--5 { inset: 38%; border-color: rgba(184,115,51,0.08); animation-delay: 6.4s; }

.hero__drum-core {
  position: absolute;
  inset: 46%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(201,162,39,0.06) 0%, transparent 70%);
  border: 1px solid rgba(201,162,39,0.08);
}

@keyframes drum-pulse {
  0%, 100% { opacity: 0.4; transform: scale(1); }
  50%      { opacity: 1; transform: scale(1.02); }
}

.hero__content {
  position: relative;
  z-index: 1;
  text-align: center;
  animation: fadeInUp 0.8s var(--ease-out) both;
}

.hero__title {
  font-family: var(--font-display);
  font-size: var(--text-6xl);
  font-weight: 900;
  line-height: var(--leading-tight);
  margin-bottom: var(--space-6);
  letter-spacing: 0.04em;
}

.hero__subtitle {
  font-size: var(--text-lg);
  color: var(--text-secondary);
  margin-bottom: var(--space-10);
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  line-height: var(--leading-relaxed);
}

.hero__cta {
  display: flex;
  gap: var(--space-4);
  justify-content: center;
}

/* ===== Features ===== */
.features {
  padding: var(--space-8) 0;
}

.features__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

.feature-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.feature-card__icon {
  color: var(--accent-gold);
  width: 32px;
  height: 32px;
}

.feature-card__title {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--text-primary);
}

.feature-card__desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  flex: 1;
}

.feature-card__link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--text-sm);
  color: var(--accent-gold);
  text-decoration: none;
  font-weight: 500;
  transition: color var(--duration-fast), gap var(--duration-fast);
}

.feature-card__link:hover {
  color: var(--accent-gold-light);
  gap: var(--space-2);
}

/* ===== Stats ===== */
.stats {
  padding: var(--space-10) 0 var(--space-4);
}

.stats__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

.stat-block {
  text-align: center;
  padding: var(--space-8) var(--space-6);
  position: relative;
}

.stat-block::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
  opacity: 0.3;
}

.stat-block__icon {
  display: block;
  font-size: 28px;
  opacity: 0.6;
  margin-bottom: var(--space-3);
}

.stat-block__value {
  display: block;
  font-family: var(--font-mono);
  font-size: var(--text-5xl);
  font-weight: 500;
  color: var(--accent-gold);
  line-height: 1;
  margin-bottom: var(--space-2);
}

.stat-block__label {
  display: block;
  font-size: var(--text-sm);
  color: var(--text-secondary);
  font-weight: var(--weight-medium);
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .hero {
    min-height: 75vh;
    padding: var(--space-16) var(--space-4);
  }

  .hero__drum {
    width: min(400px, 90vw);
    height: min(400px, 90vw);
  }

  .hero__title {
    font-size: var(--text-4xl);
    letter-spacing: 0.02em;
  }

  .hero__subtitle {
    font-size: var(--text-base);
    margin-bottom: var(--space-8);
  }

  .hero__cta {
    flex-direction: column;
    align-items: center;
    gap: var(--space-3);
  }

  .features__grid {
    grid-template-columns: 1fr;
    gap: var(--space-4);
  }

  .stats__grid {
    grid-template-columns: 1fr;
    gap: var(--space-2);
  }

  .stat-block {
    padding: var(--space-5) var(--space-4);
  }

  .stat-block__value {
    font-size: var(--text-4xl);
  }
}

@media (max-width: 480px) {
  .hero {
    min-height: 65vh;
    padding: var(--space-10) var(--space-3);
  }

  .hero__drum {
    width: min(300px, 95vw);
    height: min(300px, 95vw);
  }

  .hero__title {
    font-size: var(--text-2xl);
  }

  .hero__subtitle {
    font-size: var(--text-sm);
    margin-bottom: var(--space-6);
  }

  .hero__cta :deep(.btn-archive) {
    width: 100%;
    max-width: none;
  }

  .stat-block__value {
    font-size: var(--text-3xl);
  }
}
</style>
