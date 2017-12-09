import Vue from 'vue'
import VueResource from 'vue-resource'
import Resource from './components/Resource.vue'
import Homepage from './components/Homepage.vue'
import ResourceDetail from './components/ResourceDetail.vue'
import lodash from 'lodash'

import Vuetify from 'vuetify'

Vue.use(Vuetify)

Vue.use(VueResource)

Vue.use(lodash)

var VueCookie = require('vue-cookie');
// Tell Vue to use the plugin
Vue.use(VueCookie);

if(window.location.pathname == '/all/')
  new Vue(Resource).$mount('.resource')
if(window.location.pathname == '/')
  new Vue(Homepage).$mount('.homepage')
if(window.location.pathname.includes("resource/"))
  new Vue(ResourceDetail).$mount('.resource-detail')
