<template>
  <div id="resource-detail">
    <hr>
    <div class="row margin-top margin-left">
      <div class="col-md-3">
        <div class="row">
          <b-card no-body img-top border-variant="light"
              style="max-width: 30rem;"
              class="mb-3">
            <b-img rounded width="440" height="300" :src=imageUrl(resource.image_set[0]) alt="img" />

            <b-card-body>
              <h4>{{ resource.title }}</h4>
              <p class="card-text">
                {{ resource.description }}
              </p>
            </b-card-body>
            <b-button :href=resource.url variant="primary">Site do Recurso</b-button>
          </b-card>
        </div>
      </div>
      <div class="col-md-5">
        <div class="row margin-top">
          <div class="col-md-2">
            <b-img rounded="circle" width="75" height="75" src="https://s.ytimg.com/yts/img/avatar_720-vflYJnzBZ.png" alt="img"  />
          </div>
          <div class="col-md-10">
            <b-form>
              <b-form-group>
                <b-form-textarea id="relato"
                           v-model="descriptionFeedback"
                           placeholder="Faça um relato..."
                           :rows="3"
                           :max-rows="6">
                </b-form-textarea>
              </b-form-group>
              <b-button  @click="showModal" variant="primary">Enviar</b-button>
            </b-form>
          </div>
          <b-modal ref="myModalRef" hide-footer title="Avaliação adicional">
            <div class="d-block text-center">
              <h5>Você recomendaria o recurso?</h5>
              <b-form-radio-group v-model="selectedApOp"
                      :options="feedbackAprovOptions"
                      name="radioInline">
              </b-form-radio-group>
            </div>
            <b-btn class="mt-3" variant="primary" block @click="postFeedback">Enviar!</b-btn>
          </b-modal>
        </div>
        <hr>
        <div class="row margin-top">
          <div class="col-md-8">
            <h3>Relatos sobre o recurso:</h3>
          </div>
          <div class="col-md-4">
            <b-input-group>
              <b-input-group-addon><icon name="reorder"></icon></b-input-group-addon>
              <b-form-select v-model="feedbackOrderSelected" :options="feedbackOrderOptions">
              </b-form-select>
            </b-input-group>
          </div>
        </div>
        <hr>

        <div v-for="feedback in feedbacks">
          <b-card>
              <p class="card-text" >
                <div class="row">
                  <div class="col-md-2">
                    <b-img rounded="circle" width="75" height="75" src="https://s.ytimg.com/yts/img/avatar_720-vflYJnzBZ.png" alt="img"  />
                  </div>
                  <div class="col-md-10">
                    {{ feedback.description }}
                  </div>
                </div>
              </p>
            <div slot="footer">
              <template v-if=feedback.author>
                <small class="text-muted">Escrito por {{ feedback.author.username }} em {{ feedback.created_date }}</small>
              </template>
            </div>
          </b-card>
          <hr>
        </div>

      </div>
      <div class="col-md-2">
        <div class="row">
          <h3>outras informações:</h3>
        </div>
        <div class="row">
          <div class="col-md-4">
            <b-card bg-variant="primary"
                text-variant="white"
                class="text-center">
                <div class="col">
                  <icon name="thumbs-o-up"></icon>
                  {{ resource.likes_count }}
                </div>
            </b-card>
          </div>
          <div class="col-md-4">
            <b-card bg-variant="danger"
                text-variant="white"
                class="text-center">
                <div class="col">
                  <icon name="thumbs-o-down"></icon>
                  {{ resource.deslikes_count }}
                </div>
            </b-card>
          </div>
          <div class="col-md-4">
            <b-card bg-variant="secondary"
                text-variant="white"
                class="text-center">
                <div class="col">
                  <icon name="user-o"></icon>
                  {{ resource.visualization_count }}
                </div>
            </b-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      resource: '',

      feedbackOrderOptions: [
        { text: 'Relevancia', value:'rel' },
        { text: 'Mais antigo', value:'ant' },
        { text: 'Mais recente', value:'rec' },
      ],
      feedbackOrderSelected: 'rel',
      feedbacks: [],

      descriptionFeedback: '',
      selectedApOp: '',
      feedbackAprovOptions: [
          { text: 'Recomendaria!', value:true},
          { text: 'Não recomendaria!', value:false},
      ],
      token: '',
    }
  },
  mounted(){
    if(window.location.pathname == '/all/')
      return 0
    else {
      this.$http.get("/api"+window.location.pathname+"?format=json").then( (req) => this.resource = req.data )
      this.$http.get("/api"+window.location.pathname+"feedback/?format=json").then( (req) => this.feedbacks = req.data )
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
    onFeedbackSubmit (evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.descriptionFeedback))
    },
    showModal () {
      this.$refs.myModalRef.show()
    },
    hideModal () {
      this.$refs.myModalRef.hide()
    },
    postFeedback(evt){
      evt.preventDefault()
      this.feedbackData = {
        'resource': this.resource.id,
        'description': this.descriptionFeedback,
        'title': 'null',
        'is_pro': this.is_pro,
        'author': '',
      }
      this.$http.post("/api/feedback/", this.feedbackData).then( (req) => console.log(req.data) );
    }
  }
}
</script>

<style>
</style>
