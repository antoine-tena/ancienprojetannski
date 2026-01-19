<template>
  <USlideover
    v-model="isOpen"
    :ui="{
      width: 'max-w-md'
    }"
  >
    <UCard
      class="flex flex-col flex-1"
      :ui="{
        body: { base: 'flex-1 overflow-y-auto' },
        ring: '',
        divide: 'divide-y divide-gray-100 dark:divide-gray-800'
      }"
    >
      <!-- Header -->
      <template #header>
        <div class="flex items-center justify-between">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
            Éditer le bloc
          </h3>
          <UButton
            color="gray"
            variant="ghost"
            icon="lucide:x"
            @click="closePanel"
          />
        </div>
      </template>

      <!-- Body - Formulaire d'édition -->
      <div v-if="selectedBlock" class="space-y-6 p-4">
        <!-- Type du bloc (read-only) -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Type de bloc
          </label>
          <UBadge :label="selectedBlock.type" size="lg" />
        </div>

        <!-- Titre -->
        <div v-if="'title' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Titre
          </label>
          <UInput
            :model-value="selectedBlock.props.title"
            placeholder="Entrez le titre..."
            @update:model-value="updateField('title', $event)"
          />
        </div>

        <!-- Contenu / Texte -->
        <div v-if="'content' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Contenu
          </label>
          <UTextarea
            :model-value="selectedBlock.props.content"
            placeholder="Entrez le contenu..."
            :rows="5"
            @update:model-value="updateField('content', $event)"
          />
        </div>

        <!-- Couleur de fond -->
        <div v-if="'backgroundColor' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Couleur de fond
          </label>
          <div class="flex gap-2 items-center">
            <input
              type="color"
              :value="selectedBlock.props.backgroundColor"
              class="h-10 w-20 rounded border border-gray-300 cursor-pointer"
              @input="updateField('backgroundColor', ($event.target as HTMLInputElement).value)"
            >
            <UInput
              :model-value="selectedBlock.props.backgroundColor"
              placeholder="#000000"
              class="flex-1"
              @update:model-value="updateField('backgroundColor', $event)"
            />
          </div>
        </div>

        <!-- Couleur du texte -->
        <div v-if="'textColor' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Couleur du texte
          </label>
          <div class="flex gap-2 items-center">
            <input
              type="color"
              :value="selectedBlock.props.textColor"
              class="h-10 w-20 rounded border border-gray-300 cursor-pointer"
              @input="updateField('textColor', ($event.target as HTMLInputElement).value)"
            >
            <UInput
              :model-value="selectedBlock.props.textColor"
              placeholder="#FFFFFF"
              class="flex-1"
              @update:model-value="updateField('textColor', $event)"
            />
          </div>
        </div>

        <!-- Texte du bouton -->
        <div v-if="'buttonText' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Texte du bouton
          </label>
          <UInput
            :model-value="selectedBlock.props.buttonText"
            placeholder="Ex: En savoir plus"
            @update:model-value="updateField('buttonText', $event)"
          />
        </div>

        <!-- URL du bouton -->
        <div v-if="'buttonUrl' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            URL du bouton
          </label>
          <UInput
            :model-value="selectedBlock.props.buttonUrl"
            placeholder="https://..."
            @update:model-value="updateField('buttonUrl', $event)"
          />
        </div>

        <!-- Image URL -->
        <div v-if="'imageUrl' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            URL de l'image
          </label>
          <UInput
            :model-value="selectedBlock.props.imageUrl"
            placeholder="https://..."
            @update:model-value="updateField('imageUrl', $event)"
          />
          <div v-if="selectedBlock.props.imageUrl" class="mt-3">
            <img
              :src="selectedBlock.props.imageUrl"
              alt="Aperçu"
              class="w-full h-40 object-cover rounded-lg border border-gray-200"
            >
          </div>
        </div>

        <!-- Alignement -->
        <div v-if="'alignment' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Alignement
          </label>
          <USelect
            :model-value="selectedBlock.props.alignment"
            :options="alignmentOptions"
            @update:model-value="updateField('alignment', $event)"
          />
        </div>

        <!-- Taille -->
        <div v-if="'size' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Taille
          </label>
          <USelect
            :model-value="selectedBlock.props.size"
            :options="sizeOptions"
            @update:model-value="updateField('size', $event)"
          />
        </div>

        <!-- Espacement (padding) -->
        <div v-if="'padding' in selectedBlock.props">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Espacement intérieur (px)
          </label>
          <UInput
            :model-value="selectedBlock.props.padding"
            type="number"
            min="0"
            max="200"
            @update:model-value="updateField('padding', $event)"
          />
        </div>

        <!-- Champs personnalisés additionnels -->
        <div v-for="(value, key) in customFields" :key="key">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            {{ formatFieldName(key) }}
          </label>
          <UInput
            :model-value="value"
            @update:model-value="updateField(key, $event)"
          />
        </div>
      </div>

      <!-- Footer - Actions -->
      <template #footer>
        <div class="flex justify-between gap-3">
          <UButton
            color="red"
            variant="soft"
            icon="lucide:trash-2"
            @click="deleteBlock"
          >
            Supprimer
          </UButton>
          <div class="flex gap-2">
            <UButton
              color="gray"
              variant="soft"
              @click="closePanel"
            >
              Fermer
            </UButton>
            <UButton
              color="primary"
              icon="lucide:save"
              @click="saveChanges"
            >
              Sauvegarder
            </UButton>
          </div>
        </div>
      </template>
    </UCard>
  </USlideover>
