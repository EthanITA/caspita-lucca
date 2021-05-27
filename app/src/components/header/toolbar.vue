<template>
  <div>
    <header :style="this.$store.state.background_color_style"
            class="columns is-vcentered is-mobile navbar is-fixed-top" style="z-index: 1">
      <div class="column">
        <brand_logo :anim_icon="anim_icon"/>
      </div>
      <div class="column">
        <menu_option class="is-justify-content-flex-end"/>
      </div>
    </header>
  </div>
</template>

<script>
import Brand_logo from "./brand";
import Menu_option from "./menu";

export default {
  name: "toolbar",
  components: {Menu_option, Brand_logo},
  props: {
    anim_icon: {
      default: false,
      type: Boolean
    }
  }
}
</script>

<style scoped>
.column {
  padding-bottom: 0
}
</style>
