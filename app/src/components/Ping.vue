<template>
  <div>
    <p>{{ this.$store.state.ping }}</p>
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
