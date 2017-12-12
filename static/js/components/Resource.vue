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
        <template>
          <v-footer absolute class="pa-3" color="blue lighten-2">
            <a v-on:click="addResourceDialog= true">ADICIONE UM RECURSO</a>
          </v-footer>
        </template>
        <v-dialog v-model="addResourceDialog" persistent max-width="500px">
          <v-card>
        <v-card-title>
          <span class="headline">Adicionar Recurso</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 sm12 md12>
                <v-text-field persistent-hint label="Nome do Recurso" hint="exemplo: Hora do Código: Minecraft" required></v-text-field>
              </v-flex>
              <v-flex xs12 sm12 md12>
                <v-text-field persistent-hint label="URL" hint="exemplo: https://hourofcode.com/mchoc" required></v-text-field>
              </v-flex>
              </v-flex>
              <v-flex xs12>
                <v-text-field multi-line v-model="addResourceFormDesc" label="Descrição" required></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-select
                  label="Nível de Engajamento"
                  required
                  :items="addResourceFormNEOps"
                ></v-select>
              </v-flex>
              <v-flex xs12 sm6>
                <v-select
                  label="Idiomas"
                  multiple
                  autocomplete
                  :items="languageOptions"
                ></v-select>
              </v-flex>
              <v-flex x12 sm12>
                <v-btn>IMAGEM</v-btn>
              </v-flex>
            </v-layout>
          </v-container>
          <small>*campo obrigatório</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat @click.native="addResourceDialog = false">Fechar</v-btn>
          <v-btn color="blue darken-1 " flat @click.native="addResourceDialog = false">Adicionar</v-btn>
        </v-card-actions>
      </v-card>
        </v-dialog>
      </v-navigation-drawer>
      <v-toolbar class="white" app fixed clipped-left>
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title v-on:click="goToUrl('/')" v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <template v-if="userLogged">
          <v-btn flat>
            {{ userName }}
          </v-btn>
        </template>
        <template v-else="userLogged">
          <v-btn flat>
            Entrar
          </v-btn>
        </template>
      </v-toolbar>
      <v-container fluid class="blue lighten-4">
        <v-container grid-list-lg>
          <v-layout row wrap>
            <v-flex xs12>
              <h5> Recursos </h5>
            </v-flex>
          </v-layout>
          <v-layout row wrap>
            <v-flex
              xs6 sm6
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
                  </div>
                </v-card-title>
                <v-card-actions>

                  <v-spacer></v-spacer>
                  <!-- <v-btn flat>Compartilhar</v-btn>  futures work -->
                  <v-btn :href=resourceUrl(resource.slug)> Ver mais</v-btn>

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
      user: '',
      show: '',
      userName: '',
      title: "Nice Resource",
      drawer: true,
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
      token: '',
      addResourceDialog: false,
      addResourceFormDesc: '',
      addResourceFormNEOps: [
        { text: 'Fácil', value: 'in' },
        { text: 'Mediano', value: 'me' },
        { text: 'Difícil', value: 'av' },
      ]
    }
  },
  computed: {
    userLogged (){
      return (this.getUserFromHTML())
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
    },
    getUserFromHTML(){
      this.userName = document.getElementById('userName').value
      if (this.userName == '')
        return false
      else {
        return true
      }
    },
    postResource(evt){
      evt.preventDefault()
      this.resourceData = {
        'title': this.addResourceFormTitle,
        'description': this.addResourceFormDesc,
        'url': this.addResourceFormUrl,
        'author': this.userName,
        'difficult_student': this.addResourceFormDif,
        'languages': this.addResourceFormLangs,
      }
      this.token = this.$cookie.get('csrftoken')
      this.$http.post("/api/feedback/", this.feedbackData, { headers: { 'X-CSRFToken': this.token }}).then( (req) => {

      })
    },
  }
}
</script>

<style>
</style>
