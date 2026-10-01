<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'code', label: 'Código', type: 'text', required: true },\n  { key: 'name', label: 'Nombre', type: 'text', required: true },\n  { key: 'weekly_blocks', label: 'Bloques/semana', type: 'number', required: true },\n  { key: 'required_room_type', label: 'Tipo de salón', type: 'text', required: true },\n  { key: 'active', label: 'Activo', type: 'checkbox', required: false, defaultValue: true }
]
</script>

<template>
  <CatalogManager title="Materias" endpoint="/subjects" :fields="fields" />
</template>