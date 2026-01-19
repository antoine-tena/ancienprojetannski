<template>
  <NuxtLayout name="default">
    <div v-if="!isAdmin" style="padding: 20px;">
      <p>Accès non autorisé. Veuillez vous <NuxtLink to="/login" style="color: #0066cc;">connecter</NuxtLink>.</p>
    </div>

    <div v-else style="background: white; padding: 20px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
        <h1>Gestion du site</h1>
        <button @click="logout" style="padding: 8px 16px; background: #dc3545; color: white; border: none; border-radius: 4px; cursor: pointer;">
          Déconnexion
        </button>
      </div>

      <!-- Section modification du header -->
      <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
        <h2 style="margin-bottom: 15px;">Modifier le Header</h2>
        
        <form @submit.prevent="saveHeader" v-if="headerConfig">
          <div style="margin-bottom: 15px;">
            <label style="display: block; margin-bottom: 5px; font-weight: bold;">Titre du site</label>
            <input 
              v-model="headerConfig.title" 
              type="text"
              style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
            />
          </div>

          <div style="margin-bottom: 15px;">
            <label style="display: block; margin-bottom: 5px; font-weight: bold;">Texte du logo</label>
            <input 
              v-model="headerConfig.logo_text" 
              type="text"
              style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
            />
          </div>

          <div style="margin-bottom: 15px;">
            <label style="display: flex; align-items: center; gap: 10px;">
              <input 
                v-model="headerConfig.show_login_button" 
                type="checkbox"
              />
              <span>Afficher le bouton de connexion</span>
            </label>
          </div>

          <button 
            type="submit"
            :disabled="saving"
            style="padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer;"
          >
            {{ saving ? 'Enregistrement...' : 'Enregistrer le header' }}
          </button>

          <div v-if="saveMessage" style="margin-top: 10px; padding: 10px; background: #d4edda; color: #155724; border-radius: 4px;">
            {{ saveMessage }}
          </div>
        </form>
      </div>

      <!-- Section arborescence des pages -->
      <div>
        <h2 style="margin-bottom: 15px;">Arborescence des pages</h2>
        
        <div v-if="pages.length === 0" style="padding: 20px; background: #f8f9fa; border-radius: 4px; text-align: center;">
          Aucune page n'a été créée pour le moment.
        </div>

        <div v-else>
          <PageTree :pages="pages" />
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
definePageMeta({
  layout: false
})

const { isAdmin, logout } = useAuth()
const { headerConfig, pages, fetchHeader, updateHeader, fetchPages } = useWebsite()

const saving = ref(false)
const saveMessage = ref('')

onMounted(async () => {
  await fetchHeader()
  await fetchPages()
})

const saveHeader = async () => {
  saving.value = true
  saveMessage.value = ''
  
  const result = await updateHeader(headerConfig.value)
  
  saving.value = false
  
  if (result.success) {
    saveMessage.value = 'Header enregistré avec succès !'
    setTimeout(() => {
      saveMessage.value = ''
    }, 3000)
  } else {
    saveMessage.value = 'Erreur lors de l\'enregistrement'
  }
}
</script>
