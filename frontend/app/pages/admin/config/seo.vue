<template>
  <div :style="{
    display: 'flex',
    minHeight: '100vh',
    background: '#ffffff'
  }">
    <!-- Sidebar avec sous-catégories -->
    <div :style="{
      width: '280px',
      minHeight: '100vh',
      background: '#f8f9fa',
      borderRight: '1px solid #dee2e6',
      padding: '20px',
      display: 'flex',
      flexDirection: 'column',
      gap: '15px'
    }">
      <!-- Bouton retour -->
      <NuxtLink 
        to="/admin/config/website"
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
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
        </svg>
        <span>Retour</span>
      </NuxtLink>

      <!-- Titre -->
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
          SEO
        </h2>
      </div>

      <!-- Sous-catégories -->
      <div :style="{
        display: 'flex',
        flexDirection: 'column',
        gap: '5px',
        flex: 1
      }">
        <button
          v-for="section in sections"
          :key="section.id"
          @click="activeSection = section.id"
          :style="{
            padding: '12px 15px',
            background: activeSection === section.id ? '#007bff' : 'transparent',
            color: activeSection === section.id ? 'white' : '#495057',
            border: 'none',
            borderRadius: '4px',
            textAlign: 'left',
            cursor: 'pointer',
            fontWeight: activeSection === section.id ? 'bold' : 'normal',
            fontSize: '15px',
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            transition: 'all 0.2s'
          }"
        >
          <span v-html="section.icon"></span>
          <span>{{ section.label }}</span>
        </button>
      </div>
    </div>

    <!-- Contenu principal -->
    <div :style="{
      flex: 1,
      padding: '40px',
      maxWidth: '900px',
      overflowY: 'auto'
    }">
      <div v-if="error" :style="{
        padding: '15px',
        background: '#f8d7da',
        border: '1px solid #f5c6cb',
        borderRadius: '4px',
        color: '#721c24',
        marginBottom: '20px'
      }">
        {{ error }}
      </div>

      <div v-if="success" :style="{
        padding: '15px',
        background: '#d4edda',
        border: '1px solid #c3e6cb',
        borderRadius: '4px',
        color: '#155724',
        marginBottom: '20px'
      }">
        {{ success }}
      </div>

      <!-- Section Meta Tags -->
      <div v-if="activeSection === 'meta'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Meta Tags généraux
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Titre du site (Title Tag)
            </label>
            <input 
              v-model="form.site_title"
              type="text"
              placeholder="Mon Site Web - Description courte"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
            <p :style="{
              fontSize: '13px',
              color: '#6c757d',
              marginTop: '5px'
            }">
              50-60 caractères recommandés
            </p>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Description du site (Meta Description)
            </label>
            <textarea 
              v-model="form.site_description"
              placeholder="Description engageante de votre site qui apparaîtra dans les résultats de recherche"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                minHeight: '100px',
                resize: 'vertical',
                fontFamily: 'inherit'
              }"
            />
            <p :style="{
              fontSize: '13px',
              color: '#6c757d',
              marginTop: '5px'
            }">
              150-160 caractères recommandés
            </p>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Mots-clés (Keywords)
            </label>
            <input 
              v-model="form.keywords"
              type="text"
              placeholder="mot-clé1, mot-clé2, mot-clé3"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
            <p :style="{
              fontSize: '13px',
              color: '#6c757d',
              marginTop: '5px'
            }">
              Séparez les mots-clés par des virgules
            </p>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Auteur
            </label>
            <input 
              v-model="form.author"
              type="text"
              placeholder="Nom de l'auteur ou de l'entreprise"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>
        </div>
      </div>

      <!-- Section Open Graph -->
      <div v-if="activeSection === 'opengraph'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Open Graph (Facebook)
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Titre OG
            </label>
            <input 
              v-model="form.og_title"
              type="text"
              placeholder="Titre pour les partages Facebook"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Description OG
            </label>
            <textarea 
              v-model="form.og_description"
              placeholder="Description pour les partages Facebook"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                minHeight: '80px',
                resize: 'vertical',
                fontFamily: 'inherit'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Image OG (URL)
            </label>
            <input 
              v-model="form.og_image"
              type="text"
              placeholder="https://example.com/image.jpg"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
            <p :style="{
              fontSize: '13px',
              color: '#6c757d',
              marginTop: '5px'
            }">
              Recommandé: 1200x630 pixels
            </p>
          </div>
        </div>
      </div>

      <!-- Section Twitter Card -->
      <div v-if="activeSection === 'twitter'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Twitter Card
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Type de carte
            </label>
            <select 
              v-model="form.twitter_card"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                background: 'white'
              }"
            >
              <option value="summary">Summary</option>
              <option value="summary_large_image">Summary Large Image</option>
            </select>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Titre Twitter
            </label>
            <input 
              v-model="form.twitter_title"
              type="text"
              placeholder="Titre pour Twitter"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Description Twitter
            </label>
            <textarea 
              v-model="form.twitter_description"
              placeholder="Description pour Twitter"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                minHeight: '80px',
                resize: 'vertical',
                fontFamily: 'inherit'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Image Twitter (URL)
            </label>
            <input 
              v-model="form.twitter_image"
              type="text"
              placeholder="https://example.com/image.jpg"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>
        </div>
      </div>

      <!-- Section Indexation -->
      <div v-if="activeSection === 'indexing'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Indexation & Robots
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              cursor: 'pointer'
            }">
              <input 
                v-model="form.allow_indexing"
                type="checkbox"
                :style="{
                  width: '20px',
                  height: '20px',
                  cursor: 'pointer'
                }"
              />
              <span :style="{ fontWeight: 'bold', color: '#495057' }">
                Autoriser l'indexation par les moteurs de recherche
              </span>
            </label>
            <p :style="{
              fontSize: '13px',
              color: '#6c757d',
              marginTop: '5px',
              marginLeft: '30px'
            }">
              Si décoché, ajoute "noindex, nofollow" aux pages
            </p>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Robots.txt personnalisé
            </label>
            <textarea 
              v-model="form.robots_txt"
              placeholder="User-agent: *&#10;Disallow: /admin/"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '14px',
                fontFamily: 'monospace',
                minHeight: '150px',
                resize: 'vertical'
              }"
            />
          </div>
        </div>
      </div>

      <!-- Section Analytics -->
      <div v-if="activeSection === 'analytics'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Analytics & Tracking
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Google Analytics ID
            </label>
            <input 
              v-model="form.google_analytics_id"
              type="text"
              placeholder="G-XXXXXXXXXX ou UA-XXXXXXXXX-X"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                fontFamily: 'monospace'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Google Search Console
            </label>
            <input 
              v-model="form.google_site_verification"
              type="text"
              placeholder="Code de vérification Google"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                fontFamily: 'monospace'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Facebook Pixel ID
            </label>
            <input 
              v-model="form.facebook_pixel_id"
              type="text"
              placeholder="Votre Facebook Pixel ID"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                fontFamily: 'monospace'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Scripts personnalisés (Head)
            </label>
            <textarea 
              v-model="form.custom_head_scripts"
              placeholder="<script>...</script>"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '14px',
                fontFamily: 'monospace',
                minHeight: '120px',
                resize: 'vertical'
              }"
            />
            <p :style="{
              fontSize: '13px',
              color: '#6c757d',
              marginTop: '5px'
            }">
              Scripts insérés dans le &lt;head&gt; de chaque page
            </p>
          </div>
        </div>
      </div>

      <!-- Section Sitemap -->
      <div v-if="activeSection === 'sitemap'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Sitemap & URLs
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              URL du site
            </label>
            <input 
              v-model="form.site_url"
              type="text"
              placeholder="https://example.com"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div>
            <label :style="{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              cursor: 'pointer'
            }">
              <input 
                v-model="form.auto_generate_sitemap"
                type="checkbox"
                :style="{
                  width: '20px',
                  height: '20px',
                  cursor: 'pointer'
                }"
              />
              <span :style="{ fontWeight: 'bold', color: '#495057' }">
                Générer automatiquement le sitemap.xml
              </span>
            </label>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Fréquence de mise à jour
            </label>
            <select 
              v-model="form.sitemap_changefreq"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                background: 'white'
              }"
            >
              <option value="always">Toujours</option>
              <option value="hourly">Toutes les heures</option>
              <option value="daily">Quotidienne</option>
              <option value="weekly">Hebdomadaire</option>
              <option value="monthly">Mensuelle</option>
              <option value="yearly">Annuelle</option>
              <option value="never">Jamais</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Bouton Enregistrer -->
      <div :style="{
        position: 'sticky',
        bottom: '0',
        background: 'white',
        padding: '20px 0',
        borderTop: '1px solid #dee2e6',
        marginTop: '30px'
      }">
        <button
          @click="saveSEO"
          :disabled="loading"
          :style="{
            width: '100%',
            padding: '15px',
            background: loading ? '#6c757d' : '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            fontWeight: 'bold',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontSize: '18px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '10px'
          }"
        >
          <svg v-if="!loading" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 24px; height: 24px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {{ loading ? 'Enregistrement...' : 'Enregistrer les modifications' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: 'auth'
})

