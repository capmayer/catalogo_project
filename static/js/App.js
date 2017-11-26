import Vue from 'vue'
import VueResource from 'vue-resource'
import Resource from './components/Resource.vue'
import Homepage from './components/Homepage.vue'
import lodash from 'lodash'
import BootstrapVue from 'bootstrap-vue'
import Icon from 'vue-awesome'

import { Card, FormRadio } from 'bootstrap-vue/es/components';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-awesome/icons'

Vue.use(VueResource, lodash)
Vue.component('icon', Icon)
Vue.use(BootstrapVue)
Vue.use(Card)
Vue.use(FormRadio)

new Vue(Resource).$mount('.resource')
new Vue(Homepage).$mount('.homepage')
