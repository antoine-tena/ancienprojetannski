export default defineNuxtRouteMiddleware(async (to, from) => {
  const { isAuthenticated, isAdmin, checkAuth } = useAuth()
  
  // Vérifier l'authentification si elle n'a pas été faite
  if (!isAuthenticated.value) {
    await checkAuth()
  }
  
  // Si l'utilisateur n'est pas authentifié ou n'est pas admin, rediriger vers la page de connexion
  if (!isAuthenticated.value || !isAdmin.value) {
    return navigateTo('/login')
  }
})
