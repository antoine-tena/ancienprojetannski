<template>
  <div>
    <h1>Test Composables</h1>
    <pre>{{ testData }}</pre>
  </div>
</template>

<script setup>
const testData = ref({
  message: 'Test page',
  hasUseAuth: typeof useAuth !== 'undefined',
  hasUseWebsite: typeof useWebsite !== 'undefined'
})

try {
  const { isAuthenticated } = useAuth()
  testData.value.authWorks = true
  testData.value.isAuthenticated = isAuthenticated.value
} catch (e) {
  testData.value.authError = e.message
}

try {
  const { headerConfig } = useWebsite()
  testData.value.websiteWorks = true  
  testData.value.headerConfig = headerConfig.value
} catch (e) {
  testData.value.websiteError = e.message
}
</script>
