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
          Header
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
      <h1 :style="{
        fontSize: '32px',
        fontWeight: 'bold',
        marginBottom: '10px',
        color: '#212529'
      }">
        {{ sections.find(s => s.id === activeSection)?.label }}
      </h1>
      <p :style="{
        color: '#6c757d',
        marginBottom: '30px',
        fontSize: '15px'
      }">
        {{ sections.find(s => s.id === activeSection)?.description }}
      </p>

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

      <!-- Section Couleurs -->
      <div v-if="activeSection === 'colors'" :style="{ marginBottom: '30px' }">
        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Couleur de fond
          </label>
          <input 
            v-model="form.background_color"
            type="color"
            :style="{
              width: '100%',
              height: '50px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              cursor: 'pointer'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Couleur du texte
          </label>
          <input 
            v-model="form.text_color"
            type="color"
            :style="{
              width: '100%',
              height: '50px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              cursor: 'pointer'
            }"
          />
        </div>
      </div>

      <!-- Section Police -->
      <div v-if="activeSection === 'font'">
        <FontSelector 
          v-model="form.font_family"
          label="Police de caractères"
        />
      </div>

      <!-- Section Logo -->
      <div v-if="activeSection === 'logo'">
        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Image du logo
          </label>
          
          <!-- Input file caché -->
          <input 
            ref="logoInput"
            type="file"
            accept="image/*"
            @change="uploadLogo"
            style="display: none;"
          />
          
          <!-- Bouton custom -->
          <button
            @click="$refs.logoInput.click()"
            :disabled="uploadingLogo"
            :style="{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              padding: '12px 20px',
              background: uploadingLogo ? '#6c757d' : '#007bff',
              color: 'white',
              border: '2px dashed #0056b3',
              borderRadius: '8px',
              cursor: uploadingLogo ? 'not-allowed' : 'pointer',
              fontSize: '16px',
              fontWeight: '500',
              transition: 'all 0.2s',
              width: '100%',
              justifyContent: 'center'
            }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 24px; height: 24px;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
            </svg>
            <span>{{ uploadingLogo ? 'Upload en cours...' : 'Choisir une image' }}</span>
          </button>
          
          <div v-if="form.logo_image" :style="{
            marginTop: '15px',
            padding: '15px',
            background: '#f8f9fa',
            borderRadius: '8px',
            border: '1px solid #dee2e6'
          }">
            <p :style="{ marginBottom: '10px', fontSize: '14px', color: '#6c757d' }">Aperçu :</p>
            <img 
              :src="form.logo_image" 
              alt="Logo" 
              :style="{ 
                maxHeight: '80px',
                maxWidth: '100%',
                objectFit: 'contain'
              }" 
            />
          </div>
        </div>

        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Taille du logo : {{ form.logo_size }}px
          </label>
          <input 
            v-model.number="form.logo_size"
            type="range"
            min="20"
            max="100"
            step="1"
            @input="updateLogoSize"
            :style="{
              width: '100%',
              height: '8px',
              borderRadius: '4px',
              cursor: 'pointer'
            }"
          />
          <div :style="{
            display: 'flex',
            justifyContent: 'space-between',
            marginTop: '5px',
            fontSize: '12px',
            color: '#6c757d'
          }">
            <span>20px</span>
            <span>100px</span>
          </div>
        </div>

        <div>
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Position du logo
          </label>
          <BaseSelectInput 
            v-model="form.logo_position"
            :options="[
              { value: 'left', label: 'Gauche' },
              { value: 'center', label: 'Centre' },
              { value: 'right', label: 'Droite' }
            ]"
          />
        </div>
      </div>

      <!-- Section Bouton Connexion -->
      <div v-if="activeSection === 'login'">
        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            <input 
              v-model="form.show_login_button"
              type="checkbox"
              :style="{ marginRight: '8px' }"
            />
            Afficher le bouton connexion
          </label>
        </div>

        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Couleur du bouton
          </label>
          <input 
            v-model="form.login_button_color"
            type="color"
            :style="{
              width: '100%',
              height: '50px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              cursor: 'pointer'
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
            Position du bouton
          </label>
          <BaseSelectInput 
            v-model="form.login_button_position"
            :options="[
              { value: 'left', label: 'Gauche' },
              { value: 'center', label: 'Centre' },
              { value: 'right', label: 'Droite' }
            ]"
          />
        </div>
      </div>

      <!-- Section Mon Compte -->
      <div v-if="activeSection === 'account'">
        <div :style="{ marginBottom: '20px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Couleur du bouton
          </label>
          <input 
            v-model="form.logout_button_color"
            type="color"
            :style="{
              width: '100%',
              height: '50px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              cursor: 'pointer'
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
            Position du bouton
          </label>
          <BaseSelectInput 
            v-model="form.logout_button_position"
            :options="[
              { value: 'left', label: 'Gauche' },
              { value: 'center', label: 'Centre' },
              { value: 'right', label: 'Droite' }
            ]"
          />
        </div>
      </div>

      <!-- Section Boutons de navigation -->
      <div v-if="activeSection === 'buttons'">
        <div :style="{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '20px'
        }">
          <button
            @click="addButton"
            :style="{
              padding: '10px 20px',
              background: '#007bff',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 'bold',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
            </svg>
            <span>Ajouter un bouton</span>
          </button>
        </div>

        <div 
          v-for="(button, index) in buttons" 
          :key="index"
          :style="{
            padding: '20px',
            background: '#f8f9fa',
            border: '1px solid #dee2e6',
            borderRadius: '8px',
            marginBottom: '15px'
          }"
        >
          <div :style="{ marginBottom: '15px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              Texte du bouton
            </label>
            <input 
              v-model="button.text"
              type="text"
              placeholder="Mon bouton"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div :style="{ marginBottom: '15px' }">
            <label :style="{
              display: 'block',
              marginBottom: '8px',
              fontWeight: 'bold',
              color: '#495057'
            }">
              URL
            </label>
            <input 
              v-model="button.url"
              type="text"
              placeholder="/ma-page"
              :style="{
                width: '100%',
                padding: '10px',
                border: '1px solid #ced4da',
                borderRadius: '4px',
                fontSize: '16px'
              }"
            />
          </div>

          <div :style="{ display: 'grid', gridTemplateColumns: '1fr 1fr 100px', gap: '10px', marginBottom: '15px' }">
            <div>
              <label :style="{
                display: 'block',
                marginBottom: '8px',
                fontSize: '14px',
                color: '#495057'
              }">
                Position
              </label>
              <BaseSelectInput 
                v-model="button.position"
                :options="[
                  { value: 'left', label: 'Gauche' },
                  { value: 'center', label: 'Centre' },
                  { value: 'right', label: 'Droite' }
                ]"
              />
            </div>
            
            <div>
              <label :style="{
                display: 'block',
                marginBottom: '8px',
                fontSize: '14px',
                color: '#495057'
              }">
                Ordre
              </label>
              <input 
                v-model.number="button.order"
                type="number"
                min="0"
                :style="{
                  width: '100%',
                  padding: '10px',
                  border: '1px solid #ced4da',
                  borderRadius: '4px',
                  fontSize: '16px'
                }"
              />
            </div>

            <div :style="{ display: 'flex', alignItems: 'flex-end' }">
              <button
                @click="removeButton(index)"
                :style="{
                  width: '100%',
                  padding: '10px',
                  background: '#dc3545',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }"
              >
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <p v-if="buttons.length === 0" :style="{
          color: '#6c757d',
          fontStyle: 'italic',
          textAlign: 'center',
          padding: '40px 20px',
          background: '#f8f9fa',
          borderRadius: '8px',
          border: '2px dashed #dee2e6'
        }">
          Aucun bouton. Cliquez sur "Ajouter un bouton" pour commencer.
        </p>
      </div>

      <!-- Section Options avancées -->
      <div v-if="activeSection === 'advanced'">
        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            <input 
              v-model="form.is_fixed"
              type="checkbox"
              :style="{ marginRight: '8px' }"
            />
            Header fixe (reste visible en haut lors du scroll)
          </label>
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Opacité : {{ form.opacity }}
          </label>
          <input 
            v-model.number="form.opacity"
            type="range"
            min="0"
            max="1"
            step="0.1"
            :style="{
              width: '100%'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Flou (backdrop-filter) : {{ form.blur }}px
          </label>
          <input 
            v-model.number="form.blur"
            type="range"
            min="0"
            max="20"
            step="1"
            :style="{
              width: '100%'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Hauteur : {{ form.height }}px
          </label>
          <input 
            v-model.number="form.height"
            type="range"
            min="50"
            max="150"
            step="5"
            :style="{
              width: '100%'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Padding vertical : {{ form.padding_vertical }}px
          </label>
          <input 
            v-model.number="form.padding_vertical"
            type="range"
            min="0"
            max="50"
            step="5"
            :style="{
              width: '100%'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Padding horizontal : {{ form.padding_horizontal }}px
          </label>
          <input 
            v-model.number="form.padding_horizontal"
            type="range"
            min="0"
            max="100"
            step="5"
            :style="{
              width: '100%'
            }"
          />
        </div>
      </div>

      <!-- Section Bordures & Ombres -->
      <div v-if="activeSection === 'borders'">
        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Largeur de la bordure : {{ form.border_width }}px
          </label>
          <input 
            v-model.number="form.border_width"
            type="range"
            min="0"
            max="10"
            step="1"
            :style="{
              width: '100%'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Couleur de la bordure
          </label>
          <input 
            v-model="form.border_color"
            type="color"
            :style="{
              width: '100%',
              height: '50px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              cursor: 'pointer'
            }"
          />
        </div>

        <div :style="{ marginBottom: '25px' }">
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Ombre CSS (box-shadow)
          </label>
          <input 
            v-model="form.shadow"
            type="text"
            placeholder="0 2px 4px rgba(0,0,0,0.1)"
            :style="{
              width: '100%',
              padding: '10px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              fontSize: '16px'
            }"
          />
          <small :style="{ color: '#6c757d', fontSize: '12px', marginTop: '5px', display: 'block' }">
            Exemple: 0 4px 6px rgba(0,0,0,0.2)
          </small>
        </div>
      </div>

      <!-- Section Pages d'exclusion -->
      <div v-if="activeSection === 'exclusions'">
        <div>
          <label :style="{
            display: 'block',
            marginBottom: '8px',
            fontWeight: 'bold',
            color: '#495057'
          }">
            Pages où ne pas afficher le header
          </label>
          <textarea 
            v-model="form.exclude_pages"
            placeholder="/page1&#10;/page2&#10;/admin/config"
            :style="{
              width: '100%',
              padding: '10px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              fontSize: '16px',
              minHeight: '150px',
              resize: 'vertical',
              fontFamily: 'monospace'
            }"
          />
          <small :style="{ color: '#6c757d', fontSize: '12px', marginTop: '5px', display: 'block' }">
            Une URL par ligne. Exemple: /login, /admin/config/pages
          </small>
        </div>
      </div>

      <!-- Bouton enregistrer en bas -->
      <div :style="{ marginTop: '40px', paddingTop: '20px', borderTop: '2px solid #dee2e6' }">
        <button
          @click="saveHeader"
          :disabled="loading"
          :style="{
            width: '100%',
            padding: '15px',
            background: loading ? '#6c757d' : '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            fontWeight: 'bold',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontSize: '18px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '10px',
            transition: 'background 0.2s'
          }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 24px; height: 24px;">
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

