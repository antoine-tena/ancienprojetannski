<template>
  <div :style="{
    border: '1px solid #dee2e6',
    borderRadius: '4px',
    overflow: 'hidden'
  }">
    <button
      @click="isOpen = !isOpen"
      :style="{
        width: '100%',
        padding: '15px 20px',
        background: isOpen ? '#e7f5ff' : '#f8f9fa',
        border: 'none',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        cursor: 'pointer',
        fontSize: '16px',
        fontWeight: 'bold',
        color: '#212529',
        transition: 'background 0.2s'
      }"
    >
      <span v-if="!$slots.title">{{ title }}</span>
      <slot v-else name="title"></slot>
      <span :style="{
        transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)',
        transition: 'transform 0.2s'
      }">
        ▼
      </span>
    </button>
    
    <div
      v-show="isOpen"
      :style="{
        padding: '20px',
        background: 'white',
        borderTop: '1px solid #dee2e6'
      }"
    >
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: false,
    default: ''
  },
  defaultOpen: {
    type: Boolean,
    default: false
  }
})

const isOpen = ref(props.defaultOpen)
</script>
