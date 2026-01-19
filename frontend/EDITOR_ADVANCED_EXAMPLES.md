# 🎯 Exemples d'usage avancés - Éditeur Visuel

## 📚 Table des matières
1. [Intégration dans une page existante](#intégration-page)
2. [Créer un nouveau type de bloc](#nouveau-bloc)
3. [Sauvegarder dans une API](#api-sauvegarde)
4. [Charger depuis une API](#api-chargement)
5. [Personnaliser le panneau d'édition](#panneau-custom)
6. [Ajouter des validations](#validations)
7. [Système d'historique (Undo/Redo)](#historique)
8. [Mode preview/live](#mode-preview)

---

## <a name="intégration-page"></a>1. Intégration dans une page existante

### Option A : Page entière éditable
```vue
<!-- pages/about.vue -->
<template>
  <div>
    <BlockRenderer />
  </div>
</template>

<script setup lang="ts">
import { useEditorStore } from '~/stores/editor'

const editorStore = useEditorStore()

// Charger les blocs de cette page
onMounted(async () => {
  const data = await $fetch('/api/pages/about/blocks')
  editorStore.setBlocks(data.blocks)
})
</script>
```

### Option B : Section éditable dans une page fixe
```vue
<!-- pages/services.vue -->
<template>
  <div>
    <!-- En-tête fixe (non éditable) -->
    <header class="py-10 bg-gray-900 text-white">
      <h1>Nos Services</h1>
    </header>

    <!-- Section éditable -->
    <BlockRenderer />

    <!-- Footer fixe (non éditable) -->
    <footer class="py-6 bg-gray-800 text-white">
      © 2026 Mon Site
    </footer>
  </div>
</template>
```

---

## <a name="nouveau-bloc"></a>2. Créer un nouveau type de bloc

### Étape 1 : Créer le composant
```vue
<!-- components/blocks/TestimonialBlock.vue -->
<template>
  <section class="testimonial-block py-12">
    <UContainer>
      <div class="max-w-2xl mx-auto text-center">
        <div class="mb-4">
          <img
            :src="block.props.authorImage"
            :alt="block.props.authorName"
            class="w-20 h-20 rounded-full mx-auto"
          >
        </div>
        <blockquote class="text-xl italic mb-4">
          "{{ block.props.quote }}"
        </blockquote>
        <p class="font-semibold">{{ block.props.authorName }}</p>
        <p class="text-gray-600 text-sm">{{ block.props.authorRole }}</p>
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
```

### Étape 2 : Enregistrer dans BlockRenderer
```typescript
// Dans components/editor/BlockRenderer.vue

// Import
const TestimonialBlock = defineAsyncComponent(() => 
  import('~/components/blocks/TestimonialBlock.vue')
)

// Mapping
const blockComponents: Record<string, any> = {
  // ... existants
  testimonial: TestimonialBlock
}

// Options du select
const blockTypeOptions = [
  // ... existants
  { value: 'testimonial', label: 'Témoignage' }
]

// Props par défaut
const defaultProps: Record<string, any> = {
  // ... existants
  testimonial: {
    quote: 'Votre témoignage ici...',
    authorName: 'John Doe',
    authorRole: 'CEO, Company',
    authorImage: 'https://via.placeholder.com/100'
  }
}
```

### Étape 3 : Utiliser
```typescript
// Ajouter par programmation
editorStore.addBlock({
  id: `testimonial-${Date.now()}`,
  type: 'testimonial',
  props: {
    quote: 'Ce produit a changé ma vie !',
    authorName: 'Marie Dupont',
    authorRole: 'Utilisatrice satisfaite',
    authorImage: '/images/marie.jpg'
  }
})
```

---

## <a name="api-sauvegarde"></a>3. Sauvegarder dans une API

### Backend (Django exemple)
```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT'])
def save_page_blocks(request, page_id):
    blocks = request.data.get('blocks', [])
    
    # Sauvegarder en base de données
    page = Page.objects.get(id=page_id)
    page.blocks_json = json.dumps(blocks)
    page.save()
    
    return Response({'success': True})
```

### Frontend
```typescript
// composables/usePageEditor.ts
export const usePageEditor = () => {
  const editorStore = useEditorStore()
  
  const savePage = async (pageId: string) => {
    try {
      await $fetch(`/api/pages/${pageId}/blocks`, {
        method: 'PUT',
        body: {
          blocks: editorStore.blocks
        },
        credentials: 'include'
      })
      
      useToast().add({
        title: 'Sauvegardé',
        color: 'green'
      })
      
      return true
    } catch (error) {
      useToast().add({
        title: 'Erreur de sauvegarde',
        color: 'red'
      })
      return false
    }
  }
  
  return { savePage }
}
```

### Utilisation
```vue
<script setup>
import { usePageEditor } from '~/composables/usePageEditor'

const route = useRoute()
const { savePage } = usePageEditor()

const handleSave = async () => {
  await savePage(route.params.id)
}
</script>
```

---

## <a name="api-chargement"></a>4. Charger depuis une API

### Composable réutilisable
```typescript
// composables/usePageBlocks.ts
export const usePageBlocks = (pageId: string) => {
  const editorStore = useEditorStore()
  const loading = ref(true)
  const error = ref<Error | null>(null)
  
  const loadBlocks = async () => {
    try {
      loading.value = true
      const data = await $fetch(`/api/pages/${pageId}/blocks`, {
        credentials: 'include'
      })
      
      editorStore.setBlocks(data.blocks || [])
    } catch (err) {
      error.value = err as Error
      console.error('Erreur chargement:', err)
    } finally {
      loading.value = false
    }
  }
  
  // Charger automatiquement
  onMounted(loadBlocks)
  
  return {
    loading,
    error,
    reload: loadBlocks
  }
}
```

### Usage dans une page
```vue
<template>
  <div>
    <div v-if="loading" class="text-center py-10">
      <USpinner />
      <p>Chargement...</p>
    </div>
    
    <div v-else-if="error" class="text-red-600 p-4">
      Erreur : {{ error.message }}
    </div>
    
    <BlockRenderer v-else />
  </div>
</template>

<script setup>
const route = useRoute()
const { loading, error } = usePageBlocks(route.params.id)
</script>
```

---

## <a name="panneau-custom"></a>5. Personnaliser le panneau d'édition

### Ajouter un champ custom
```vue
<!-- Dans EditorPanel.vue, ajoutez avant "Champs personnalisés" -->

<!-- Animation -->
<div v-if="'animation' in selectedBlock.props">
  <label class="block text-sm font-medium mb-2">
    Animation
  </label>
  <USelect
    :model-value="selectedBlock.props.animation"
    :options="animationOptions"
    @update:model-value="updateField('animation', $event)"
  />
</div>

<script setup>
const animationOptions = [
  { value: 'none', label: 'Aucune' },
  { value: 'fade-in', label: 'Apparition en fondu' },
  { value: 'slide-up', label: 'Glissement vers le haut' },
  { value: 'zoom-in', label: 'Zoom avant' }
]
</script>
```

### Champ avec validation
```vue
<!-- URL avec validation -->
<div v-if="'buttonUrl' in selectedBlock.props">
  <label class="block text-sm font-medium mb-2">
    URL du bouton
  </label>
  <UInput
    :model-value="selectedBlock.props.buttonUrl"
    placeholder="https://..."
    :error="!isValidUrl(selectedBlock.props.buttonUrl)"
    @update:model-value="updateField('buttonUrl', $event)"
  />
  <p v-if="!isValidUrl(selectedBlock.props.buttonUrl)" 
     class="text-red-500 text-sm mt-1">
    URL invalide
  </p>
</div>

<script setup>
const isValidUrl = (url: string) => {
  if (!url) return true // Vide = OK
  try {
    new URL(url)
    return true
  } catch {
    return false
  }
}
</script>
```

---

## <a name="validations"></a>6. Ajouter des validations

### Dans le store
```typescript
// stores/editor.ts

// Ajouter une action de validation
validate(blockId: string): string[] {
  const block = this.blocks.find(b => b.id === blockId)
  if (!block) return []
  
  const errors: string[] = []
  
  // Validation du titre
  if (block.props.title && block.props.title.length < 3) {
    errors.push('Le titre doit contenir au moins 3 caractères')
  }
  
  // Validation de l'URL
  if (block.props.buttonUrl) {
    try {
      new URL(block.props.buttonUrl)
    } catch {
      errors.push('URL du bouton invalide')
    }
  }
  
  // Validation de l'image
  if (block.props.imageUrl && !block.props.imageUrl.match(/\.(jpg|jpeg|png|gif|webp)$/i)) {
    errors.push('Format d\'image non supporté')
  }
  
  return errors
}
```

### Dans le panneau
```vue
<script setup>
const validationErrors = computed(() => {
  if (!editorStore.selectedBlockId) return []
  return editorStore.validate(editorStore.selectedBlockId)
})
</script>

<template>
  <!-- Afficher les erreurs -->
  <div v-if="validationErrors.length > 0" 
       class="bg-red-50 border border-red-200 rounded p-3 mb-4">
    <p class="font-semibold text-red-800 mb-2">Erreurs de validation :</p>
    <ul class="list-disc list-inside text-red-700 text-sm">
      <li v-for="error in validationErrors" :key="error">
        {{ error }}
      </li>
    </ul>
  </div>
</template>
```

---

## <a name="historique"></a>7. Système d'historique (Undo/Redo)

### Extension du store
```typescript
// stores/editor.ts

interface EditorState {
  // ... existants
  history: Block[][]
  historyIndex: number
}

export const useEditorStore = defineStore('editor', {
  state: (): EditorState => ({
    // ... existants
    history: [],
    historyIndex: -1
  }),
  
  actions: {
    // Sauvegarder l'état actuel
    saveToHistory() {
      // Supprimer le futur si on a fait undo
      this.history = this.history.slice(0, this.historyIndex + 1)
      
      // Ajouter l'état actuel
      this.history.push(JSON.parse(JSON.stringify(this.blocks)))
      this.historyIndex++
      
      // Limiter à 50 états
      if (this.history.length > 50) {
        this.history.shift()
        this.historyIndex--
      }
    },
    
    undo() {
      if (this.historyIndex > 0) {
        this.historyIndex--
        this.blocks = JSON.parse(JSON.stringify(this.history[this.historyIndex]))
      }
    },
    
    redo() {
      if (this.historyIndex < this.history.length - 1) {
        this.historyIndex++
        this.blocks = JSON.parse(JSON.stringify(this.history[this.historyIndex]))
      }
    },
    
    // Modifier updateBlockField pour sauvegarder
    updateBlockField(blockId: string, field: string, value: any) {
      // ... code existant
      
      // Sauvegarder dans l'historique après 1 seconde d'inactivité
      clearTimeout(this._historyTimeout)
      this._historyTimeout = setTimeout(() => {
        this.saveToHistory()
      }, 1000)
    }
  },
  
  getters: {
    canUndo: (state) => state.historyIndex > 0,
    canRedo: (state) => state.historyIndex < state.history.length - 1
  }
})
```

### UI dans BlockRenderer
```vue
<template>
  <div class="editor-topbar">
    <UContainer>
      <div class="flex items-center gap-3">
        <!-- ... existants -->
        
        <!-- Undo/Redo -->
        <UButton
          icon="lucide:undo"
          :disabled="!editorStore.canUndo"
          @click="editorStore.undo()"
        >
          Annuler
        </UButton>
        <UButton
          icon="lucide:redo"
          :disabled="!editorStore.canRedo"
          @click="editorStore.redo()"
        >
          Refaire
        </UButton>
      </div>
    </UContainer>
  </div>
</template>
```

---

## <a name="mode-preview"></a>8. Mode preview/live

### Switch de mode
```vue
<!-- Dans BlockRenderer.vue -->
<template>
  <div class="editor-topbar">
    <div class="flex items-center gap-3">
      <!-- Mode selector -->
      <USelect
        v-model="viewMode"
        :options="[
          { value: 'edit', label: 'Édition' },
          { value: 'preview', label: 'Aperçu' },
          { value: 'mobile', label: 'Mobile' }
        ]"
      />
    </div>
  </div>
  
  <!-- Wrapper avec classe conditionnelle -->
  <div :class="viewModeClass">
    <draggable v-model="draggableBlocks" ...>
      <!-- ... -->
    </draggable>
  </div>
</template>

<script setup>
const viewMode = ref('edit')

const viewModeClass = computed(() => {
  return {
    'editor-view-edit': viewMode.value === 'edit',
    'editor-view-preview': viewMode.value === 'preview',
    'editor-view-mobile': viewMode.value === 'mobile'
  }
})

// Désactiver l'édition en mode preview
watch(viewMode, (mode) => {
  if (mode === 'preview' || mode === 'mobile') {
    editorStore.isEditing = false
  }
})
</script>

<style>
.editor-view-mobile {
  max-width: 375px;
  margin: 0 auto;
  border: 1px solid #ccc;
  box-shadow: 0 0 20px rgba(0,0,0,0.1);
}
</style>
```

---

## 🎓 Exemples complets

### Page de produit éditable
```vue
<!-- pages/products/[id].vue -->
<template>
  <div>
    <BlockRenderer />
  </div>
</template>

<script setup lang="ts">
import { useEditorStore } from '~/stores/editor'
import { usePageEditor } from '~/composables/usePageEditor'

const route = useRoute()
const editorStore = useEditorStore()
const { savePage } = usePageEditor()

// Charger les blocs du produit
onMounted(async () => {
  const data = await $fetch(`/api/products/${route.params.id}/blocks`)
  
  if (data.blocks && data.blocks.length > 0) {
    editorStore.setBlocks(data.blocks)
  } else {
    // Template par défaut pour un nouveau produit
    editorStore.setBlocks([
      {
        id: 'hero-1',
        type: 'hero',
        order: 0,
        props: {
          title: 'Nouveau Produit',
          content: 'Description du produit...',
          buttonText: 'Acheter maintenant'
        }
      },
      {
        id: 'text-1',
        type: 'text',
        order: 1,
        props: {
          title: 'Caractéristiques',
          content: 'Liste des caractéristiques...'
        }
      }
    ])
  }
})

// Auto-save toutes les 30 secondes
const autoSaveInterval = ref<NodeJS.Timer | null>(null)

onMounted(() => {
  autoSaveInterval.value = setInterval(async () => {
    if (editorStore.isEditing) {
      await savePage(route.params.id as string)
    }
  }, 30000)
})

onUnmounted(() => {
  if (autoSaveInterval.value) {
    clearInterval(autoSaveInterval.value)
  }
})
</script>
```

---

**Prêt pour des cas d'usage avancés ! 🚀**