</template>

<script setup lang="ts">
import { useEditorStore } from '~/stores/editor'

const editorStore = useEditorStore()

const isOpen = computed({
  get: () => editorStore.selectedBlockId !== null,
  set: (value) => {
    if (!value) {
      editorStore.selectBlock(null)
    }
  }
})

const selectedBlock = computed(() => editorStore.selectedBlock)

// Options pour les selects
const alignmentOptions = [
  { value: 'left', label: 'Gauche' },
  { value: 'center', label: 'Centré' },
  { value: 'right', label: 'Droite' }
]

const sizeOptions = [
  { value: 'sm', label: 'Petit' },
  { value: 'md', label: 'Moyen' },
  { value: 'lg', label: 'Grand' },
  { value: 'xl', label: 'Très grand' }
]

// Champs personnalisés (ceux qui ne sont pas dans les champs standards)
const customFields = computed(() => {
  if (!selectedBlock.value) return {}
  
  const standardFields = [
    'title', 'content', 'backgroundColor', 'textColor',
    'buttonText', 'buttonUrl', 'imageUrl', 'alignment',
    'size', 'padding'
  ]
  
  const custom: Record<string, any> = {}
  for (const [key, value] of Object.entries(selectedBlock.value.props)) {
    if (!standardFields.includes(key)) {
      custom[key] = value
    }
  }
  return custom
})

// Mise à jour d'un champ (réactivité immédiate)
const updateField = (field: string, value: any) => {
  if (editorStore.selectedBlockId) {
    editorStore.updateBlockField(editorStore.selectedBlockId, `props.${field}`, value)
  }
}

// Formater le nom d'un champ personnalisé
const formatFieldName = (key: string): string => {
  return key
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, str => str.toUpperCase())
}

// Fermer le panneau
const closePanel = () => {
  editorStore.selectBlock(null)
}

// Supprimer le bloc
const deleteBlock = () => {
  if (selectedBlock.value && confirm('Êtes-vous sûr de vouloir supprimer ce bloc ?')) {
    editorStore.removeBlock(selectedBlock.value.id)
    closePanel()
  }
}

// Sauvegarder les modifications (appel API si nécessaire)
const saveChanges = async () => {
  // TODO: Appeler l'API pour sauvegarder les modifications
  console.log('Sauvegarde des modifications:', selectedBlock.value)
  
  // Afficher une notification
  useToast().add({
    title: 'Modifications sauvegardées',
    description: 'Le bloc a été mis à jour avec succès',
    color: 'green'
  })
  
  closePanel()
}
</script>

<style scoped>
/* Styles additionnels si nécessaire */
</style>
