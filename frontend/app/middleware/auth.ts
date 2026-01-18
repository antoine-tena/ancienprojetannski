export default defineNuxtRouteMiddleware(async (to, from) => {
  const { isAuthenticated, isSuperuser, checkAuth } = useAuth()
  
  // Vérifier l'authentification si elle n'a pas été faite
  if (!isAuthenticated.value) {
    await checkAuth()
  }
  
  // Si l'utilisateur n'est pas authentifié, rediriger vers la page de connexion
  if (!isAuthenticated.value) {
    return navigateTo('/login')
  }
  
  // Si la route nécessite les droits superuser et l'utilisateur n'est pas superuser
  if (to.path.startsWith('/admin') && !isSuperuser.value) {
    return navigateTo('/mon-compte')
  }
})
