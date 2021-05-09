import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

const gcloud_api = 'https://caspita-lucca.ew.r.appspot.com/api';
const heroku_api = 'https://caspita-lucca.herokuapp.com/';

function api_call_strategy(axios_http_method, api, on_success, on_failure) {
  let main_url = Vuex.$store.state.api
  let secondary_url = main_url === gcloud_api ? heroku_api : gcloud_api
  axios_http_method(`${main_url}/${api}`).then(
    (response) => {
      return on_success(response)
    }
  ).catch(
    (error) => {
      console.warn(`${main_url}: ${error}`)
      axios_http_method(`${secondary_url}/${api}`).then(
        (response) => {
          return on_success(response)
        }
      ).catch(
        (error) => {
          console.error(`${secondary_url}: ${error}`)
          return on_failure(error)
        }
      )
    }
  )
}

export default new Vuex.Store({
  state: {
    api: gcloud_api,
    ping: "",
    google_maps: {
      link: "https://maps.app.goo.gl/UNLD1YJkm6N92RYT7",
      link_web: "https://g.page/caspitaSRL-lucca",
      text: "Google Maps"
    },
    instagram: {
      link: "https://www.instagram.com/caspita_srl/",
      text: "Instagram"
    },
    loaded: false
  },
  mutations: {
    // eslint-disable-next-line camelcase
    setApi(state, is_heroku) {
      state.api = is_heroku ? heroku_api : gcloud_api;
    },
    set_loaded_home_page(state, loaded) {
      state.loaded = loaded
    }
  },
  getters: {
    getApi(state) {
      return state.api ? state.api : gcloud_api;
    },
    get_loaded(state) {
      return state.loaded;
    }
  },
  actions: {
    async ping({state}) {
      axios.get(`${state.api}/ping`).then((response) => {
          console.log(response.data)
          state.ping = response.data;
        }
      ).catch((error) => {
          console.error(error)
          state.ping = "error"
        }
      )

    },

  },
})

