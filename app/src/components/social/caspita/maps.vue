<template>
  <social_template :link="gmaps_link" :link_title="gmaps_title" :is_icon="is_icon"
                   :icon_src="gmaps_icon" :icon_alt="gmaps_alt" :button_text="text"/>
</template>

<script>
import social_template from "@/components/social/caspita/template";

export default {
  name: "gmaps_option",
  components: {social_template},
  props: {
    is_icon: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      gmaps_link_web: "https://g.page/caspitaSRL-lucca",
      gmaps_link: "https://maps.app.goo.gl/UNLD1YJkm6N92RYT7",
      gmaps_title: "Caspita su Google Maps",
      gmaps_icon: require("@/assets/icons/google_maps_icon.svg"),
      gmaps_alt: "Icona Google Maps",
      text: "Google Maps"
    }
  }
}
</script>