const { user, logout } = useAuth()

const sections = [
  {
    id: 'colors',
    label: 'Couleurs',
    description: 'Personnalisez les couleurs du header',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z" /></svg>'
  },
  {
    id: 'font',
    label: 'Police',
    description: 'Choisissez la police de caractères',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" /></svg>'
  },
  {
    id: 'logo',
    label: 'Logo',
    description: 'Configurez le logo du site',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" /></svg>'
  },
  {
    id: 'login',
    label: 'Bouton Connexion',
    description: 'Paramètres du bouton de connexion',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" /></svg>'
  },
  {
    id: 'account',
    label: 'Bouton Mon Compte',
    description: 'Paramètres du bouton Mon Compte',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" /></svg>'
  },
  {
    id: 'buttons',
    label: 'Boutons navigation',
    description: 'Gérez les boutons de navigation',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" /></svg>'
  },
  {
    id: 'advanced',
    label: 'Options avancées',
    description: 'Position, opacité, flou, dimensions',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" /></svg>'
  },
  {
    id: 'borders',
    label: 'Bordures & Ombres',
    description: 'Bordures et effets d\'ombre',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 8.25V6a2.25 2.25 0 00-2.25-2.25H6A2.25 2.25 0 003.75 6v8.25A2.25 2.25 0 006 16.5h2.25m8.25-8.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-7.5A2.25 2.25 0 018.25 18v-1.5m8.25-8.25h-6a2.25 2.25 0 00-2.25 2.25v6" /></svg>'
  },
  {
    id: 'exclusions',
    label: 'Pages d\'exclusion',
    description: 'Pages où le header ne s\'affiche pas',
    icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;"><path stroke-linecap="round" stroke-linejoin="round" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" /></svg>'
  }
]

