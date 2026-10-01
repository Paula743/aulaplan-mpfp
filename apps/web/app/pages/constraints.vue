<script setup lang="ts">
import type { CatalogField } from '~/types'
const { request } = useApi()
const naturalText = ref('')
const parsed = ref<unknown>(null)
const fields: CatalogField[] = [
  { key: 'type', label: 'Tipo', required: true },
  { key: 'priority', label: 'Prioridad', required: true },
  { key: 'target_type', label: 'Tipo objetivo', required: true },
  { key: 'target_id', label: 'ID objetivo', required: true },
  { key: 'weight', label: 'Peso', type: 'number', defaultValue: 0 },
  { key: 'active', label: 'Activo', type: 'checkbox', defaultValue: true },
]
async function parseText() {
  parsed.value = await request('/ai/constraints/parse', {
    method: 'POST', body: { text: naturalText.value },
  })
}
</script>

<template>
  <section class="space-y-8">
    <CatalogManager title="Restricciones" endpoint="/constraints" :fields="fields" />
    <div class="card border border-base-300 bg-base-100">
      <div class="card-body">
        <h2 class="card-title">Interpretar con Gemini</h2>
        <textarea v-model="naturalText" class="textarea textarea-bordered min-h-32" placeholder="Ej. Marco no puede dar clases los martes..." />
        <button class="btn btn-secondary w-fit" @click="parseText">Interpretar</button>
        <pre v-if="parsed" class="overflow-auto rounded bg-base-200 p-4 text-xs">{{ JSON.stringify(parsed, null, 2) }}</pre>
      </div>
    </div>
  </section>
</template>