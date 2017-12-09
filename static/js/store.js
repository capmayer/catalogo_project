import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    user: '',
    token: ''
  },
  mutations: {
    login (state) {
      state.user = 'ola'
    }
  }
});
