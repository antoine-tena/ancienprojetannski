<template>
  <div style="min-height: 100vh; background: #f5f5f5; padding: 20px;">
    <div style="max-width: 1200px; margin: 0 auto;">
      <div style="background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <h1 style="margin-bottom: 30px;">Configuration du Header</h1>

        <div v-if="message" :style="{
          padding: '10px',
          marginBottom: '20px',
          borderRadius: '4px',
          background: messageType === 'success' ? '#d4edda' : '#f8d7da',
          color: messageType === 'success' ? '#155724' : '#721c24'
        }">
          {{ message }}
        </div>

        <form @submit.prevent="handleSubmit">
          <!-- Informations générales -->
          <fieldset style="border: 1px solid #ddd; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
            <legend style="font-weight: bold; padding: 0 10px;">Informations générales</legend>
            
            <div style="margin-bottom: 15px;">
              <label style="display: block; margin-bottom: 5px; font-weight: bold;">Titre du header</label>
              <input 
                v-model="form.title" 
                type="text"
                style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
              />
            </div>

            <div style="margin-bottom: 15px;">
              <label style="display: block; margin-bottom: 5px; font-weight: bold;">Texte du logo</label>
              <input 
                v-model="form.logo_text" 
                type="text"
                style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
              />
            </div>

            <div style="margin-bottom: 15px;">
              <label style="display: flex; align-items: center; gap: 10px;">
                <input 
                  v-model="form.show_login_button" 
                  type="checkbox"
                />
                <span style="font-weight: bold;">Afficher le bouton de connexion</span>
              </label>
            </div>
          </fieldset>

          <!-- Styles -->
          <fieldset style="border: 1px solid #ddd; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
            <legend style="font-weight: bold; padding: 0 10px;">Styles</legend>
            
            <div style="margin-bottom: 15px;">
              <label style="display: block; margin-bottom: 5px; font-weight: bold;">Couleur de fond</label>
              <div style="display: flex; gap: 10px; align-items: center;">
                <input 
                  v-model="form.background_color" 
                  type="color"
                  style="height: 40px; width: 80px; border: 1px solid #ddd; border-radius: 4px;"
                />
                <input 
                  v-model="form.background_color" 
                  type="text"
                  style="flex: 1; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                  placeholder="#333333"
                />
              </div>
            </div>

            <div style="margin-bottom: 15px;">
              <label style="display: block; margin-bottom: 5px; font-weight: bold;">Couleur du texte</label>
              <div style="display: flex; gap: 10px; align-items: center;">
                <input 
                  v-model="form.text_color" 
                  type="color"
                  style="height: 40px; width: 80px; border: 1px solid #ddd; border-radius: 4px;"
                />
                <input 
                  v-model="form.text_color" 
                  type="text"
                  style="flex: 1; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                  placeholder="#ffffff"
                />
              </div>
            </div>

            <div style="margin-bottom: 15px;">
              <label style="display: block; margin-bottom: 5px; font-weight: bold;">Police de caractères</label>
              <input 
                v-model="form.font_family" 
                type="text"
                style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                placeholder="Arial, sans-serif"
              />
            </div>
          </fieldset>

          <!-- Boutons personnalisés -->
          <fieldset style="border: 1px solid #ddd; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
            <legend style="font-weight: bold; padding: 0 10px;">Boutons personnalisés</legend>
            
            <div v-for="(button, index) in buttons" :key="button.id || `new-${index}`" 
                 style="border: 1px solid #e0e0e0; padding: 15px; margin-bottom: 15px; border-radius: 4px; background: #fafafa;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <strong>Bouton {{ index + 1 }}</strong>
                <button 
                  type="button"
                  @click="removeButton(index)"
                  style="background: #dc3545; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;"
                >
                  Supprimer
                </button>
              </div>

              <div style="margin-bottom: 10px;">
                <label style="display: block; margin-bottom: 5px;">Libellé</label>
                <input 
                  v-model="button.label" 
                  type="text"
                  style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                  placeholder="Contact"
                />
              </div>

              <div style="margin-bottom: 10px;">
                <label style="display: block; margin-bottom: 5px;">URL</label>
                <input 
                  v-model="button.url" 
                  type="text"
                  style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                  placeholder="/contact"
                />
              </div>

              <div style="margin-bottom: 10px;">
                <label style="display: block; margin-bottom: 5px;">Ordre</label>
                <input 
                  v-model.number="button.order" 
                  type="number"
                  style="width: 100px; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                />
              </div>

              <div>
                <label style="display: flex; align-items: center; gap: 10px;">
                  <input 
                    v-model="button.is_visible" 
                    type="checkbox"
                  />
                  <span>Visible</span>
                </label>
              </div>
            </div>

            <button 
              type="button"
              @click="addButton"
              style="background: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; width: 100%;"
            >
              + Ajouter un bouton
            </button>
          </fieldset>

          <!-- Aperçu -->
          <fieldset style="border: 1px solid #ddd; padding: 20px; margin-bottom: 20px; border-radius: 4px;">
            <legend style="font-weight: bold; padding: 0 10px;">Aperçu</legend>
            
            <div :style="{
              background: form.background_color,
              color: form.text_color,
              fontFamily: form.font_family,
              padding: '15px 20px',
              borderRadius: '4px'
            }">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 20px;">
                  <span style="font-size: 20px; font-weight: bold;">{{ form.logo_text || 'Logo' }}</span>
                  <span style="font-size: 14px; opacity: 0.8;">{{ form.title || 'Mon Site' }}</span>
                </div>
                <div style="display: flex; gap: 10px;">
                  <span v-for="btn in buttons.filter(b => b.is_visible)" :key="btn.label"
                        style="padding: 5px 10px; background: rgba(255,255,255,0.2); border-radius: 4px; font-size: 14px;">
                    {{ btn.label }}
                  </span>
                </div>
              </div>
            </div>
          </fieldset>

          <!-- Actions -->
          <div style="display: flex; gap: 10px; justify-content: flex-end;">
            <NuxtLink 
              to="/"
              style="padding: 10px 20px; background: #6c757d; color: white; border: none; border-radius: 4px; text-decoration: none; display: inline-block;"
            >
              Annuler
            </NuxtLink>
            <button 
              type="submit"
              :disabled="loading"
              style="padding: 10px 20px; background: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer;"
            >
              {{ loading ? 'Enregistrement...' : 'Enregistrer' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false,
  middleware: 'auth'
})

