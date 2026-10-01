<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'teacher_id', label: 'ID profesor', type: 'text', required: true },\n  { key: 'time_block_id', label: 'ID bloque', type: 'text', required: true },\n  { key: 'available', label: 'Disponible', type: 'checkbox', required: false, defaultValue: true },\n  { key: 'preference_weight', label: 'Preferencia', type: 'number', required: false }
]
</script>

<template>
  <CatalogManager title="Disponibilidad docente" endpoint="/availability" :fields="fields" />
</template>