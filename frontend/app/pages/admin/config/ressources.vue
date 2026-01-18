<template>
  <div :style="{
    display: 'flex',
    minHeight: '100vh',
    background: '#ffffff'
  }">
    <AdminSidebar title="Ressources">
      <button
        @click="uploadFiles"
        :disabled="uploading"
        :style="{
          width: '100%',
          padding: '12px',
          background: uploading ? '#6c757d' : '#007bff',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          fontWeight: 'bold',
          cursor: uploading ? 'not-allowed' : 'pointer',
          fontSize: '16px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '8px',
          marginBottom: '10px'
        }"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
        </svg>
        {{ uploading ? 'Upload en cours...' : 'Upload fichiers' }}
      </button>
      <input 
        ref="fileInput"
        type="file"
        multiple
        accept="image/*,video/*,.pdf,.doc,.docx,.xls,.xlsx"
        @change="handleFileSelect"
        style="display: none;"
      />
      
      <button
        @click="showCreateFolder = !showCreateFolder"
        :style="{
          width: '100%',
          padding: '12px',
          background: '#28a745',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          fontWeight: 'bold',
          cursor: 'pointer',
          fontSize: '16px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '8px'
        }"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 10.5v6m3-3H9m4.06-7.19l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z" />
        </svg>
        Nouveau dossier
      </button>
    </AdminSidebar>

    <div :style="{
      flex: 1,
      padding: '40px'
    }">
      <div :style="{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '30px'
      }">
        <h1 :style="{
          fontSize: '32px',
          fontWeight: 'bold',
          color: '#212529',
          margin: 0
        }">
          Gestion des ressources
        </h1>
        
        <div :style="{
          display: 'flex',
          gap: '10px',
          alignItems: 'center'
        }">
          <BaseSelectInput 
            v-model="viewMode"
            :options="[
              { value: 'grid', label: 'Grille' },
              { value: 'list', label: 'Liste' }
            ]"
            :style="{ width: '120px' }"
          />
          <BaseSelectInput 
            v-model="fileFilter"
            :options="[
              { value: 'all', label: 'Tous' },
              { value: 'images', label: 'Images' },
              { value: 'videos', label: 'Vidéos' },
              { value: 'documents', label: 'Documents' }
            ]"
            :style="{ width: '150px' }"
          />
        </div>
      </div>

      <!-- Breadcrumb navigation -->
      <div :style="{
        marginBottom: '20px',
        padding: '10px',
        background: '#f8f9fa',
        borderRadius: '4px',
        display: 'flex',
        alignItems: 'center',
        gap: '10px'
      }">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 20px; height: 20px;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
        </svg>
        <span @click="currentFolder = ''" :style="{
          cursor: 'pointer',
          color: '#007bff',
          fontWeight: currentFolder === '' ? 'bold' : 'normal'
        }">
          Racine
        </span>
        <template v-if="currentFolder">
          <span>/</span>
          <span :style="{ fontWeight: 'bold' }">{{ currentFolder }}</span>
        </template>
      </div>

      <!-- Create folder form -->
      <div v-if="showCreateFolder" :style="{
        marginBottom: '20px',
        padding: '20px',
        background: '#f8f9fa',
        border: '2px solid #007bff',
        borderRadius: '4px'
      }">
        <h3 :style="{ marginBottom: '15px', fontSize: '18px' }">Créer un nouveau dossier</h3>
        <div :style="{ display: 'flex', gap: '10px' }">
          <input 
            v-model="newFolderName"
            type="text"
            placeholder="Nom du dossier"
            :style="{
              flex: 1,
              padding: '10px',
              border: '1px solid #ced4da',
              borderRadius: '4px',
              fontSize: '16px'
            }"
            @keyup.enter="createFolder"
          />
          <button
            @click="createFolder"
            :style="{
              padding: '10px 20px',
              background: '#28a745',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 'bold'
            }"
          >
            Créer
          </button>
          <button
            @click="showCreateFolder = false"
            :style="{
              padding: '10px 20px',
              background: '#6c757d',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 'bold'
            }"
          >
            Annuler
          </button>
        </div>
      </div>

      <!-- Messages -->
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

      <!-- Folders -->
      <div v-if="folders.length > 0" :style="{ marginBottom: '30px' }">
        <h2 :style="{
          fontSize: '20px',
          fontWeight: 'bold',
          marginBottom: '15px',
          color: '#495057',
          display: 'flex',
          alignItems: 'center',
          gap: '10px'
        }">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 24px; height: 24px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.75V12A2.25 2.25 0 014.5 9.75h15A2.25 2.25 0 0121.75 12v.75m-8.69-6.44l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z" />
          </svg>
          Dossiers
        </h2>
        <div :style="{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(150px, 1fr))',
          gap: '15px'
        }">
          <div 
            v-for="folder in folders" 
            :key="folder.id"
            @click="currentFolder = folder.name"
            :style="{
              padding: '20px',
              background: '#fff3cd',
              border: '2px solid #ffc107',
              borderRadius: '8px',
              cursor: 'pointer',
              textAlign: 'center',
              transition: 'transform 0.2s',
              ':hover': {
                transform: 'scale(1.05)'
              }
            }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 48px; height: 48px; margin: 0 auto 10px; color: #ffc107;">
              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.75V12A2.25 2.25 0 014.5 9.75h15A2.25 2.25 0 0121.75 12v.75m-8.69-6.44l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z" />
            </svg>
            <div :style="{ fontWeight: 'bold', color: '#856404' }">
              {{ folder.name }}
            </div>
          </div>
        </div>
      </div>

      <!-- Files Grid View -->
      <div v-if="viewMode === 'grid'">
        <h2 :style="{
          fontSize: '20px',
          fontWeight: 'bold',
          marginBottom: '15px',
          color: '#495057',
          display: 'flex',
          alignItems: 'center',
          gap: '10px'
        }">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 24px; height: 24px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
          </svg>
          Fichiers ({{ filteredFiles.length }})
        </h2>
        <div :style="{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
          gap: '20px'
        }">
          <div 
            v-for="file in filteredFiles" 
            :key="file.id"
            :style="{
              border: '1px solid #dee2e6',
              borderRadius: '8px',
              overflow: 'hidden',
              background: 'white',
              transition: 'box-shadow 0.2s',
              cursor: 'pointer'
            }"
            @click="selectFile(file)"
          >
            <!-- File preview -->
            <div :style="{
              height: '150px',
              background: '#f8f9fa',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              overflow: 'hidden'
            }">
              <img 
                v-if="file.type === 'image'" 
                :src="file.url" 
                :alt="file.name"
                :style="{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  cursor: 'pointer'
                }"
                @click.stop="showImagePreview(file)"
              />
              <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 64px; height: 64px; color: #6c757d;">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
              </svg>
            </div>
            
            <!-- File info -->
            <div :style="{ padding: '10px' }">
              <div 
                v-if="!file.isRenaming"
                @dblclick="startRename(file)"
                :style="{
                  fontSize: '14px',
                  fontWeight: 'bold',
                  marginBottom: '5px',
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  whiteSpace: 'nowrap',
                  cursor: 'pointer'
                }"
                :title="'Double-cliquez pour renommer'"
              >
                {{ file.name }}
              </div>
              <div 
                v-else
                :style="{
                  marginBottom: '5px',
                  display: 'flex',
                  gap: '5px'
                }"
              >
                <input
                  v-model="file.newName"
                  @keyup.enter="saveRename(file)"
                  @keyup.esc="cancelRename(file)"
                  @blur="saveRename(file)"
                  :style="{
                    flex: 1,
                    fontSize: '14px',
                    fontWeight: 'bold',
                    padding: '2px 5px',
                    border: '1px solid #007bff',
                    borderRadius: '4px',
                    outline: 'none'
                  }"
                />
              </div>
              <div :style="{
                fontSize: '12px',
                color: '#6c757d',
                marginBottom: '10px'
              }">
                {{ formatFileSize(file.size) }} • {{ file.uploaded_at }}
              </div>
              <div :style="{
                display: 'flex',
                gap: '5px'
              }">
                <button
                  @click.stop="copyUrl(file.url)"
                  :style="{
                    flex: 1,
                    padding: '6px',
                    background: '#007bff',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    fontSize: '12px',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '5px'
                  }"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 14px; height: 14px;">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.666 3.888A2.25 2.25 0 0013.5 2.25h-3c-1.03 0-1.9.693-2.166 1.638m7.332 0c.055.194.084.4.084.612v0a.75.75 0 01-.75.75H9a.75.75 0 01-.75-.75v0c0-.212.03-.418.084-.612m7.332 0c.646.049 1.288.11 1.927.184 1.1.128 1.907 1.077 1.907 2.185V19.5a2.25 2.25 0 01-2.25 2.25H6.75A2.25 2.25 0 014.5 19.5V6.257c0-1.108.806-2.057 1.907-2.185a48.208 48.208 0 011.927-.184" />
                  </svg>
                  Copier le lien
                </button>
                <button
                  @click.stop="deleteFile(file.id)"
                  :style="{
                    padding: '6px 10px',
                    background: '#dc3545',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    fontSize: '12px',
                    cursor: 'pointer'
                  }"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 14px; height: 14px;">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Files List View -->
      <div v-else>
        <h2 :style="{
          fontSize: '20px',
          fontWeight: 'bold',
          marginBottom: '15px',
          color: '#495057'
        }">
          Fichiers ({{ filteredFiles.length }})
        </h2>
        <div :style="{
          background: 'white',
          border: '1px solid #dee2e6',
          borderRadius: '8px',
          overflow: 'hidden'
        }">
          <div 
            v-for="file in filteredFiles" 
            :key="file.id"
            :style="{
              display: 'flex',
              alignItems: 'center',
              padding: '15px',
              borderBottom: '1px solid #dee2e6',
              transition: 'background 0.2s',
              cursor: 'pointer'
            }"
            @click="selectFile(file)"
          >
            <div :style="{ width: '50px', marginRight: '15px' }">
              <img 
                v-if="file.type === 'image'" 
                :src="file.url" 
                :alt="file.name"
                :style="{
                  width: '40px',
                  height: '40px',
                  objectFit: 'cover',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
                @click.stop="showImagePreview(file)"
              />
              <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 40px; height: 40px; color: #6c757d;">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
              </svg>
            </div>
            <div :style="{ flex: 1 }">
              <div 
                v-if="!file.isRenaming"
                @dblclick="startRename(file)"
                :style="{ 
                  fontWeight: 'bold', 
                  marginBottom: '3px',
                  cursor: 'pointer'
                }"
                :title="'Double-cliquez pour renommer'"
              >
                {{ file.name }}
              </div>
              <div 
                v-else
                :style="{
                  marginBottom: '3px',
                  display: 'flex',
                  gap: '5px'
                }"
              >
                <input
                  v-model="file.newName"
                  @keyup.enter="saveRename(file)"
                  @keyup.esc="cancelRename(file)"
                  @blur="saveRename(file)"
                  :style="{
                    flex: 1,
                    fontSize: '14px',
                    fontWeight: 'bold',
                    padding: '2px 5px',
                    border: '1px solid #007bff',
                    borderRadius: '4px',
                    outline: 'none'
                  }"
                />
              </div>
              <div :style="{ fontSize: '12px', color: '#6c757d' }">
                {{ formatFileSize(file.size) }} • {{ file.uploaded_at }}
              </div>
            </div>
            <div :style="{ display: 'flex', gap: '10px' }">
              <button
                @click.stop="copyUrl(file.url)"
                :style="{
                  padding: '8px 16px',
                  background: '#007bff',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
              >
                Copier le lien
              </button>
              <button
                @click.stop="deleteFile(file.id)"
                :style="{
                  padding: '8px 16px',
                  background: '#dc3545',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }"
              >
                Supprimer
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty state -->
      <div v-if="filteredFiles.length === 0 && folders.length === 0" :style="{
        padding: '60px 40px',
        background: '#f8f9fa',
        border: '2px dashed #dee2e6',
        borderRadius: '8px',
        textAlign: 'center'
      }">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 64px; height: 64px; margin: 0 auto 20px; color: #6c757d;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
        </svg>
        <h3 :style="{
          fontSize: '24px',
          fontWeight: 'bold',
          marginBottom: '10px',
          color: '#495057'
        }">
          Aucun fichier
        </h3>
        <p :style="{ color: '#6c757d', marginBottom: '20px' }">
          Commencez par uploader des fichiers ou créer un dossier
        </p>
        <button
          @click="uploadFiles"
          :style="{
            padding: '12px 24px',
            background: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontWeight: 'bold',
            fontSize: '16px'
          }"
        >
          Upload des fichiers
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: 'auth'
})

