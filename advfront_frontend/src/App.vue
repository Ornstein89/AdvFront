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
    </v-app-bar>

    <v-main>
      <v-container fill-height>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

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
