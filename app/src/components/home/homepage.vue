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
        <md-app-content class="hero" style="padding: 0">
          <homepage_body class="hero-body"/>
        </md-app-content>
        <md-app-content>
          <below_body/>
        </md-app-content>
      </md-app>
    </div>


  </div>
</template>

<script>


import Below_body from "@/components/home/below_body";
import Homepage_body from "./body";
import Loader from "./loader";
import Brand_logo from "@/components/header/caspita_logo";
import Menu_option from "@/components/header/menu";

export default {
  name: 'homepage',
  components: {Menu_option, Brand_logo, Loader, Homepage_body, Below_body},
};
</script>
<style scoped>
</style>
