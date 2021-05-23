<template>
  <header class="columns is-vcentered is-mobile">

    <div class="column" style="margin-left: 0.5rem">
      <brand_logo/>
    </div>
    <div class="column">
      <menu_option class="is-justify-content-flex-end"/>
    </div>
  </header>
</template>

<script>
import Brand_logo from "./brand";
import Menu_option from "./menu";

export default {
  name: "toolbar",
  components: {Menu_option, Brand_logo}
}
</script>

<style scoped>

</style>
