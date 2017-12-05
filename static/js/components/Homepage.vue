<template>
  <div id="homepage">
    <v-app light>
      <v-toolbar class="white">
        <v-toolbar-title v-text="title"></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn flat href="accounts/login/">
          Login
        </v-btn>

      </v-toolbar>

      <v-content>
        <section>
          <v-parallax src="/static/resources/img/kids2.jpg" height="600">
            <v-layout
              column
              align-center
              justify-center
              class="white--text">

            <h1 class="white--text mb-2 display-1 text-xs-center">Encontre o recurso certo para sua aula</h1>
            <v-btn
              class="blue mt-5"
              dark
              large
              href="/all">
              <v-icon>search</v-icon>
              Buscar
            </v-btn>
            </v-layout>
            </v-parallax>
          </section>

          <section>
            <v-layout
              column
              wrap
              class="my-5"
              align-center>
              <v-flex xs12 sm4 class="my-3">
                <div class="text-xs-center">
                  <h2 class="headline">Uma plataforma colaborativa</h2>
                  <span class="subheading">

                  </span>
                </div>
              </v-flex>
              <v-flex xs12>
                <v-container grid-list-xl>
                  <v-layout row wrap align-center>
                    <v-flex xs12 md4>
                      <v-card class="elevation-0 transparent">
                        <v-card-text class="text-xs-center">
                          <v-icon x-large class="blue--text text--lighten-2">search</v-icon>
                        </v-card-text>
                        <v-card-title primary-title class="layout justify-center">
                          <div class="headline text-xs-center">Encontre</div>
                        </v-card-title>
                        <v-card-text>
                          Há uma infinidade de recursos para o ensino de programação, mas como você sabe qual o melhor para você? Utilize nossos filtros para encontra-lo.
                        </v-card-text>
                      </v-card>
                    </v-flex>
                    <v-flex xs12 md4>
                      <v-card class="elevation-0 transparent">
                        <v-card-text class="text-xs-center">
                          <v-icon x-large class="blue--text text--lighten-2">thumb_up</v-icon>
                        </v-card-text>
                        <v-card-title primary-title class="layout justify-center">
                          <div class="headline">Avalie</div>
                        </v-card-title>
                        <v-card-text>
                          Faça uma avaliação das caractéristicas de um recurso de programação que mais lhe agradaram.
                        </v-card-text>
                      </v-card>
                    </v-flex>
                    <v-flex xs12 md4>
                      <v-card class="elevation-0 transparent">
                        <v-card-text class="text-xs-center">
                          <v-icon x-large class="blue--text text--lighten-2">share</v-icon>
                        </v-card-text>
                        <v-card-title primary-title class="layout justify-center">
                          <div class="headline text-xs-center">Compartilhe</div>
                        </v-card-title>
                        <v-card-text>
                          Escreva um relato compartilhando sua experiência em sala de aula utilizando o recurso.
                        </v-card-text>
                      </v-card>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-flex>
            </v-layout>
          </section>

          <section>
            <v-parallax src="/static/resources/img/kids.jpg" height="380">
              <v-layout column align-center justify-center>
                <div class="headline white--text mb-3 text-xs-center">Ensine programação, encontre o recurso.</div>
                <v-btn
                  class="blue mt-5"
                  dark
                  large
                  href="/all">
                  <v-icon>search</v-icon>
                  Buscar
                </v-btn>
              </v-layout>
            </v-parallax>
          </section>

          <section>
            <v-container grid-list-xl>
              <v-layout row wrap justify-center class="my-5">
                <v-flex xs12 sm4>
                  <v-card class="elevation-0 transparent">
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">Sobre</div>
                    </v-card-title>
                    <v-card-text>
                      Somos uma plataforma para compartilhar experiências em sala de aula.
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 sm4 offset-sm1>
                  <v-card class="elevation-0 transparent">
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">Contato</div>
                    </v-card-title>
                    <v-card-text>
                      Esse projeto é apoiado pelo Clube da Computação projeto de extensão da Universidade Federal de Santa Maria - UFSM.
                    </v-card-text>
                    <v-list class="transparent">

                      <v-list-tile>
                        <v-list-tile-action>
                          <v-icon class="blue--text text--lighten-2">email</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                          <v-list-tile-title>henriqmayer@gmail.com</v-list-tile-title>
                        </v-list-tile-content>
                      </v-list-tile>
                    </v-list>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </section>

          <v-footer class="blue darken-2">
            <v-layout row wrap align-center>
              <v-flex xs12>
                <div class="white--text ml-3">
                  Contribua com nossa ideia, acesse nosso repositório no <a class="white--text" href="https://github.com/capmayer/catalogo_project" target="_blank">Github.</a>
                </div>
              </v-flex>
            </v-layout>
          </v-footer>
        </v-content>
  </v-app>
  </div>
</template>
<script>
export default {
  data() {
    return {
      title: 'Catalogy',
    }
  },
}
</script>

<style>
#homepage{
  color:blue;
}
.margin-top{
  margin-top: 50px;
}
</style>
