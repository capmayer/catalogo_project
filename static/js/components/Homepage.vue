<template>
  <div id="homepage">
    <div class="margin-top">
    <b-carousel id="carousel1"
                style="text-shadow: 1px 1px 2px #333;"
                controls
                indicators
                background="#ababab"
                :interval="4000"
                img-width="1024"
                img-height="480"
                v-model="slide"
    >
    <b-carousel-slide caption="First slide"
                      text="Nulla vitae elit libero, a pharetra augue mollis interdum."
                      img-src="https://lorempixel.com/1024/480/technics/2/"
    ></b-carousel-slide>
    </b-carousel>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sortDirection: '',
    }
  }
}
</script>

<style>
#homepage{
  color:blue;
}
.margin-top{
  margin-top: 50px;
}
</style>
