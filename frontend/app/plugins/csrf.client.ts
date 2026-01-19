export default defineNuxtPlugin(() => {
  const getCsrfToken = () => {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1]
    return cookieValue || ''
  }

  // Intercepter toutes les requêtes $fetch pour ajouter le CSRF token
  globalThis.$fetch = new Proxy(globalThis.$fetch, {
    apply(target, thisArg, argumentsList) {
      const [url, options = {}] = argumentsList
      
      // Ajouter le CSRF token aux requêtes qui modifient les données
      if (options.method && ['POST', 'PUT', 'PATCH', 'DELETE'].includes(options.method.toUpperCase())) {
        const csrfToken = getCsrfToken()
        
        if (csrfToken) {
          options.headers = {
            ...options.headers,
            'X-CSRFToken': csrfToken
          }
        }
      }
      
      return Reflect.apply(target, thisArg, [url, options])
    }
  })
})
