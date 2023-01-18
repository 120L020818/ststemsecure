import {createRouter, createWebHistory} from 'vue-router'
import MyTest  from "@/components/MyTest.vue";


const router=createRouter({
    history:createWebHistory(),
    routes:[
        {
            path:'/test',
            name:"test",
            component:MyTest,
        }
    ]
})

export default router
