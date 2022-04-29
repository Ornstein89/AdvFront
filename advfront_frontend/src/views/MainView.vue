<template>
  <v-container>
    <v-row>

      <v-col
        cols="12"
        sm="6"
        md="6"
        class="pa-2"
      >
        <v-row align="center">
          <v-col class="d-flex">
            <v-icon
              size="150px">
              <!-- style="font-size:200px;"> -->
              mdi-file-music
            </v-icon>
            <div class="text-left">
              <h2>Inspect suspicious audio</h2>
              <p>Try out service using prepared audio or check your own</p>
            </div>
          </v-col>
        </v-row>
        <v-row class="ma-2">
        <v-file-input
          counter
          show-size
          clearable
          accept="audio/*"
          label="Choose file"
          @change="fileUpload"
          :loading="uploadLoading"
        >
        </v-file-input>
        <!-- <v-btn>Upload</v-btn> -->
        </v-row>

        <audio
          ref="audio"
          style="width:100%"
          :src="'http://localhost:8000/media/'+this.soundFile"
          preload="auto"
          controls
        >
          <!-- <source src="xxx.wav" type="audio/mpeg"> -->
          Your browser does not support the audio tag.
        </audio>

        <!-- <audio-player
          url="https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3"
          playerid="audio-player"
        > </audio-player> -->

        <v-row class="ma-2"
          align="center"
          justify="space-around">

            <!-- <v-btn
              ref="btnPlay"
              class="ma-2"
              v-on="btnPlayClick"
              :loading="btnPlayLoading"
              :disabled="btnPlayLoading"
            >Play</v-btn> -->

            <v-btn
              ref="btnPredict"
              class="ma-2"
              color="primary"
              :loading="btnPlayLoading"
              @click="btnPredictClick"
            >Predict</v-btn>

        </v-row>
      </v-col>

      <v-col
        cols="12"
        sm="6"
        md="6"
        class="pa-2"
      >
        <v-row>
          <v-col class="d-flex">
            <v-icon
              class="d-flex"
              size="150px">
              <!-- style="font-size:200px;"> -->
              mdi-graph
            </v-icon>
            <div  class="text-left">
              <h2>Select between robust and regular models</h2>
              <p>Experience the difference between unprotected and thrusted AI</p>
            </div>
          </v-col>
        </v-row>
        <v-progress-linear
          v-model="completed"
          color="blue"
          class="ma-3"
          height="50"
          rounded
          outline
          
        >
          <strong>{{ Math.ceil(completed) }}%</strong>
        </v-progress-linear>
        <!-- <v-row class="ma-2"
          align="center"
          justify="space-around"> -->

          <v-btn-toggle
            v-model="method"
            mandatory
            group
            color="primary"
          >
            <v-btn
              outlined
            >
              <v-icon v-if="method===0">mdi-check</v-icon>
              Regular
            </v-btn>

            <v-btn
              outlined
            >
              <v-icon v-if="method===1">mdi-check</v-icon>
              Robust
            </v-btn>
          </v-btn-toggle>
        <!-- </v-row> -->
      </v-col>

    </v-row>

    <v-snackbar
      v-model="showmessage"
      timeout="2000"
      color="red accent-2"
    >
      {{ messagetext }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="showmessage = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>

import axios from 'axios'

export default {
  name: 'MainView',
  components: {

  },
  data () {
    return {
      completed : 50,
      method : 0,
      btnPredictLoading : false,
      uploadLoading : true,
      showmessage : false,
      messagetext : "",
      soundFile : "",
    }
  },
  methods: {
    btnPredictClick(){
      this.btnPredictLoading = true;
      axios.post("/predict", {params:{}})
      .then(response => {
        console.log("response = ", response)
        this.btnPredictLoading = false;
      })
      .catch(error => {
        console.log("error=",error);
        this.messagetext = error;
        this.showmessage = true;
        this.btnPredictLoading = false;
      })
      .finally(() => {
        console.log("finally");
        this.btnPredictLoading = false;
      });
    },

    fileUpload(File) {
      if(File===null)
        return;
      console.log(File)
      const formData = new FormData();
      formData.append("file", File);
      axios.post(
        "/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            // "Content-Type": "application/form-data"
          },
          onUploadProgress:this.onUploadProgress,
        }
      )
      .then(response => {
        console.log("response = ", response)
        this.soundFile = response.data.file;
        this.uploadLoading = false;
      })
      .catch(error => {
        console.log("error=",error);
        this.messagetext = error;
        this.showmessage = true;
        this.uploadLoading = false;
      })
      .finally(() => {
        console.log("finally");
        this.uploadLoading = false;
      });
    },

    onUploadProgress(progressEvent){
      // console.log("onUploadProgress = ", progressEvent);
      // console.log("onUploadProgress = ", progressEvent.loaded);
      this.uploadLoading = progressEvent.loaded/progressEvent.total * 100;
    },
  },
}
</script>
