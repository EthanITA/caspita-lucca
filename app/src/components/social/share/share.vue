<template>
  <md-menu md-size="auto" md-direction="bottom-start" md-align-trigger :md-active.sync="share_menu_enabled">
    <rounded-button :md_icon="share_icon" :description="share_text" md-menu-trigger/>

    <md-menu-content>
      <ShareNetwork v-for="network in networks"
                    :key="network.text"
                    :network="network.network"
                    :url="$store.state.google_maps.link"
                    title="Caspita SRL - centro del risparmio a Lucca"
                    description="Tutto per la casa... Tantissimi prodotti di buona qualità a prezzo contenuto, vieni a trovarci!"
      >
        <rounded-button :has_img="true" :img_src="require('@/assets/icons/'+network.network + '_icon.svg')"
                        :img_alt="'Icona ' + network.text" :description="network.text"
                        :is_raised="false"
        />
        <md-divider/>
      </ShareNetwork>
    </md-menu-content>
  </md-menu>
</template>

<script>

import RoundedButton from "../../rounded-button";

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
