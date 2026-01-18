# 🎯 Structure Frontend - Guide Complet

## 📂 Nouvelle Organisation des Dossiers

```
frontend/app/
├── components/           # Composants réutilisables
│   ├── base/            # Composants de base du site (Header, Footer)
│   │   ├── HeaderMain.vue    # Header du site (visible par tous)
│   │   └── FooterMain.vue    # Footer du site
│   ├── AdminSidebar.vue      # Sidebar pour les pages admin (superusers)
│   ├── UserSidebar.vue       # Sidebar pour les pages utilisateur
│   └── PageTree.vue          # Arbre de navigation des pages
│
├── pages/               # Pages de l'application
│   ├── index.vue            # 🌍 Page d'accueil (PUBLIC)
│   ├── login.vue            # 🌍 Connexion (PUBLIC)
│   ├── mon-compte.vue       # 👤 Compte utilisateur (AUTHENTIFIÉ)
│   │
│   ├── account/             # 👤 Espace utilisateur (à développer)
│   │   └── [futures pages utilisateur]
│   │
│   └── admin/               # 👑 Administration
│       └── config/          # 👑 Pages de configuration (SUPERUSER)
│           ├── website.vue      # Dashboard admin principal
│           ├── header.vue       # Config header (9 sous-sections)
│           ├── footer.vue       # Config footer + liens
│           ├── pages.vue        # Gestion des pages
│           ├── styles.vue       # Gestion des thèmes
│           ├── ressources.vue   # Gestion des fichiers
│           └── seo.vue          # Configuration SEO
│
├── composables/         # Fonctions réutilisables
│   ├── useAuth.ts           # Authentification (isAuthenticated, isSuperuser, logout)
│   └── useWebsite.ts        # Configuration du site (header, footer, etc.)
│
└── middleware/          # Middlewares de route
    └── auth.ts              # Vérification authentification
```

## 🔐 Niveaux d'Accès

### 🌍 Pages Publiques (/)
**Accessible à tous**
- `index.vue` - Page d'accueil
- `login.vue` - Connexion

### 👤 Pages Utilisateur (/mon-compte)
**Accessible aux utilisateurs connectés**
- Middleware: `auth`
- Vérification: `isAuthenticated`
- Composant sidebar: `<UserSidebar>`

**Pages existantes:**
- `/mon-compte` - Profil + infos utilisateur + lien admin (si superuser)

**À créer dans `/account/`:**
- `/account/profile` - Modifier profil
- `/account/settings` - Paramètres
- `/account/history` - Historique d'activité

### 👑 Pages Admin (/admin/config/*)
**Accessible uniquement aux superusers**
- Middleware: `auth`
- Vérification: `isSuperuser`
- Composant sidebar: `<AdminSidebar>`

**Pages:**
| Page | Description | Fonctionnalités |
|------|-------------|-----------------|
| `website.vue` | Dashboard | 6 cartes vers les différentes sections |
| `header.vue` | Header | 9 sous-sections (couleurs, logo, boutons, advanced, etc.) |
| `footer.vue` | Footer | Texte + liens avec création auto des pages |
| `pages.vue` | Pages | Création/édition de pages avec sections |
| `styles.vue` | Thèmes | Gestion des thèmes visuels (polices, couleurs) |
| `ressources.vue` | Ressources | Upload et gestion de fichiers |
| `seo.vue` | SEO | Meta tags globaux |

## 🧩 Composants

### Base Components (site public)
**`components/base/HeaderMain.vue`**
- Utilisé sur toutes les pages du site
- Affiche logo, boutons de navigation, connexion/compte
- Configurable depuis `/admin/config/header`
- Props: headerConfig depuis useWebsite()

**`components/base/FooterMain.vue`**
- Footer du site
- Configurable depuis `/admin/config/footer`

### Sidebar Components

**`components/AdminSidebar.vue`** (pour superusers)
```vue
<AdminSidebar title="Titre de la page">
  <!-- Contenu custom de la sidebar -->
</AdminSidebar>
```
Fonctionnalités:
- Bouton retour
- Titre de la page
- Slot pour contenu personnalisé
- Bouton "Gérer le site" (vers /admin/config/website)
- Bouton "Déconnexion"

**`components/UserSidebar.vue`** (pour utilisateurs)
```vue
<UserSidebar title="Mon Compte" back-url="/">
  <!-- Contenu custom de la sidebar -->
</UserSidebar>
```
Fonctionnalités:
- Bouton retour
- Titre de la page
- Slot pour contenu personnalisé
- Bouton "Déconnexion"

## 🔧 Composables

### useAuth()
```js
const { 
  user,              // Objet user (username, email, is_superuser)
  isAuthenticated,   // Boolean: utilisateur connecté?
  isSuperuser,       // Boolean: utilisateur est superuser?
  logout             // Fonction de déconnexion
} = useAuth()
```

### useWebsite()
```js
const { 
  headerConfig,      // Configuration du header
  footerConfig       // Configuration du footer
} = useWebsite()
```

## 📝 Patterns de Code

### Créer une page utilisateur
```vue
<template>
  <div style="display: flex; min-height: 100vh;">
    <UserSidebar title="Ma Page" back-url="/">
      <!-- Navigation sidebar si besoin -->
    </UserSidebar>
    
    <div style="flex: 1; padding: 40px;">
      <h1>Ma Page Utilisateur</h1>
      <p>Contenu pour {{ user?.username }}</p>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: 'auth'
})

const { user } = useAuth()
</script>
```

### Créer une page admin
```vue
<template>
  <div style="display: flex; min-height: 100vh;">
    <AdminSidebar title="Configuration">
      <!-- Boutons de navigation -->
    </AdminSidebar>
    
    <div style="flex: 1; padding: 40px;">
      <h1>Page Admin</h1>
      <!-- Contenu admin -->
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: 'auth'
})

const { isSuperuser } = useAuth()

// Rediriger si pas superuser
if (!isSuperuser.value) {
  navigateTo('/')
}
</script>
```

## 🎨 Conventions

### Icônes
- ✅ Utiliser uniquement des SVG (Heroicons)
- ❌ Plus d'emojis

### Couleurs
- Primary: `#007bff` (bleu)
- Success: `#28a745` (vert)
- Danger: `#dc3545` (rouge)
- Warning: `#ffc107` (jaune)
- Info: `#17a2b8` (cyan)

### Spacing
- Sidebar width: `280px`
- Content padding: `40px`
- Bouton padding: `12px 24px`
- Gap entre éléments: `15-20px`

## 🚀 Prochaines Étapes

1. **Déplacer `/mon-compte.vue` vers `/account/index.vue`**
   - Créer `/pages/account/index.vue` avec le même contenu
   - Supprimer `/pages/mon-compte.vue`
   - Mettre à jour les liens dans HeaderMain.vue

2. **Créer d'autres pages utilisateur**
   - `/account/profile` - Éditer profil
   - `/account/settings` - Paramètres
   - `/account/notifications` - Notifications

3. **Améliorer la navigation**
   - Ajouter un menu dans UserSidebar avec liens vers les pages account
   - Breadcrumbs pour mieux s'orienter

4. **Tests**
   - Tester le bouton "Mon compte" depuis le header
   - Vérifier l'accès admin/user
   - Vérifier la création auto des pages depuis header/footer
