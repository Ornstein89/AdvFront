<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      clipped-left
    >
      <v-toolbar-title>Simple Antifraud</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn-toggle
        v-model="navigation_model"
        mandatory
        group
        @change="onNavButtonClick">
        <v-btn
          :disabled="loading"
          class="ma-1"
          color="white"
          plain

        >
          Origin sample
        </v-btn>
              <v-btn
          :disabled="loading"
          class="ma-1"
          color="white"
          plain
        >
          Adversarial sample
        </v-btn>
              <v-btn
          :disabled="loading"
          class="ma-1"
          color="white"
          plain
        >
          Try your own
        </v-btn>
      </v-btn-toggle>
    </v-app-bar>

    <v-main>
      <v-container fill-height>
        <router-view :key="$route.path"></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      loading : false,
      navigation_model : 0,
      navigation_refs : [
        {name:'originalsamples'},
        {name:'adversarialsamples'},
        {name:'usersample'}
      ],
      soundfiles : ["original", "adversarial", "user"],
    }
  },
  methods :{
    onNavButtonClick(){
      var x_sndfiles = this.soundfiles[this.navigation_model];
      console.log("onNavButtonClick, sndfiles = ", x_sndfiles);
      this.$router.replace({
        name:this.navigation_refs[this.navigation_model].name,
          params : {sndfiles:x_sndfiles}})
    },
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
