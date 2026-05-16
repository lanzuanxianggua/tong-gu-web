<template>
  <div class="container-narrow section">
    <SectionHeader :title="t('pages.preface.title')" :subtitle="t('pages.preface.subtitle')" />

    <BronzeDivider decorated />

    <div class="content-prose">
      <p>{{ t('pages.preface.p1') }}</p>
      <p>{{ t('pages.preface.p2') }}</p>
    </div>

    <BronzeDivider />

    <figure class="content-figure">
      <img
        :src="tongguImg"
        :alt="t('pages.preface.figCaption')"
        class="preface-image"
      />
      <figcaption>{{ t('pages.preface.figCaption') }}</figcaption>
    </figure>

    <BronzeDivider />

    <div class="cta-wrapper">
      <span class="cta-link" @click="router.push('/origin')">
        {{ t('pages.preface.ctaText') }}
        <span class="cta-arrow">&rarr;</span>
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import SectionHeader from '@/components/SectionHeader.vue'
import BronzeDivider from '@/components/BronzeDivider.vue'
import tongguImg from '@/assets/tonggu06.png'

const router = useRouter()
const { t } = useI18n()
</script>

<style scoped>
.content-prose p {
  text-indent: 2em;
  margin-bottom: var(--space-4);
  line-height: var(--leading-relaxed);
  color: var(--text-primary);
  font-size: var(--text-lg);
}

.content-prose p:last-child {
  margin-bottom: 0;
}

.preface-image {
  width: 280px;
  height: 280px;
  object-fit: cover;
  border: 1px solid var(--border-gold);
  border-radius: 50%;
  margin: 0 auto;
  transition: transform var(--duration-normal) var(--ease-out),
              box-shadow var(--duration-normal) var(--ease-out);
}

.preface-image:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-elevated);
}

.content-figure figcaption {
  margin-top: var(--space-4);
  font-size: var(--text-sm);
  color: var(--text-muted);
  font-style: italic;
}

.cta-wrapper {
  text-align: center;
  padding: var(--space-4) 0 var(--space-8);
}

.cta-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-body);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--accent-gold);
  cursor: pointer;
  transition: color var(--duration-fast) var(--ease-out),
              gap var(--duration-fast) var(--ease-out);
  letter-spacing: 0.05em;
}

.cta-link:hover {
  color: var(--accent-gold-light);
  gap: var(--space-3);
}

.cta-arrow {
  transition: transform var(--duration-fast) var(--ease-out);
}

.cta-link:hover .cta-arrow {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .preface-image {
    width: 220px;
    height: 220px;
  }

  .content-prose p {
    font-size: var(--text-base);
  }
}

@media (max-width: 480px) {
  .preface-image {
    width: 160px;
    height: 160px;
  }

  .cta-link {
    font-size: var(--text-base);
  }
}
</style>
