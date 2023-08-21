<template>
	<div class="w-full border-2 flex flex-wrap bg-white shadow-lg rounded-lg my-3 p-4">
		<div class="w-full md:w-1/4 pb-2">
			<h3 class="text-xl font-semibold mb-1">Nome:</h3>
			<p class="text-md text-gray-600">{{ person.nome?.split(" ")[0] }}</p>
		</div>
		<div class="w-full lg:w-1/4 pb-2">
			<h3 class="text-xl font-semibold mb-1">Data de Admissão:</h3>
			<p class="text-md text-gray-600">
				{{ moment(person.data_admissao).utc().format("DD/MM/YYYY") }}
			</p>
		</div>
		<buttons 
			@delete="$emit('delete', person)"
			@edit="$emit('edit', person)"
			@view="$emit('view', person)"
		/>
	</div>
</template>

<script setup lang="ts">
import { Person } from "../models/Person.interface";
import Buttons from "./Buttons.Component.vue";
import moment from "moment";

defineProps<{ person: Person }>();
</script>

<style scoped>
</style>