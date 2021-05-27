<template>
  <div>
    <md-dialog :md-active.sync="qrcode_showed" :md-fullscreen="false" class="has-text-centered">
      <md-dialog-title class="is-size-3">
        QR Code
      </md-dialog-title>
      <md-dialog-content class="content">
        <div ref="qart"/>
        <a :href="config.value" class="has-text-info is-size-5">{{ config.value }}</a>
      </md-dialog-content>
      <md-dialog-actions>
        <md-button class="md-primary" @click="save_qrcode">
          Salva QR Code
        </md-button>
      </md-dialog-actions>
    </md-dialog>
    <rounded-button :is_icon="is_icon" :is_raised="is_icon" :tooltip="is_icon?'QR Code di Caspita':''"
                    description="QR Code" md_icon="qr_code_2"
                    @click.native="show_qrcode_dialog(true)"/>
  </div>
</template>

<script>
import QArt from 'qartjs';
import RoundedButton from "../utilities/rounded-button";

export default {
  name: "qr_code",
  components: {RoundedButton},
  props: {
    is_icon: {
      type: Boolean,
      default: true
    }
  },
  data: () => {
    return {
      qrcode_showed: false,
      config: {
        value: "",
        imagePath: require("../../assets/brand/new_icon/caspita_icon.svg"),
        filter: "color",
        size: 500
      },
    }
  },
  methods: {
    save_qrcode() {
      const link = document.createElement('a');
      link.download = 'caspita_qrcode.png';
      link.href = this.$refs.qart.children[0].toDataURL('image/png')
      link.click();
      link.delete;
    },
    show_qrcode_dialog() {
      this.qrcode_showed = true
      setTimeout(() => {
        new QArt(this.config).make(this.$refs.qart);
      }, 5)
    }
  },
  mounted() {
    this.config.value = this.$store.getters.is_production ?
      window.location.href : "https://caspitasrl.github.io/lucca"
  }
}
</script>

<style scoped>
</style>
