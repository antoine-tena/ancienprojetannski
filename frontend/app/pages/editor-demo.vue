<template>
  <div class="editor-demo-page">
    <BlockRenderer />
  </div>
</template>

<script setup lang="ts">
import { useEditorStore } from '~/stores/editor'
import { useAuth } from '~/composables/useAuth'

const editorStore = useEditorStore()
const { isSuperuser } = useAuth()

// Initialiser isAdmin en fonction de l'authentification
onMounted(() => {
  // Définir si l'utilisateur est admin
  // Pour la démo, on force isAdmin à true si isSuperuser n'est pas défini
  const isAdmin = isSuperuser.value !== undefined ? isSuperuser.value : true
  editorStore.setAdmin(isAdmin)
  
  console.log('Editor Demo - isAdmin:', isAdmin, 'isSuperuser:', isSuperuser.value)
  
  // Charger des blocs de démonstration si le store est vide
  if (editorStore.blocks.length === 0) {
    editorStore.setBlocks([
      {
        id: 'hero-1',
        type: 'hero',
        order: 0,
        props: {
          title: 'Bienvenue sur votre éditeur visuel',
          content: 'Créez des pages magnifiques avec le drag & drop et l\'édition en temps réel',
          backgroundColor: '#1f2937',
          textColor: '#ffffff',
          buttonText: 'Commencer',
          buttonUrl: '#'
        }
      },
      {
        id: 'text-1',
        type: 'text',
        order: 1,
        props: {
          title: 'Éditez en temps réel',
          content: 'Chaque modification que vous faites dans le panneau d\'édition se reflète instantanément sur la page. C\'est magique !',
          alignment: 'center'
        }
      },
      {
        id: 'image-1',
        type: 'image',
        order: 2,
        props: {
          imageUrl: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200',
          alt: 'Workspace'
        }
      },
      {
        id: 'cta-1',
        type: 'cta',
        order: 3,
        props: {
          title: 'Prêt à créer ?',
          content: 'Activez le mode édition pour commencer à personnaliser cette page',
          buttonText: 'Activer l\'édition',
          buttonUrl: '#',
          backgroundColor: '#3b82f6'
        }
      }
    ])
  }
})

definePageMeta({
  layout: 'default'
})
</script>

<style scoped>
.editor-demo-page {
  min-height: 100vh;
}
</style>
