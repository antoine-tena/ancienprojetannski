# 🚀 Guide de démarrage rapide - Éditeur Visuel

## 📍 Accéder à l'éditeur

1. **Démarrez le serveur** (si ce n'est pas déjà fait) :
   ```bash
   cd frontend
   npm run dev
   ```

2. **Visitez la page de démonstration** :
   ```
   http://localhost:3000/editor-demo
   ```

## 🎨 Comment utiliser l'éditeur

### Étape 1 : Activer le mode édition
- En haut de la page, vous verrez une barre d'outils avec un toggle "Activer l'édition"
- Cliquez sur le toggle pour activer le mode édition
- La barre devient verte avec "Mode édition activé"

### Étape 2 : Voir les contrôles d'édition
Une fois le mode édition activé :
1. **Survolez un bloc** → Une bordure bleue pointillée apparaît
2. **Un handle de drag** (icône "move") apparaît en haut à gauche
3. **Cliquez sur un bloc** → Trois boutons apparaissent :
   - 🖊️ **Crayon bleu** (en haut à droite) : Ouvrir l'éditeur
   - 🗑️ **Poubelle rouge** (en haut à droite) : Supprimer le bloc
   - 📋 **Copie verte** (en haut à droite) : Dupliquer le bloc

### Étape 3 : Éditer un bloc
1. Cliquez sur le **bouton crayon** 🖊️
2. Un panneau latéral s'ouvre à droite
3. Modifiez les champs (titre, contenu, couleurs, etc.)
4. **Les changements sont instantanés** - pas besoin de sauvegarder !

### Étape 4 : Réorganiser les blocs
1. En mode édition, attrapez le **handle de drag** (icône "move" en haut à gauche)
2. Glissez-déposez le bloc à la position souhaitée
3. L'ordre est automatiquement sauvegardé

### Étape 5 : Ajouter un nouveau bloc
1. Cliquez sur **"Ajouter un bloc"** dans la barre d'outils
2. Choisissez le type de bloc (Hero, Text, Image, CTA, Card)
3. Cliquez sur "Ajouter"
4. Le nouveau bloc apparaît en bas de la page

## 🎯 Types de blocs disponibles

| Type | Description | Champs éditables |
|------|-------------|------------------|
| **Hero** | Bannière d'accueil avec titre, texte et bouton | Titre, contenu, couleurs, texte du bouton, URL |
| **Text** | Bloc de texte simple | Titre, contenu, alignement |
| **Image** | Image responsive | URL de l'image, texte alternatif |
| **CTA** | Call-to-action coloré | Titre, contenu, texte du bouton, URL, couleur de fond |
| **Card** | Carte avec image et contenu | Titre, contenu, URL de l'image |

## 🔧 Résolution de problèmes

### Je ne vois pas la barre d'outils
- Assurez-vous d'être sur `/editor-demo` (pas `/test` ou autre)
- Vérifiez que vous êtes connecté en tant que superuser
- Pour la démo, `isAdmin` est forcé à `true` automatiquement

### Je ne vois pas le crayon
- Vous devez d'abord **activer le mode édition** avec le toggle
- Ensuite **survolez un bloc** pour voir la bordure
- Puis **cliquez sur le bloc** pour voir les boutons (crayon, poubelle, copie)

### Le panneau d'édition ne s'ouvre pas
- Cliquez bien sur le **bouton crayon** (pas sur le bloc lui-même)
- Assurez-vous que le mode édition est activé

### Les changements ne sont pas instantanés
- Vérifiez la console du navigateur (F12) pour les erreurs
- Les changements devraient être visibles dès que vous modifiez un champ

## 💡 Astuces

- **Double-clic rapide** : Cliquez sur un bloc puis immédiatement sur le crayon pour éditer rapidement
- **Échap** : Fermez le panneau d'édition avec la touche Échap
- **Drag & Drop** : Attrapez toujours le handle "move" (pas le bloc lui-même)
- **Sauvegarde** : Pour l'instant, les changements sont en mémoire. Cliquez sur "Tout sauvegarder" pour simuler une sauvegarde (console)

## 🎓 Prochaines étapes

1. Intégrez l'éditeur dans vos pages existantes
2. Créez de nouveaux types de blocs personnalisés
3. Connectez-le à votre API backend pour la persistence
4. Ajoutez l'historique Undo/Redo

Consultez `EDITOR_ADVANCED_EXAMPLES.md` pour des exemples avancés !
