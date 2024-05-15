import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const routes = [
  {
    name: 'Dashboard',
    path: '/dash',
    component: () => import(/* webpackChunkName: "about" */ '../views/master/dashboard.vue'),
    children: [
      {
        path: '/home',
        name: 'home',
        component: () => import(/* webpackChunkName: "about" */ '../views/HomeView'),
      },{
        path: '/news',
        name: 'news',
        component: () => import(/* webpackChunkName: "about" */ '../views/news'),
      },
      {
        path: '/market',
        name: 'market',
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
      },
      {
        path: '/about',
        name: 'about',
        component: () => import(/* webpackChunkName: "about" */ '../views/StockPage.vue')
      },
      {
        path: '/research',
        name: 'research',
        component: () => import(/* webpackChunkName: "about" */ '../views/research.vue')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
