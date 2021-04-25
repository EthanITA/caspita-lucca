import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

const gcloud_api = 'https://caspita-lucca.ew.r.appspot.com/api';
const heroku_api = 'https://caspita-lucca.herokuapp.com/';

export default new Vuex.Store({
  state: {
    api: gcloud_api,
    ping: ""
  },
  mutations: {
    // eslint-disable-next-line camelcase
    setApi(state, is_heroku) {
      state.api = is_heroku ? heroku_api : gcloud_api;
    }
  },
  getters: {
    getApi(state) {
      return state.api ? state.api : gcloud_api;
    }
  },
  actions: {
    async ping({state}) {
      axios.get(`${state.api}/ping`).then((response) => {
          return response.data
        }
      ).catch((error) => {
          console.error(error)
          return "error"
        }
      )

    },

  },
})

