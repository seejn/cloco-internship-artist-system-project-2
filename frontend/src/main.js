import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store from './store/store.js'
import router from './router.js'
import PageLayout from './pages/Layout.vue'
import Toasts from './components/toasts/Toasts.vue'

createApp(App)
.component("PageLayout", PageLayout)
.component("Toasts", Toasts)
.use(router)
.use(store)
.mount('#app')
