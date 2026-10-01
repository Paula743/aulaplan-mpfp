<script setup lang="ts">
import type { CatalogField } from '~/types'

const fields: CatalogField[] = [
  { key: 'academic_period_id', label: 'ID periodo', type: 'text', required: true },\n  { key: 'subject_id', label: 'ID materia', type: 'text', required: true },\n  { key: 'group_id', label: 'ID grupo', type: 'text', required: true },\n  { key: 'teacher_id', label: 'ID profesor', type: 'text', required: true },\n  { key: 'active', label: 'Activo', type: 'checkbox', required: false, defaultValue: true }
]
</script>

<template>
  <CatalogManager title="Ofertas académicas" endpoint="/offerings" :fields="fields" />
</template>