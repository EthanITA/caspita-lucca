<template>
  <md-button :href="link" target="_blank"
             class="md-button has-text-centered"
             :class="is_icon ? 'md-icon-button md-raised':''"
             :style="is_icon ? '' : 'margin:0.5rem'"
  >
    <img style="min-width:28px;width:auto;height:28px;"
         :src="icon_src" :alt="icon_alt"
    />
    <span v-if="!is_icon" style="margin-left:0.5rem;">
      {{ button_text }}
    </span>
    <md-tooltip >{{ link_title }}</md-tooltip>

  </md-button>
</template>

<script>
export default {
  name: "social_template",
  props: {
    link: {
      required: true,
      type: String
    },
    link_title: {
      type: String,
      default: ""
    },
    icon_src: {
      required: true,
      type: String
    },
    icon_alt: {
      type: String,
      default: ""
    },
    button_text: {
      type: String,
      default: ""
    },
    is_icon: {
      type: Boolean,
      required: true
    }
  },
}
</script>

<style scoped>

</style>
