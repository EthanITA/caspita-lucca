<template>
  <div v-if="loader_show" class="is-justify-content-center">
    <img :src="require('@/assets/brand/caspita_icon.png')"
         class="is-flex animate__animated animate__infinite animate__slow"
         @load="on_logo_load" :rounded="true" style="  display: block;
  margin-left: auto;
  margin-right: auto;height: 180px;width:210px"
         alt="Icona Caspita SRL" :class="animation"/>
  </div>
</template>

<script>

export default {
  name: "loader",
  data() {
    return {
      loader_show: true,
      animation: ''
    }
  },
  methods: {
    on_logo_load() {
      this.animation = "animate__heartBeat"
      setTimeout(() => {
        this.animation = "animate__rollOut"
      }, 1500)
    }
  }
}
</script>

<style scoped>

</style>
