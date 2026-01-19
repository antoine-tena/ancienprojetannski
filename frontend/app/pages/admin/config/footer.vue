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
          Footer
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

      <!-- Section Texte -->
      <div v-if="activeSection === 'text'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Texte du footer
        </h3>

        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Texte principal
          </label>
          <textarea 
            v-model="form.text"
            placeholder="© 2024 Mon Site. Tous droits réservés."
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
            Ce texte s'affichera dans le footer de toutes les pages
          </p>
        </div>

        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Texte secondaire (optionnel)
          </label>
          <textarea 
            v-model="form.secondaryText"
            placeholder="Informations additionnelles"
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
      </div>

      <!-- Section Liens -->
      <div v-if="activeSection === 'links'" :style="{ marginBottom: '30px' }">
        <div :style="{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '20px'
        }">
          <h3 :style="{
            fontSize: '24px',
            fontWeight: 'bold',
            margin: 0,
            color: '#212529'
          }">
            Liens du footer
          </h3>
          <button
            @click="addLink"
            :style="{
              padding: '10px 20px',
              background: '#007bff',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 'bold',
              fontSize: '14px',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
            </svg>
            Ajouter un lien
          </button>
        </div>

        <div 
          v-for="(link, index) in links" 
          :key="index"
          :style="{
            padding: '20px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            marginBottom: '15px'
          }"
        >
          <div :style="{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: '15px',
            marginBottom: '15px'
          }">
            <div>
              <label :style="{
                display: 'block',
                marginBottom: '8px',
                fontWeight: 'bold',
                color: '#495057',
                fontSize: '14px'
              }">
                Texte du lien
              </label>
              <input 
                v-model="link.text"
                type="text"
                placeholder="Mentions légales"
                :style="{
                  width: '100%',
                  padding: '10px',
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
                color: '#495057',
                fontSize: '14px'
              }">
                URL du lien
              </label>
              <input 
                v-model="link.url"
                type="text"
                placeholder="/mentions-legales"
                :style="{
                  width: '100%',
                  padding: '10px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  fontSize: '16px'
                }"
              />
            </div>
          </div>
          <button
            @click="removeLink(index)"
            :style="{
              padding: '8px 15px',
              background: '#dc3545',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 'bold',
              fontSize: '14px',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
            </svg>
            Supprimer
          </button>
        </div>

        <p v-if="links.length === 0" :style="{
          color: '#6c757d',
          fontStyle: 'italic',
          textAlign: 'center',
          padding: '40px',
          background: '#f8f9fa',
          borderRadius: '8px'
        }">
          Aucun lien configuré. Cliquez sur "Ajouter un lien" pour commencer.
        </p>
      </div>

      <!-- Section Réseaux sociaux -->
      <div v-if="activeSection === 'social'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Réseaux sociaux
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div v-for="social in socials" :key="social.name">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              {{ social.label }}
            </label>
            <input 
              v-model="form.socials[social.name]"
              type="text"
              :placeholder="social.placeholder"
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

      <!-- Section Couleurs -->
      <div v-if="activeSection === 'colors'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Couleurs
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Couleur de fond
            </label>
            <div :style="{ display: 'flex', gap: '10px', alignItems: 'center' }">
              <input 
                v-model="form.bgColor"
                type="color"
                :style="{
                  width: '60px',
                  height: '45px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
              />
              <input 
                v-model="form.bgColor"
                type="text"
                :style="{
                  flex: 1,
                  padding: '12px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  fontSize: '16px'
                }"
              />
            </div>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Couleur du texte
            </label>
            <div :style="{ display: 'flex', gap: '10px', alignItems: 'center' }">
              <input 
                v-model="form.textColor"
                type="color"
                :style="{
                  width: '60px',
                  height: '45px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
              />
              <input 
                v-model="form.textColor"
                type="text"
                :style="{
                  flex: 1,
                  padding: '12px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  fontSize: '16px'
                }"
              />
            </div>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Couleur des liens
            </label>
            <div :style="{ display: 'flex', gap: '10px', alignItems: 'center' }">
              <input 
                v-model="form.linkColor"
                type="color"
                :style="{
                  width: '60px',
                  height: '45px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
              />
              <input 
                v-model="form.linkColor"
                type="text"
                :style="{
                  flex: 1,
                  padding: '12px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  fontSize: '16px'
                }"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Section Typographie -->
      <div v-if="activeSection === 'typography'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Typographie
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Police de caractères
            </label>
            <select 
              v-model="form.fontFamily"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                background: 'white'
              }"
            >
              <option value="Arial, sans-serif">Arial</option>
              <option value="'Times New Roman', serif">Times New Roman</option>
              <option value="'Courier New', monospace">Courier New</option>
              <option value="Georgia, serif">Georgia</option>
              <option value="Verdana, sans-serif">Verdana</option>
              <option value="'Trebuchet MS', sans-serif">Trebuchet MS</option>
            </select>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Taille du texte (px)
            </label>
            <input 
              v-model.number="form.fontSize"
              type="number"
              min="10"
              max="24"
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
              Alignement du texte
            </label>
            <select 
              v-model="form.textAlign"
              :style="{
                width: '100%',
                padding: '12px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px',
                background: 'white'
              }"
            >
              <option value="left">Gauche</option>
              <option value="center">Centre</option>
              <option value="right">Droite</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Section Espacement -->
      <div v-if="activeSection === 'spacing'" :style="{ marginBottom: '30px' }">
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '20px',
          color: '#212529'
        }">
          Espacement
        </h3>

        <div :style="{ display: 'grid', gap: '20px' }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Espacement vertical (padding-top/bottom en px)
            </label>
            <input 
              v-model.number="form.paddingVertical"
              type="number"
              min="0"
              max="100"
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
              Espacement horizontal (padding-left/right en px)
            </label>
            <input 
              v-model.number="form.paddingHorizontal"
              type="number"
              min="0"
              max="100"
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
                v-model="form.hasBorder"
                type="checkbox"
                :style="{
                  width: '20px',
                  height: '20px',
                  cursor: 'pointer'
                }"
              />
              <span :style="{ fontWeight: 'bold', color: '#495057' }">
                Bordure supérieure
              </span>
            </label>
          </div>

          <div v-if="form.hasBorder">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Couleur de la bordure
            </label>
            <div :style="{ display: 'flex', gap: '10px', alignItems: 'center' }">
              <input 
                v-model="form.borderColor"
                type="color"
                :style="{
                  width: '60px',
                  height: '45px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
              />
              <input 
                v-model="form.borderColor"
                type="text"
                :style="{
                  flex: 1,
                  padding: '12px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  fontSize: '16px'
                }"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Bouton Enregistrer (en bas) -->
      <div :style="{
        position: 'sticky',
        bottom: '0',
        background: 'white',
        padding: '20px 0',
        borderTop: '1px solid #dee2e6',
        marginTop: '30px'
      }">
        <button
          @click="saveFooter"
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
            <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
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

