<template>
  <div id="resource">
    <v-app>
      <v-navigation-drawer
        clipped
        fixed
        v-model="drawer"
        app>
        <v-subheader>Filtrar</v-subheader>
        <div class="pa-2">
            <v-text-field
              v-model="searchFilter"
              label="Nome"
              single-line
              prepend-icon="search">
            </v-text-field>

            <v-select
              v-bind:items="languageOptions"
              v-model="language"
              label="Idioma"
              single-line
              prepend-icon="map">
            </v-select>
        </div>
        <v-subheader>Engajamento</v-subheader>
        <div class="pa-2">
          <v-switch label="Fácil" v-model="difIn" value="in"></v-switch>
          <v-switch label="Mediano" v-model="difMe" value="me"></v-switch>
          <v-switch label="Difícil" v-model="difAv" value="av"></v-switch>
        </div>
      </v-navigation-drawer>
      <v-toolbar class="white" app fixed clipped-left>
        <v-toolbar-title v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn flat href="accounts/login/">
          Login
        </v-btn>
      </v-toolbar>
      <v-container fluid class="cyan lighten-4">
        <v-container grid-list-lg>
          <v-layout row wrap>
            <v-flex xs12>
              <h5> Recursos </h5>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex
              xs6
              v-for="(resource, index) in listFilter"
              :key="index">
              <v-card contain>
                <v-card-media
                  :src=imageUrl(resource.image_set[0])
                  height="200px">
                </v-card-media>
                <v-card-title primary-title>
                  <div>
                    <div class="headline">{{ resource.title }}</div>
                    <span class="grey--text">{{ resource.description }}</span>
                  </div>
                </v-card-title>
                <v-card-actions>

                  <v-spacer></v-spacer>
                  <!-- <v-btn flat>Compartilhar</v-btn>  futures work -->
                  <v-btn :href=resourceUrl(resource.slug) > Ver mais</v-btn>

                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-container>
    </v-app>
  </div>
</template>

<script>

export default {
  data() {
    return {
      show: '',
      title: "Catalogy",
      drawer: null,
      sortDirection: 'desc',
      searchFilter: '',
      listSave: [],
      listFilter: [],
      language: 'pt-br',
      languageOptions: [
        { text: 'Português', value:'pt-br' },
        { text: 'Inglês', value:'en-us' },
      ],
      featuresSelected: [],
      difAv: false,
      difMe: false,
      difIn: false,
    }
  },
  mounted() {
    if(window.location.pathname == '/all/')
      this.$http.get("/api/resource/?format=json").then( (req) => this.listSave = req.data = this.listFilter = req.data )
  },
  watch: {
    searchFilter(val){
      this.listFilter = this.listSave.filter(item => {
         return item.title.toLowerCase().indexOf(this.searchFilter.toLowerCase()) > -1
      })
    },
    difAv(val){
      if (val) {
        this.listFilter = this.listSave.filter(item => { return item.difficult_student == 'av'})
        this.difMe = false
        this.difIn = false
      }
    },
    difMe(val){
      if (val) {
        this.listFilter = this.listSave.filter(item => { return item.difficult_student == 'me'})
        this.difAv = false
        this.difIn = false
      }
    },
    difIn(val){
      if (val) {
        this.listFilter = this.listSave.filter(item => { return item.difficult_student == 'in'})
        this.difMe = false
        this.difAv = false
      }
    },
    language(val){
      if(val == "pt-br"){
        this.listFilter = this.listSave.filter(item => { return item })
      }
      if(val == "en-us"){
        this.listFilter = null
      }
    }
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

      this.listFilter = _.orderBy(this.listSave, campo, this.sortDirection)

    },
    imageUrl(image){
      if (image != null)
        return image.image
      else {
        return ""
      }
    },
    resourceUrl(slug){
      return "../resource/"+slug
    }
  }
}
</script>

<style>
</style>
