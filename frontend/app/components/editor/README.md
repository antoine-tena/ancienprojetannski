# 🎨 Système d'Édition Visuelle In-Situ

## 📋 Vue d'ensemble

Ce système d'édition visuelle permet aux administrateurs de modifier le contenu des pages en temps réel avec une interface de type "Wix-like". Il inclut :

- ✨ **Édition en temps réel** : Les modifications sont visibles instantanément
- 🎯 **Drag & Drop** : Réorganisez les blocs par glisser-déposer
- 🎨 **Interface intuitive** : Panneau latéral avec tous les contrôles
- 🔒 **Sécurisé** : Accessible uniquement aux superusers

## 🚀 Installation

Les dépendances ont été ajoutées automatiquement :

```bash
cd frontend
pnpm install
```

## 📁 Architecture

```
app/
├── stores/
│   └── editor.ts                 # Store Pinia pour l'état de l'éditeur
├── components/
│   ├── editor/
│   │   ├── EditorWrapper.vue     # Wrapper pour chaque bloc (drag handle, edit button)
│   │   ├── EditorPanel.vue       # Panneau latéral d'édition
│   │   └── BlockRenderer.vue     # Rendu des blocs avec drag & drop
│   └── blocks/
│       ├── HeroBlock.vue         # Bloc Hero/Bannière
│       ├── TextBlock.vue         # Bloc de texte
│       ├── ImageBlock.vue        # Bloc image
│       ├── CtaBlock.vue          # Bloc Call-to-Action
│       └── CardBlock.vue         # Bloc carte
└── pages/
    └── editor-demo.vue           # Page de démonstration
```

## 🎯 Utilisation

### 1. Accéder à la page de démonstration

```
http://localhost:3000/editor-demo
```

### 2. Activer le mode édition

Si vous êtes connecté en tant que **superuser**, vous verrez une **TopBar** en haut de la page avec un toggle "Activer l'édition".

### 3. Éditer un bloc

1. Activez le mode édition
2. Survolez un bloc → Une bordure pointillée apparaît
3. Cliquez sur le bloc → Les boutons d'action apparaissent :
   - **Crayon** (bleu) : Ouvrir le panneau d'édition
   - **Copier** (vert) : Dupliquer le bloc
   - **Corbeille** (rouge) : Supprimer le bloc
4. Modifiez les champs dans le panneau latéral
5. **Les changements sont visibles en temps réel !**

### 4. Réorganiser les blocs

1. Activez le mode édition
2. Cliquez sur la **poignée de déplacement** (icône move)
3. Glissez-déposez le bloc à la position souhaitée
4. L'ordre est mis à jour automatiquement

### 5. Ajouter un nouveau bloc

1. Cliquez sur **"Ajouter un bloc"** dans la TopBar
2. Choisissez le type de bloc (Hero, Text, Image, CTA, Card)
3. Le bloc est ajouté en bas de la page
4. Éditez-le immédiatement

## 🛠️ API du Store Pinia

### State

```typescript
{
  isEditing: boolean           // Mode édition activé/désactivé
  isAdmin: boolean            // L'utilisateur est-il admin ?
  blocks: Block[]             // Liste des blocs de la page
  selectedBlockId: string     // ID du bloc en cours d'édition
}
```

### Actions principales

```typescript
// Activer/désactiver l'édition
editorStore.toggleEditing()

// Mettre à jour un champ d'un bloc (réactivité immédiate)
editorStore.updateBlockField(blockId, 'props.title', 'Nouveau titre')

// Réorganiser les blocs
editorStore.reorderBlocks(newOrderArray)

// Ajouter un bloc
editorStore.addBlock({
  id: 'unique-id',
  type: 'hero',
  props: { title: '...' }
})

// Supprimer un bloc
editorStore.removeBlock(blockId)
```

## 🎨 Créer un nouveau type de bloc

1. Créez un composant dans `components/blocks/`

```vue
<!-- components/blocks/MyCustomBlock.vue -->
<template>
  <section class="my-custom-block">
    <UContainer>
      <h2>{{ block.props.customTitle }}</h2>
      <!-- Votre contenu -->
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

2. Enregistrez-le dans `BlockRenderer.vue`

```typescript
const MyCustomBlock = defineAsyncComponent(() => import('~/components/blocks/MyCustomBlock.vue'))

const blockComponents: Record<string, any> = {
  // ... existants
  'my-custom': MyCustomBlock
}

