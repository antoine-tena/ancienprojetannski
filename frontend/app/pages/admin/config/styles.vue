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
          Styles & Thèmes
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

      <!-- Section: Liste des thèmes -->
      <div v-if="activeSection === 'list'">
        <h1 :style="{
          fontSize: '32px',
          marginBottom: '30px',
          color: '#212529'
        }">
          Liste des thèmes
        </h1>

        <button
          @click="createNewTheme"
          :style="{
            padding: '12px 24px',
            background: '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontWeight: 'bold',
            fontSize: '16px',
            marginBottom: '20px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
          </svg>
          Nouveau thème
        </button>

        <div :style="{ display: 'flex', flexDirection: 'column', gap: '15px' }">
          <div
            v-for="theme in themes"
            :key="theme.id"
            :style="{
              padding: '20px',
              background: '#f8f9fa',
              border: '1px solid #dee2e6',
              borderRadius: '8px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center'
            }"
          >
            <div>
              <h3 :style="{ margin: '0 0 5px 0', fontSize: '20px', color: '#212529' }">
                {{ theme.name }}
                <span v-if="theme.is_active" :style="{ color: '#28a745', fontSize: '14px', marginLeft: '10px' }">
                  ● Actif
                </span>
              </h3>
              <p :style="{ margin: 0, color: '#6c757d', fontSize: '14px' }">
                Police: {{ theme.font_pack }} • Couleur principale: {{ theme.primary_color }}
              </p>
            </div>
            <button
              @click="editTheme(theme)"
              :style="{
                padding: '8px 16px',
                background: '#007bff',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer',
                fontWeight: '500'
              }"
            >
              Modifier
            </button>
          </div>
        </div>
      </div>

      <!-- Section: Informations générales -->
      <div v-if="activeSection === 'general'">
        <h1 :style="{
          fontSize: '32px',
          marginBottom: '30px',
          color: '#212529'
        }">
          Informations générales
        </h1>

        <div :style="{
          padding: '25px',
          background: '#f8f9fa',
          border: '1px solid #dee2e6',
          borderRadius: '8px',
          marginBottom: '20px'
        }">
          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Nom du thème</label>
            <input
              v-model="currentTheme.name"
              type="text"
              placeholder="Ex: Thème principal"
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
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              cursor: 'pointer',
              fontWeight: '600',
              color: '#495057'
            }">
              <input
                v-model="currentTheme.is_active"
                type="checkbox"
                :style="{ width: '20px', height: '20px', cursor: 'pointer' }"
              />
              <span>Thème actif</span>
            </label>
            <p :style="{ margin: '5px 0 0 28px', fontSize: '14px', color: '#6c757d' }">
              Si activé, ce thème sera appliqué à tout le site
            </p>
          </div>
        </div>
      </div>

      <!-- Section: Polices -->
      <div v-if="activeSection === 'fonts'">
        <h1 :style="{
          fontSize: '32px',
          marginBottom: '30px',
          color: '#212529'
        }">
          Polices
        </h1>

        <div :style="{
          padding: '25px',
          background: '#f8f9fa',
          border: '1px solid #dee2e6',
          borderRadius: '8px',
          marginBottom: '20px'
        }">
          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Pack de polices</label>
            <select
              v-model="currentTheme.font_pack"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            >
              <option value="system">Système</option>
              <option value="google">Google Fonts</option>
              <option value="custom">Personnalisé</option>
            </select>
          </div>

          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Taille de base (px)</label>
            <input
              v-model.number="currentTheme.base_font_size"
              type="number"
              min="12"
              max="24"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Police des titres</label>
            <input
              v-model="currentTheme.heading_font"
              type="text"
              placeholder="Ex: Arial, sans-serif"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Police du corps de texte</label>
            <input
              v-model="currentTheme.body_font"
              type="text"
              placeholder="Ex: Georgia, serif"
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
              fontWeight: '600',
              color: '#495057'
            }">Police des boutons</label>
            <input
              v-model="currentTheme.button_font"
              type="text"
              placeholder="Ex: Arial, sans-serif"
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
      </div>

      <!-- Section: Couleurs -->
      <div v-if="activeSection === 'colors'">
        <h1 :style="{
          fontSize: '32px',
          marginBottom: '30px',
          color: '#212529'
        }">
          Couleurs
        </h1>

        <div :style="{
          padding: '25px',
          background: '#f8f9fa',
          border: '1px solid #dee2e6',
          borderRadius: '8px',
          marginBottom: '20px'
        }">
          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Couleur principale</label>
            <input
              v-model="currentTheme.primary_color"
              type="color"
              :style="{
                width: '100%',
                height: '50px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                cursor: 'pointer'
              }"
            />
            <span :style="{ fontSize: '14px', color: '#6c757d', marginTop: '5px', display: 'block' }">
              {{ currentTheme.primary_color }}
            </span>
          </div>

          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Couleur secondaire</label>
            <input
              v-model="currentTheme.secondary_color"
              type="color"
              :style="{
                width: '100%',
                height: '50px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                cursor: 'pointer'
              }"
            />
            <span :style="{ fontSize: '14px', color: '#6c757d', marginTop: '5px', display: 'block' }">
              {{ currentTheme.secondary_color }}
            </span>
          </div>

          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Couleur d'accent</label>
            <input
              v-model="currentTheme.accent_color"
              type="color"
              :style="{
                width: '100%',
                height: '50px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                cursor: 'pointer'
              }"
            />
            <span :style="{ fontSize: '14px', color: '#6c757d', marginTop: '5px', display: 'block' }">
              {{ currentTheme.accent_color }}
            </span>
          </div>

          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Couleur de fond</label>
            <input
              v-model="currentTheme.background_color"
              type="color"
              :style="{
                width: '100%',
                height: '50px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                cursor: 'pointer'
              }"
            />
            <span :style="{ fontSize: '14px', color: '#6c757d', marginTop: '5px', display: 'block' }">
              {{ currentTheme.background_color }}
            </span>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Couleur du texte</label>
            <input
              v-model="currentTheme.text_color"
              type="color"
              :style="{
                width: '100%',
                height: '50px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                cursor: 'pointer'
              }"
            />
            <span :style="{ fontSize: '14px', color: '#6c757d', marginTop: '5px', display: 'block' }">
              {{ currentTheme.text_color }}
            </span>
          </div>
        </div>
      </div>

      <!-- Section: Boutons -->
      <div v-if="activeSection === 'buttons'">
        <h1 :style="{
          fontSize: '32px',
          marginBottom: '30px',
          color: '#212529'
        }">
          Boutons
        </h1>

        <div :style="{
          padding: '25px',
          background: '#f8f9fa',
          border: '1px solid #dee2e6',
          borderRadius: '8px',
          marginBottom: '20px'
        }">
          <div :style="{ marginBottom: '20px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Rayon des bords (px)</label>
            <input
              v-model.number="currentTheme.button_radius"
              type="number"
              min="0"
              max="50"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
            <p :style="{ margin: '5px 0 0 0', fontSize: '14px', color: '#6c757d' }">
              0 = coins carrés, valeurs plus élevées = coins plus arrondis
            </p>
          </div>

          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Padding (px)</label>
            <input
              v-model.number="currentTheme.button_padding"
              type="number"
              min="5"
              max="30"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
            <p :style="{ margin: '5px 0 0 0', fontSize: '14px', color: '#6c757d' }">
              Espace intérieur du bouton
            </p>
          </div>
        </div>

        <!-- Aperçu du bouton -->
        <div :style="{
          padding: '25px',
          background: '#ffffff',
          border: '1px solid #dee2e6',
          borderRadius: '8px'
        }">
          <h3 :style="{ margin: '0 0 15px 0', fontSize: '18px', color: '#212529' }">Aperçu</h3>
          <button :style="{
            padding: `${currentTheme.button_padding}px ${currentTheme.button_padding * 2}px`,
            background: currentTheme.primary_color,
            color: '#ffffff',
            border: 'none',
            borderRadius: `${currentTheme.button_radius}px`,
            fontFamily: currentTheme.button_font,
            fontSize: '16px',
            cursor: 'pointer',
            fontWeight: '500'
          }">
            Exemple de bouton
          </button>
        </div>
      </div>

      <!-- Section: Espacement -->
      <div v-if="activeSection === 'spacing'">
        <h1 :style="{
          fontSize: '32px',
          marginBottom: '30px',
          color: '#212529'
        }">
          Espacement
        </h1>

        <div :style="{
          padding: '25px',
          background: '#f8f9fa',
          border: '1px solid #dee2e6',
          borderRadius: '8px',
          marginBottom: '20px'
        }">
          <div>
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: '600',
              color: '#495057'
            }">Unité de base (px)</label>
            <input
              v-model.number="currentTheme.spacing_unit"
              type="number"
              min="4"
              max="16"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
            <p :style="{ margin: '5px 0 0 0', fontSize: '14px', color: '#6c757d' }">
              Unité de base utilisée pour tous les espacements du site (marges, paddings)
            </p>
          </div>
        </div>

        <!-- Aperçu -->
        <div :style="{
          padding: '25px',
          background: '#ffffff',
          border: '1px solid #dee2e6',
          borderRadius: '8px'
        }">
          <h3 :style="{ margin: '0 0 15px 0', fontSize: '18px', color: '#212529' }">Aperçu des espacements</h3>
          <div :style="{ display: 'flex', flexDirection: 'column', gap: '10px' }">
            <div :style="{
              padding: `${currentTheme.spacing_unit}px`,
              background: '#e9ecef',
              borderRadius: '4px'
            }">
              1× spacing ({{ currentTheme.spacing_unit }}px)
            </div>
            <div :style="{
              padding: `${currentTheme.spacing_unit * 2}px`,
              background: '#e9ecef',
              borderRadius: '4px'
            }">
              2× spacing ({{ currentTheme.spacing_unit * 2 }}px)
            </div>
            <div :style="{
              padding: `${currentTheme.spacing_unit * 3}px`,
              background: '#e9ecef',
              borderRadius: '4px'
            }">
              3× spacing ({{ currentTheme.spacing_unit * 3 }}px)
            </div>
          </div>
        </div>
      </div>

      <!-- Bouton de sauvegarde (sticky) -->
      <div v-if="activeSection !== 'list'" :style="{
        position: 'sticky',
        bottom: '20px',
        marginTop: '30px',
        padding: '20px',
        background: '#ffffff',
        borderTop: '1px solid #dee2e6',
        borderRadius: '8px',
        boxShadow: '0 -2px 10px rgba(0,0,0,0.1)'
      }">
        <button
          @click="saveTheme"
          :disabled="loading"
          :style="{
            padding: '15px 30px',
            background: loading ? '#6c757d' : '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontWeight: 'bold',
            fontSize: '16px',
            width: '100%'
          }"
        >
          {{ loading ? 'Enregistrement...' : 'Enregistrer le thème' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: 'auth'
})

