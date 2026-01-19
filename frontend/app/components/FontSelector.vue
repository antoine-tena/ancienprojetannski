<template>
  <div :style="{ position: 'relative' }" data-font-selector>
    <label v-if="label" :style="{
      display: 'block',
      marginBottom: '8px',
      fontWeight: 'bold',
      color: '#495057'
    }">
      {{ label }}
    </label>
    
    <div :style="{ position: 'relative' }">
      <input 
        v-model="searchQuery"
        type="text"
        :placeholder="placeholder"
        @focus="showDropdown = true"
        @input="filterFonts"
        :style="{
          width: '100%',
          padding: '10px',
          paddingRight: '35px',
          border: '1px solid #ced4da',
          borderRadius: '4px',
          fontSize: '16px'
        }"
      />
      <button
        type="button"
        @click="showDropdown = !showDropdown"
        :style="{
          position: 'absolute',
          right: '5px',
          top: '50%',
          transform: 'translateY(-50%)',
          background: 'transparent',
          border: 'none',
          cursor: 'pointer',
          fontSize: '18px',
          padding: '5px 10px'
        }"
      >
        {{ showDropdown ? '▲' : '▼' }}
      </button>
    </div>

    <div 
      v-if="showDropdown"
      :style="{
        position: 'absolute',
        top: '100%',
        left: 0,
        right: 0,
        maxHeight: '300px',
        overflowY: 'auto',
        background: 'white',
        border: '1px solid #ced4da',
        borderRadius: '4px',
        marginTop: '5px',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
        zIndex: 1000
      }"
    >
      <div
        v-for="font in filteredFonts"
        :key="font"
        @click="selectFont(font)"
        :style="{
          padding: '10px 15px',
          cursor: 'pointer',
          borderBottom: '1px solid #f0f0f0',
          fontFamily: font,
          background: modelValue === font ? '#e7f5ff' : 'white',
          transition: 'background 0.2s'
        }"
        @mouseover="(e) => e.currentTarget.style.background = '#f8f9fa'"
        @mouseleave="(e) => e.currentTarget.style.background = modelValue === font ? '#e7f5ff' : 'white'"
      >
        {{ font }}
      </div>
      <div 
        v-if="filteredFonts.length === 0"
        :style="{
          padding: '20px',
          textAlign: 'center',
          color: '#6c757d',
          fontStyle: 'italic'
        }"
      >
        Aucune police trouvée
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: 'Rechercher une police...'
  }
})

const emit = defineEmits(['update:modelValue'])

const showDropdown = ref(false)
const searchQuery = ref(props.modelValue || '')
const filteredFonts = ref([])

const fonts = [
  'Arial, sans-serif',
  'Arial Black, sans-serif',
  'Courier New, monospace',
  'Georgia, serif',
  'Helvetica, sans-serif',
  'Impact, sans-serif',
  'Lucida Console, monospace',
  'Lucida Sans Unicode, sans-serif',
  'Palatino Linotype, serif',
  'Tahoma, sans-serif',
  'Times New Roman, serif',
  'Trebuchet MS, sans-serif',
  'Verdana, sans-serif',
  'Comic Sans MS, cursive',
  'Brush Script MT, cursive'
].sort()

const filterFonts = () => {
  const query = searchQuery.value.toLowerCase()
  if (query === '') {
    filteredFonts.value = fonts
  } else {
    filteredFonts.value = fonts.filter(font => 
      font.toLowerCase().includes(query)
    )
  }
}

const selectFont = (font) => {
  searchQuery.value = font
  emit('update:modelValue', font)
  showDropdown.value = false
}

// Initialiser avec toutes les polices
filteredFonts.value = fonts

// Gérer le clic en dehors pour fermer le dropdown
onMounted(() => {
  const handleClickOutside = (e) => {
    if (!e.target.closest('[data-font-selector]')) {
      showDropdown.value = false
    }
  }
  document.addEventListener('click', handleClickOutside)
  onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside)
  })
})

watch(() => props.modelValue, (newValue) => {
  searchQuery.value = newValue || ''
})
</script>
