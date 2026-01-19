<template>
  <div
    :class="[
      'editor-wrapper',
      {
        'editor-wrapper--editing': editorStore.isEditing,
        'editor-wrapper--selected': isSelected
      }
    ]"
    @click.stop="handleBlockClick"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
  >
    <!-- Drag Handle (visible uniquement en mode édition) -->
    <div
      v-if="editorStore.isEditing"
      class="editor-drag-handle"
      :class="{ 'editor-drag-handle--visible': showControls }"
    >
      <Icon name="lucide:move" class="w-4 h-4" />
    </div>

    <!-- Edit Button (visible au clic) -->
    <button
      v-if="editorStore.isEditing && showEditButton"
      class="editor-edit-button"
      @click.stop="handleEditClick"
    >
      <Icon name="lucide:pencil" class="w-4 h-4" />
    </button>

    <!-- Delete Button -->
    <button
      v-if="editorStore.isEditing && showEditButton"
      class="editor-delete-button"
      @click.stop="handleDeleteClick"
    >
      <Icon name="lucide:trash-2" class="w-4 h-4" />
    </button>

    <!-- Duplicate Button -->
    <button
      v-if="editorStore.isEditing && showEditButton"
      class="editor-duplicate-button"
      @click.stop="handleDuplicateClick"
    >
      <Icon name="lucide:copy" class="w-4 h-4" />
    </button>

    <!-- Block Content (Slot par défaut) -->
    <div class="editor-content">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useEditorStore } from '~/stores/editor'

const props = defineProps<{
  blockId: string
}>()

const editorStore = useEditorStore()
const showControls = ref(false)
const showEditButton = ref(false)

const isSelected = computed(() => editorStore.selectedBlockId === props.blockId)

const handleMouseEnter = () => {
  if (editorStore.isEditing) {
    showControls.value = true
  }
}

const handleMouseLeave = () => {
  if (editorStore.isEditing && !isSelected.value) {
    showControls.value = false
  }
}

const handleBlockClick = () => {
  if (editorStore.isEditing) {
    showEditButton.value = true
  }
}

const handleEditClick = () => {
  editorStore.selectBlock(props.blockId)
}

const handleDeleteClick = () => {
  if (confirm('Êtes-vous sûr de vouloir supprimer ce bloc ?')) {
    editorStore.removeBlock(props.blockId)
  }
}

const handleDuplicateClick = () => {
  editorStore.duplicateBlock(props.blockId)
}

// Reset edit button when deselecting
watch(isSelected, (newVal) => {
  if (!newVal) {
    showEditButton.value = false
  }
})

// Close edit button when exiting edit mode
watch(() => editorStore.isEditing, (newVal) => {
  if (!newVal) {
    showEditButton.value = false
    showControls.value = false
  }
})
</script>

<style scoped>
.editor-wrapper {
  position: relative;
  transition: all 0.2s ease;
}

.editor-wrapper--editing {
  cursor: pointer;
}

.editor-wrapper--editing:hover {
  outline: 2px dashed #3b82f6;
  outline-offset: 4px;
}

.editor-wrapper--selected {
  outline: 2px solid #3b82f6 !important;
  outline-offset: 4px;
}

.editor-drag-handle {
  position: absolute;
  top: 8px;
  left: 8px;
  z-index: 100;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  padding: 8px;
  cursor: move;
  opacity: 0;
  transition: opacity 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.editor-drag-handle--visible {
  opacity: 1;
}

.editor-drag-handle:hover {
  background: #f3f4f6;
  border-color: #3b82f6;
}

.editor-edit-button {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 100;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
}

.editor-edit-button:hover {
  background: #2563eb;
  transform: scale(1.05);
}

.editor-delete-button {
  position: absolute;
  top: 8px;
  right: 52px;
  z-index: 100;
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
}

.editor-delete-button:hover {
  background: #dc2626;
  transform: scale(1.05);
}

.editor-duplicate-button {
  position: absolute;
  top: 8px;
  right: 96px;
  z-index: 100;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

.editor-duplicate-button:hover {
  background: #059669;
  transform: scale(1.05);
}

.editor-content {
  position: relative;
  z-index: 1;
}
</style>
