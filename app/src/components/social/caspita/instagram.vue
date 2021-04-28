<template>
  <social_template :link="link" :link_title="link_title" :is_icon="is_icon"
                   :icon_src="icon" :icon_alt="icon_alt" :button_text="text"/>
</template>

<script>
import social_template from "@/components/social/caspita/template";

export default {
  name: "instagram_option",
  components: {social_template},
  props: {
    is_icon: {
      type: Boolean,
      required: true,
    }
  },
  data() {
    return {
      link: "https://www.instagram.com/caspita_srl/",
      link_title: "Caspita SRL su Instagram",
      icon: require("@/assets/icons/instagram_logo.svg"),
      icon_alt: "Icona Instagram",
      text: "Instagram"
    }
  },
}
</script>

<style scoped>

</style>
