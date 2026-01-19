<template>
  <div :style="{
    display: 'flex',
    minHeight: '100vh',
    background: '#ffffff'
  }">
    <AdminSidebar title="Site Web" back-url="/" :show-logout="false">
      <div :style="{
        padding: '10px 0',
        color: '#6c757d',
        fontSize: '14px'
      }">
        Gérez tous les aspects de votre site web depuis cette interface.
      </div>
    </AdminSidebar>

    <div :style="{
      flex: 1,
      padding: '40px'
    }">
      <h1 :style="{
        fontSize: '32px',
        fontWeight: 'bold',
        marginBottom: '10px',
        color: '#212529'
      }">
        Configuration du Site Web
      </h1>
      <p :style="{
        color: '#6c757d',
        marginBottom: '40px'
      }">
        Sélectionnez une section pour la configurer
      </p>

      <div :style="{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
        gap: '20px',
        maxWidth: '900px'
      }">
        <!-- Card Header -->
        <NuxtLink 
          to="/admin/config/header"
          :style="{
            display: 'block',
            padding: '30px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.2s',
            cursor: 'pointer'
          }"
          @mouseover="(e) => e.currentTarget.style.transform = 'translateY(-2px)'"
          @mouseleave="(e) => e.currentTarget.style.transform = 'translateY(0)'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :style="{
            width: '48px',
            height: '48px',
            color: '#007bff',
            marginBottom: '10px'
          }">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
          <h3 :style="{
            fontSize: '20px',
            fontWeight: 'bold',
            margin: '0 0 10px 0',
            color: '#212529'
          }">Header</h3>
          <p :style="{
            margin: 0,
            color: '#6c757d',
            fontSize: '14px'
          }">
            Personnalisez l'en-tête et les boutons de navigation
          </p>
        </NuxtLink>

        <!-- Card Footer -->
        <NuxtLink 
          to="/admin/config/footer"
          :style="{
            display: 'block',
            padding: '30px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.2s',
            cursor: 'pointer'
          }"
          @mouseover="(e) => e.currentTarget.style.transform = 'translateY(-2px)'"
          @mouseleave="(e) => e.currentTarget.style.transform = 'translateY(0)'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :style="{
            width: '48px',
            height: '48px',
            color: '#28a745',
            marginBottom: '10px'
          }">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" />
          </svg>
          <h3 :style="{
            fontSize: '20px',
            fontWeight: 'bold',
            margin: '0 0 10px 0',
            color: '#212529'
          }">Footer</h3>
          <p :style="{
            margin: 0,
            color: '#6c757d',
            fontSize: '14px'
          }">
            Configurez le pied de page et les liens
          </p>
        </NuxtLink>

        <!-- Card Pages -->
        <NuxtLink 
          to="/admin/config/pages"
          :style="{
            display: 'block',
            padding: '30px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.2s',
            cursor: 'pointer'
          }"
          @mouseover="(e) => e.currentTarget.style.transform = 'translateY(-2px)'"
          @mouseleave="(e) => e.currentTarget.style.transform = 'translateY(0)'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :style="{
            width: '48px',
            height: '48px',
            color: '#6c757d',
            marginBottom: '10px'
          }">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
          </svg>
          <h3 :style="{
            fontSize: '20px',
            fontWeight: 'bold',
            margin: '0 0 10px 0',
            color: '#212529'
          }">Pages</h3>
          <p :style="{
            margin: 0,
            color: '#6c757d',
            fontSize: '14px'
          }">
            Gérez les pages et les sections de contenu
          </p>
        </NuxtLink>

        <!-- Card Styles -->
        <NuxtLink 
          to="/admin/config/styles"
          :style="{
            display: 'block',
            padding: '30px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.2s',
            cursor: 'pointer'
          }"
          @mouseover="(e) => e.currentTarget.style.transform = 'translateY(-2px)'"
          @mouseleave="(e) => e.currentTarget.style.transform = 'translateY(0)'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :style="{
            width: '48px',
            height: '48px',
            color: '#dc3545',
            marginBottom: '10px'
          }">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z" />
          </svg>
          <h3 :style="{
            fontSize: '20px',
            fontWeight: 'bold',
            margin: '0 0 10px 0',
            color: '#212529'
          }">Styles</h3>
          <p :style="{
            margin: 0,
            color: '#6c757d',
            fontSize: '14px'
          }">
            Thèmes, polices, couleurs et styles visuels
          </p>
        </NuxtLink>

        <!-- Card Ressources -->
        <NuxtLink 
          to="/admin/config/ressources"
          :style="{
            display: 'block',
            padding: '30px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.2s',
            cursor: 'pointer'
          }"
          @mouseover="(e) => e.currentTarget.style.transform = 'translateY(-2px)'"
          @mouseleave="(e) => e.currentTarget.style.transform = 'translateY(0)'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :style="{
            width: '48px',
            height: '48px',
            color: '#ffc107',
            marginBottom: '10px'
          }">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.75V12A2.25 2.25 0 014.5 9.75h15A2.25 2.25 0 0121.75 12v.75m-8.69-6.44l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z" />
          </svg>
          <h3 :style="{
            fontSize: '20px',
            fontWeight: 'bold',
            margin: '0 0 10px 0',
            color: '#212529'
          }">Ressources</h3>
          <p :style="{
            margin: 0,
            color: '#6c757d',
            fontSize: '14px'
          }">
            Images, fichiers et médias du site
          </p>
        </NuxtLink>

        <!-- Card SEO -->
        <NuxtLink 
          to="/admin/config/seo"
          :style="{
            display: 'block',
            padding: '30px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.2s',
            cursor: 'pointer'
          }"
          @mouseover="(e) => e.currentTarget.style.transform = 'translateY(-2px)'"
          @mouseleave="(e) => e.currentTarget.style.transform = 'translateY(0)'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :style="{
            width: '48px',
            height: '48px',
            color: '#17a2b8',
            marginBottom: '10px'
          }">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
          </svg>
          <h3 :style="{
            fontSize: '20px',
            fontWeight: 'bold',
            margin: '0 0 10px 0',
            color: '#212529'
          }">SEO</h3>
          <p :style="{
            margin: 0,
            color: '#6c757d',
            fontSize: '14px'
          }">
            Optimisation pour les moteurs de recherche
          </p>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: 'auth'
})
</script>
