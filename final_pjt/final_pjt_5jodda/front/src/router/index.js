import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Movies from '../views/Movies.vue'
import Movie from '../views/Movie.vue'
import User from '../views/User.vue'
import AdminMovie from '../views/AdminMovie.vue'
import AdminUser from '../views/AdminUser.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/movies',
    name: 'movies',
    component: Movies
  },
  {
    path: '/movie',
    name: 'movie',
    component: Movie
  },
  {
    path: '/user',
    name: 'user',
    component: User
  },
  {
    path: '/adminmovie',
    name: 'adminmovie',
    component: AdminMovie
  },
  {
    path: '/adminuser',
    name: 'adminuser',
    component: AdminUser
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
