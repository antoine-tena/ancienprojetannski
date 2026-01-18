# AnnSki - Système de gestion de site web

Un système de gestion de contenu permettant de créer et gérer des sites web avec Django REST Framework et Nuxt 3.

## 🚀 Démarrage rapide

### Backend (Django)

```bash
cd backend
source venv/Scripts/activate  # Windows Git Bash
python manage.py runserver
```

Le backend sera accessible sur http://localhost:8000

### Frontend (Nuxt 3)

**Option 1 : Via le fichier batch (Windows)**
```bash
# Double-cliquez sur start-frontend.bat
# OU en ligne de commande :
start-frontend.bat
```

**Option 2 : Manuellement**
```bash
cd frontend
npm run dev
# ou
pnpm dev
```

Le frontend sera accessible sur http://localhost:3000

## 👤 Compte administrateur

- **Username:** admin
- **Password:** admin

## 📁 Structure du projet

```
.
├── backend/              # Django REST Framework API
│   ├── config/          # Configuration Django
│   ├── website/         # Application principale
│   │   ├── models.py   # HeaderConfig, Page
│   │   ├── views.py    # API endpoints
│   │   └── serializers.py
│   └── venv/           # Environnement virtuel Python
│
├── frontend/            # Nuxt 3 Application
│   ├── components/     # HeaderMain.vue, PageTree.vue
│   ├── composables/    # useAuth.ts, useWebsite.ts
│   ├── layouts/        # default.vue
│   ├── pages/          # Routes Nuxt
│   │   ├── index.vue   # Page d'accueil
│   │   ├── login.vue   # Page de connexion
│   │   └── admin/
│   │       └── pages.vue  # Administration
│   └── nuxt.config.ts
```

## ✨ Fonctionnalités implémentées

### 1. Page d'accueil
- Page blanche simple avec header
- Accessible à http://localhost:3000

### 2. Header dynamique
- Affichage du logo et titre configurables
- Bouton "Connexion" (configurable)
- Bouton "Administration" si connecté en tant qu'admin

### 3. Authentification
- Page de login à http://localhost:3000/login
- Connexion avec le compte admin/admin
- Session persistante avec cookies

### 4. Administration (admin/admin uniquement)
- Page d'administration à http://localhost:3000/admin/pages
- **Modification du header en temps réel** :
  - Titre du site
  - Texte du logo
  - Affichage/masquage du bouton connexion
- Affichage de l'arborescence des pages
- Bouton de déconnexion

## 🔧 Technologies utilisées

### Backend
- Django 6.0.1
- Django REST Framework 3.16.1
- django-cors-headers 4.9.0
- SQLite

### Frontend
- Nuxt 3 (v4.2.2)
- Vue 3
- TypeScript
- Nuxt UI

## 📡 API Endpoints

```
POST   /api/auth/login/      # Connexion
POST   /api/auth/logout/     # Déconnexion
GET    /api/auth/me/         # Utilisateur courant
GET    /api/header/current/  # Configuration header
PUT    /api/header/{id}/     # Modifier header (admin only)
GET    /api/pages/tree/      # Arborescence des pages
```

## 🎯 Prochaines étapes suggérées

1. Ajouter la création/édition/suppression de pages
2. Implémenter un éditeur de contenu pour les pages
3. Gérer les templates de pages
4. Ajouter un système de médias
5. Implémenter le drag & drop pour réorganiser l'arborescence

## 🐛 Debug

Si le frontend ne démarre pas avec npm/pnpm, utilisez le fichier `start-frontend.bat` qui contient les bonnes commandes Windows.

Le backend Django doit être démarré en premier pour que l'authentification fonctionne.


# annski.fr