const { headerConfig } = useWebsite()
const API_URL = 'http://localhost:8000/api'

const form = ref({
  id: null,
  title: '',
  logo_text: '',
  show_login_button: true,
  background_color: '#333333',
  text_color: '#ffffff',
  font_family: 'Arial, sans-serif'
})

const buttons = ref([])
const loading = ref(false)
const message = ref('')
const messageType = ref('')

// Charger les données existantes
onMounted(async () => {
  try {
    const config = await $fetch(`${API_URL}/header/current/`, {
      credentials: 'include'
    })
    
    form.value = {
      id: config.id,
      title: config.title,
      logo_text: config.logo_text,
      show_login_button: config.show_login_button,
      background_color: config.background_color,
      text_color: config.text_color,
      font_family: config.font_family
    }
    
    buttons.value = config.buttons || []
  } catch (error) {
    console.error('Erreur chargement:', error)
    message.value = 'Erreur lors du chargement de la configuration'
    messageType.value = 'error'
  }
})

const addButton = () => {
  buttons.value.push({
    label: '',
    url: '',
    order: buttons.value.length,
    is_visible: true
  })
}

const removeButton = (index) => {
  buttons.value.splice(index, 1)
}

const handleSubmit = async () => {
  loading.value = true
  message.value = ''
  
  try {
    // Mettre à jour la configuration du header
    await $fetch(`${API_URL}/header/${form.value.id}/`, {
      method: 'PUT',
      credentials: 'include',
      body: form.value
    })
    
    // Supprimer tous les anciens boutons et créer les nouveaux
    const existingButtons = await $fetch(`${API_URL}/header-buttons/`, {
      credentials: 'include'
    })
    
    for (const btn of existingButtons) {
      await $fetch(`${API_URL}/header-buttons/${btn.id}/`, {
        method: 'DELETE',
        credentials: 'include'
      })
    }
    
    // Créer les nouveaux boutons
    for (const btn of buttons.value) {
      await $fetch(`${API_URL}/header-buttons/`, {
        method: 'POST',
        credentials: 'include',
        body: {
          ...btn,
          header_config: form.value.id
        }
      })
    }
    
    message.value = 'Configuration enregistrée avec succès!'
    messageType.value = 'success'
    
    // Recharger les données pour l'aperçu
    const { fetchHeader } = useWebsite()
    await fetchHeader()
    
  } catch (error) {
    console.error('Erreur sauvegarde:', error)
    message.value = 'Erreur lors de l\'enregistrement'
    messageType.value = 'error'
  } finally {
    loading.value = false
  }
}
</script>
