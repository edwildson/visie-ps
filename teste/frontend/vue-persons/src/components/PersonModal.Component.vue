<template>
	<transition name="modal">
		<div class="modal" v-if="show">
			<div class="modal-overlay" @click="closeModal"></div>
			<div class="modal-container">
				<div class="modal-content">
					<!-- Conteúdo do modal aqui -->
					<!-- <slot></slot> -->
					<h2 class="text-2xl font-bold capitalize px-2 py-4">
						{{ newPerson ? 'Novo registro' : 'Editar registro' }}
					</h2>
					<hr class="mb-4" />
					<div class="modal-form">
						<div class="flex flex-wrap w-full">
							<div class="form-group mb-4 px-2 w-full lg:w-1/2">
								<label
									class="block mb-1 text-base 2xl:text-lg font-semibold"
									for="nome"
								>
									Nome: <span class="required-indicator">*</span>
									
								</label>
								<input
									id="nome"
									class="w-full border px-4 py-2 rounded focus:border-blue-500 focus:shadow-outline outline-none"
									type="text"
									autofocus
									placeholder="Digite o nome"
									v-model="person.nome"
									required
								/>
								<div
									v-if="errors.nome"
									class="text-xs text-red-600 mt-1"
								>
									O nome é obrigatório
								</div>
							</div>
							<div class="form-group mb-4 px-2 w-full lg:w-1/4">
								<label
									class="block mb-1 text-base 2xl:text-lg font-semibold"
									for="cpf"
									>CPF: <span class="required-indicator">*</span></label
								>
								<input
									class="w-full border px-4 py-2 rounded focus:border-blue-500 focus:shadow-outline outline-none"
									type="text"
									autofocus
                                    v-maska:[options]
									placeholder="Digite o CPF"
									v-model="person.cpf"
									id="cpf"
									required
								/>
								<div
									v-if="errors.cpf"
									class="text-xs text-red-600 mt-1"
								>
									O CPF é obrigatório
								</div>
							</div>
                            <div class="form-group mb-4 px-2 w-full lg:w-1/4">
								<label
									class="block mb-1 text-base 2xl:text-lg font-semibold"
									for="rg"
									>RG: <span class="required-indicator">*</span></label
								>
								<input
									class="w-full border px-4 py-2 rounded focus:border-blue-500 focus:shadow-outline outline-none"
									type="text"
									autofocus
									placeholder="Digite o RG"
									v-model="person.rg"
									id="rg"
									required
								/>
								<div
									v-if="errors.rg"
									class="text-xs text-red-600 mt-1"
								>
									O RG é obrigatório
								</div>
							</div>
						</div>
						<div class="flex flex-wrap w-full">
							<div class="form-group mb-4 px-2 w-full lg:w-1/4">
								<label
									class="block mb-1 text-base 2xl:text-lg font-semibold"
									for="data_nascimento"
									>Data de Nascimento: <span class="required-indicator">*</span></label
								>
								<input
									class="w-full border px-4 py-2 rounded focus:border-blue-500 focus:shadow-outline outline-none"
									type="date"
									autofocus
									placeholder="Digite a data de nascimento"
									v-model="data_nascimento"
									id="data_nascimento"
									required
								/>
								<div
									v-if="errors.data_nascimento"
									class="text-xs text-red-600 mt-1"
								>
									A data de nascimento é obrigatória
								</div>
							</div>
                            <div class="form-group mb-4 px-2 w-full lg:w-1/4">
								<label
									class="block mb-1 text-base 2xl:text-lg font-semibold"
									for="data_admissao"
									>Data de Admissão: <span class="required-indicator">*</span></label
								>
								<input
									class="w-full border px-4 py-2 rounded focus:border-blue-500 focus:shadow-outline outline-none"
									type="date"
									autofocus
									placeholder="Digite a data de admissão"
									v-model="data_admissao"
									id="data_admissao"
									required
								/>
								<div
									v-if="errors.data_admissao"
									class="text-xs text-red-600 mt-1"
								>
									A data de admissão é obrigatória
								</div>
							</div>
							<div class="form-group mb-4 px-2 w-full lg:w-1/3">
								<label
									class="block mb-1 text-base 2xl:text-lg font-semibold"
									for="funcao"
                                >
                                    Função:
								</label>
								<div class="relative">
									<input
                                        id="funcao"
                                        class="w-full border px-4 py-2 rounded focus:border-blue-500 focus:shadow-outline outline-none"
                                        type="text"
                                        autofocus
                                        placeholder="Digite a função"
                                        v-model="person.funcao"
								    />
								</div>
							</div>
						</div>
					</div>
					<div class="modal-buttons">
						<button @click="closeModal" class="btn btn-secondary">
							Cancelar
						</button>
						<button @click="saveChanges" class="btn btn-primary">
							Salvar
						</button>
					</div>
				</div>
				<button class="modal-close" @click="closeModal">×</button>
			</div>
		</div>
	</transition>
