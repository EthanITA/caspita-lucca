<template>
  <div class="navbar-item">
    <div class="md-xsmall-hide md-layout">
      <gmaps_option :is_icon="true" class="md-layout-item "/>
      <instagram_option :is_icon="true" class="md-layout-item"/>
      <qr_code class="md-layout-item"/>
      <social_share class="md-layout-item"/>
    </div>
    <div class="md-xsmall-show">
      <md-menu class=" is-justify-content-flex-end is-flex" md-direction="bottom-end" md-size="auto">

        <md-button class="md-icon-button" md-menu-trigger>
          <md-icon>more_vert</md-icon>
        </md-button>

        <md-menu-content>

          <gmaps_option :is_icon="false"/>

          <md-divider/>

          <instagram_option :is_icon="false"/>

          <md-divider/>

          <qr_code :is_icon="false"/>

          <md-divider/>

          <social_share/>

        </md-menu-content>
      </md-menu>
    </div>
  </div>
</template>

<script>
import Gmaps_option from "../social/maps";
import Instagram_option from "../social/instagram";
import Social_share from "../social/share";
import Qr_code from "../social/qr_code";

export default {
  name: "menu_option",
  components: {Qr_code, Social_share, Instagram_option, Gmaps_option},
}
</script>

<style scoped>
@media (max-width: 600px) {
  .md-xsmall-hide {
    display: none
  }
}

@media (min-width: 601px) {
  .md-xsmall-show {
    display: none;
  }
}

</style>
