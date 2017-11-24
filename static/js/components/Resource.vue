<template>
  <div id="resource">
    <h1>Filtre os Recursos:</h1>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-3">

            <h1 >Filtros</h1>
            <hr>
            <b-form-input type="text" v-model="searchFilter" placeholder="Search for..." /></b-form-input>
            <b-form-radio-group id="btnradios1"
                        buttons
                        v-model="difficultStudentSelected"
                        :options="options"
                        name="radiosBtnDefault" />
        </div>
        <div class="col-md-9">
          <b-card-group deck>
            <div v-for="resource in listFilter">
              <b-card :title=resource.title
                  :img-src=imageUrl(image)
                  img-alt="Image"
                  img-top
                  tag="article"
                  style="max-width: 40rem;"
                  class="mb-4">
                <p class="card-text">
                  {{ resource.description }}
                </p>
                <a :href=resourceUrl(resource.slug)><b-button variant="primary">detalhes</b-button></a>
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

      this.listFilter = _.orderBy(this.listFilter, campo, this.sortDirection)

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
  #exemplo{
      color: red;
  }
</style>
