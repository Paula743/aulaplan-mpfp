<script setup lang="ts">
const { request } = useApi()
const rows = ref<any[]>([])
onMounted(async () => { rows.value = await request<any[]>('/schedules') })
async function publish(id: string) {
  await request(`/schedules/${id}/publish`, { method: 'POST' })
  rows.value = await request<any[]>('/schedules')
}
</script>

<template>
  <section class="space-y-6">
    <div><h1 class="text-3xl font-bold">Horarios</h1><p class="opacity-60">Versiones generadas y publicadas.</p></div>
    <div class="overflow-x-auto rounded-box border border-base-300 bg-base-100">
      <table class="table"><thead><tr><th>ID</th><th>Periodo</th><th>Estado</th><th>Score</th><th></th></tr></thead>
        <tbody><tr v-for="row in rows" :key="row.id"><td class="font-mono text-xs">{{ row.id }}</td><td>{{ row.academic_period_id }}</td><td>{{ row.status }}</td><td>{{ row.score }}</td><td><button v-if="row.status !== 'PUBLISHED'" class="btn btn-xs btn-primary" @click="publish(row.id)">Publicar</button></td></tr></tbody>
      </table>
    </div>
  </section>
</template>