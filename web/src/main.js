import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import {createRouter, createWebHistory } from 'vue-router'

loadFonts()
const Login = { template: '<div>Login</div>' }


const routes = [
  { path: '/login', name: 'Login'}
]

const router = createRouter({
  history: createWebHistory(),
  routes, 
})

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
