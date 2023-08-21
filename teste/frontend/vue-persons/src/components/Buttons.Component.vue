<template>
    <div class="w-full md:w-2/4 flex flex-col-reverse md:flex-row justify-end gap-2 md:gap-4 py-2">
        <button @click="$emit('delete')" class="flex border-2 border-red-200 justify-center items-center rounded-full border py-2 px-4 rounded-md text-center">
            <vue-feather type="trash-2" class="mr-2"></vue-feather> Deletar
        </button>
        <button @click="$emit('edit')" class="flex border-2 border-blue-200 justify-center items-center rounded-full border py-2 px-4 rounded-md fit-content">
            <vue-feather type="edit" class="mr-2"></vue-feather> Editar
        </button>
        <button v-if="!props.view" @click="$emit('view')" class="flex border-2 border-green-200 justify-center items-center rounded-full border py-2 px-4 rounded-md fit-content">
            <vue-feather type="eye" class="mr-2"></vue-feather> Ver mais
        </button>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{view: boolean}>();

const classes = () => ref(props.view ? "w-full md:w-2/4 flex flex-col-reverse md:flex-row justify-end gap-2 md:gap-4 py-2" : "w-full md:w-2/4 flex flex-col-reverse md:flex-row justify-end gap-2 md:gap-4 py-2");
</script>

<style scoped>

</style>