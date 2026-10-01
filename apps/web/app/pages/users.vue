<script setup lang="ts">
const { request } = useApi()
const users = ref<any[]>([])
onMounted(async () => { users.value = await request<any[]>('/users') })
</script>

<template>
  <section class="space-y-6">
    <div><h1 class="text-3xl font-bold">Usuarios</h1><p class="opacity-60">Solo ADMIN puede consultar esta vista.</p></div>
    <div class="overflow-x-auto rounded-box border border-base-300 bg-base-100">
      <table class="table"><thead><tr><th>Correo</th><th>Nombre</th><th>Rol</th><th>Activo</th></tr></thead>
        <tbody><tr v-for="user in users" :key="user.uid"><td>{{ user.email }}</td><td>{{ user.display_name }}</td><td>{{ user.role }}</td><td>{{ user.active }}</td></tr></tbody>
      </table>
    </div>
  </section>
</template>