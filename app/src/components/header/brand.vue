<template>
  <b-tooltip label="Caspita SRL: Tutto per la casa..."
             position="is-right"
             :triggers="['hover','focus']"
             style="margin-left: 0.5rem;">

    <router-link to="/" class="md-button md-icon-button"
                 style="height: auto;width: auto"
    >
      <img
        :class="{'animate__animated animate__rubberBand animate__delay-1s':anim_icon}"
        style="height:5rem;width: auto;"
        src="../../assets/brand/new_icon/caspita_icon.svg"
        alt="Caspita SRL brand"
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
