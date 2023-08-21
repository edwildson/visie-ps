import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Inicio',
    component: () => import('../pages/Index.vue'),
  },
  {
    path: '/registro/:id',
    name: 'Registro',
    component: () => import('../pages/registro/Index.vue'),
  },
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: () => import('@/pages/notfound/Index.vue'),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;