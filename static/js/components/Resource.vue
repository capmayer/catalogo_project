<template>
  <div id="resource">
    <div class="container-fluid margin-top">
      <div class="row">
        <hr>
      </div>
      <div class="row">
        <div class="col-md-3">
          <div class="row margin-left">
            <icon name="filter" scale="1.7"></icon><h3 class="margin-left">Filtros</h3>
          </div>
          <hr>
          <b-input-group>
            <b-input-group-addon><icon name="search"></icon></b-input-group-addon>
            <b-form-input type="search" v-model="searchFilter" placeholder="Filtrar pelo nome..."/></b-form-input></b-col>
          </b-input-group>
          <hr>
          <h3>Nível de engajamento:</h3>
          <b-form-radio-group id="btnradios1"
                        buttons
                        v-model="difficultStudentSelected"
                        :options="options"
                        name="radiosBtnDefault" />
          <hr>
          <b-input-group>
            <b-input-group-addon><icon name="globe"></icon></b-input-group-addon>
            <b-form-select v-model="language" :options="languageOptions">
            </b-form-select>
          </b-input-group>
          <hr>
          <h3 class="center">Caracteristicas</h3>
          <b-form-checkbox-group v-model="featuresSelected" stacked :options="featuresOptions">
          </b-form-checkbox-group>
        </div>
        <div class="col-md-9">
          <b-card-group deck>
            <div v-for="resource in listFilter">
              <b-card no-body img-top
                  style="max-width: 30rem;"
                  class="mb-3">
                <b-img rounded width="450" height="300" :src=imageUrl(resource.image_set[0]) alt="img" />

                <b-card-body>
                  <h4>{{ resource.title }}</h4>
                  <p class="card-text">
                    {{ resource.description }}
                  </p>
                  <div class="row">
                    <div class="col-md-8">
                      <div class="row">
                        <icon name="thumbs-o-up" class="margin-15 blue" scale="1.5"></icon>
                        <h4 class="margin-left margin-right blue">{{ resource.likes.length }}</h4>
                        <icon name="thumbs-o-down" class="margin-left red" scale="1.5"></icon>
                        <h4 class="margin-left margin-right red">{{ resource.deslikes.length }}</h4>
                        <icon name="comment-o" class="margin-left" scale="1.5"></icon>
                        <h4 class="margin-left">{{ resource.feedback_set.length }}</h4>
                      </div>
                    </div>
                    <div class="col-md-3">
                      <a :href=resourceUrl(resource.slug)><b-button variant="primary">detalhes</b-button></a>
                    </div>
                  </div>
                </b-card-body>
              </b-card>
            </div>
          </b-card-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
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
      featuresOptions: [
        { text: 'Computador', value: 'computador' },
        { text: 'Projetor', value: 'projetor' },
        { text: 'Ferramentas', value: 'ferramentas' },
      ],
      difficultStudentSelected: 'in',
      options: [
        { text: 'Fácil', value: 'in' },
        { text: 'Mediano', value: 'me' },
        { text: 'Difícil', value: 'av' }
      ]
    }
  },
  mounted() {
    this.$http.get("/api/resource/?format=json").then( (req) => this.listSave = req.data = this.listFilter = req.data )
  },
  watch: {
    difficultStudentSelected(val){
      console.log(val)
      if (val == 'in')
        this.listFilter = this.listSave.filter(function(resource){
          return resource.difficult_student == 'in'
        })
      else if ( val == 'me')
        this.listFilter = this.listSave.filter(function(resource){
          return resource.difficult_student == 'me'
        })
        else if ( val == 'av')
          this.listFilter = this.listSave.filter(function(resource){
            return resource.difficult_student == 'av'
        })
    },
    searchFilter(val){
      this.listFilter = this.listSave.filter(item => {
         return item.title.toLowerCase().indexOf(this.searchFilter.toLowerCase()) > -1
      })
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
  .margin-top{
    margin-top: 50px;
  }
  .margin-left{
    margin-left: 5px;
  }
  .margin-15{
    margin-left: 15px;
  }
  .margin-right{
    margin-right: 20px;
  }
  .blue{
    color: #5b9aff;
  }
  .red {
    color: #db0f3b;
  }
  .right{
    text-align: right;
  }
  .center {
    text-align: center;
  }
</style>
