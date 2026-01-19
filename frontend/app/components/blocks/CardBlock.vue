<template>
  <section class="card-block py-12">
    <UContainer>
      <UCard>
        <img
          v-if="block.props.imageUrl"
          :src="block.props.imageUrl"
          :alt="block.props.title"
          class="w-full h-48 object-cover rounded-t-lg"
        >
        <template #header>
          <h3 class="text-2xl font-bold">
            {{ block.props.title }}
          </h3>
        </template>
        <p class="text-gray-600 dark:text-gray-400">
          {{ block.props.content }}
        </p>
      </UCard>
    </UContainer>
  </section>
</template>

<script setup lang="ts">
import type { Block } from '~/stores/editor'

defineProps<{
  block: Block
}>()
</script>
