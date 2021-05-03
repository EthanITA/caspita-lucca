import Vue from 'vue';
import Router from 'vue-router';
import homepage_body from '../components/home/homepage.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'homepage_body',
      component: homepage_body,
    },
  ],
});
