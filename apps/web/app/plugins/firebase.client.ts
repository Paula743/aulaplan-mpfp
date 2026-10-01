import { initializeApp, getApps } from 'firebase/app'
import {
  connectAuthEmulator,
  getAuth,
  onAuthStateChanged,
} from 'firebase/auth'

export default defineNuxtPlugin(async () => {
  const config = useRuntimeConfig()

  const firebaseConfig = {
    apiKey: config.public.firebaseApiKey,
    authDomain: config.public.firebaseAuthDomain,
    projectId: config.public.firebaseProjectId,
    storageBucket: config.public.firebaseStorageBucket,
    messagingSenderId: config.public.firebaseMessagingSenderId,
    appId: config.public.firebaseAppId,
  }

  const app = getApps()[0] || initializeApp(firebaseConfig)
  const auth = getAuth(app)

  if (config.public.useFirebaseEmulators) {
    try {
      connectAuthEmulator(auth, 'http://127.0.0.1:9099', {
        disableWarnings: true,
      })
    } catch {
      // El plugin se carga una vez; este catch evita fallar durante HMR.
    }
  }

  const authStore = useAuthStore()

  await new Promise<void>((resolve) => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      authStore.setFirebaseUser(user)
      authStore.setReady(true)
      unsubscribe()
      resolve()
    })
  })

  return {
    provide: {
      firebaseAuth: auth,
    },
  }
})