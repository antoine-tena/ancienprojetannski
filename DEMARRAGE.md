# Guide de démarrage rapide

## Backend Django

1. Démarrer le serveur backend :
```bash
cd backend
python manage.py runserver
```

Le backend sera accessible sur http://localhost:8000

## Frontend Nuxt

1. Dans un autre terminal, démarrer le serveur frontend :
```bash
cd frontend
npm run dev
# ou
pnpm dev
```

Le frontend sera accessible sur http://localhost:3000

## Connexion

- **URL de connexion**: http://localhost:3000/login
- **Username**: admin
- **Password**: admin

## Interface d'administration

Une fois connecté en tant qu'admin, vous aurez accès à :

1. **Configuration du Header** : http://localhost:3000/admin/header
   - Modifier la couleur de fond
   - Modifier la couleur du texte
   - Changer la police
   - Ajouter/supprimer des boutons personnalisés

2. **Gestion des pages** : http://localhost:3000/admin/pages

## Django Admin (optionnel)

Vous pouvez également utiliser l'interface d'administration Django :
- URL: http://localhost:8000/admin
- Username: admin
- Password: admin

## Fonctionnalités implémentées

✅ Superuser créé (admin/admin)
✅ Header avec bouton de connexion sur la page d'accueil
✅ Page de connexion fonctionnelle
✅ Interface d'administration pour modifier le header :
  - Couleur de fond
  - Couleur de texte
  - Police de caractères
  - Boutons personnalisables (libellé, URL, ordre, visibilité)
✅ Aperçu en temps réel des modifications
✅ Middleware d'authentification pour protéger les pages admin
✅ Structure Nuxt respectée (composables, components, pages, middleware)
