<template>
  <div>
    <md-dialog :md-fullscreen="false" :md-active.sync="qrcode_showed">
      <md-dialog-title>QR Code di Caspita</md-dialog-title>
      <div ref="qart" class="column">
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="save_qrcode">
          Salva QR Code
        </md-button>
      </md-dialog-actions>
    </md-dialog>
    <md-button @click="show_qrcode_dialog(true)"
               class="md-button has-text-centered"
               :class="is_icon ? 'md-icon-button md-raised':''"
               :style="is_icon ? '' : 'margin:0.5rem'"
    >
      <md-icon class="material-icons-two-tone" style="min-width:28px;width:auto;height:28px;">qr_code_2</md-icon>
      <span v-if="!is_icon" style="margin-left:0.5rem;">
        QR Code
      </span>
      <md-tooltip>QR Code del sito</md-tooltip>

    </md-button>
  </div>
</template>

<script>
import QArt from 'qartjs';

const qrcode_link = process.env.NODE_ENV === 'production' ? window.location.href : "https://caspitasrl.github.io/lucca"
export default {
  name: "qr_code",
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
