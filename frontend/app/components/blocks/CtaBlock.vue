<template>
  <section
    class="cta-block py-16"
    :style="{
      backgroundColor: block.props.backgroundColor || '#3b82f6'
    }"
  >
    <UContainer>
      <div class="text-center text-white">
        <h2 class="text-4xl font-bold mb-4">
          {{ block.props.title }}
        </h2>
        <p class="text-xl mb-8 opacity-90">
          {{ block.props.content }}
        </p>
        <UButton
          v-if="block.props.buttonText"
          :to="block.props.buttonUrl"
          size="xl"
          color="white"
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
