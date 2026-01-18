# GUIDE D'ARCHITECTURE NUXT 3 (GÉNÉRAL)
# Rôle et utilisation standard des dossiers

Ce document décrit la structure standard d'un projet Nuxt 3 et les bonnes pratiques associées à chaque dossier.
Nuxt repose sur le principe de "Convention over Configuration" : le nom des dossiers détermine le comportement du framework.

---

### 1. app (Fichier app.vue)
> Le point d'entrée racine de l'application Vue.
- **Rôle :** C'est le composant parent de TOUTES les pages. Il est chargé une seule fois au démarrage.
- **Usage :**
  - Définir la structure globale minimale (généralement `<NuxtLayout>` qui contient `<NuxtPage>`).
  - Initialiser des styles globaux ou des transitions de page par défaut.
  - C'est l'équivalent du fichier `App.vue` dans une application Vue.js classique (Vite).

### 2. assets
> Les ressources statiques qui doivent être TRAITÉES (Compilées).
- **Rôle :** Contient les fichiers (CSS, SASS, Images, Fonts) qui passeront par le moteur de build (Vite/Webpack).
- **Comportement :**
  - Les images sont optimisées (et renommées avec un hash pour le cache).
  - Les fichiers CSS/SCSS sont minifiés et injectés.
- **Usage :** `import logo from '~/assets/logo.png'` ou `@import '~/assets/css/main.scss'`.

### 3. components
> Les briques visuelles de l'interface (Composants Vue).
- **Rôle :** Contient les fichiers `.vue` réutilisables.
- **Fonctionnalité clé :** "Auto-import". Vous n'avez pas besoin d'importer les composants manuellement.
- **Convention de nommage :** La structure des dossiers crée le nom du composant.
  - Exemple : `components/base/Button.vue` devient `<BaseButton />`.
- **Usage :** Boutons, cartes, formulaires, modales, éléments d'interface.

### 4. composables
> La logique métier réutilisable (État & Fonctions).
- **Rôle :** Contient des fonctions qui exploitent la Composition API de Vue (`ref`, `computed`, `onMounted`).
- **Fonctionnalité clé :** Auto-importé partout dans l'application.
- **Usage :**
  - Gestion d'état global (remplace souvent Vuex/Pinia pour des cas simples).
  - Logique partagée (ex: `useUser`, `useFetchAPI`, `useTheme`).
  - Hooks personnalisés.

### 5. layouts
> Les gabarits de mise en page (Wrappers).
- **Rôle :** Définit l'enveloppe visuelle qui entoure le contenu d'une page. Permet de ne pas répéter le Header et le Footer dans chaque fichier.
- **Usage :**
  - `default.vue` : Layout standard (Navbar + Footer).
  - `auth.vue` : Layout vide ou centré (pour Login/Register).
  - `dashboard.vue` : Layout avec Sidebar latérale.

### 6. middleware
> La logique de navigation (Gardiens de route).
- **Rôle :** Fonctions qui s'exécutent *entre* le changement de route et l'affichage de la page.
- **Usage :**
  - Authentification (rediriger vers /login si non connecté).
  - Permissions (vérifier le rôle admin).
  - Redirections conditionnelles ou A/B testing.
- **Format :** Peut être global (suffixe `.global.ts`) ou spécifique à une page.

### 7. pages
> Le routage automatique (File-based Routing).
- **Rôle :** Chaque fichier `.vue` dans ce dossier crée automatiquement une URL correspondante.
- **Fonctionnement :**
  - `index.vue` -> `/`
  - `contact.vue` -> `/contact`
  - `blog/[id].vue` -> `/blog/123` (Route dynamique)
  - `[...slug].vue` -> Catch-all route (attrape toutes les URLs non définies).

### 8. plugins
> La configuration au démarrage (Initialisation).
- **Rôle :** Scripts exécutés à la création de l'application (côté serveur et/ou client).
- **Usage :**
  - Injecter des bibliothèques externes (Google Analytics, Chart.js, Axios).
  - Créer des directives Vue globales.
  - Initialiser des configurations spécifiques avant que l'utilisateur ne voie l'interface.

### 9. public
> Les fichiers statiques servis TELS QUELS (Racine).
- **Rôle :** Fichiers accessibles directement via l'URL du navigateur, sans modification par le build.
- **Différence avec assets :** Ils ne sont ni renommés, ni optimisés, ni hashés.
- **Usage :** `favicon.ico`, `robots.txt`, `sitemap.xml`, images qui doivent conserver un nom de fichier fixe.
- **Accès :** Un fichier `public/image.jpg` est accessible via `domaine.com/image.jpg`.

### 10. server
> Le backend intégré (API Nitro).
- **Rôle :** Permet de créer une API Backend, des routes serveur et des middlewares serveur directement dans Nuxt.
- **Usage :**
  - `server/api/hello.ts` crée une route API `/api/hello`.
  - Cacher des clés API privées (proxy vers une API externe).
  - Connexion directe à une base de données (si Nuxt est utilisé comme Fullstack).
  - *Note :* Inutile si vous utilisez un backend externe (comme Django ou Laravel), sauf pour faire passe-plat.

### 11. utils
> Les fonctions utilitaires (Helpers purs).
- **Rôle :** Boîte à outils de fonctions génériques.
- **Différence avec Composables :** Les `utils` sont stateless (sans état réactif Vue). Ce sont des fonctions JavaScript/TypeScript pures.
- **Usage :**
  - Formatage de dates ou de devises.
  - Validation d'emails (Regex).
  - Calculs mathématiques.
  - Manipulation de chaînes de caractères.

---

### AIDE-MÉMOIRE DÉCISIONNEL

1. **C'est une page avec une URL ?** -> `pages/`
2. **C'est un morceau d'interface (bouton, header) ?** -> `components/`
3. **C'est une logique réactive partagée (state, user) ?** -> `composables/`
4. **C'est une fonction mathématique ou de formatage ?** -> `utils/`
5. **C'est une image ou du CSS à compiler ?** -> `assets/`
6. **C'est un fichier statique fixe (robots.txt) ?** -> `public/`
7. **Je veux protéger l'accès à une page ?** -> `middleware/`
8. **Je veux configurer une lib au démarrage ?** -> `plugins/`