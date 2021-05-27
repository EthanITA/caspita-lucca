<template>
  <b-tooltip :triggers="['hover','focus']"
             label="Caspita SRL: Tutto per la casa..."
             position="is-right"
             style="margin-left: 0.5rem;">

    <router-link class="md-button md-icon-button" style="height: auto;width: auto"
                 to="/"
    >
      <img
        :class="{'animate__animated animate__rubberBand animate__delay-1s':anim_icon}"
        alt="Caspita SRL brand"
        src="../../assets/brand/new_icon/caspita_icon.svg"
        style="height:5rem;width: auto;"
      />
    </router-link>
  </b-tooltip>
</template>

<script>
export default {
  name: "brand_logo",
  props: {
    anim_icon: {
      default: false,
      type: Boolean
    }
  }
}
</script>

<style scoped>

</style>
