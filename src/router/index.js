import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/explore',
      name: 'Explore',
      component: () => import('../views/ExploreView.vue')
    },
    {
      path: '/cars/new',
      name: 'Add New Car',
      component: () => import('../views/NewCarView.vue')
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/logout',
      name: 'Sign Out',
      component: () => import('../views/LogoutView.vue')
    },
    {
      path: '/users/:user_id',
      name: 'User Profile',
      component: () => import('../views/UserView.vue')
    },
    {
      path: '/cars/:car_id',
      name: 'Car',
      component: () => import('../views/ExploreView.vue')
    }
  ]
})

export default router
