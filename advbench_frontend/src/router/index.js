import Vue from 'vue'
import VueRouter from 'vue-router'
import OriginalView from '../views/OriginalView.vue'
import AdversarialView from '../views/AdversarialView.vue'
import UserView from '../views/UserView.vue'

// import Axios from 'axios'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'originalsamples',
    component: OriginalView,
    params: true,
  },
  {
    path: '/adversarialsamples',
    name: 'adversarialsamples',
    component: OriginalView,
    // params: true,
  },
  {
    path: '/usersample',
    name: 'usersample',
    component: UserView
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/LoginView.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
