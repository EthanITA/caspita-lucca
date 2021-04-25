import Vue from 'vue';
import Buefy from 'buefy';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import 'buefy/dist/buefy.css';

Vue.use(Buefy);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
Vue.prototype.$api_heroku = "https://caspita-lucca.herokuapp.com/api"
Vue.prototype["$api_gcloud"] = "https://caspita-lucca.ew.r.appspot.com/"
