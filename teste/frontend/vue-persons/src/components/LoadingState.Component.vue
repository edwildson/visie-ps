<template>
    <div v-if="loading" class="flex items-center justify-center h-screen">
      <div class="animate-spin rounded-full border-t-4 border-blue-500 border-opacity-50 h-16 w-16"></div>
    </div>
  </template>
  
  <script setup>
  
  const props = defineProps({
    loading: Boolean(true),
  });
  </script>
  
  <style scoped>
  /* Estilos específicos do componente aqui, se necessário */
  </style>
  