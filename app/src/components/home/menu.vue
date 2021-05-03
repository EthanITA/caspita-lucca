<template>
  <div>
    <div class="md-xsmall-hide">
      <gmaps_option :is_icon="true"/>
      <instagram_option :is_icon="true"/>
      <social_share/>
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

export default {
  name: "menu_option",
  components: {Social_share, Instagram_option, Gmaps_option},
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