const fileInput = ref(null)
const uploading = ref(false)
const error = ref('')
const success = ref('')
const viewMode = ref('grid')
const fileFilter = ref('all')
const currentFolder = ref('')
const showCreateFolder = ref(false)
const newFolderName = ref('')

// Mock data - TODO: remplacer par de vraies données depuis l'API
const folders = ref([
  { id: 1, name: 'Images', count: 12 },
  { id: 2, name: 'Vidéos', count: 3 },
  { id: 3, name: 'Documents', count: 8 }
])

const files = ref([
  {
    id: 1,
    name: 'banner.jpg',
    url: 'http://localhost:8000/media/uploads/banner.jpg',
    type: 'image',
    size: 245678,
    uploaded_at: '2024-01-15',
    folder: ''
  },
  {
    id: 2,
    name: 'logo.png',
    url: 'http://localhost:8000/media/uploads/logo.png',
    type: 'image',
    size: 45678,
    uploaded_at: '2024-01-14',
    folder: ''
  }
])

const filteredFiles = computed(() => {
  let result = files.value.filter(f => f.folder === currentFolder.value)
  
  if (fileFilter.value === 'images') {
    result = result.filter(f => f.type === 'image')
  } else if (fileFilter.value === 'videos') {
    result = result.filter(f => f.type === 'video')
  } else if (fileFilter.value === 'documents') {
    result = result.filter(f => f.type === 'document')
  }
  
  return result
})

