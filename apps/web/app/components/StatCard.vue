<script setup lang="ts">
defineProps<{ title: string; value: string | number; description?: string }>()
</script>

<template>
  <div class="card border border-base-300 bg-base-100 shadow-sm">
    <div class="card-body">
      <p class="text-sm opacity-60">{{ title }}</p>
      <p class="text-3xl font-bold">{{ value }}</p>
      <p v-if="description" class="text-sm opacity-60">{{ description }}</p>
    </div>
  </div>
</template>