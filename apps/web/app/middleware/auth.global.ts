export default defineNuxtRouteMiddleware(async (to) => {
  if (import.meta.server) return

  const store = useAuthStore()
  const publicRoutes = ['/login']

  if (!store.ready) return

  if (!store.isAuthenticated && !publicRoutes.includes(to.path)) {
    return navigateTo('/login')
  }

  if (store.isAuthenticated && to.path === '/login') {
    return navigateTo('/dashboard')
  }
})