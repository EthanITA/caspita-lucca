import Vue from 'vue';
import Router from 'vue-router';
import homepage_body from '../components/home/homepage.vue';
import private_login from "../components/private_area/login";
import virtual_tour from "../components/home/virtual_tour";
import clothes from "../components/private_area/receipt/clothes";
import dashboard from "../components/private_area/dashboard";

Vue.use(Router);

const router = new Router({
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
    {
      path: "/private_login",
      name: "private_login",
      component: private_login,
    },
    {
      path: "/internal/receipt/clothes",
      name: "internal_clothes_receipt",
      component: clothes,
      meta: {requires_auth: true}
    },
    {
      path: "/private_area",
      name: "private_area",
      component: dashboard,
      meta: {requires_auth: true}
    }
  ],
});

function authenticate(password) {

}

router.beforeEach((to, from, next) => {
  if (to.meta.requires_auth) {
    if (!authenticate())
      next({
        path: '/'
      })
    else
      next()
  } else {
    next()
  }
});
export default router
