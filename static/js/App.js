import Vue from 'vue'
import VueResource from 'vue-resource'
import Resource from './components/Resource.vue'
import Homepage from './components/Homepage.vue'
import ResourceDetail from './components/ResourceDetail.vue'
import lodash from 'lodash'
import BootstrapVue from 'bootstrap-vue'
import Icon from 'vue-awesome'

import { Card, FormRadio, Form, FormInput, FormTextarea, Button, Collapse } from 'bootstrap-vue/es/components';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-awesome/icons'

Vue.use(VueResource, lodash)
Vue.component('icon', Icon)
Vue.use(BootstrapVue)
Vue.use(Card)
Vue.use(FormRadio)
Vue.use(FormInput)
Vue.use(Form)
Vue.use(FormTextarea)
Vue.use(Button)
Vue.use(Collapse)

var VueCookie = require('vue-cookie');
// Tell Vue to use the plugin
Vue.use(VueCookie);

new Vue(Resource).$mount('.resource')
new Vue(Homepage).$mount('.homepage')
new Vue(ResourceDetail).$mount('.resource-detail')
