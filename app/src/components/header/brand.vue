<template>
  <b-tooltip label="Caspita SRL: Tutto per la casa..."
             position="is-right"
             :triggers="['hover','focus']">

    <router-link to="/" class="md-button md-icon-button"
                 style="height: auto;width: auto"
    >
      <img
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
}
</script>

<style scoped>

</style>
