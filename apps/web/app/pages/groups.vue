<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'code', label: 'Código', type: 'text', required: true },\n  { key: 'name', label: 'Nombre', type: 'text', required: true },\n  { key: 'student_count', label: 'Alumnos', type: 'number', required: true },\n  { key: 'academic_period_id', label: 'ID periodo', type: 'text', required: true },\n  { key: 'active', label: 'Activo', type: 'checkbox', required: false, defaultValue: true }
]
</script>

<template>
  <CatalogManager title="Grupos" endpoint="/groups" :fields="fields" />
</template>