const sections = ref([
  {
    id: 'list',
    label: 'Liste des thèmes',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M8.25 6.75h12M8.25 12h12m-12 5.25h12M3.75 6.75h.007v.008H3.75V6.75zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zM3.75 12h.007v.008H3.75V12zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm-.375 5.25h.007v.008H3.75v-.008zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" /></svg>'
  },
  {
    id: 'general',
    label: 'Informations',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" /></svg>'
  },
  {
    id: 'fonts',
    label: 'Polices',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" /></svg>'
  },
  {
    id: 'colors',
    label: 'Couleurs',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z" /></svg>'
  },
  {
    id: 'buttons',
    label: 'Boutons',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75a4.5 4.5 0 01-4.884 4.484c-1.076-.091-2.264.071-2.95.904l-7.152 8.684a2.548 2.548 0 11-3.586-3.586l8.684-7.152c.833-.686.995-1.874.904-2.95a4.5 4.5 0 016.336-4.486l-3.276 3.276a3.004 3.004 0 002.25 2.25l3.276-3.276c.256.565.398 1.192.398 1.852z" /></svg>'
  },
  {
    id: 'spacing',
    label: 'Espacement',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 18px; height: 18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>'
  }
])

const activeSection = ref('list')
const themes = ref([])
const currentTheme = ref({
  name: '',
  is_active: false,
  font_pack: 'system',
  base_font_size: 16,
  heading_font: 'Arial, sans-serif',
  body_font: 'Georgia, serif',
  button_font: 'Arial, sans-serif',
  primary_color: '#007bff',
  secondary_color: '#6c757d',
  accent_color: '#28a745',
  background_color: '#ffffff',
  text_color: '#212529',
  button_radius: 4,
  button_padding: 12,
  spacing_unit: 8
})

