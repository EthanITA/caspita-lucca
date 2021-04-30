import Vue from 'vue';
import Router from 'vue-router';
import homepage from '../components/home/homepage.vue';
import loader from '../components/home/loader.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: homepage,
    },
    {
      path:'/loader',
      name: 'name',
      component: loader
    }
  ],
});
