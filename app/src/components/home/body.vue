<template>
  <div
    class="image ani-slide-in-bck-center ani-900 ani-timing-ease-out has-text-centered">
    <img
      alt="caspita logo"
      class="is-rounded is-unselectable"
      src="../../assets/brand/original/custom_caspita_icon.svg"/>
    <router-link to="/virtual_tour">
      <rounded-button description="Fai un tour" md_icon="tour"/>
    </router-link>


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