const activeSection = ref('colors')

const form = ref({
  background_color: '#ffffff',
  text_color: '#000000',
  font_family: 'Arial, sans-serif',
  logo_image: '',
  logo_size: 40,
  logo_position: 'left',
  show_login_button: true,
  login_button_color: '#007bff',
  login_button_position: 'right',
  logout_button_color: '#dc3545',
  logout_button_position: 'right',
  is_fixed: false,
  opacity: 1.0,
  blur: 0,
  border_width: 0,
  border_color: '#000000',
  height: 70,
  padding_vertical: 15,
  padding_horizontal: 20,
  shadow: '0 2px 4px rgba(0,0,0,0.1)',
  exclude_pages: ''
})

const buttons = ref([])
const loading = ref(false)
const uploadingLogo = ref(false)
const error = ref('')
const success = ref('')
const headerId = ref(null)

onMounted(async () => {
  const { ensureCsrfToken } = useAuth()
  await ensureCsrfToken()
  
  try {
    const data = await $fetch('http://localhost:8000/api/header/', {
      credentials: 'include'
    })
    if (data && data.length > 0) {
      const header = data[0]
      headerId.value = header.id
      form.value = {
        background_color: header.background_color,
        text_color: header.text_color,
        font_family: header.font_family,
        logo_image: header.logo_image || '',
        logo_size: header.logo_size || 40,
        logo_position: header.logo_position || 'left',
        show_login_button: header.show_login_button !== false,
        login_button_color: header.login_button_color || '#007bff',
        login_button_position: header.login_button_position || 'right',
        logout_button_color: header.logout_button_color || '#dc3545',
        logout_button_position: header.logout_button_position || 'right',
        is_fixed: header.is_fixed || false,
        opacity: header.opacity !== undefined ? header.opacity : 1.0,
        blur: header.blur || 0,
        border_width: header.border_width || 0,
        border_color: header.border_color || '#000000',
        height: header.height || 70,
        padding_vertical: header.padding_vertical !== undefined ? header.padding_vertical : 15,
        padding_horizontal: header.padding_horizontal !== undefined ? header.padding_horizontal : 20,
        shadow: header.shadow || '0 2px 4px rgba(0,0,0,0.1)',
        exclude_pages: header.exclude_pages || ''
      }
      buttons.value = header.buttons.map(b => ({
        id: b.id,
        text: b.text || b.label,
        url: b.url,
        order: b.order,
        position: b.position || 'left'
      }))
    }
  } catch (err) {
    error.value = 'Erreur lors du chargement des données'
    console.error(err)
  }
})

