<template>
  <header :style="{
    position: headerConfig?.is_fixed ? 'fixed' : 'relative',
    top: headerConfig?.is_fixed ? '0' : 'auto',
    left: '0',
    right: '0',
    zIndex: headerConfig?.is_fixed ? '1000' : 'auto',
    background: headerConfig?.background_color || '#333',
    color: headerConfig?.text_color || 'white',
    fontFamily: headerConfig?.font_family || 'Arial, sans-serif',
    padding: `${headerConfig?.padding_vertical || 15}px ${headerConfig?.padding_horizontal || 20}px`,
    height: `${headerConfig?.height || 70}px`,
    opacity: headerConfig?.opacity !== undefined ? headerConfig.opacity : 1,
    backdropFilter: headerConfig?.blur ? `blur(${headerConfig.blur}px)` : 'none',
    borderBottom: headerConfig?.border_width ? `${headerConfig.border_width}px solid ${headerConfig.border_color || '#000'}` : 'none',
    boxShadow: headerConfig?.shadow || '0 2px 4px rgba(0,0,0,0.1)'
  }">
    <div :style="{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', maxWidth: '1200px', margin: '0 auto', height: '100%' }">
      <!-- Section gauche -->
      <div style="display: flex; align-items: center; gap: 20px; flex: 1;">
        <!-- Logo gauche -->
        <NuxtLink v-if="headerConfig?.logo_position === 'left'" to="/" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
          <img 
            v-if="headerConfig?.logo_image" 
            :src="headerConfig.logo_image" 
            alt="Logo"
            :style="{
              maxHeight: (headerConfig?.logo_size || 40) + 'px',
              width: 'auto',
              objectFit: 'contain',
              cursor: 'pointer'
            }"
          />
        </NuxtLink>

        <!-- Boutons gauche -->
        <template v-for="button in leftButtons" :key="button.id">
          <NuxtLink
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
            {{ button.text || button.label }}
          </NuxtLink>
        </template>

        <!-- Bouton connexion gauche -->
        <NuxtLink 
          v-if="!isAuthenticated && headerConfig?.show_login_button && headerConfig?.login_button_position === 'left'" 
          to="/login" 
          :style="{
            color: 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: headerConfig?.login_button_color || '#0066cc',
            borderRadius: '4px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
          </svg>
          <span>Connexion</span>
        </NuxtLink>

        <!-- Bouton Mon Compte gauche -->
        <a 
          v-if="isAuthenticated && headerConfig?.logout_button_position === 'left'"
          href="/mon-compte"
          @click.prevent="navigateTo('/mon-compte')"
          :style="{
            color: 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: headerConfig?.logout_button_color || '#0066cc',
            borderRadius: '4px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            cursor: 'pointer'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
          </svg>
          <span>Mon Compte</span>
        </a>
      </div>

      <!-- Section centre -->
      <div style="display: flex; align-items: center; gap: 20px; flex: 1; justify-content: center;">
        <!-- Logo centre -->
        <NuxtLink v-if="headerConfig?.logo_position === 'center'" to="/" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
          <img 
            v-if="headerConfig?.logo_image" 
            :src="headerConfig.logo_image" 
            alt="Logo"
            :style="{
              maxHeight: (headerConfig?.logo_size || 40) + 'px',
              width: 'auto',
              objectFit: 'contain',
              cursor: 'pointer'
            }"
          />
        </NuxtLink>

        <!-- Boutons centre -->
        <template v-for="button in centerButtons" :key="button.id">
          <NuxtLink
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
            {{ button.text || button.label }}
          </NuxtLink>
        </template>

        <!-- Bouton connexion centre -->
        <NuxtLink 
          v-if="!isAuthenticated && headerConfig?.show_login_button && headerConfig?.login_button_position === 'center'" 
          to="/login" 
          :style="{
            color: 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: headerConfig?.login_button_color || '#0066cc',
            borderRadius: '4px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
          </svg>
          <span>Connexion</span>
        </NuxtLink>

        <!-- Bouton Mon Compte centre -->
        <a 
          v-if="isAuthenticated && headerConfig?.logout_button_position === 'center'"
          href="/mon-compte"
          @click.prevent="navigateTo('/mon-compte')"
          :style="{
            color: 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: headerConfig?.logout_button_color || '#0066cc',
            borderRadius: '4px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            cursor: 'pointer'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
          </svg>
          <span>Mon Compte</span>
        </a>
      </div>

      <!-- Section droite -->
      <div style="display: flex; align-items: center; gap: 15px; flex: 1; justify-content: flex-end;">
        <!-- Logo droite -->
        <NuxtLink v-if="headerConfig?.logo_position === 'right'" to="/" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
          <img 
            v-if="headerConfig?.logo_image" 
            :src="headerConfig.logo_image" 
            alt="Logo"
            :style="{
              maxHeight: (headerConfig?.logo_size || 40) + 'px',
              width: 'auto',
              objectFit: 'contain',
              cursor: 'pointer'
            }"
          />
        </NuxtLink>

        <!-- Boutons droite -->
        <template v-for="button in rightButtons" :key="button.id">
          <NuxtLink
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
            {{ button.text || button.label }}
          </NuxtLink>
        </template>
        
        <!-- Bouton connexion droite (défaut) -->
        <NuxtLink 
          v-if="!isAuthenticated && headerConfig?.show_login_button && (!headerConfig?.login_button_position || headerConfig?.login_button_position === 'right')" 
          to="/login" 
          :style="{
            color: 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: headerConfig?.login_button_color || '#0066cc',
            borderRadius: '4px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
          </svg>
          <span>Connexion</span>
        </NuxtLink>

        <!-- Bouton Mon Compte droite (défaut) -->
        <a 
          v-if="isAuthenticated && (!headerConfig?.logout_button_position || headerConfig?.logout_button_position === 'right')"
          href="/mon-compte"
          @click.prevent="navigateTo('/mon-compte')"
          :style="{
            color: 'white',
            textDecoration: 'none',
            padding: '8px 16px',
            background: headerConfig?.logout_button_color || '#0066cc',
            borderRadius: '4px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            cursor: 'pointer'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
          </svg>
          <span>Mon Compte</span>
        </a>
      </div>
    </div>
  </header>
</template>

<script setup>
const { isAuthenticated, isSuperuser, logout } = useAuth()
const { headerConfig } = useWebsite()

const leftButtons = computed(() => {
  if (!headerConfig.value?.buttons) return []
  return headerConfig.value.buttons
    .filter(btn => btn.is_visible && btn.position === 'left')
    .sort((a, b) => a.order - b.order)
})

const centerButtons = computed(() => {
  if (!headerConfig.value?.buttons) return []
  return headerConfig.value.buttons
    .filter(btn => btn.is_visible && btn.position === 'center')
    .sort((a, b) => a.order - b.order)
})

const rightButtons = computed(() => {
  if (!headerConfig.value?.buttons) return []
  return headerConfig.value.buttons
    .filter(btn => btn.is_visible && btn.position === 'right')
    .sort((a, b) => a.order - b.order)
})
</script>