const { logout } = useAuth()

const sections = ref([
  {
    id: 'meta',
    label: 'Meta Tags',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 005.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 009.568 3z" /><path stroke-linecap="round" stroke-linejoin="round" d="M6 6h.008v.008H6V6z" /></svg>'
  },
  {
    id: 'opengraph',
    label: 'Open Graph',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M7.217 10.907a2.25 2.25 0 100 2.186m0-2.186c.18.324.283.696.283 1.093s-.103.77-.283 1.093m0-2.186l9.566-5.314m-9.566 7.5l9.566 5.314m0 0a2.25 2.25 0 103.935 2.186 2.25 2.25 0 00-3.935-2.186zm0-12.814a2.25 2.25 0 103.933-2.185 2.25 2.25 0 00-3.933 2.185z" /></svg>'
  },
  {
    id: 'twitter',
    label: 'Twitter Card',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" /></svg>'
  },
  {
    id: 'indexing',
    label: 'Indexation',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418" /></svg>'
  },
  {
    id: 'analytics',
    label: 'Analytics',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" /></svg>'
  },
  {
    id: 'sitemap',
    label: 'Sitemap',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 12h16.5m-16.5 3.75h16.5M3.75 19.5h16.5M5.625 4.5h12.75a1.875 1.875 0 010 3.75H5.625a1.875 1.875 0 010-3.75z" /></svg>'
  }
])

