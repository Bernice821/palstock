import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    redirect: '/dash/home'  // 添加这一行来设置首页的重定向
  },
  {
    name: 'Dashboard',
    path: '/dash',
    component: () => import(/* webpackChunkName: "about" */ '../views/master/dashboard.vue'),
    children: [
      {
        path: 'home',  // 确保是相对于 '/dash' 的相对路径
        name: 'home',
        component: () => import(/* webpackChunkName: "about" */ '../views/HomeView'),
      },
      {
        path: 'news',
        name: 'news',
        component: () => import(/* webpackChunkName: "about" */ '../views/news'),
      },
      {
        path: 'market',
        name: 'market',
        component: () => import(/* webpackChunkName: "about" */ '../views/MarketPage.vue'),
      },
      {
        path: 'result',
        name: 'result',
        component: () => import(/* webpackChunkName: "about" */ '../views/research_result'),
      },
      {
        path: 'about',
        name: 'about',
        component: () => import(/* webpackChunkName: "about" */ '../views/StockPage.vue')
      },
      {
        path: 'research',
        name: 'research',
        component: () => import(/* webpackChunkName: "about" */ '../views/research.vue')
      }
    ]
  },
  // 为每个需要的子路由添加重定向
  { path: '/home', redirect: '/dash/home' },
  { path: '/news', redirect: '/dash/news' },
  { path: '/market', redirect: '/dash/market' },
  { path: '/result', redirect: '/dash/result' },
  { path: '/about', redirect: '/dash/about' },
  { path: '/research', redirect: '/dash/research' }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
