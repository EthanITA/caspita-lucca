<template>
  <div>
    <loader v-if="!this.$store.state.homepage_loader_loaded"/>
    <div v-else>

      <section class="hero is-warning is-bold is-fullheight ani-slide-in-left ani-800"
      >
        <!-- Hero head: will stick at the top -->
        <div class="hero-head ">
          <toolbar/>
        </div>

        <!-- Hero content: will be in the middle -->
        <div class="hero-body">
          <div class="container">
            <homepage_body/>
          </div>
        </div>

        <!-- Hero footer: will stick at the bottom -->
      </section>
    </div>
  </div>
</template>

<script>


import Below_body from "./below_body";
import Homepage_body from "./body";
import Loader from "./loader";
import Toolbar from "../header/toolbar";

export default {
  name: 'homepage',
  components: {Toolbar, Loader, Homepage_body, Below_body},
  mounted() {
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
