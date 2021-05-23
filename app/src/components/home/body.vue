<template>
  <div v-show="this.$store.state.homepage_loader_loaded"
       class="ani-timing-ease-out ani-bg-pan-left ani-10000">
    <div
      class="image ani-slide-in-elliptic-right-bck ani-1300 ani-timing-ease-out">
      <img
        class="is-rounded"
        src="../../assets/brand/original/caspita_icon.svg"
        alt="caspita logo"/>
      <router-link to="/virtual_tour">
        <rounded-button md_icon="tour" description="Fai un tour"/>
      </router-link>


    </div>
  </div>
</template>

<script>

import RoundedButton from "../utilities/rounded-button";

export default {
  name: "homepage_body",
  components: {RoundedButton},
}
</script>

<style scoped>

.caspita_background {
  background-position: left;
  background-image: url("../../assets/images/store_scaled.jpg");
  background-attachment: fixed;

}
</style>
