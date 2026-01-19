<template>
  <header :style="{
    background: headerConfig?.background_color || '#333',
    color: headerConfig?.text_color || 'white',
    fontFamily: headerConfig?.font_family || 'Arial, sans-serif',
    padding: '15px 20px'
  }">
    <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto;">
      <div style="display: flex; align-items: center; gap: 20px;">
        <NuxtLink 
          to="/" 
          :style="{
            color: headerConfig?.text_color || 'white',
            textDecoration: 'none',
            fontSize: '20px',
            fontWeight: 'bold'
          }"
        >
          {{ headerConfig?.logo_text || 'Logo' }}
        </NuxtLink>
        <span v-if="headerConfig?.title" :style="{
          fontSize: '14px',
          opacity: '0.8'
        }">
          {{ headerConfig.title }}
        </span>
      </div>

      <div style="display: flex; align-items: center; gap: 15px;">
        <!-- Boutons personnalisés -->
        <template v-if="headerConfig?.buttons">
          <NuxtLink
            v-for="button in visibleButtons"
            :key="button.id"
            :to="button.url"
            :style="{
              color: headerConfig?.text_color || 'white',
              textDecoration: 'none',
              padding: '8px 16px',
              background: 'rgba(255,255,255,0.15)',
              borderRadius: '4px',
              transition: 'background 0.3s'
            }"
          >
            {{ button.label }}
          </NuxtLink>
        </template>

        <!-- Actions utilisateur -->
        <template v-if="isAuthenticated">
          <NuxtLink 
            v-if="isAdmin" 
            to="/admin/header" 
            :style="{
              color: headerConfig?.text_color || 'white',
              textDecoration: 'none',
              padding: '8px 16px',
              background: '#0066cc',
              borderRadius: '4px'
            }"
          >
            ⚙️ Config Header
          </NuxtLink>
          <NuxtLink 
            v-if="isAdmin" 
            to="/admin/pages" 
            :style="{
              color: headerConfig?.text_color || 'white',
              textDecoration: 'none',
              padding: '8px 16px',
              background: '#0066cc',
              borderRadius: '4px'
            }"
          >
            📄 Pages
          </NuxtLink>
          <button 
            @click="logout" 
            style="color: white; background: #dc3545; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;"
          >
            Déconnexion
          </button>
        </template>
        
        <NuxtLink 
          v-else-if="headerConfig?.show_login_button" 
          to="/login" 
          :style="{
            color: headerConfig?.text_color || 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: '#0066cc',
            borderRadius: '4px'
          }"
        >
          Connexion
        </NuxtLink>
      </div>
    </div>
  </header>
</template>

<script setup>
const { isAuthenticated, isAdmin, logout } = useAuth()
const { headerConfig } = useWebsite()

const visibleButtons = computed(() => {
  if (!headerConfig.value?.buttons) return []
  return headerConfig.value.buttons
    .filter(btn => btn.is_visible)
    .sort((a, b) => a.order - b.order)
})
</script>
