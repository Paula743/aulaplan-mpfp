<script setup lang="ts">
const cards = [
  ['Profesores', '—', 'Carga desde Firestore'],
  ['Materias', '—', 'Catálogo académico'],
  ['Grupos', '—', 'Grupos activos'],
  ['Horarios', '—', 'Versiones generadas'],
]
</script>

<template>
  <section class="space-y-6">
    <div>
      <h1 class="text-3xl font-bold">Dashboard</h1>
      <p class="opacity-60">Resumen operativo de AulaPlan AI.</p>
    </div>
    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
      <StatCard v-for="card in cards" :key="card[0]" :title="card[0]" :value="card[1]" :description="card[2]" />
    </div>
    <div class="card border border-base-300 bg-base-100">
      <div class="card-body">
        <h2 class="card-title">Flujo recomendado</h2>
        <ol class="list-decimal space-y-2 pl-6">
          <li>Captura catálogos y periodo académico.</li>
          <li>Define ofertas, disponibilidad y restricciones.</li>
          <li>Genera un horario y revisa el score.</li>
          <li>Publica una versión cuando sea aprobada.</li>
        </ol>
      </div>
    </div>
  </section>
</template>