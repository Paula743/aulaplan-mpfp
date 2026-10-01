export function useApi() {
  const config = useRuntimeConfig()
  const { $firebaseAuth } = useNuxtApp()

  async function request<T>(path: string, options: Record<string, unknown> = {}) {
    const user = $firebaseAuth.currentUser
    const token = user ? await user.getIdToken() : null
    const headers = new Headers((options.headers as HeadersInit | undefined) || {})

    if (token) headers.set('Authorization', `Bearer ${token}`)
    headers.set('Content-Type', 'application/json')

    return await $fetch<T>(path, {
      baseURL: config.public.apiBase,
      ...options,
      headers,
    })
  }

  return { request }
}