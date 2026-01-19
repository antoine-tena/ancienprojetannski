<template>
  <div>
    <BaseHeaderMain />
    <div :style="{
      padding: '20px',
      paddingTop: headerConfig?.is_fixed ? `${(headerConfig?.height || 70) + 20}px` : '20px'
    }">
      <slot />
    </div>
    <BaseFooterMain />
  </div>
</template>

<script setup>
const { checkAuth } = useAuth()
const { fetchHeader, headerConfig } = useWebsite()

onMounted(async () => {
  await checkAuth()
  await fetchHeader()
})
</script>
