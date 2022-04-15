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
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/logout',
      name: 'Sign Out',
      component: HomeView
    },

    {
      path: '/users',
      name: 'User Profile',
      component: () => import('../views/ProfileView.vue'),
      props: true
    },

    {
      path: '/cars/new',
      name: 'Add New Car',
      component: () => import('../views/NewCarView.vue')
    },
    
    {
      path: '/cars/:car_id',
      name: 'Car',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/RegisterView.vue')
    }
  ]
})

export default router
