<template>
  <div>
    <section class="section hero is-fullheight is-link">
      <div class="hero-head ">
        <b-navbar>
          <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
              <b-image
                :src="require(`@/assets/logo.png`)"
                alt="Caspita SRL brand"
              />
            </b-navbar-item>
          </template>
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
