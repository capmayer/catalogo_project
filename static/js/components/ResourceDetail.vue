<template>
  <div id="resource-detail">
    <v-app>
      <v-navigation-drawer
        clipped
        fixed
        app
        v-model="drawer">
        <v-card flat class="pa-2">
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
          <v-btn block color="primary" v-on:click=goToUrl(resource.url)>ACESSAR RECURSO</v-btn>
        </v-card>

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
      <v-container fluid class="grey lighten-3">
        <v-container class="mt-5">
          <v-layout row>
            <v-flex xs10>
              <v-card>
                <v-card-text>
                  <v-layout row>
                    <v-avatar size="100px" class="mr-3">
                      <img src="/static/resources/img/nopic.png" alt="avatar">
                    </v-avatar>
                    <v-text-field
                      name="input-1"
                      label="Faça um relato..."
                      auto-grow
                      multi-line
                      rows=1
                      v-model="feedbackDescription">
                    </v-text-field>
                  </v-layout>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    flat
                    color="primary"
                    type="submit"
                    :disabled="!feedbackIsValid"
                    @click.stop="feedbackDialog=true">
                    Enviar
                  </v-btn>
                </v-card-actions>
              </v-card>
              <v-tabs fixed icons centered class="mt-5">
                <v-tabs-bar dark class="light-blue lighten-1">
                  <v-tabs-slider color="black"></v-tabs-slider>
                  <v-tabs-item href="#pros">
                    <v-icon>thumb_up</v-icon>
                    Pros
                  </v-tabs-item>
                  <v-tabs-item href="#contras">
                    <v-icon>thumb_down</v-icon>
                    Contras
                  </v-tabs-item>
                  <v-tabs-item href="#relatos">
                    <v-icon>account_box</v-icon>
                    Relatos
                  </v-tabs-item>
                </v-tabs-bar>
                <v-tabs-items>
                  <v-tabs-content id="pros">
                    <v-card name="baseCard">
                      <v-container fluid>
                        <v-layout row wrap>
                          <v-flex xs12 v-if=!feedbacks.length>
                            <v-card flat>
                              <v-card-text>
                                Nenhum feedback registrado ainda, seja o primeiro!
                              </v-card-text>
                            </v-card>
                          </v-flex>
                          <v-flex xs12 v-for="(feedback, index) in feedbacks" :key=index v-if=feedback.is_pro>
                            <v-card flat>
                              <v-card-text>
                                <v-layout row wrap>
                                  <v-flex xs1>
                                    <v-avatar>
                                    <img src="/static/resources/img/nopic.png">
                                  </v-avatar>
                                  </v-flex>
                                  <v-flex xs11>
                                    <v-layout row wrap>
                                      <v-flex xs3>
                                        <h4>{{ feedback.author }}</h4>
                                      </v-flex>
                                      <v-flex xs9>
                                        <!-- fure work, last edit -->
                                      </v-flex>
                                      <v-flex xs12>
                                        <p class="body-1">
                                          {{ feedback.description }}
                                        </p>
                                      </v-flex>
                                    </v-layout>
                                  </v-flex>
                                </v-layout>
                              </v-card-text>
                            </v-card>
                            <v-divider></v-divider>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-card>
                  </v-tabs-content>
                  <v-tabs-content id="contras">
                    <v-card name="baseCard">
                      <v-container fluid>
                        <v-layout row wrap>
                          <v-flex xs12 v-if=!feedbacks.length>
                            <v-card flat>
                              <v-card-text>
                                Nenhum feedback negativo registrado ainda, seja o primeiro!
                              </v-card-text>
                            </v-card>
                          </v-flex>
                          <v-flex xs12 v-for="(feedback, index) in feedbacks" :key=index v-if=!feedback.is_pro>
                            <v-card flat>
                              <v-card-text>
                                <v-layout row wrap>
                                  <v-flex xs1>
                                    <v-avatar>
                                    <img src="/static/resources/img/nopic.png">
                                  </v-avatar>
                                  </v-flex>
                                  <v-flex xs11>
                                    <v-layout row wrap>
                                      <v-flex xs3>
                                        <h4>{{ feedback.author }}</h4>
                                      </v-flex>
                                      <v-flex xs9>
                                        <!-- fure work, last edit -->
                                      </v-flex>
                                      <v-flex xs12>
                                        <p class="body-1">
                                          {{ feedback.description }}
                                        </p>
                                      </v-flex>
                                    </v-layout>
                                  </v-flex>
                                </v-layout>
                              </v-card-text>
                            </v-card>
                            <v-divider></v-divider>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-card>
                  </v-tabs-content>
                  <v-tabs-content id="relatos">
                    <v-card name="baseCard">
                      <v-container fluid>
                        <v-layout row wrap>
                          <v-flex xs12 v-if=!relatos.length>
                            <v-card flat>
                              <v-card-text>
                                Nenhum relato registrado ainda, seja o primeiro!
                              </v-card-text>
                            </v-card>
                          </v-flex>
                          <v-flex xs12 v-for="(relato, index) in relatos" :key=index>
                            <v-card flat>
                              <v-card-text>
                                <v-layout row wrap>
                                  <v-flex xs1>
                                    <v-avatar>
                                    <img src="/static/resources/img/nopic.png">
                                  </v-avatar>
                                  </v-flex>
                                  <v-flex xs11>
                                    <v-layout row wrap>
                                      <v-flex xs3>
                                        <h4>{{ relato.author }}</h4>
                                      </v-flex>
                                      <v-flex xs9>
                                        <!-- fure work, last edit -->
                                      </v-flex>
                                      <v-flex xs12>
                                        <p class="body-1">
                                          {{ relato.description }}
                                        </p>
                                      </v-flex>
                                    </v-layout>
                                  </v-flex>
                                </v-layout>
                              </v-card-text>
                            </v-card>
                            <v-divider></v-divider>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-card>
                  </v-tabs-content>
                </v-tabs-items>
              </v-tabs>
            </v-flex>
            <v-flex xs2 class="ml-5">
              <v-card flat class="grey lighten-3">
                <v-subheader>
                  Recursos relacionados
                </v-subheader>
                <v-container fluid>
                  <v-layout row wrap>
                    <v-flex xs12 v-for="(resource, index) in resource.resources" :key="index">
                      <a :href=resourceUrl(resource.slug) >
                        <v-card class="mb-2">
                          <v-card-media :src=imageUrl(resource.image_set[0]) height="150px"></v-card-media>
                        </v-card>
                      </a>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-card>
            </v-flex>
          </v-layout>
          <v-dialog v-model="feedbackDialog" max-width="500px">
            <v-card>
              <v-card-title>
                Mais alguns detalhes...
              </v-card-title>
              <v-card-text>
                <v-layout row wrap>
                  <v-flex xs12>
                    <v-switch label="Recomendar recurso"
                        v-model="resourceFeedbackAp"
                        color="success"
                        hide-details></v-switch>
                  </v-flex>
                </v-layout>
              </v-card-text>
            <v-card-actions>
              <v-btn color="secundary" flat @click.stop="feedbackDialog=false">Cancelar</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary" raised @click="postFeedback">Enviar</v-btn>
            </v-card-actions>
            </v-card>
          </v-dialog>
          <v-snackbar
            :timeout=timeOut
            v-model="feedbackSnackbar">
            Relato registrado
            <v-btn flat @click.native="feedbackSnackbar = false">Close</v-btn>
          </v-snackbar>
        </v-container>
      </v-container>
    </v-app>
  </div>
