<template>
  <div class="is-flex is-align-items-center is-justify-content-center caspita_background
  ani-timing-ease-out ani-bg-pan-left ani-10000">

    <div
      class="has-text-centered image
      ani-slide-in-elliptic-right-bck ani-1300 ani-timing-ease-out">
      <img
        class="is-rounded"
        src="../../assets/brand/original/caspita_icon.svg"
        alt="caspita logo"/>
      <router-link to="/virtual_tour" tag="button" class="button is-rounded">
        <span class="icon is-small">
          <md-icon>tour</md-icon>
        </span>
        <span>Fai un Tour</span>
      </router-link>


    </div>
  </div>
</template>

<script>

export default {
  name: "homepage_body",
}
</script>

<style scoped>

.caspita_background {
  background-position: left;
  background-image: url("../../assets/images/store_scaled.jpg");
  background-attachment: fixed;

}
</style>
