import Vue from 'vue';
import Router from 'vue-router';
import homepage_body from '../components/home/homepage.vue';
import virtual_tour from "../components/home/virtual_tour";

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
    {
      path: "/virtual_tour",
      name: "virtual_tour",
      component: virtual_tour

    }
  ],
});
