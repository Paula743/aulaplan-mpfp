<script setup lang="ts">
const { logout } = useAuth()
const store = useAuthStore()
</script>

<template>
  <header class="navbar sticky top-0 z-30 border-b border-base-300 bg-base-100 px-4">
    <div class="flex-none lg:hidden">
      <label for="aulaplan-drawer" class="btn btn-square btn-ghost" aria-label="Abrir menú">☰</label>
    </div>
    <div class="flex-1">
      <span class="font-semibold">AulaPlan AI</span>
    </div>
    <div class="flex items-center gap-3">
      <div class="hidden text-right sm:block">
        <p class="text-sm font-medium">{{ store.profile?.display_name || store.firebaseUser?.email }}</p>
        <p class="text-xs opacity-60">{{ store.profile?.role }}</p>
      </div>
      <button class="btn btn-sm btn-outline" @click="logout">Salir</button>
    </div>
  </header>
</template>