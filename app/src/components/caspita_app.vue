<template>
  <div>
    <div :style="this.$store.state.background_color_style">

      <section class="hero is-bold is-fullheight "


      >
        <!-- Hero head: will stick at the top -->
        <div class="hero-head ">
          <slot name="header">
            <toolbar :anim_icon="is_home"/>
          </slot>
        </div>

        <!-- Hero content: will be in the middle -->
        <div class="hero-body" :class="{'ani-scale-in-tl ani-800':is_home}">
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
</template>

<script>
import Toolbar from "./header/toolbar";
import Below_body from "./home/below_body";

export default {
  name: "caspita_app",
  components: {Below_body, Toolbar},
  props: {
    is_home: {
      default: false,
      type: Boolean
    }
  }

}
</script>

<style scoped>

</style>
