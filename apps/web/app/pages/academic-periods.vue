<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'code', label: 'Código', type: 'text', required: true },\n  { key: 'name', label: 'Nombre', type: 'text', required: true },\n  { key: 'start_date', label: 'Inicio', type: 'text', required: true },\n  { key: 'end_date', label: 'Fin', type: 'text', required: true },\n  { key: 'active', label: 'Activo', type: 'checkbox', required: false, defaultValue: true }
]
</script>

<template>
  <CatalogManager title="Periodos académicos" endpoint="/academic-periods" :fields="fields" />
</template>