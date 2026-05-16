<template>
  <div class="detection-card">
    <!-- Stamp -->
    <div class="detection-card__stamp">№{{ String(index + 1).padStart(3, '0') }}</div>

    <!-- Content -->
    <div class="detection-card__inner">
      <!-- Label tag -->
      <div class="detection-card__tag">{{ result.label }}</div>

      <!-- Confidence bar -->
      <div class="detection-card__confidence">
        <span class="detection-card__confidence-label">置信度</span>
        <div class="detection-card__confidence-bar">
          <div
            class="detection-card__confidence-fill"
            :style="{ width: `${result.confidence * 100}%` }"
          ></div>
        </div>
        <span class="detection-card__confidence-value">{{ (result.confidence * 100).toFixed(1) }}%</span>
      </div>

      <!-- Info list -->
      <dl class="detection-card__info" v-if="result.era || result.region">
        <template v-if="result.era">
          <dt>年代推测</dt>
          <dd>{{ result.era }}</dd>
        </template>
        <template v-if="result.region">
          <dt>地域类型</dt>
          <dd>{{ result.region }}</dd>
        </template>
      </dl>

      <!-- Remark input slot -->
      <slot name="remark" />

      <!-- Actions slot -->
      <slot name="actions" />
    </div>
  </div>
</template>

<script setup lang="ts">
import type { DetectionResult } from '@/types'

defineProps<{
  result: DetectionResult
  index: number
}>()
</script>

<style scoped>
.detection-card {
  position: relative;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: var(--space-6);
  box-shadow: var(--shadow-inset);
  transition: border-color var(--duration-normal) var(--ease-out);
  overflow: hidden;
}

.detection-card:hover {
  border-color: rgba(201, 162, 39, 0.35);
}

/* Stamp */
.detection-card__stamp {
  position: absolute;
  top: var(--space-4);
  right: var(--space-4);
  width: 36px;
  height: 36px;
  border: 1px solid var(--accent-gold);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 9px;
  color: var(--accent-gold);
  opacity: 0.7;
  letter-spacing: -0.5px;
}

/* Tag */
.detection-card__tag {
  display: inline-block;
  font-family: var(--font-display);
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--accent-gold);
  padding-bottom: var(--space-2);
  border-bottom: 1px solid var(--border-gold);
  margin-bottom: var(--space-4);
}

/* Confidence */
.detection-card__confidence {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}

.detection-card__confidence-label {
  font-size: var(--text-xs);
  color: var(--text-muted);
  white-space: nowrap;
}

.detection-card__confidence-bar {
  flex: 1;
  height: 4px;
  background: var(--bg-hover);
  border-radius: 2px;
  overflow: hidden;
}

.detection-card__confidence-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-copper), var(--accent-gold));
  border-radius: 2px;
  transition: width 0.6s var(--ease-out);
}

.detection-card__confidence-value {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  min-width: 48px;
  text-align: right;
}

/* Info list */
.detection-card__info {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: var(--space-1) var(--space-4);
  margin-bottom: var(--space-4);
}

.detection-card__info dt {
  font-size: var(--text-xs);
  color: var(--text-muted);
  white-space: nowrap;
}

.detection-card__info dd {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

@media (max-width: 768px) {
  .detection-card {
    padding: var(--space-4);
  }

  .detection-card__stamp {
    width: 28px;
    height: 28px;
    font-size: 8px;
  }

  .detection-card__confidence {
    flex-wrap: wrap;
    gap: var(--space-2);
  }

  .detection-card__confidence-bar {
    flex-basis: 100%;
    order: 2;
  }

  .detection-card__confidence-value {
    order: 3;
    margin-left: auto;
  }
}
</style>
