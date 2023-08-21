import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import VueFeather from 'vue-feather';
import router from './routes'

createApp(App).component(VueFeather.name, VueFeather).use(router).mount('#app')
