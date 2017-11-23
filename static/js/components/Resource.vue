<template>
  <div id="resource">

    <table class="table">
      <thead>
        <th><a href="#" @click="sort($event, 'fields.title')">Titulo</a></th>
        <th><a href="#" @click="sort($event, 'fields.description')">Plataformas</a></th>
      </thead>
      <tbody>
        <tr v-for="resource in lista">
          <td>{{ resource.fields.title }}</td>
          <td>{{ resource.fields.description }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
export default {

  data() {
    return {
      sortDirection: 'desc',
      lista: []
    }
  },
  mounted() {
    this.$http.get("/resource/all").then( (req) => this.lista = req.data )
  },
  methods:{
    sort(event, campo){
      event.preventDefault()

      if ( this.sortDirection == "desc" )
      {
          this.sortDirection = "asc"
      }else{
        this.sortDirection = "desc"
      }

      this.lista = _.orderBy(this.lista, campo, this.sortDirection)

    }
  }
}
</script>

<style>

  #exemplo{
      color: red;
  }
</style>
