<template>
  <div>
    <HeaderMain />
    <div style="padding: 20px;">
      <slot />
    </div>
  </div>
</template>

<script setup>
const { checkAuth } = useAuth()
const { fetchHeader } = useWebsite()

onMounted(async () => {
  await checkAuth()
  await fetchHeader()
})
</script>