function uploadFiles() {
  fileInput.value?.click()
}

async function handleFileSelect(event) {
  const selectedFiles = Array.from(event.target.files)
  if (selectedFiles.length === 0) return

  uploading.value = true
  error.value = ''
  success.value = ''

  try {
    for (const file of selectedFiles) {
      const formData = new FormData()
      formData.append('file', file)

      const response = await $fetch('http://localhost:8000/api/upload/', {
        method: 'POST',
        body: formData,
        credentials: 'include'
      })

      // Ajouter le fichier à la liste
      const fileType = file.type.startsWith('image/') ? 'image' : 
                       file.type.startsWith('video/') ? 'video' : 'document'
      
      files.value.push({
        id: Date.now() + Math.random(),
        name: file.name,
        url: 'http://localhost:8000' + response.url,
        type: fileType,
        size: file.size,
        uploaded_at: new Date().toISOString().split('T')[0],
        folder: currentFolder.value
      })
    }

    success.value = `${selectedFiles.length} fichier(s) uploadé(s) avec succès !`
    setTimeout(() => {
      success.value = ''
    }, 3000)
  } catch (err) {
    error.value = 'Erreur lors de l\'upload des fichiers'
    console.error(err)
  } finally {
    uploading.value = false
    event.target.value = ''
  }
}

