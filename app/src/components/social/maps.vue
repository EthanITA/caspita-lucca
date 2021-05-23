<template>
  <div>
    <rounded-button @click.native="open_gmaps"
                    :is_icon="is_icon" :has_img="true" :img_src="gmaps_icon" :img_alt="gmaps_alt" :tooltip="gmaps_title"
                    :is_raised="is_icon"
                    :description="text"
    />
  </div>
</template>

<script>
import RoundedButton from "../utilities/rounded-button";

export default {
  name: "gmaps_option",
  components: {RoundedButton},
  props: {
    is_icon: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      gmaps_link: this.$store.state.google_maps.link,
      gmaps_title: "Caspita su Google Maps",
      gmaps_icon: require("@/assets/icons/google_maps_icon.svg"),
      gmaps_alt: "Icona Google Maps",
      text: this.$store.state.google_maps.text
    }
  },
  methods: {
    open_gmaps() {
      window.open(this.gmaps_link, '_blank');
    }
  }
}
</script>
