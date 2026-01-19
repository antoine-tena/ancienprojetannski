<template>
  <div :style="{
    width: '280px',
    minHeight: '100vh',
    background: '#f8f9fa',
    borderRight: '1px solid #dee2e6',
    padding: '20px',
    display: 'flex',
    flexDirection: 'column',
    gap: '20px'
  }">
    <!-- Bouton retour -->
    <NuxtLink 
      :to="backUrl"
      :style="{
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        padding: '10px 15px',
        background: '#e9ecef',
        borderRadius: '4px',
        textDecoration: 'none',
        color: '#495057',
        fontWeight: '500',
        transition: 'background 0.2s'
      }"
    >
      <span>←</span>
      <span>Retour</span>
    </NuxtLink>

    <!-- Titre de la page -->
    <div :style="{
      padding: '15px 0',
      borderBottom: '2px solid #dee2e6'
    }">
      <h2 :style="{
        margin: 0,
        fontSize: '24px',
        fontWeight: 'bold',
        color: '#212529'
      }">
        {{ title }}
      </h2>
    </div>

    <!-- Slot pour le contenu personnalisé de la sidebar -->
    <div :style="{
      display: 'flex',
      flexDirection: 'column',
      gap: '10px',
      flex: 1
    }">
      <slot></slot>
    </div>

    <!-- Bouton déconnexion -->
    <button
      @click="auth.logout"
      :style="{
        display: 'flex',
        alignItems: 'center',
        gap: '10px',
        padding: '12px 16px',
        background: '#dc3545',
        color: 'white',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        fontWeight: '500',
        marginTop: 'auto',
        transition: 'background 0.2s'
      }"
    >
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
      </svg>
      <span>Déconnexion</span>
    </button>
  </div>
</template>

<script setup>
const auth = useAuth()

defineProps({
  title: {
    type: String,
    required: true
  },
  backUrl: {
    type: String,
    default: '/'
  }
})
</script>
