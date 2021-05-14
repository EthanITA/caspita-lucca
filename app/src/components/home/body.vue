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
      <div class="md-layout" v-if="keyword.toLowerCase()!=='guoxiaofeng'">
        <md-field class="md-layout-item">
          <md-input v-model="keyword"/>
        </md-field>
      </div>
      <form v-else>
        <div class="columns is-vcentered">
          <md-field class="column">
            <md-icon>password</md-icon>
            <md-input v-model="private_login_password" type="password"/>
          </md-field>
          <md-button type="submit" @click.stop.prevent="submit()" class="column md-accent ">OK</md-button>
        </div>
      </form>
    </md-dialog>
  </div>
</template>

<script>
export default {
  name: "homepage_body",
  data: () => {
    return {
      login_form_showed: false,
      keyword: '',
      private_login_password: ""
    }
  },
  methods: {
    show_login_form(e) {
      e.preventDefault();
      this.login_form_showed = true
    },
    submit() {
      this.$store.dispatch("private_area_auth", this.private_login_password).then(response =>{
        console.log(response)
      }).catch(error =>{
        console.log(error)
      })
    }
  },
}
</script>

<style scoped>

.caspita_background {
  background-position: left;
  background-image: url("../../assets/images/store_scaled.jpg");
  background-attachment: fixed;

}
</style>
