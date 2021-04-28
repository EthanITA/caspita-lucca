<template>
  <md-app md-waterfall mode="fixed">
    <md-app-toolbar class="is-large">
      <div class="md-toolbar-row">
        <div class="md-toolbar-section-start">
          <brand_logo/>
        </div>
        <div class="md-toolbar-section-end">
          <menu_option/>
        </div>
      </div>
    </md-app-toolbar>
    <md-app-content>
      <body/>
      <below_body/>
    </md-app-content>
  </md-app>
</template>

<script>


import brand_logo from "@/components/home/brand_logo";
import Body from "@/components/home/body";
import Below_body from "@/components/home/below_body";
import Menu_option from "@/components/home/menu";
export default {
  name: 'homepage',
  components: {Menu_option, Below_body, Body, brand_logo},
  data() {
    return {
      msg: "",
    };
  },
  methods: {},
  created() {
    console.log(this.msg);
    this.$store.dispatch("ping")
  },
};
</script>
<style scoped>
</style>