function createFolder() {
  if (!newFolderName.value.trim()) return
  
  folders.value.push({
    id: Date.now(),
    name: newFolderName.value,
    count: 0
  })
  
  success.value = `Dossier "${newFolderName.value}" créé avec succès !`
  newFolderName.value = ''
  showCreateFolder.value = false
  
  setTimeout(() => {
    success.value = ''
  }, 3000)
}

function selectFile(file) {
  // TODO: Afficher un modal avec les détails du fichier
  console.log('File selected:', file)
}

function startRename(file) {
  file.isRenaming = true
  file.newName = file.name
}

function cancelRename(file) {
  file.isRenaming = false
  file.newName = ''
}

async function saveRename(file) {
  if (!file.newName || file.newName === file.name) {
    file.isRenaming = false
    return
  }
  
  // TODO: Appel API pour renommer
  file.name = file.newName
  file.isRenaming = false
  success.value = 'Fichier renommé avec succès !'
  setTimeout(() => {
    success.value = ''
  }, 2000)
}

function showImagePreview(file) {
  // Ouvrir l'image dans un nouvel onglet
  window.open(file.url, '_blank')
}

async function copyUrl(url) {
  try {
    await navigator.clipboard.writeText(url)
    success.value = 'URL copiée dans le presse-papier !'
    setTimeout(() => {
      success.value = ''
    }, 2000)
  } catch (err) {
    error.value = 'Erreur lors de la copie'
  }
}

function deleteFile(fileId) {
  if (confirm('Êtes-vous sûr de vouloir supprimer ce fichier ?')) {
    files.value = files.value.filter(f => f.id !== fileId)
    success.value = 'Fichier supprimé avec succès !'
    setTimeout(() => {
      success.value = ''
    }, 3000)
  }
}

function formatFileSize(bytes) {
  if (bytes === 0) return '0 B'
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i]
}

onMounted(async () => {
  const { ensureCsrfToken } = useAuth()
  await ensureCsrfToken()
  
  // TODO: Charger les fichiers et dossiers depuis l'API
})
</script>