const blockTypeOptions = [
  // ... existants
  { value: 'my-custom', label: 'Mon Bloc Personnalisé' }
]
```

3. Ajoutez les props par défaut

```typescript
const defaultProps: Record<string, any> = {
  // ... existants
  'my-custom': {
    customTitle: 'Mon titre',
    customContent: 'Mon contenu'
  }
}
```

## 🔧 Personnalisation

### Modifier les champs du panneau d'édition

Le composant `EditorPanel.vue` détecte automatiquement les champs standards :
- `title` → Input texte
- `content` → Textarea
- `backgroundColor` → Color picker
- `textColor` → Color picker
- `buttonText` → Input texte
- `buttonUrl` → Input URL
- `imageUrl` → Input URL avec aperçu
- `alignment` → Select
- `size` → Select

Les autres champs sont affichés automatiquement comme des inputs texte.

### Ajouter un champ personnalisé

Il suffit de l'ajouter dans les `props` du bloc et il apparaîtra automatiquement dans le panneau d'édition !

## 💾 Sauvegarde des données

Actuellement, les modifications sont stockées dans le store Pinia (en mémoire). Pour persister les données :

1. **API Backend** : Ajoutez des endpoints pour sauvegarder les blocs
2. **Dans `BlockRenderer.vue`**, implémentez `saveAllBlocks()` :

```typescript
const saveAllBlocks = async () => {
  await $fetch('http://localhost:8000/api/pages/1/blocks/', {
    method: 'PUT',
    body: { blocks: editorStore.blocks },
    credentials: 'include'
  })
}
```

3. **Chargement initial** : Dans la page, chargez les blocs depuis l'API :

```typescript
onMounted(async () => {
  const data = await $fetch('http://localhost:8000/api/pages/1/blocks/')
  editorStore.setBlocks(data.blocks)
})
```

## 🎯 Fonctionnalités clés

### Réactivité en temps réel ✨

Grâce à Pinia et Vue 3, chaque modification dans le panneau d'édition met à jour instantanément le bloc visible sur la page. Pas besoin de "prévisualiser" ou "rafraîchir" !

```typescript
// Dans EditorPanel.vue
const updateField = (field: string, value: any) => {
  // Cette ligne met à jour le store ET déclenche la réactivité
  editorStore.updateBlockField(
    editorStore.selectedBlockId,
    `props.${field}`,
    value
  )
}
```

### Drag & Drop avec vuedraggable 🎯

```vue
<draggable
  v-model="draggableBlocks"
  :disabled="!editorStore.isEditing"
  item-key="id"
  handle=".editor-drag-handle"
  @end="onDragEnd"
>
```

- **Handle** : Seule la poignée permet de déplacer
- **Disabled** : Le drag & drop est désactivé en mode lecture
- **@end** : Callback quand le déplacement est terminé

## 🔒 Sécurité

- L'édition est disponible uniquement pour les **superusers**
- Le composant vérifie `isSuperuser` du composable `useAuth`
- Les sauvegardes doivent être protégées côté backend

## 🐛 Debug

Pour voir l'état actuel du store :

```javascript
// Dans la console du navigateur
const { useEditorStore } = await import('/app/stores/editor')
const store = useEditorStore()
console.log(store.blocks)
```

## 📚 Technologies utilisées

- **Nuxt 4** : Framework Vue.js
- **Nuxt UI** : Composants UI (USlideover, UInput, UButton, etc.)
- **Pinia** : State management
- **vuedraggable** : Drag & drop
- **Tailwind CSS** : Styling

## 🎓 Exemples d'utilisation

### Charger des blocs depuis une API

```typescript
// pages/my-page.vue
const route = useRoute()
const editorStore = useEditorStore()

onMounted(async () => {
  const pageId = route.params.id
  const data = await $fetch(`/api/pages/${pageId}/blocks`)
  editorStore.setBlocks(data)
})
```

### Ajouter un bloc par programmation

```typescript
editorStore.addBlock({
  id: `text-${Date.now()}`,
  type: 'text',
  props: {
    title: 'Titre dynamique',
    content: 'Contenu généré'
  }
})
```

## 🚀 Prochaines étapes

- [ ] Ajouter un système d'historique (Undo/Redo)
- [ ] Implémenter la sauvegarde automatique
- [ ] Ajouter plus de types de blocs (Galerie, Video, FAQ, etc.)
- [ ] Système de templates de blocs prédéfinis
- [ ] Export/Import de configurations de pages
- [ ] Gestion des médias (upload d'images)

---

**Bon développement ! 🎉**
