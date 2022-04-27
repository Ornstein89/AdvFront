import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'
import AudioPlayer from './components/AudioPlayer.vue'
Vue.component('audio-player', AudioPlayer)

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  AudioPlayer,
  render: h => h(App)
}).$mount('#app')
