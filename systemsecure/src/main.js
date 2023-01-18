import { createApp } from 'vue'
import App from './App.vue'
import router from "./router/index"
import "element-plus/dist/index.css"
import ElementPlus from 'element-plus'
const app=createApp(App);
import './assets/main.css'

app.use(router).mount('#app')
