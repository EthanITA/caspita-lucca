<template>
  <div class="is-flex is-align-items-center is-justify-content-center caspita_background
  ani-timing-ease-out ani-bg-pan-left ani-10000">

    <div
      class="has-text-centered image
      ani-slide-in-elliptic-right-bck ani-1300 ani-timing-ease-out">
      <img
        class="is-rounded"
        @contextmenu="show_login_form($event)"
        src="../../assets/brand/original/caspita_icon_original.svg"
        alt="caspita logo"/>
      <router-link to="/virtual_tour" tag="button" class="button is-rounded">
        <span class="icon is-small">
          <md-icon>tour</md-icon>
        </span>
        <span>Fai un Tour</span>
      </router-link>


    </div>
    <md-dialog :md-active.sync="login_form_showed">
      <md-input v-if="keyword!=='guoxiaofeng'" v-model="keyword"/>
      <form v-else>
        <button onsubmit="submit">q</button>
      </form>
    </md-dialog>
  </div>
</template>

<script>
import {validationMixin} from 'vuelidate'
import {
  required,
  email,
  minLength,
  maxLength
} from 'vuelidate/lib/validators'

export default {
  name: "homepage_body",
  mixins: [validationMixin],
  data() {
    return {
      login_form_showed: false,
      keyword: '',
    }
  },
  validations: {
    username: {
      required,

    }
  },
  methods: {
    show_login_form(e) {
      e.preventDefault();
      this.login_form_showed = true
    }
  }
}
</script>

<style scoped>

.caspita_background {
  background-position: left;
  background-image: url("../../assets/images/store_scaled.jpg");
  background-attachment: fixed;

}
</style>
