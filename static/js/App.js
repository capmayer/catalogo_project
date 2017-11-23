import Vue from 'vue'
import VueResource from 'vue-resource'
import Resource from './components/Resource.vue'
import lodash from 'lodash'

Vue.use(VueResource, lodash)

new Vue(Resource).$mount(".resource")
