<script setup lang="ts">
definePageMeta({ layout: 'auth' })
const email = ref('')
const password = ref('')
const loading = ref(false)
const errorMessage = ref('')
const { login } = useAuth()

async function submit() {
  loading.value = true
  errorMessage.value = ''
  try {
    await login(email.value, password.value)
    await navigateTo('/dashboard')
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'No fue posible iniciar sesión.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <form class="card border border-base-300 bg-base-100 shadow-xl" @submit.prevent="submit">
    <div class="card-body">
      <h1 class="card-title text-2xl">AulaPlan AI</h1>
      <p class="text-sm opacity-60">Acceso al generador inteligente de horarios.</p>
      <div v-if="errorMessage" class="alert alert-error text-sm">{{ errorMessage }}</div>
      <label class="form-control">
        <span class="label-text mb-1">Correo</span>
        <input v-model="email" type="email" class="input input-bordered" required />
      </label>
      <label class="form-control">
        <span class="label-text mb-1">Contraseña</span>
        <input v-model="password" type="password" class="input input-bordered" required />
      </label>
      <button class="btn btn-primary mt-2" :disabled="loading">{{ loading ? 'Entrando…' : 'Entrar' }}</button>
    </div>
  </form>
</template>