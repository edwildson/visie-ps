<template>
	<div class="container mx-auto py-4">
		<div class="flex flex-wrap justify-center">
			<div class="w-10/12 md:w-full">
				<h1 class="text-2xl font-bold">Registros</h1>
				<hr class="my-4" />
				<button
					type="button"
					class="2xl:text-lg text-white bg-blue-600 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2"
				>
				Adicionar novo registro
				</button>
				<br /><br />
				<div class="relative overflow-x-auto">
					<PersonItem 
						v-for="(person, index) in persons" :key="index"
						:person="person"
					/>
				</div>
			</div>
		</div>
	</div>
</template>
  

<script setup lang="ts">
// import PersonCard from "./PersonCard.vue";
// import PersonModal from "./PersonModal.vue";
// import ConfirmationModal from "./ConfirmationModal.vue";
// import FlashMessage from "./FlashMessage.vue";
// import EmptyState from "./EmptyState.vue";
import PersonItem from "./PersonItem.Component.vue";

import { onMounted, ref } from "vue";
import api from "../services/Api.service";

import type { PersonInterface } from "../models/Person.interface";

const persons = ref<PersonInterface[]>([]);
// const selectedPerson = ref<PersonInterface>();
// const deletePerson = ref<PersonInterface>();
// const showModal: boolean = ref(false);
// const showDeleteModal: boolean = ref(false);
// const newPerson: boolean = ref(true);
// const showFlashMessage: boolean = ref(false);
// const flashMessage: string = ref("");
// const flashType: string = ref("");

const fetchPersons = () =>
	api.get("/persons").then(
		(response: any) => {
			console.log(response.data);
			persons.value = response.data;
		}
		// (response: any) => showMessage(response.data.message, "error")
	);

onMounted(fetchPersons);
</script>

<style scoped>
</style>