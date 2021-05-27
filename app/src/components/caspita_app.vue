<template>
  <div>
    <div v-if="full_navbar">

      <div
        :style="this.$store.state.background_color_style">

        <section class="hero is-bold is-fullheight "


        >
          <!-- Hero head: will stick at the top -->
          <div class="hero-head ">
            <slot name="header">
              <toolbar :anim_icon="has_animation"/>
            </slot>
          </div>

          <!-- Hero content: will be in the middle -->
          <div :class="{'ani-scale-in-tl ani-800':has_animation}" class="hero-body">
            <slot/>
          </div>

          <!-- Hero footer: will stick at the bottom -->
          <div class="hero-foot">
            <slot name="footer"/>
          </div>
        </section>

      </div>
      <slot name="below"/>
    </div>
    <div v-else :style="this.$store.state.background_color_style">
      <brand_logo style="position: fixed"></brand_logo>
      <slot/>
    </div>
  </div>
</template>

<script>
import Toolbar from "./header/toolbar";
import Below_body from "./home/below_body";
import Brand_logo from "./header/brand";

export default {
  name: "caspita_app",
  components: {Brand_logo, Below_body, Toolbar},
  props: {
    has_animation: Boolean,
    full_navbar: Boolean
  }

}
</script>

<style scoped>

</style>
