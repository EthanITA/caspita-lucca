<template>
  <md-menu :md-active.sync="share_menu_enabled" md-align-trigger md-direction="bottom-start" md-size="auto">
    <rounded-button :description="share_text" :is_raised="false" :md_icon="share_icon"
                    @click.native="share_menu_enabled=!share_menu_enabled"
    />

    <md-menu-content>
      <ShareNetwork v-for="network in networks"
                    :key="network.text"
                    :network="network.network"
                    :url="$store.state.google_maps.link"
                    description="Tutto per la casa... Tantissimi prodotti di buona qualità a prezzo contenuto, vieni a trovarci!"
                    title="Caspita SRL - centro del risparmio a Lucca"
      >
        <rounded-button :description="network.text" :has_img="true"
                        :img_alt="'Icona ' + network.text"
                        :img_src="require('@/assets/icons/'+network.network + '_icon.svg')"
                        :is_raised="false"
        />
        <md-divider/>
      </ShareNetwork>
    </md-menu-content>
  </md-menu>
</template>

<script>

import RoundedButton from "../utilities/rounded-button";

export default {
  name: "social_share",
  components: {RoundedButton},
  data() {
    return {
      share_icon: "share",
      share_text: "Condividi",
      share_menu_enabled: false,
      networks: [
        {network: "email", text: "Email"},
        {network: "facebook", text: "Facebook"},
        //{network: "line", text: "Line"},
        //{network: "linkedin", text: "LinkedIn"},
        {network: "messenger", text: "Messenger"},
        //{network: "pinterest", text: "Pinterest"},
        //{network: "reddit", text: "Reddit"},
        {network: "telegram", text: "Telegram"},
        {network: "twitter", text: "Twitter"},
        {network: "whatsapp", text: "WhatsApp"},
      ]
    }
  },
}
</script>

<style scoped>
</style>
