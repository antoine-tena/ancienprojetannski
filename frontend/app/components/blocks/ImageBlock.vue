<template>
  <section class="image-block py-12">
    <UContainer>
      <img
        v-if="block.props.imageUrl"
        :src="block.props.imageUrl"
        :alt="block.props.alt || 'Image'"
        class="w-full h-auto rounded-lg shadow-lg"
      >
    </UContainer>
  </section>
</template>

<script setup lang="ts">
import type { Block } from '~/stores/editor'

defineProps<{
  block: Block
}>()
</script>
