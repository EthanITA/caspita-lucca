<template>
  <div>
    <md-dialog :md-active.sync="qrcode_showed">
      <md-dialog-title>QR Code di Caspita</md-dialog-title>
      <div ref="qart" class="column">
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="save_qrcode">
          Salva QR Code
        </md-button>
      </md-dialog-actions>
    </md-dialog>
    <md-button @click="show_qrcode_dialog(true)" class="md-button has-text-centered md-icon-button md-raised"
    >
      <md-icon class="material-icons-two-tone">qr_code_2</md-icon>
      <md-tooltip>QR Code del sito</md-tooltip>

    </md-button>
  </div>
</template>

<script>
import QArt from 'qartjs';


export default {
  name: "qr_code",
  data: () => {
    return {
      qrcode_showed: false,
      config: {
        value: window.location.href,
        imagePath: require("@/assets/brand/new_icon/caspita_icon.svg"),
        filter: "color"
      },
    }
  },
  methods: {
    save_qrcode() {
      const link = document.createElement('a');
      link.download = 'caspita_qrcode.png';
      link.href = this.$refs.qart.children[0].toDataURL()
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
  }
}
</script>

<style scoped>
</style>
