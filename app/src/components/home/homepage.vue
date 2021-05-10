<template>
  <div>
    <loader/>
    <div v-show="this.$store.state.homepage_loader_loaded" class="ani-slide-in-left ani-800">
      <md-app style="height: 100vh;">
        <md-app-toolbar>
          <div class="md-toolbar-row">
            <div class="md-toolbar-section-start">
              <brand_logo/>
            </div>
            <div class="md-toolbar-section-end">
              <menu_option/>
            </div>
          </div>
        </md-app-toolbar>
        <md-divider/>
        <md-app-content class="hero" style="padding: 0">
          <homepage_body class="hero-body"/>
        </md-app-content>
      </md-app>
    </div>


  </div>
</template>

<script>


import brand_logo from "@/components/home/brand_logo";
import Below_body from "@/components/home/below_body";
import Menu_option from "@/components/home/menu";
import Homepage_body from "./body";
import Loader from "./loader";

export default {
  name: 'homepage',
  components: {Loader, Homepage_body, Menu_option, Below_body, brand_logo},
};
</script>
<style scoped>

</style>
