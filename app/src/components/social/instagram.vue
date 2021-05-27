<template>
  <div>
    <rounded-button :description="text"
                    :has_img="true" :img_alt="icon_alt" :img_src="icon" :is_icon="is_icon" :is_raised="is_icon"
                    :tooltip="link_title" @click.native="open_instagram"
    />
  </div>
</template>

<script>
import RoundedButton from "../utilities/rounded-button";

export default {
  name: "instagram_option",
  components: {RoundedButton},
  props: {
    is_icon: {
      type: Boolean,
      required: true,
    }
  },
  data() {
    return {
      link: this.$store.state.instagram.link,
      link_title: "Caspita su Instagram",
      icon: require("@/assets/icons/instagram_icon.svg"),
      icon_alt: "Icona Instagram",
      text: this.$store.state.instagram.text
    }
  },
  methods: {
    open_instagram() {
      window.open(this.link, '_blank')
    }
  }
}
</script>

<style scoped>

</style>
