<template>
  <div class="md-app">

    <div class="md-toolbar">
      <div class="md-toolbar-row">
        <div class="md-toolbar-section-start">
          <a href="/" class="router-link-exact-active md-button"
             style="height: 3.25rem;width: auto"
             title="Caspita SRL: Tutto per la casa...">
            <img
              style="height: 3.25rem;width: auto"

              src="../assets/brand_logo.png"
              alt="Caspita SRL brand"

            />
          </a>
        </div>
        <div class="md-toolbar-section-end">
          <a href="https://g.page/caspitaSRL-lucca" target="_blank"
             class="md-button md-icon-button has-text-centered"
             style="height: 2.5rem;width: auto"
             title="Caspita SRL su Google Maps"
          >
            <img
              style="height: 2.5rem;width: auto"
              src="../assets/google_maps_icon.png"
              alt="Caspita SRL su Google Maps"
            />
          </a>

        </div>
      </div>

    </div>
  </div>
</template>

<script>

export default {
  name: 'Ping',
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
<style>
</style>
