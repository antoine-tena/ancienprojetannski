<template>
  <div style="min-height: 100vh; display: flex; align-items: center; justify-content: center; background: #f5f5f5;">
    <div style="background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); max-width: 400px; width: 100%;">
      <h1 style="margin-bottom: 20px;">Connexion</h1>
      
      <div v-if="error" style="background: #fee; color: #c00; padding: 10px; margin-bottom: 20px; border-radius: 4px;">
        {{ error }}
      </div>

      <form @submit.prevent="handleLogin">
        <div style="margin-bottom: 15px;">
          <label style="display: block; margin-bottom: 5px;">Username</label>
          <input 
            v-model="username" 
            type="text" 
            required
            style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
          />
        </div>

        <div style="margin-bottom: 20px;">
          <label style="display: block; margin-bottom: 5px;">Password</label>
          <input 
            v-model="password" 
            type="password" 
            required
            style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
          />
        </div>

        <button 
          type="submit" 
          :disabled="loading"
          style="width: 100%; padding: 10px; background: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer;"
        >
          {{ loading ? 'Connexion...' : 'Se connecter' }}
        </button>
      </form>

      <div style="margin-top: 20px; text-align: center;">
        <NuxtLink to="/" style="color: #0066cc;">Retour à l'accueil</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false
})

const { login, checkAuth } = useAuth()
const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true
  error.value = ''
  
  const result = await login(username.value, password.value)
  
  loading.value = false
  
  if (result.success) {
    await checkAuth()
    navigateTo('/admin/pages')
  } else {
    error.value = result.error || 'Erreur de connexion'
  }
}
</script>
