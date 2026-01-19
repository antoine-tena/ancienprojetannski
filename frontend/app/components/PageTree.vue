<template>
  <div>
    <ul style="list-style: none; padding-left: 0;">
      <li v-for="page in pages" :key="page.id" style="margin-bottom: 10px;">
        <div style="padding: 10px; background: #fff; border: 1px solid #ddd; border-radius: 4px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
              <strong>{{ page.title }}</strong>
              <span style="color: #666; margin-left: 10px; font-size: 12px;">{{ page.slug }}</span>
              <span v-if="!page.is_visible" style="color: #dc3545; margin-left: 10px; font-size: 12px;">(Caché)</span>
            </div>
            <div style="color: #666; font-size: 12px;">
              {{ page.full_path }}
            </div>
          </div>
          
          <!-- Sous-pages récursives -->
          <div v-if="page.children && page.children.length > 0" style="margin-top: 10px; padding-left: 20px; border-left: 2px solid #ddd;">
            <PageTree :pages="page.children" />
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  pages: {
    type: Array,
    default: () => []
  }
})
</script>