const activeSection = ref('meta')

const form = ref({
  site_title: '',
  site_description: '',
  keywords: '',
  author: '',
  og_title: '',
  og_description: '',
  og_image: '',
  twitter_card: 'summary_large_image',
  twitter_title: '',
  twitter_description: '',
  twitter_image: '',
  allow_indexing: true,
  robots_txt: '',
  google_analytics_id: '',
  google_site_verification: '',
  facebook_pixel_id: '',
  custom_head_scripts: '',
  site_url: '',
  auto_generate_sitemap: true,
  sitemap_changefreq: 'weekly'
})

const loading = ref(false)
const error = ref('')
const success = ref('')
const seoId = ref(null)

onMounted(async () => {
  const { ensureCsrfToken } = useAuth()
  await ensureCsrfToken()
  
  try {
    const data = await $fetch('http://localhost:8000/api/seo/', {
      credentials: 'include'
    })
    if (data && data.length > 0) {
      const seo = data[0]
      seoId.value = seo.id
      Object.keys(form.value).forEach(key => {
        if (seo[key] !== undefined) {
          form.value[key] = seo[key]
        }
      })
    }
  } catch (err) {
    error.value = 'Erreur lors du chargement des données'
    console.error(err)
  }
})

async function saveSEO() {
  loading.value = true
  error.value = ''
  success.value = ''

  try {
    if (seoId.value) {
      await $fetch(`http://localhost:8000/api/seo/${seoId.value}/`, {
        method: 'PUT',
        body: form.value,
        credentials: 'include'
      })
    } else {
      const newSEO = await $fetch('http://localhost:8000/api/seo/', {
        method: 'POST',
        body: form.value,
        credentials: 'include'
      })
      seoId.value = newSEO.id
    }

    success.value = 'Configuration SEO enregistrée avec succès !'
    setTimeout(() => {
      success.value = ''
    }, 3000)
  } catch (err) {
    error.value = err.data?.detail || 'Erreur lors de l\'enregistrement'
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>
