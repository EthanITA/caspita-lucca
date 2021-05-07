<template>
  <div class="is-flex is-align-items-center is-justify-content-center caspita_background
  ani-timing-ease-out ani-bg-pan-left ani-10000">

    <div
      class="box"
      :class="box_logo_animation"
      style="background-color: rgba(255,255,255,0.55)">
      <b-image
        :src="require('@/assets/brand/caspita_logo_full_original.png')"
      />
      <div
        class="content">
        <p class="text has-text-centered has-text-weight-bold">
          Caspita SRL - Via Nuova per Pisa, 354, Lucca (LU)
        </p>
      </div>
    </div>
    <div class=""/>
  </div>
</template>

<script>

export default {
  name: "homepage_body",
  data() {
    return {
      bg_loaded: true,
      box_logo_animation: 'ani-slide-in-blurred-top ani-timing-ease-out ani-1200',
      logo_showed: true
    }
  },
  methods: {
    box_clicked() {
      const box_flip_time = 800
      this.box_logo_animation = 'ani-flip-2-hor-top-1 ani-timing-ease-out ' + 'ani-' + box_flip_time
      setTimeout(() => {
        this.box_logo_animation = ''
        this.logo_showed = !this.logo_showed
      }, box_flip_time)
    }
  },
}
</script>

<style scoped>
.h_center {
  margin: auto;

}

.caspita_background {
  background-position: left;
  height: 100%;
  background-image: url("../../assets/images/store_scaled.jpg");
  background-attachment: fixed;

}

.gray_layer_background {

  background-color: rgba(255, 255, 255, 0.1);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.container_center {
  justify-content: center;
  align-items: center;
  display: flex
}
</style>
