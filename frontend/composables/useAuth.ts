export const useAuth = () => {
  const user = useState('user', () => null)
  const isAuthenticated = computed(() => user.value !== null)
  const isAdmin = computed(() => user.value?.is_superuser || false)

  const API_URL = 'http://localhost:8000/api'

  const checkAuth = async () => {
    try {
      const response = await $fetch(`${API_URL}/auth/me/`, {
        credentials: 'include'
      })
      if (response.authenticated) {
        user.value = response.user
      } else {
        user.value = null
      }
    } catch (error) {
      user.value = null
    }
  }

  const login = async (username: string, password: string) => {
    try {
      const response = await $fetch(`${API_URL}/auth/login/`, {
        method: 'POST',
        credentials: 'include',
        body: { username, password }
      })
      
      if (response.success) {
        user.value = response.user
        return { success: true }
      } else {
        return { success: false, error: response.error }
      }
    } catch (error) {
      return { success: false, error: 'Erreur de connexion' }
    }
  }

  const logout = async () => {
    try {
      await $fetch(`${API_URL}/auth/logout/`, {
        method: 'POST',
        credentials: 'include'
      })
      user.value = null
      navigateTo('/')
    } catch (error) {
      console.error('Erreur logout:', error)
    }
  }

  return {
    user,
    isAuthenticated,
    isAdmin,
    checkAuth,
    login,
    logout
  }
}