function addButton() {
  const maxOrder = buttons.value.length > 0 
    ? Math.max(...buttons.value.map(b => b.order)) 
    : 0
  buttons.value.push({
    text: '',
    url: '',
    order: maxOrder + 1,
    position: 'left'
  })
}

function removeButton(index) {
  buttons.value.splice(index, 1)
}

async function uploadLogo(event) {
  const file = event.target.files[0]
  if (!file) return

  uploadingLogo.value = true
  error.value = ''

  try {
    const formData = new FormData()
    formData.append('file', file)

    const response = await $fetch('http://localhost:8000/api/upload/', {
      method: 'POST',
      body: formData,
      credentials: 'include'
    })

    form.value.logo_image = 'http://localhost:8000' + response.url
    success.value = 'Logo uploadé avec succès !'
    setTimeout(() => { success.value = '' }, 2000)
  } catch (err) {
    error.value = 'Erreur lors du téléchargement de l\'image'
    console.error(err)
  } finally {
    uploadingLogo.value = false
  }
}

function updateLogoSize() {
  // Force update to trigger reactivity
}

async function saveHeader() {
  loading.value = true
  error.value = ''
  success.value = ''

  try {
    const payload = {
      ...form.value,
      buttons: buttons.value
    }

    await $fetch(`http://localhost:8000/api/header/${headerId.value}/save_with_buttons/`, {
      method: 'POST',
      body: payload,
      credentials: 'include'
    })

    success.value = 'Header enregistré avec succès !'
    
    // Rafraîchir le header sans recharger la page
    const { fetchHeader } = useWebsite()
    await fetchHeader()
    
    // Masquer le message après 3 secondes
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