const loading = ref(false)
const error = ref('')
const success = ref('')

onMounted(async () => {
  const { ensureCsrfToken } = useAuth()
  await ensureCsrfToken()
  await loadThemes()
})

async function loadThemes() {
  try {
    themes.value = await $fetch('http://localhost:8000/api/themes/', {
      credentials: 'include'
    })
  } catch (err) {
    console.error('Erreur lors du chargement des thèmes:', err)
  }
}

function createNewTheme() {
  currentTheme.value = {
    name: '',
    is_active: false,
    font_pack: 'system',
    base_font_size: 16,
    heading_font: 'Arial, sans-serif',
    body_font: 'Georgia, serif',
    button_font: 'Arial, sans-serif',
    primary_color: '#007bff',
    secondary_color: '#6c757d',
    accent_color: '#28a745',
    background_color: '#ffffff',
    text_color: '#212529',
    button_radius: 4,
    button_padding: 12,
    spacing_unit: 8
  }
  activeSection.value = 'general'
}

function editTheme(theme) {
  currentTheme.value = { ...theme }
  activeSection.value = 'general'
}

async function saveTheme() {
  loading.value = true
  error.value = ''
  success.value = ''

  try {
    if (currentTheme.value.id) {
      await $fetch(`http://localhost:8000/api/themes/${currentTheme.value.id}/`, {
        method: 'PUT',
        body: currentTheme.value,
        credentials: 'include'
      })
    } else {
      await $fetch('http://localhost:8000/api/themes/', {
        method: 'POST',
        body: currentTheme.value,
        credentials: 'include'
      })
    }

    success.value = 'Thème enregistré avec succès !'
    await loadThemes()
    
    setTimeout(() => {
      success.value = ''
      activeSection.value = 'list'
    }, 2000)
  } catch (err) {
    error.value = err.data?.detail || 'Erreur lors de l\'enregistrement'
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>
