<template>
    <md-toolbar>
      <div class="md-toolbar-row">
        <div class="md-toolbar-section-start">
          <brand_logo/>
        </div>
        <div class="md-toolbar-section-end">
          <menu_option/>
        </div>
      </div>
    </md-toolbar>
</template>

<script>
import Brand_logo from "@/components/header/caspita_logo";
import Menu_option from "@/components/header/menu";
export default {
  name: "toolbar",
  components: {Menu_option, Brand_logo}
}
</script>

<style scoped>

</style>
