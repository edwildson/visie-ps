<template>
	<div class="w-full border-2 flex flex-wrap bg-white shadow-lg rounded-lg my-3 p-4">
		<div class="w-full md:w-1/4 pb-2">
			<h3 class="text-xl font-semibold mb-1">Nome:</h3>
			<p class="text-md text-gray-600">{{ person.nome.split(" ")[0] }}</p>
		</div>
		<div class="w-full lg:w-1/4 pb-2">
			<h3 class="text-xl font-semibold mb-1">Data de Admissão:</h3>
			<p class="text-md text-gray-600">
				{{ moment(person.data_admissao).format("DD/MM/YYYY") }}
			</p>
		</div>
		<div class="w-full md:w-2/4 flex flex-col-reverse md:flex-row justify-end gap-2 md:gap-4 py-2">
			<button class="flex justify-center items-center rounded-full border py-2 px-4 rounded-md text-center">
				<vue-feather type="trash-2" class="mr-2"></vue-feather> Deletar
			</button>
			<button class="flex justify-center items-center rounded-full border py-2 px-4 rounded-md fit-content">
				<vue-feather type="edit" class="mr-2"></vue-feather> Editar
			</button>
			<button class="flex justify-center items-center rounded-full border py-2 px-4 rounded-md fit-content">
				<vue-feather type="eye" class="mr-2"></vue-feather> Ver mais
			</button>
		</div>
	</div>
</template>

<script setup lang="ts">
import { PersonInterface } from "../models/Person.interface";
import moment from "moment";

defineProps<{ person: PersonInterface }>();
</script>

<style scoped>
</style>