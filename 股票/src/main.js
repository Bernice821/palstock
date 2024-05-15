import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue } from 'bootstrap-vue'
import VueApexCharts from 'vue-apexcharts'
import { CarouselPlugin } from 'bootstrap-vue'


// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import "bootstrap/dist/css/bootstrap.min.css"
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import "bootstrap"

// Make BootstrapVue available throughout your project
Vue.component('apexChart', VueApexCharts)
Vue.component('vue-sidebar-menu-akahon', VueSidebarMenuAkahon);

Vue.use(BootstrapVue)
Vue.use(VueApexCharts)
Vue.use(CarouselPlugin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
