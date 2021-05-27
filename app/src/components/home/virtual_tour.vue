<template>
  <caspita_app>
    <b-loading :active="!iframe_loaded" :is-full-page="false"/>
    <iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; vr"
            allowfullscreen="true"
            allowvr="true"
            frameborder="0" mozallowfullscreen="true" src="https://www.klapty.com/tour/tunnel/QV50KELvRk"
            style="width: 100vw;height: 100vh"
            webkitallowfullscreen="true"
            @load="iframe_loaded=true">

    </iframe>
  </caspita_app>
</template>
<script>
import Toolbar from "../header/toolbar";
import Caspita_app from "../caspita_app";
import Brand_logo from "../header/brand";

export default {
  components: {Brand_logo, Caspita_app, Toolbar},
  data: () => {
    return {
      iframe_loaded: false
    }
  }
}
</script>

<style scoped>
</style>
