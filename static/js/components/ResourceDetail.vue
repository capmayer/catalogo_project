<template>
  <div id="resource-detail">
    <v-app>
      <v-navigation-drawer
        clipped
        fixed
        app>
        <v-card flat class="pa-2">
          <v-card-media
            src="/static/resources/img/kids3.jpg"
            height="200px">
          </v-card-media>
          <v-card-title primary-title>
            <div>
              <div class="headline">{{ resource.title }}</div>
              <span class="grey--text">{{ resource.description }}</span>
            </div>
          </v-card-title>
          <v-btn block color="primary" :href=resource.url>ACESSAR RECURSO</v-btn>
        </v-card>

      </v-navigation-drawer>
      <v-toolbar class="white" app fixed clipped-left>
        <v-toolbar-title v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn flat href="accounts/login/">
          Login
        </v-btn>
      </v-toolbar>
      <v-container fluid class="cyan lighten-4">
        <v-container class="mt-5">
          <v-layout row wrap>
            <v-flex xs10>
              <v-card>
                <v-card-text>
                  <v-layout row>
                    <v-avatar size="100px" class="mr-3">
                      <img :src=imageUrl(resource.image_set[0]) alt="avatar">
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
        <v-container>
          <v-layout row wrap>
            <v-flex xs10>
              <v-card name="baseCard">
                <v-subheader>
                  Relatos
                </v-subheader>
                <v-container fluid>
                  <v-layout row wrap>
                    <v-flex xs12 v-for="(feedback, index) in feedbacks" :key=index>
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
                                  <h4>{{ feedback.author.username }}</h4>
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
            </v-flex>
          </v-layout>
        </v-container>
      </v-container>
    </v-app>
  </div>
</template>

<script>
export default {
  data(){
    return {
      title: 'Catalogy',
      resource: '',

      feedbackOrderOptions: [
        { text: 'Relevancia', value:'rel' },
        { text: 'Mais antigo', value:'ant' },
        { text: 'Mais recente', value:'rec' },
      ],
      feedbackOrderSelected: 'rel',
      feedbacks: [],
      feedbackDialog: false,
      feedbackDescription: '',
      resourceFeedbackAp: false,
      token: '',
      feedbackSnackbar: '',
      timeOut: 300,
    }
  },
  mounted(){
    if(window.location.pathname.includes("resource/")){
      this.$http.get("/api"+window.location.pathname+"?format=json").then((req) => {
         this.resource = req.data
      })
      this.$http.get("/api"+window.location.pathname+"feedback/?format=json").then( (req) => this.feedbacks = req.data )

    }


  },
  computed: {
      feedbackIsValid () {
        return (
          this.feedbackDescription
        )
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
    postFeedback(evt){
      evt.preventDefault()
      this.feedbackData = {
        'resource': this.resource.id,
        'description': this.feedbackDescription,
        'title': 'null',
        'is_pro': this.resourceFeedbackAp,
        'author': '',
      }
      this.token = this.$cookie.get('csrftoken')
      this.$http.post("/api/feedback/", this.feedbackData, { headers: { 'X-CSRF-TOKEN': this.token }}).then( (req) => {
        this.feedbackDialog = false
        this.feedbackSnackbar = true
      })
    },
    checkToken(){
      if (this.$cookie.get('csrftoken'))
        this.token = this.$cookie.get('csrftoken')
    }
  }
}
</script>

<style>
</style>
