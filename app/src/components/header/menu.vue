<template>
  <div>
    <div class="md-xsmall-hide md-layout">
      <gmaps_option :is_icon="true" class="md-layout-item"/>
      <instagram_option :is_icon="true" class="md-layout-item"/>
      <qr_code class="md-layout-item"/>
      <social_share class="md-layout-item"/>
    </div>
    <div class="md-xsmall-show">
      <md-menu md-size="auto"  md-direction="bottom-start">

        <md-button md-menu-trigger class="md-icon-button">
          <md-icon>more_vert</md-icon>
        </md-button>

        <md-menu-content>

          <md-menu-item>
            <gmaps_option :is_icon="false"/>
          </md-menu-item>

          <md-divider/>

          <md-menu-item>
            <instagram_option :is_icon="false"/>
          </md-menu-item>

          <md-divider/>

          <md-menu-item >
            <social_share class="has-text-centered"/>
          </md-menu-item>
        </md-menu-content>
      </md-menu>
    </div>
  </div>
</template>

<script>
import Gmaps_option from "@/components/social/caspita/maps";
import Instagram_option from "@/components/social/caspita/instagram";
import Social_share from "@/components/social/share/share";
import Qr_code from "../social/share/qr_code";

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
