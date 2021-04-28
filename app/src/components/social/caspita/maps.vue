<template>
  <social_template :link="gmaps_link" :link_title="gmaps_title" :is_icon="is_icon"
                   :icon_src="gmaps_icon" :icon_alt="gmaps_alt" :button_text="text"/>
</template>

<script>
import social_template from "@/components/social/caspita/template";

export default {
  name: "gmaps_option",
  components: {social_template},
  props:{
    is_icon: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      gmaps_link: "https://g.page/caspitaSRL-lucca",
      gmaps_title: "Caspita SRL su Google Maps",
      gmaps_icon: require("@/assets/google_maps_logo.svg"),
      gmaps_alt: "Icona Google Maps",
      text: "Google Maps"
    }
  }
}
</script>
