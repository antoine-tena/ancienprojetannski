# Structure des Pages

## 📁 Organisation

### `/` - Pages publiques
Pages accessibles à tous les visiteurs (connectés ou non)
- `index.vue` - Page d'accueil
- `login.vue` - Page de connexion

### `/account/` - Espace utilisateur
Pages accessibles uniquement aux utilisateurs connectés
- Nécessite le middleware `auth`
- Visible pour tous les utilisateurs authentifiés (superuser ou non)
- Exemples: profil, paramètres, historique, etc.

**Pages actuelles:**
- **Note:** `/mon-compte` est actuellement à la racine mais devrait être déplacé vers `/account/`

### `/admin/config/` - Administration du site (Superusers uniquement)
Pages de configuration du site, accessibles uniquement aux superusers
- Nécessite le middleware `auth` + vérification `isSuperuser`
- Permet de gérer tout le contenu et l'apparence du site

**Pages actuelles:**
- `website.vue` - Dashboard principal de l'admin
- `header.vue` - Configuration du header (logo, couleurs, boutons, options avancées)
- `footer.vue` - Configuration du footer (texte, liens)
- `pages.vue` - Gestion des pages (création, modification, sections)
- `styles.vue` - Gestion des thèmes visuels
- `ressources.vue` - Gestion des ressources (images, fichiers)
- `seo.vue` - Configuration SEO globale

## 🔐 Niveaux d'accès

| Route | Accès | Middleware | Vérification |
|-------|-------|------------|--------------|
| `/` | Public | - | - |
| `/login` | Public | - | - |
| `/mon-compte` | Utilisateur | `auth` | `isAuthenticated` |
| `/admin/config/*` | Superuser | `auth` | `isSuperuser` |

## 🎯 Recommandations

### Pour créer une nouvelle page utilisateur:
1. Créer le fichier dans `/pages/account/`
2. Ajouter `definePageMeta({ middleware: 'auth' })`
3. Utiliser `const { user, isAuthenticated } = useAuth()`

### Pour créer une nouvelle page admin:
1. Créer le fichier dans `/pages/admin/config/`
2. Ajouter `definePageMeta({ middleware: 'auth' })`
3. Vérifier `isSuperuser` dans le composant
4. Utiliser le composant `<AdminSidebar>` pour la navigation

## 🧹 Nettoyage effectué

- ✅ Suppression de `/admin/header.vue` (doublon de `/admin/config/header.vue`)
- ✅ Correction de `/mon-compte.vue` pour utiliser `isSuperuser` au lieu de `isAdmin`
- ✅ Suppression de tous les emojis, remplacement par des icônes SVG
