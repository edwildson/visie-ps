<template>
	<div class="container mx-auto py-4">
		<div class="flex flex-wrap justify-center">
			<div class="w-10/12 md:w-full">
				<h1 class="text-2xl font-bold">Registros</h1>
				<hr class="my-4" />
				<button
					@click="handleShowAddModal"
					type="button"
					class="2xl:text-lg text-white bg-blue-600 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2"
				>
					Adicionar novo registro
				</button>
				<br /><br />
				<div v-if="!loading">
					<div v-if="persons.length" class="relative overflow-x-auto">
						<person-item 
							v-for="(person, index) in persons" :key="index"
							:person="person"
							@delete="handleDelete"
							@edit="handleShowEditModal"
							@view="handleView"
						/>
					</div>
					<div v-else>
						<empty-state
							@create="handleShowAddModal"
						/>
					</div>
				</div>
				<loading-state v-else :loading="loading"/>
				
			</div>
		</div>

		<person-modal
			:person="selectedPerson"
			:show="showModal"
			:newPerson="newPerson"
			@close="handleCloseEditModal"
			@update="handleUpdatePerson"
			@create="handleCreatePerson"
		/>

		<confirmation-modal
			:person="deletePerson"
			:show="showDeleteModal"
			@close="handleCloseDeleteModal"
			@delete="handleDeleteConfirmation"
		/>

		<div>
			<flash-message
				:message="flashMessage"
				:type="flashType"
				v-if="showFlashMessage"
			/>
		</div>
	</div>
</template>
  

<script setup lang="ts">

// import PersonCard from "./PersonCard.vue";
import ConfirmationModal from "./ConfirmationDeleteModal.Component.vue";
import FlashMessage from "./FlashMessage.Component.vue";
import EmptyState from "./EmptyState.Component.vue";
import PersonItem from "./PersonItem.Component.vue";
import PersonModal from "./PersonModal.Component.vue";
import type { Person } from "../models/Person.interface";
import LoadingState from "./LoadingState.Component.vue";

import { onMounted, ref } from "vue";
import api from "../services/Api.service";
import { useRouter } from 'vue-router';

const router = useRouter();



const loading = ref(true);
const persons = ref<Person[]>([]);
const selectedPerson = ref<Person>();
const deletePerson = ref<Person>();
const showModal = ref(false);
const showDeleteModal = ref(false);
const newPerson = ref(true);
const showFlashMessage = ref(false);
const flashMessage = ref("");
const flashType = ref("");


const fetchPersons = () =>
	api.get("/api/persons").then(
		(response: any) => {
			console.log(response.data);
			persons.value = response.data;
			loading.value = false;
		}
		// (response: any) => showMessage(response.data.message, "error")
	);

const handleCloseEditModal = () => {
	showModal.value = false;
	selectedPerson.value = {}
};
const handleShowEditModal = (personToEdit: Person) => {
	selectedPerson.value = personToEdit;
	newPerson.value = false;
	showModal.value = true;
};

const handleShowAddModal = () => {
	selectedPerson.value = {};
	newPerson.value = true;
	showModal.value = true;
};

const handleView = (person: Person) => {
	router.push(`/registro/${person.id}`);
}

const handleCloseDeleteModal = () => (showDeleteModal.value = false);

const handleDelete = (personToDelete: Person) => {
	deletePerson.value = personToDelete;
	showDeleteModal.value = true;
};

const handleUpdatePerson = async (personToUpdate: Person) => {
	try {
		const response = await api.patch(`/api/persons/${personToUpdate.id}`, personToUpdate);
		
		persons.value = persons.value.map((person) =>
			person.id != personToUpdate.id ? person : response.data.data
		);
		showModal.value = false;
		showMessage("Registro atualizado com sucesso!", "success");
	} catch (err: any) {
		showMessage(err.response.message, "error")
	}
};

const handleCreatePerson = async (personToCreate: Person) => {
	try {
		const response = await api.post("/api/persons", personToCreate);
		console.log(response.data.data);
		persons.value.push(response.data.data);
		showModal.value = false;
		showMessage("Registro cadastrado com sucesso!", "success");
	} catch(err: any) {
		showMessage(err.response.data.message, "error");
	}
};

const handleDeleteConfirmation = (personToDelete: Person) => {
	api.delete(`/api/persons/${personToDelete.id}`).then(
		() => {
			persons.value = persons.value.filter(
				(person) => person.id != personToDelete.id
			);
			showDeleteModal.value = false;
			showMessage('Registro deletado com sucesso!', "success");
		},
		(response: any) => showMessage(response.data.message, "error")
	);
};

const showMessage = (message: string, type: string) => {
	flashMessage.value = message;
	flashType.value = type;
	showFlashMessage.value = true;

	setTimeout(() => {
		showFlashMessage.value = false;
	}, 5000);
};

onMounted(fetchPersons);
</script>

<style scoped>
</style>