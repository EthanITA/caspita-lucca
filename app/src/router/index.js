import Vue from 'vue';
import Router from 'vue-router';
import homepage from '../components/home/homepage.vue';

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
  ],
});