// Sections de la sidebar
const sections = ref([
  {
    id: 'text',
    label: 'Texte',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" /></svg>'
  },
  {
    id: 'links',
    label: 'Liens',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244" /></svg>'
  },
  {
    id: 'social',
    label: 'Réseaux sociaux',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M7.217 10.907a2.25 2.25 0 100 2.186m0-2.186c.18.324.283.696.283 1.093s-.103.77-.283 1.093m0-2.186l9.566-5.314m-9.566 7.5l9.566 5.314m0 0a2.25 2.25 0 103.935 2.186 2.25 2.25 0 00-3.935-2.186zm0-12.814a2.25 2.25 0 103.933-2.185 2.25 2.25 0 00-3.933 2.185z" /></svg>'
  },
  {
    id: 'colors',
    label: 'Couleurs',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z" /></svg>'
  },
  {
    id: 'typography',
    label: 'Typographie',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5" /></svg>'
  },
  {
    id: 'spacing',
    label: 'Espacement',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>'
  }
])

const activeSection = ref('text')

// Données du formulaire
const form = ref({
  text: '',
  secondaryText: '',
  socials: {
    facebook: '',
    twitter: '',
    instagram: '',
    linkedin: '',
    youtube: ''
  },
  bgColor: '#212529',
  textColor: '#ffffff',
  linkColor: '#007bff',
  fontFamily: 'Arial, sans-serif',
  fontSize: 14,
  textAlign: 'center',
  paddingVertical: 40,
  paddingHorizontal: 20,
  hasBorder: true,
  borderColor: '#dee2e6'
})

