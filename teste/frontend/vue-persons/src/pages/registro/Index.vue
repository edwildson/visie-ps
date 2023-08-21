<template>
    <div>
        <NavBar />
        <person-view
            v-if="!loading"
            :person="personData"
            @delete="handleDelete"
            @edit="handleShowEditModal"
        />
        <loading-state v-else :loading="loading"/>


        <confirmation-modal
			:person="deletePerson"
			:show="showDeleteModal"
			@close="handleCloseDeleteModal"
			@delete="handleDeleteConfirmation"
		/>

        <person-modal
			:person="selectedPerson"
			:show="showModal"
			:newPerson="false"
			@close="handleCloseEditModal"
			@update="handleUpdatePerson"
		/>

        <flash-message
            :message="flashMessage"
            :type="flashType"
            v-if="showFlashMessage"
        />

    </div>
  </template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from "@/services/Api.service";
import NavBar from "@/components/Navbar.vue";
import PersonList from "@/components/PersonList.Component.vue";
import PersonView from "@/components/PersonView.Component.vue";
import { Person } from '../../models/Person.interface';
import ConfirmationModal from '@/components/ConfirmationDeleteModal.Component.vue';
import PersonModal from '@/components/PersonModal.Component.vue';
import LoadingState from '@/components/LoadingState.Component.vue';
import FlashMessage from '@/components/FlashMessage.Component.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();
const loading = ref(true);
const personId = ref<number | null>(null);
const personData = ref<Person | null>(null);
const selectedPerson = ref<Person>();
const showModal = ref(false);
const deletePerson = ref<Person>();
const showDeleteModal = ref(false);
const showFlashMessage = ref(false);
const flashMessage = ref("");
const flashType = ref("");


const handleCloseDeleteModal = () => (showDeleteModal.value = false);
const handleCloseEditModal = () => {
	showModal.value = false;
	selectedPerson.value = {}
};

const handleDelete = () => {
    console.log(personData.value);
	deletePerson.value = personData.value;
	showDeleteModal.value = true;
};

const handleDeleteConfirmation = (personToDelete: Person) => {
	api.delete(`/api/persons/${personToDelete.id}`).then(
		() => {
			showDeleteModal.value = false;
			showMessage('Registro deletado com sucesso!', "success");
            router.push('/');
		},
		(response: any) => showMessage(response.data.message, "error")
	);
};

const handleShowEditModal = () => {
    console.log(personData);
	selectedPerson.value = personData.value;
	showModal.value = true;
};

const handleUpdatePerson = async () => {
	try {
		const response = await api.patch(`/api/persons/${personData.value.id}`, personData.value);
		
		personData.value = response.data.data;
		showModal.value = false;
		showMessage("Registro atualizado com sucesso!", "success");
	} catch (err: any) {
		showMessage(err.response.message, "error")
	}
};

const showMessage = (message: string, type: string) => {
	flashMessage.value = message;
	flashType.value = type;
	showFlashMessage.value = true;

	setTimeout(() => {
		showFlashMessage.value = false;
	}, 5000);
};

onMounted(async () => {
  personId.value = Number(route.params.id);

  if (personId.value) {
    try {
        const response = await api.get(`/api/persons/${personId.value}`);
        personData.value = response.data;
    } catch (error) {
        console.error('Erro ao carregar pessoa:', error);
    } finally {
        loading.value = false;
    }
  }
});
  </script>
  
  <style scoped>
  
  </style>