</template>

<script>
export default {
  data(){
    return {
      title: 'Nice Resource',
      resource: '',
      userName: '',
      userNameGetter: false,
      drawer: true,
      feedbackOrderOptions: [
        { text: 'Relevancia', value:'rel' },
        { text: 'Mais antigo', value:'ant' },
        { text: 'Mais recente', value:'rec' },
      ],
      feedbackOrderSelected: 'rel',
      feedbacks: [],
      relatos: [],
      feedbackDialog: false,
      feedbackDescription: '',
      resourceFeedbackAp: false,
      token: this.$cookie.get('csrftoken'),
      feedbackSnackbar: '',
      timeOut: 1000,
    }
  },
  mounted(){
    if(window.location.pathname.includes("resource/")){
      this.$http.get("/api"+window.location.pathname+"?format=json").then((req) => {
         this.resource = req.data
      })
      this.$http.get("/api"+window.location.pathname+"feedback/?format=json").then( (req) => this.feedbacks = req.data )
      this.$http.get("/api"+window.location.pathname+"relato/?format=json").then( (req) => this.relatos = req.data )
      this.userName = document.getElementById('userName').value
    }
  },
  computed: {
      feedbackIsValid () {
        return (
          this.feedbackDescription
        )
      },
      userLogged (){
        return (this.getUserFromHTML())
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
    goToUrl(url){
      location.href = url
    },
    postFeedback(evt){
      evt.preventDefault()
      this.feedbackData = {
        'resource': this.resource.id,
        'description': this.feedbackDescription,
        'title': 'null',
        'is_pro': this.resourceFeedbackAp,
        'author': this.userName,
      }
      this.token = this.$cookie.get('csrftoken')
      this.$http.post("/api/feedback/", this.feedbackData, { headers: { 'X-CSRFToken': this.token }}).then( (req) => {
        this.feedbackDialog = false
        this.feedbackSnackbar = true
      })
    },
    checkToken(){
      if (this.$cookie.get('csrftoken'))
        this.token = this.$cookie.get('csrftoken')
    },
    getUserFromHTML(){
      this.userName = document.getElementById('userName').value
      if (this.userName == '')
        return false
      else {
        return true
      }
    },
    resourceUrl(slug){
      return "/all/"+slug
    }
  }
}
</script>

<style>
</style>
