<template>
  <div>
    <section class="section hero is-fullheight">
      <div class="hero-head">

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
