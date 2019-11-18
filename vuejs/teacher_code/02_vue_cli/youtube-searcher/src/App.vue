<template>
  <div class="bg-color-search-bar bg-app">
    <h1>Youtube Searcher</h1>
    <SearchBar @inputChange="onInputChange" />
    <VideoDetail :video="selectedVideo" />
    <VideoList :videos="videos" @selectedVideo="randerVideo" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/videoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY2
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function() {
    return {
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange (inputValue) {
      console.log(inputValue)
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      }).then(res => {
        this.videos = res.data.items
      }).catch(err => {
        console.log(err)
      })
    },
    randerVideo(video) {
      console.log(video)
      this.selectedVideo = video
    },

  }
}
</script>

<style scoped>
  .bg-app{
    background-color: aquamarine;
  }
</style>