const links = ref([])
const loading = ref(false)
const error = ref('')
const success = ref('')
const footerId = ref(null)

const socials = [
  { name: 'facebook', label: 'Facebook', placeholder: 'https://facebook.com/votrecompte' },
  { name: 'twitter', label: 'Twitter / X', placeholder: 'https://twitter.com/votrecompte' },
  { name: 'instagram', label: 'Instagram', placeholder: 'https://instagram.com/votrecompte' },
  { name: 'linkedin', label: 'LinkedIn', placeholder: 'https://linkedin.com/company/votrecompte' },
  { name: 'youtube', label: 'YouTube', placeholder: 'https://youtube.com/@votrecompte' }
]

onMounted(async () => {
  const { ensureCsrfToken } = useAuth()
  await ensureCsrfToken()
  
  try {
    const data = await $fetch('http://localhost:8000/api/footer/', {
      credentials: 'include'
    })
    if (data && data.length > 0) {
      const footer = data[0]
      footerId.value = footer.id
      
      // Charger les données existantes
      form.value.text = footer.text || ''
      form.value.secondaryText = footer.secondary_text || ''
      form.value.bgColor = footer.bg_color || '#212529'
      form.value.textColor = footer.text_color || '#ffffff'
      form.value.linkColor = footer.link_color || '#007bff'
      form.value.fontFamily = footer.font_family || 'Arial, sans-serif'
      form.value.fontSize = footer.font_size || 14
      form.value.textAlign = footer.text_align || 'center'
      form.value.paddingVertical = footer.padding_vertical || 40
      form.value.paddingHorizontal = footer.padding_horizontal || 20
      form.value.hasBorder = footer.has_border !== undefined ? footer.has_border : true
      form.value.borderColor = footer.border_color || '#dee2e6'
      
      // Parse links from JSON
      if (footer.links) {
        try {
          links.value = typeof footer.links === 'string' 
            ? JSON.parse(footer.links) 
            : footer.links
        } catch {
          links.value = []
        }
      }
      
      // Parse socials from JSON
      if (footer.socials) {
        try {
          const parsedSocials = typeof footer.socials === 'string' 
            ? JSON.parse(footer.socials) 
            : footer.socials
          form.value.socials = { ...form.value.socials, ...parsedSocials }
        } catch {
          // Garde les valeurs par défaut
        }
      }
    }
  } catch (err) {
    error.value = 'Erreur lors du chargement des données'
    console.error(err)
  }
})

function addLink() {
  links.value.push({
    text: '',
    url: ''
  })
}

function removeLink(index) {
  links.value.splice(index, 1)
}

async function saveFooter() {
  loading.value = true
  error.value = ''
  success.value = ''

  try {
    const payload = {
      text: form.value.text,
      secondary_text: form.value.secondaryText,
      links: links.value,
      socials: form.value.socials,
      bg_color: form.value.bgColor,
      text_color: form.value.textColor,
      link_color: form.value.linkColor,
      font_family: form.value.fontFamily,
      font_size: form.value.fontSize,
      text_align: form.value.textAlign,
      padding_vertical: form.value.paddingVertical,
      padding_horizontal: form.value.paddingHorizontal,
      has_border: form.value.hasBorder,
      border_color: form.value.borderColor
    }

    if (footerId.value) {
      await $fetch(`http://localhost:8000/api/footer/${footerId.value}/`, {
        method: 'PUT',
        body: payload,
        credentials: 'include'
      })
    } else {
      const newFooter = await $fetch('http://localhost:8000/api/footer/', {
        method: 'POST',
        body: payload,
        credentials: 'include'
      })
      footerId.value = newFooter.id
    }

    success.value = 'Footer enregistré avec succès !'
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
