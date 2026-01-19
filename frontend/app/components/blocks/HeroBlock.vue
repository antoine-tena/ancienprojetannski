<template>
  <section
    class="hero-block"
    :style="{
      backgroundColor: block.props.backgroundColor || '#1f2937',
      color: block.props.textColor || '#ffffff'
    }"
  >
    <UContainer>
      <div class="py-20 text-center">
        <h1 class="text-5xl font-bold mb-6">
          {{ block.props.title }}
        </h1>
        <p class="text-xl mb-8 max-w-2xl mx-auto opacity-90">
          {{ block.props.content }}
        </p>
        <UButton
          v-if="block.props.buttonText"
          :to="block.props.buttonUrl"
          size="xl"
          color="primary"
        >
          {{ block.props.buttonText }}
        </UButton>
      </div>
    </UContainer>
  </section>
</template>

<script setup lang="ts">
import type { Block } from '~/stores/editor'

defineProps<{
  block: Block
}>()
</script>

<style scoped>
.hero-block {
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
