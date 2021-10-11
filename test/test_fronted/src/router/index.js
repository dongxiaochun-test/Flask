import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Testcase from '../views/Testcase.vue'
import Layout from '../views/Layout.vue'
import Task from '../views/Task.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },

    {
        path: '/layout',
        name: 'layout',
        component: Layout,
        // children添加子路由，是一个数组嵌套对象的形式，可以添加多个子路由
        children: [
            // path代表路由地址， name表示这个路由的名称，
            // component表示这个路由和哪个页面相关
            {
                path: '/testcase',
                name: 'Testcase',
                component: Testcase
            },
            {
                path: '/task',
                name: 'Task',
                component: Task
            },
        ]
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
