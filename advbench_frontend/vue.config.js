const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  outputDir : "../advbench_backend/media", // собирать в каталог django
  devServer: {
    proxy: 'http://localhost:8000'
  },
  // devServer: {
  //   public: '0.0.0.0:8080',
  //   disableHostCheck: true,
  //   // proxy: 'http://178.154.222.68/api'
  //   // proxy: {
  //   //     '^/api': {
  //   //         target: 'http://178.154.222.68',
  //   //         ws: true,
  //   //         changeOrigin: true
  //   //     }
  //   // }
  //   // public: "http://178.154.222.68",
  //   // headers: { 'Access-Control-Allow-Origin': '*' },

  //   // "proxy":'http://127.0.0.1:8000',

  //   // proxy: {

  //   //   "^/": {
  //   //     //TODO вернуть на проде - здесь задаётся хост
  //   //     // target: 'http://178.154.222.68',
  //   //     target: 'http://127.0.0.1:8000',
  //   //     headers: { 'Access-Control-Allow-Origin': '*' },
  //   //     // pathRewrite: { '^/api': '' },
  //   //     changeOrigin: true,
  //   //     // secure: false,
  //   //     pathRewrite: { '^/': '/' },
  //   //     logLevel: 'debug'
  //   //   }
  //   // }
  // }  
})
