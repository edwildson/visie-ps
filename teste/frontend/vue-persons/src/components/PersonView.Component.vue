<template>
	<div class="bg-white rounded shadow-md">
		<div class="px-6 sm:px-8 md:px-10 lg:px-12">
			<breadcumb />
			<h2 class="text-xl font-bold mb-4">Informações do Registro</h2>
			<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
				<div>
					<label class="text-gray-600">Nome:</label>
					<p class="text-xl font-semibold">{{ props.person.nome }}</p>
				</div>
				<div>
					<label class="text-gray-600">RG:</label>
					<p class="text-xl font-semibold">{{ props.person.rg }}</p>
				</div>
				<div>
					<label class="text-gray-600">CPF:</label>
					<p class="text-xl font-semibold">{{ props.person.cpf }}</p>
				</div>
				<div>
					<label class="text-gray-600">Data de Nascimento:</label>
					<p class="text-xl font-semibold">
						{{
							moment(props.person.data_nascimento)
								.utc()
								.format("DD/MM/YYYY")
						}}
					</p>
				</div>
				<div>
					<label class="text-gray-600">Data de Admissão:</label>
					<p class="text-xl font-semibold">
						{{
							moment(props.person.data_admissao)
								.utc()
								.format("DD/MM/YYYY")
						}}
					</p>
				</div>
				<div>
					<label class="text-gray-600">Função:</label>
					<p class="text-xl font-semibold">
						{{ props.person.funcao }}
					</p>
				</div>
			</div>
		</div>
		<div
			class="w-full flex flex-col-reverse md:flex-row justify-end gap-2 md:gap-4 p-6"
		>
			<button
				@click="$emit('delete')"
				class="flex border-2 border-red-200 justify-center items-center rounded-full border py-2 px-4 rounded-md text-center"
			>
				<vue-feather type="trash-2" class="mr-2"></vue-feather> Deletar
			</button>
			<button
				@click="$emit('edit')"
				class="flex border-2 border-blue-200 justify-center items-center rounded-full border py-2 px-4 rounded-md fit-content"
			>
				<vue-feather type="edit" class="mr-2"></vue-feather> Editar
			</button>
		</div>
	</div>
</template>

<script setup lang="ts">
import { Person } from "../models/Person.interface";
import Buttons from "./Buttons.Component.vue";
import moment from "moment";
import Breadcumb from "./Breadcumb.Component.vue";

const props = defineProps<{ person: Person }>();
</script>
  
<style scoped>
/* Estilos específicos do componente aqui, se necessário */
</style>
  