<template>
  <md-menu md-size="auto" md-direction="bottom-start" md-align-trigger :md-active.sync="share_menu_enabled">
    <md-button style="height:40px" class="md-button-spaced" md-menu-trigger>
      <md-icon class="md-button-content" style="min-width:28px;width:auto;height:28px;">
        {{ share_icon }}
      </md-icon>
      <span class="md-button-content" style="margin-left:0.5rem;">{{ share_text }}</span>
    </md-button>

    <md-menu-content>
      <ShareNetwork v-for="network in networks"
                    :key="network.text"
                    :network="network.network"
                    :url="$store.state.google_maps.link"
                    title="Caspita SRL - centro del risparmio a Lucca"
                    description="Tutto per la casa... Tantissimi prodotti di buona qualità a prezzo contenuto, vieni a trovarci!"
      >
        <md-button class="md-button-spaced "
        >
          <md-icon>
            <img style="min-width:28px;width:auto;height:28px;"
                 :src=" require('@/assets/icons/'+network.network + '_icon.svg')"
                 :alt="'Icona ' + network.text"/>
          </md-icon>
          <span style="margin-left:0.5rem;"> {{ network.text }}</span>
        </md-button>
        <md-divider/>
      </ShareNetwork>
    </md-menu-content>
  </md-menu>
</template>

<script>

export default {
  name: "social_share",
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
