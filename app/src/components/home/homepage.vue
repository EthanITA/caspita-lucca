<template>
  <div>
    <loader/>
    <toolbar v-show="this.$store.state.homepage_loader_loaded" class="ani-slide-in-left ani-800"/>
    <div v-show="this.$store.state.homepage_loader_loaded" class="ani-slide-in-left ani-800">
      <md-app style="height:auto;" mode="fixed">
        <md-divider/>
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
import Toolbar from "@/components/header/toolbar";

export default {
  name: 'homepage',
  components: {Toolbar, Loader, Homepage_body, Below_body},
};
</script>
<style scoped>
</style>
