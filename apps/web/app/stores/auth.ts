import type { User } from 'firebase/auth'
import type { UserProfile } from '~/types'

export const useAuthStore = defineStore('auth', () => {
  const firebaseUser = shallowRef<User | null>(null)
  const profile = ref<UserProfile | null>(null)
  const ready = ref(false)

  const isAuthenticated = computed(() => Boolean(firebaseUser.value))
  const role = computed(() => profile.value?.role ?? null)

  function setFirebaseUser(user: User | null) {
    firebaseUser.value = user
    if (!user) profile.value = null
  }

  function setProfile(value: UserProfile | null) {
    profile.value = value
  }

  function setReady(value: boolean) {
    ready.value = value
  }

  return {
    firebaseUser,
    profile,
    ready,
    isAuthenticated,
    role,
    setFirebaseUser,
    setProfile,
    setReady,
  }
})