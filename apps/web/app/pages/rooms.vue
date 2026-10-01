<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'code', label: 'Código', type: 'text', required: true },\n  { key: 'name', label: 'Nombre', type: 'text', required: true },\n  { key: 'capacity', label: 'Capacidad', type: 'number', required: true },\n  { key: 'type', label: 'Tipo', type: 'text', required: true },\n  { key: 'building', label: 'Edificio', type: 'text', required: false },\n  { key: 'active', label: 'Activo', type: 'checkbox', required: false, defaultValue: true }
]
</script>

<template>
  <CatalogManager title="Salones" endpoint="/rooms" :fields="fields" />
</template>