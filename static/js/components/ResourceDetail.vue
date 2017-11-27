<template>
  <div id="resource-detail">
    <hr>
    <div class="row margin-top">
      <div class="col-md-3">
          <b-card no-body img-top
              style="max-width: 30rem;"
              class="mb-3">
            <b-img rounded width="440" height="300" :src=imageUrl(resource.image_set[0]) alt="img" />

            <b-card-body>
              <h4>{{ resource.title }}</h4>
              <p class="card-text">
                {{ resource.description }}
              </p>
            </b-card-body>
            <b-button :href=resource.url variant="primary">Acessar Recurso</b-button>
          </b-card>
      </div>
      <div class="col-md-5">
        <h3>Relatos sobre o recurso:</h3>
        <hr>

        <div v-for="feedback in resource.feedback_set">
          <b-card :title=feedback.title>
          <p class="card-text">
              {{ feedback.description }}
          </p>
          <div slot="footer">
            <small class="text-muted">Relatado em {{ feedback.created_date }}</small>
          </div>
          </b-card>
          <hr>
        </div>
      </div>
      <div class="col-md-4">
        <h1>Outras estatisticas:</h1>
      </div>
    </div>
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
    if(window.location.pathname == '/all/')
      return 0
    else {
      this.$http.get("/api"+window.location.pathname+"?format=json").then( (req) => this.resource = req.data )
    }

  },
  methods:{
    imageUrl(image){
      if (image != null)
        return image.image
      else {
        return ""
      }
    },
  }
}
</script>

<style>
</style>