</template>
  
<script setup lang="ts">
import { ref, watch } from "vue";
import { vMaska } from "maska";
import moment from "moment";

const emit = defineEmits(['close', 'create', 'update'])
const props = defineProps(["show", "person",  "newPerson"]);
const errors = ref({});
const options = { mask: '###.###.###-##' };

let data_nascimento = ref('1001/00/01');
let data_admissao = ref('1001/00/01');

const closeModal = () => {
    emit("close");
};

const saveChanges = () => {
    props.person.data_nascimento = data_nascimento;
    props.person.data_admissao = data_admissao;

	if (props.newPerson) {
		if (validateFields())  emit('create', props.person);
	}
	else {
		if (validateFields()) emit('update', props.person)
	}
};

const validateFields = () => {
	const fields = ['nome', 'cpf', 'rg', 'data_nascimento', 'data_nascimento'];
	let valid = true;

	for (const field of fields) {
		if (props.person.value == undefined || props.person.value.hasOwnProperty(key)) {
			if (!props.person[field]) {
				errors.value[field] = true;
				valid = false;
			}
			else {
				errors.value[field] = false;
			}
		}				
  	}
	return valid;
}

const handleDates = () => {
    data_nascimento.value = moment(props.person?.data_nascimento).utc().format('YYYY-MM-DD');
    data_admissao.value = moment(props.person?.data_admissao).utc().format('YYYY-MM-DD');
}

watch([() => props.person], handleDates);
</script>
  
<style scoped>
.modal {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 10;
}

.modal-overlay {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	z-index: -1;
}

.modal-container {
	background-color: white;
	width: 90%;
	height: 80%;
	overflow: auto;
	border-radius: 0.5rem;
	box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
	position: relative;
}

.modal-content {
	background-color: white;
	height: 100%;
	padding: 20px;
	border-radius: 8px;
	box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
	margin: 0 auto;
}

.modal-title {
	font-size: 1.5rem;
	margin-bottom: 10px;
}

.form-group {
	margin-bottom: 15px;
}

.label {
	font-weight: bold;
	display: block;
	margin-bottom: 5px;
}

.input {
	width: 100%;
	padding: 8px;
	border: 1px solid #000000;
	border-radius: 4px;
	transition: border-color 0.3s;
}

.input:focus {
	border-color: #3490dc;
	outline: none;
}

.modal-buttons {
	text-align: right;
	margin-top: 15px;
}

.btn {
	padding: 8px 15px;
	border: none;
	border-radius: 4px;
	cursor: pointer;
	transition: background-color 0.3s, color 0.3s;
}

.btn-primary {
	background-color: #3490dc;
	color: white;
}

.btn-secondary {
	background-color: #ccc;
	color: #333;
	margin-right: 10px;
}

.btn:hover {
	background-color: #1d68a7;
	color: white;
}

.modal-close {
	position: absolute;
	top: 0.5rem;
	right: 0.5rem;
	padding: 0.5rem;
	cursor: pointer;
}

.required-indicator {
  color: red;
  font-size: 16px;
}
</style>
  