<template>
  <section class="text-block py-12">
    <UContainer>
      <div :class="alignmentClass">
        <h2 v-if="block.props.title" class="text-3xl font-bold mb-4">
          {{ block.props.title }}
        </h2>
        <div class="prose dark:prose-invert max-w-none">
          <p>{{ block.props.content }}</p>
        </div>
      </div>
    </UContainer>
  </section>
</template>

<script setup lang="ts">
import type { Block } from '~/stores/editor'

const props = defineProps<{
  block: Block
}>()

const alignmentClass = computed(() => {
  const alignment = props.block.props.alignment || 'left'
  return {
    left: 'text-left',
    center: 'text-center',
    right: 'text-right'
  }[alignment]
})
</script>
