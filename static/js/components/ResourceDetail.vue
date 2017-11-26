<template>
  <div id="resource-detail">
    <h1>{{ resource }}</h1>
  </div>
</template>

<script>
export default {
  data(){
    return {
      resource: '',
    }
  },
  mounted(){
    this.$http.get("/api"+window.location.pathname+"?format=json").then( (req) => this.resource = req.data )
  }
}
</script>

<style>
</style>
