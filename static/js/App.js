import Vue from 'vue'
import VueResource from 'vue-resource'
import Resource from './components/Resource.vue'
import lodash from 'lodash'
import BootstrapVue from 'bootstrap-vue'

import { Card, FormRadio } from 'bootstrap-vue/es/components';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueResource, lodash)

Vue.use(BootstrapVue)

Vue.use(Card)
Vue.use(FormRadio);

new Vue(Resource).$mount(".resource")
