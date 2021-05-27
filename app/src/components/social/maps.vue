<template>
  <div>
    <rounded-button :description="text"
                    :has_img="true" :img_alt="gmaps_alt" :img_src="gmaps_icon" :is_icon="is_icon" :is_raised="is_icon"
                    :tooltip="gmaps_title"
                    @click.native="open_gmaps"
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
