<script setup lang="ts">
const items = [
  ['Dashboard', '/dashboard'],
  ['Periodos', '/academic-periods'],
  ['Profesores', '/teachers'],
  ['Materias', '/subjects'],
  ['Grupos', '/groups'],
  ['Salones', '/rooms'],
  ['Bloques', '/time-blocks'],
  ['Ofertas académicas', '/offerings'],
  ['Disponibilidad', '/availability'],
  ['Restricciones', '/constraints'],
  ['Generador', '/generator'],
  ['Horarios', '/schedules'],
  ['Usuarios', '/users'],
]
</script>

<template>
  <aside class="min-h-full w-72 border-r border-base-300 bg-base-100 p-4">
    <NuxtLink to="/dashboard" class="mb-6 block text-xl font-bold">AulaPlan AI</NuxtLink>
    <ul class="menu gap-1 p-0">
      <li v-for="item in items" :key="item[1]">
        <NuxtLink :to="item[1]" active-class="menu-active">{{ item[0] }}</NuxtLink>
      </li>
    </ul>
  </aside>
</template>