<template>
  <div>
    <loader v-if="!this.$store.state.homepage_loader_loaded"/>
    <div v-show="this.$store.state.homepage_loader_loaded">

      <caspita_app has_animation full_navbar>
        <div class="container">
          <Homepage_body/>
        </div>
        <template #below>
          <below_body/>
        </template>
      </caspita_app>

    </div>

  </div>
</template>

<script>


import Below_body from "./below_body";
import Homepage_body from "./body";
import Loader from "./loader";
import Toolbar from "../header/toolbar";
import Caspita_app from "../caspita_app";

export default {
  name: 'homepage',
  components: {Caspita_app, Toolbar, Loader, Homepage_body, Below_body},
  mounted() {
    if (this.$store.getters.is_production)
      this.$store.dispatch("ping")
  }
};
</script>
<style>

body > div.md-menu-content-bottom-end.md-menu-content-auto.md-menu-content.md-theme-default > div > ul {
  padding: 0
}

body > div.md-menu-content-bottom-start.md-menu-content-auto.md-menu-content.md-theme-default > div > ul {
  padding: 0
}
</style>
