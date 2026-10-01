<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'day', label: 'Día', type: 'text', required: true },\n  { key: 'start_time', label: 'Inicio', type: 'text', required: true },\n  { key: 'end_time', label: 'Fin', type: 'text', required: true },\n  { key: 'order', label: 'Orden', type: 'number', required: true },\n  { key: 'active', label: 'Activo', type: 'checkbox', required: false, defaultValue: true }
]
</script>

<template>
  <CatalogManager title="Bloques horarios" endpoint="/time-blocks" :fields="fields" />
</template>