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
          v-model="soundFiles"
          :loading="uploadLoading"
          @change="fileUpload($event)"
        >
        </v-file-input>
        <!-- <v-btn @click="fileUpload">Upload</v-btn> -->
        </v-row>

        <audio
          ref="audio"
          style="width:100%"
          :src="uploadedfileurl"
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
              :loading="isBtnPredictLoading"
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
      isBtnPredictLoading : false,
      uploadLoading : true,
      showmessage : false,
      messagetext : "",
      soundFiles : [],
      uploadedfileurl : "",
    }
  },
  methods: {
    btnPredictClick(){
      this.isBtnPredictLoading = true;
      axios.post("/predict", {params:{}})
      .then(response => {
        console.log("response = ", response)
        this.isBtnPredictLoading = false;
      })
      .catch(error => {
        console.log("error=",error);
        this.messagetext = error;
        this.showmessage = true;
        this.isBtnPredictLoading = false;
      })
      .finally(() => {
        console.log("finally");
        this.isBtnPredictLoading = false;
      });
    },

    fileUpload(event) {
      console.log("event=", event)
      console.log("event.target=", event.target)
      if(!this.soundFiles)
        return;
      // console.log("File = ", File, File.name);
      console.log('this.soundFiles = ', this.soundFiles);
      let formData = new FormData();
      formData.append("files", this.soundFiles, this.soundFiles.name); // soundFiles - модель v-file-input
      console.log("File = ", File, File.name);
      axios.post(
        "/upload",
        formData,
        {
          headers:{
            "Content-Type": "multipart/form-data",
          },
          onUploadProgress: function (progressEvent) {
            this.uploadLoading =
            progressEvent.loaded/progressEvent.total * 100;
          },
        },
        
      )
      .then(response => {
        console.log("response = ", response)
        if(response.data.status==="ok"){
          this.uploadedfileurl = response.data.fileurl;
          console.log("response.data.fileurl = ", response.data.fileurl);
          console.log("this.uploadedfileurl = ", this.uploadedfileurl);
        }
        else{
          this.messagetext = response.data.message;
          this.showmessage = true;
        }
        // this.uploadLoading = false;
      })
      .catch(error => {
        console.log("error=",error);
        this.messagetext = error;
        this.showmessage = true;
        // this.uploadLoading = false;
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
