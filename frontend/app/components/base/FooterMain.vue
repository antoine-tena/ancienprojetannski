<template>
  <footer :style="{
    background: '#2c3e50',
    color: '#ecf0f1',
    padding: '40px 20px',
    marginTop: 'auto'
  }">
    <div :style="{
      maxWidth: '1200px',
      margin: '0 auto',
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
      gap: '30px'
    }">
      <!-- Colonne 1 -->
      <div>
        <h3 :style="{ marginBottom: '15px', fontSize: '18px' }">À propos</h3>
        <p :style="{ lineHeight: '1.6', opacity: '0.9' }">
          Plateforme de gestion de contenu moderne et flexible.
        </p>
      </div>

      <!-- Colonne 2 -->
      <div>
        <h3 :style="{ marginBottom: '15px', fontSize: '18px' }">Liens rapides</h3>
        <ul :style="{ listStyle: 'none', padding: 0 }">
          <li :style="{ marginBottom: '10px' }">
            <NuxtLink to="/" :style="{ color: '#ecf0f1', textDecoration: 'none', opacity: '0.9' }">
              Accueil
            </NuxtLink>
          </li>
          <li :style="{ marginBottom: '10px' }">
            <NuxtLink to="/contact" :style="{ color: '#ecf0f1', textDecoration: 'none', opacity: '0.9' }">
              Contact
            </NuxtLink>
          </li>
        </ul>
      </div>

      <!-- Colonne 3 -->
      <div>
        <h3 :style="{ marginBottom: '15px', fontSize: '18px' }">Contact</h3>
        <p :style="{ lineHeight: '1.6', opacity: '0.9' }">
          Email: contact@example.com<br>
          Téléphone: +33 1 23 45 67 89
        </p>
      </div>
    </div>

    <div :style="{
      textAlign: 'center',
      marginTop: '40px',
      paddingTop: '20px',
      borderTop: '1px solid rgba(236, 240, 241, 0.2)',
      opacity: '0.8'
    }">
      © {{ new Date().getFullYear() }} Tous droits réservés.
    </div>
  </footer>
</template>

<script setup>
</script>
