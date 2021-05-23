<template>
  <b-tooltip :active="Boolean(tooltip)" :label="tooltip" :triggers="['hover','focus']" :position="tooltip_position">
    <md-button style="height:40px;padding:0;margin:0.25rem"
               :class="{
                      'md-raised':is_raised,
                      'button is-rounded':is_rounded && !is_icon,
                      'md-icon-button':is_icon
             }">
      <md-icon v-if="has_img && !is_icon">
        <img
          :style="icon_size"
          :src="img_src"
          :alt="img_alt"/>
      </md-icon>

      <md-icon v-else-if="md_icon"
               :style="icon_size"
      >
        {{ md_icon }}
      </md-icon>
      <img v-else
           :style="icon_size"
           :src="img_src" :alt="img_alt"
      />
      <span v-if="description && !is_icon" style="margin-left:0.5rem;">{{ description }}</span>
    </md-button>
  </b-tooltip>

</template>

<script>
export default {
  name: "rounded-button",
  props: {
    md_icon: {
      type: String,
    },
    is_icon: {
      type: Boolean,
      default: false
    },
    description: {
      type: String
    },
    has_img: {
      type: Boolean,
      default: false
    },
    img_src: {
      type: String,
    },
    img_alt: {
      type: String,
    },
    is_raised: {
      type: Boolean,
      default: true
    },
    is_rounded: {
      type: Boolean,
      default: true
    },
    tooltip: {
      type: String,
    },
    tooltip_position:{
      type:String,
      default:"is-bottom"
    }
  },
  data: () => {
    return {
      icon_size: "min-width:28px;width:auto;height:28px;"
    }
  }
}
</script>

<style scoped>

</style>
