<script setup lang="ts">
import type { CatalogField, CatalogRecord } from '~/types'

const props = defineProps<{
  title: string
  endpoint: string
  fields: CatalogField[]
}>()

const { request } = useApi()
const rows = ref<CatalogRecord[]>([])
const form = reactive<Record<string, unknown>>({})
const editingId = ref<string | null>(null)
const loading = ref(false)
const errorMessage = ref('')

function resetForm() {
  editingId.value = null
  for (const key of Object.keys(form)) delete form[key]
  for (const field of props.fields) {
    form[field.key] = field.defaultValue ?? (field.type === 'checkbox' ? true : '')
  }
}

async function load() {
  loading.value = true
  errorMessage.value = ''
  try {
    rows.value = await request<CatalogRecord[]>(props.endpoint)
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'No fue posible cargar los datos.'
  } finally {
    loading.value = false
  }
}

function edit(row: CatalogRecord) {
  editingId.value = row.id
  for (const field of props.fields) form[field.key] = row[field.key]
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function save() {
  const method = editingId.value ? 'PUT' : 'POST'
  const path = editingId.value ? `${props.endpoint}/${editingId.value}` : props.endpoint
  await request(path, { method, body: { ...form } })
  resetForm()
  await load()
}

async function remove(id: string) {
  if (!confirm('¿Eliminar este registro?')) return
  await request(`${props.endpoint}/${id}`, { method: 'DELETE' })
  await load()
}

onMounted(async () => {
  resetForm()
  await load()
})
</script>

<template>
  <section class="space-y-6">
    <div>
      <h1 class="text-2xl font-bold">{{ title }}</h1>
      <p class="text-sm opacity-60">Catálogo conectado al backend Python.</p>
    </div>

    <div v-if="errorMessage" class="alert alert-error">{{ errorMessage }}</div>

    <form class="card border border-base-300 bg-base-100" @submit.prevent="save">
      <div class="card-body grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        <label v-for="field in fields" :key="field.key" class="form-control">
          <span class="label-text mb-1">{{ field.label }}</span>

          <select v-if="field.type === 'select'" v-model="form[field.key]" class="select select-bordered" :required="field.required">
            <option value="">Selecciona una opción</option>
            <option v-for="option in field.options" :key="option.value" :value="option.value">{{ option.label }}</option>
          </select>

          <input v-else-if="field.type === 'checkbox'" v-model="form[field.key]" type="checkbox" class="toggle toggle-primary" />

          <input v-else v-model="form[field.key]" :type="field.type || 'text'" class="input input-bordered" :required="field.required" />
        </label>

        <div class="md:col-span-2 xl:col-span-3 flex gap-2">
          <button class="btn btn-primary" type="submit">{{ editingId ? 'Actualizar' : 'Guardar' }}</button>
          <button v-if="editingId" class="btn" type="button" @click="resetForm">Cancelar</button>
        </div>
      </div>
    </form>

    <div class="overflow-x-auto rounded-box border border-base-300 bg-base-100">
      <table class="table">
        <thead>
          <tr>
            <th v-for="field in fields" :key="field.key">{{ field.label }}</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading"><td :colspan="fields.length + 1">Cargando…</td></tr>
          <tr v-for="row in rows" :key="row.id">
            <td v-for="field in fields" :key="field.key">{{ row[field.key] }}</td>
            <td class="flex gap-2">
              <button class="btn btn-xs" @click="edit(row)">Editar</button>
              <button class="btn btn-xs btn-error btn-outline" @click="remove(row.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>