import Vue from 'vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import './registerServiceWorker';
import router from './router';
import store from './store'
import App from './App.vue';
import VueSocialSharing from 'vue-social-sharing'
import 'animate.css/animate.css';

Vue.use(VueSocialSharing);
Vue.use(Buefy);
Vue.use(VueMaterial)
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount('#app');
