export const useWebsite = () => {
  const headerConfig = useState('headerConfig', () => null)
  const pages = useState('pages', () => [])

  const API_URL = 'http://localhost:8000/api'

  const fetchHeader = async () => {
    try {
      const response = await $fetch(`${API_URL}/header/current/`, {
        credentials: 'include'
      })
      headerConfig.value = response
    } catch (error) {
      console.error('Erreur fetch header:', error)
    }
  }

  const updateHeader = async (data: any) => {
    try {
      const response = await $fetch(`${API_URL}/header/${data.id}/`, {
        method: 'PUT',
        credentials: 'include',
        body: data
      })
      headerConfig.value = response
      return { success: true }
    } catch (error) {
      console.error('Erreur update header:', error)
      return { success: false, error }
    }
  }

  const fetchPages = async () => {
    try {
      const response = await $fetch(`${API_URL}/pages/tree/`, {
        credentials: 'include'
      })
      pages.value = response
    } catch (error) {
      console.error('Erreur fetch pages:', error)
    }
  }

  return {
    headerConfig,
    pages,
    fetchHeader,
    updateHeader,
    fetchPages
  }
}
