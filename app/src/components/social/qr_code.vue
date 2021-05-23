<template>
  <div>
    <md-dialog :md-fullscreen="false" :md-active.sync="qrcode_showed">
      <md-dialog-title>QR Code di Caspita</md-dialog-title>
      <div ref="qart">
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="save_qrcode">
          Salva QR Code
        </md-button>
      </md-dialog-actions>
    </md-dialog>
    <rounded-button @click.native="show_qrcode_dialog(true)" :is_icon="is_icon" md_icon="qr_code_2"
                    :tooltip="is_icon?'QR Code di Caspita':''" :is_raised="is_icon"
                    description="QR Code"/>
  </div>
</template>

<script>
import QArt from 'qartjs';
import RoundedButton from "../utilities/rounded-button";

const qrcode_link = process.env.NODE_ENV === 'production' ? window.location.href : "https://caspitasrl.github.io/lucca"
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
        value: qrcode_link,
        imagePath: require("@/assets/brand/new_icon/caspita_icon.svg"),
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
  }
}
</script>

<style scoped>
</style>
