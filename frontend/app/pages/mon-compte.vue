<template>
  <div :style="{
    display: 'flex',
    minHeight: '100vh',
    background: '#ffffff'
  }">
    <UserSidebar title="Mon Compte" back-url="/">
    </UserSidebar>

    <div :style="{
      flex: 1,
      padding: '40px',
      maxWidth: '800px'
    }">
      <h1 :style="{
        fontSize: '32px',
        fontWeight: 'bold',
        marginBottom: '30px',
        color: '#212529'
      }">
        Mon Compte
      </h1>

      <!-- Informations du compte -->
      <div :style="{
        padding: '25px',
        background: '#f8f9fa',
        border: '1px solid #dee2e6',
        borderRadius: '8px',
        marginBottom: '25px'
      }">
        <h2 :style="{
          fontSize: '20px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Informations personnelles
        </h2>

        <div :style="{ marginBottom: '15px' }">
          <label :style="{
            display: 'block',
            marginBottom: '5px',
            fontWeight: '600',
            color: '#495057'
          }">
            Nom d'utilisateur
          </label>
          <div :style="{
            padding: '10px',
            background: 'white',
            border: '1px solid #ced4da',
            borderRadius: '4px'
          }">
            {{ user?.username || 'N/A' }}
          </div>
        </div>

        <div :style="{ marginBottom: '15px' }">
          <label :style="{
            display: 'block',
            marginBottom: '5px',
            fontWeight: '600',
            color: '#495057'
          }">
            Email
          </label>
          <div :style="{
            padding: '10px',
            background: 'white',
            border: '1px solid #ced4da',
            borderRadius: '4px'
          }">
            {{ user?.email || 'N/A' }}
          </div>
        </div>

        <div :style="{ marginBottom: '15px' }">
          <label :style="{
            display: 'block',
            marginBottom: '5px',
            fontWeight: '600',
            color: '#495057'
          }">
            Rôle
          </label>
          <div :style="{
            padding: '10px',
            background: user?.is_superuser ? '#d4edda' : 'white',
            border: '1px solid #ced4da',
            borderRadius: '4px',
            color: user?.is_superuser ? '#155724' : '#212529'
          }">
            {{ user?.is_superuser ? 'Administrateur' : 'Utilisateur' }}
          </div>
        </div>
      </div>

      <!-- Actions administrateur -->
      <div v-if="isSuperuser" :style="{
        padding: '25px',
        background: '#e7f5ff',
        border: '1px solid #339af0',
        borderRadius: '8px'
      }">
        <h2 :style="{
          fontSize: '20px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Administration
        </h2>

        <NuxtLink 
          to="/admin/config/website"
          :style="{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '8px',
            padding: '12px 24px',
            background: '#007bff',
            color: 'white',
            textDecoration: 'none',
            borderRadius: '4px',
            fontWeight: 'bold'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.324.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 011.37.49l1.296 2.247a1.125 1.125 0 01-.26 1.431l-1.003.827c-.293.24-.438.613-.431.992a6.759 6.759 0 010 .255c-.007.378.138.75.43.99l1.005.828c.424.35.534.954.26 1.43l-1.298 2.247a1.125 1.125 0 01-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 01-.22.128c-.331.183-.581.495-.644.869l-.213 1.28c-.09.543-.56.941-1.11.941h-2.594c-.55 0-1.02-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 01-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 01-1.369-.49l-1.297-2.247a1.125 1.125 0 01.26-1.431l1.004-.827c.292-.24.437-.613.43-.992a6.932 6.932 0 010-.255c.007-.378-.138-.75-.43-.99l-1.004-.828a1.125 1.125 0 01-.26-1.43l1.297-2.247a1.125 1.125 0 011.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.087.22-.128.332-.183.582-.495.644-.869l.214-1.281z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          Gérer le site web
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: 'auth'
})

const { user, isSuperuser } = useAuth()
</script>
