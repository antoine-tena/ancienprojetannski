<template>
  <div class="block-renderer">
    <!-- TopBar d'édition (visible uniquement pour les admins) -->
    <div v-if="editorStore.isAdmin" class="editor-topbar">
      <UContainer>
        <div class="flex items-center justify-between py-4">
          <div class="flex items-center gap-4">
            <h2 class="text-lg font-semibold text-gray-900 dark:text-white">
              Éditeur de page
            </h2>
            <UBadge
              :color="editorStore.isEditing ? 'green' : 'gray'"
              size="lg"
            >
              {{ editorStore.isEditing ? 'Mode édition activé' : 'Mode lecture' }}
            </UBadge>
          </div>

          <div class="flex items-center gap-3">
            <!-- Toggle édition -->
            <UToggle
              :model-value="editorStore.isEditing"
              @update:model-value="editorStore.toggleEditing()"
            >
              <template #label>
                <span class="text-sm font-medium">
                  {{ editorStore.isEditing ? 'Désactiver' : 'Activer' }} l'édition
                </span>
              </template>
            </UToggle>

            <!-- Bouton ajouter un bloc -->
            <UButton
              v-if="editorStore.isEditing"
              color="primary"
              icon="lucide:plus"
              @click="showAddBlockModal = true"
            >
              Ajouter un bloc
            </UButton>

            <!-- Bouton sauvegarder tout -->
            <UButton
              v-if="editorStore.isEditing"
              color="green"
              icon="lucide:save"
              @click="saveAllBlocks"
            >
              Tout sauvegarder
            </UButton>
          </div>
        </div>
      </UContainer>
    </div>

    <!-- Liste des blocs avec Drag & Drop -->
    <draggable
      v-model="draggableBlocks"
      :disabled="!editorStore.isEditing"
      item-key="id"
      class="blocks-container"
      handle=".editor-drag-handle"
      @end="onDragEnd"
    >
      <template #item="{ element: block }">
        <EditorWrapper :block-id="block.id">
          <!-- Rendu du bloc en fonction de son type -->
          <component
            :is="getBlockComponent(block.type)"
            v-bind="block.props"
            :block="block"
          />
        </EditorWrapper>
      </template>
    </draggable>

    <!-- Panneau d'édition latéral -->
    <EditorPanel />

    <!-- Modal d'ajout de bloc -->
    <UModal v-model="showAddBlockModal">
      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Ajouter un nouveau bloc</h3>
        </template>

        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-2">Type de bloc</label>
            <USelect
              v-model="newBlockType"
              :options="blockTypeOptions"
              placeholder="Choisir un type..."
            />
          </div>
        </div>

        <template #footer>
          <div class="flex justify-end gap-2">
            <UButton
              color="gray"
              variant="soft"
              @click="showAddBlockModal = false"
            >
              Annuler
            </UButton>
            <UButton
              color="primary"
              :disabled="!newBlockType"
              @click="addNewBlock"
            >
              Ajouter
            </UButton>
          </div>
        </template>
      </UCard>
    </UModal>
  </div>
</template>

<script setup lang="ts">
import { VueDraggableNext as draggable } from 'vuedraggable'
import { useEditorStore, type Block } from '~/stores/editor'

// Import dynamique des composants de blocs
const HeroBlock = defineAsyncComponent(() => import('~/components/blocks/HeroBlock.vue'))
const TextBlock = defineAsyncComponent(() => import('~/components/blocks/TextBlock.vue'))
const ImageBlock = defineAsyncComponent(() => import('~/components/blocks/ImageBlock.vue'))
const CtaBlock = defineAsyncComponent(() => import('~/components/blocks/CtaBlock.vue'))
const CardBlock = defineAsyncComponent(() => import('~/components/blocks/CardBlock.vue'))

const editorStore = useEditorStore()
const { isSuperuser } = useAuth()

// Initialiser le mode admin
onMounted(() => {
  editorStore.setAdmin(isSuperuser.value)
})

// Gestion du drag & drop
const draggableBlocks = computed({
  get: () => editorStore.sortedBlocks,
  set: (value: Block[]) => {
    editorStore.reorderBlocks(value)
  }
})

const onDragEnd = () => {
  console.log('Ordre des blocs mis à jour:', draggableBlocks.value)
  // TODO: Sauvegarder l'ordre dans l'API
}

// Mapping des types de blocs vers leurs composants
const blockComponents: Record<string, any> = {
  hero: HeroBlock,
  text: TextBlock,
  image: ImageBlock,
  cta: CtaBlock,
  card: CardBlock
}

const getBlockComponent = (type: string) => {
  return blockComponents[type] || TextBlock
}

// Ajout de bloc
const showAddBlockModal = ref(false)
const newBlockType = ref('')

const blockTypeOptions = [
  { value: 'hero', label: 'Hero / Bannière' },
  { value: 'text', label: 'Texte' },
  { value: 'image', label: 'Image' },
  { value: 'cta', label: 'Call-to-Action' },
  { value: 'card', label: 'Carte' }
]

const addNewBlock = () => {
  if (!newBlockType.value) return

  const defaultProps: Record<string, any> = {
    hero: {
      title: 'Nouveau Hero',
      content: 'Votre contenu ici...',
      backgroundColor: '#1f2937',
      textColor: '#ffffff',
      buttonText: 'En savoir plus',
      buttonUrl: '#'
    },
    text: {
      title: 'Nouveau titre',
      content: 'Votre texte ici...',
      alignment: 'left'
    },
    image: {
      imageUrl: 'https://via.placeholder.com/800x400',
      alt: 'Description de l\'image'
    },
    cta: {
      title: 'Prêt à commencer ?',
      content: 'Rejoignez-nous dès maintenant',
      buttonText: 'S\'inscrire',
      buttonUrl: '#',
      backgroundColor: '#3b82f6'
    },
    card: {
      title: 'Titre de la carte',
      content: 'Description de la carte',
      imageUrl: 'https://via.placeholder.com/400x300'
    }
  }

  const newBlock: Omit<Block, 'order'> = {
    id: `${newBlockType.value}-${Date.now()}`,
    type: newBlockType.value,
    props: defaultProps[newBlockType.value] || {}
  }

  editorStore.addBlock(newBlock)
  showAddBlockModal.value = false
  newBlockType.value = ''

  useToast().add({
    title: 'Bloc ajouté',
    description: 'Le nouveau bloc a été ajouté avec succès',
    color: 'green'
  })
}

// Sauvegarde de tous les blocs
const saveAllBlocks = async () => {
  try {
    // TODO: Implémenter l'appel API pour sauvegarder tous les blocs
    console.log('Sauvegarde de tous les blocs:', editorStore.blocks)
    
    useToast().add({
      title: 'Sauvegardé',
      description: 'Tous les blocs ont été sauvegardés avec succès',
      color: 'green'
    })
  } catch (error) {
    useToast().add({
      title: 'Erreur',
      description: 'Une erreur est survenue lors de la sauvegarde',
      color: 'red'
    })
  }
}
</script>

<style scoped>
.editor-topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: white;
  border-bottom: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.blocks-container {
  min-height: 400px;
}

/* Animation pour le drag & drop */
.blocks-container :deep(.sortable-ghost) {
  opacity: 0.4;
  background: #f3f4f6;
}

.blocks-container :deep(.sortable-drag) {
  opacity: 0.8;
}
</style>
