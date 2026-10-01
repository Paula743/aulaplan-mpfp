<script setup lang="ts">
const { request } = useApi()
const periodId = ref('')
const maxNodes = ref(50000)
const result = ref<unknown>(null)
const loading = ref(false)
async function generate() {
  loading.value = true
  try {
    result.value = await request('/schedules/generate', {
      method: 'POST',
      body: { academic_period_id: periodId.value, max_nodes: maxNodes.value },
    })
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <section class="space-y-6">
    <div><h1 class="text-3xl font-bold">Generador de horarios</h1><p class="opacity-60">Ejecuta el scheduler Python.</p></div>
    <div class="card border border-base-300 bg-base-100">
      <div class="card-body max-w-2xl">
        <label class="form-control"><span class="label-text mb-1">ID periodo académico</span><input v-model="periodId" class="input input-bordered" /></label>
        <label class="form-control"><span class="label-text mb-1">Máximo de nodos</span><input v-model="maxNodes" type="number" class="input input-bordered" /></label>
        <button class="btn btn-primary w-fit" :disabled="loading || !periodId" @click="generate">{{ loading ? 'Generando…' : 'Generar horario' }}</button>
      </div>
    </div>
    <pre v-if="result" class="overflow-auto rounded-box bg-neutral p-4 text-xs text-neutral-content">{{ JSON.stringify(result, null, 2) }}</pre>
  </section>
</template>