<template>
	<div class="flex flex-col items-center justify-center h-screen">
		<h1 class="text-4xl font-bold text-gray-600 mb-4">
			404 - Página não encontrada
		</h1>
		<p class="text-lg text-gray-400">
			A página que você está procurando não existe.
		</p>
		<p @click="router.push('/')" class="text-lg text-gray-400">
			<span class="text-sky-500 cursor-pointer">Clique aqui</span> para voltar ao início.
		</p>
	</div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

</script>

  
<style scoped>
/* Estilos específicos do componente aqui, se necessário */
</style>
  