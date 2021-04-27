<template>
  <div>
    <nav class="navbar docs-navbar is-spaced has-shadow is-primary is-transparent">
      <div class="container">
        <div class="navbar-brand is-vcentered">
          <img
            src="../assets/brand_logo.png"
            alt="Caspita SRL brand" style="height: 3.25rem; width:auto"
          />
        </div>
      </div>
    </nav>
    <section class="section hero is-fullheight is-link">
      <div class="hero-head ">
        <b-navbar>
        </b-navbar>
      </div>
      <p>{{ this.$store.state.ping }}</p>
    </section>
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
