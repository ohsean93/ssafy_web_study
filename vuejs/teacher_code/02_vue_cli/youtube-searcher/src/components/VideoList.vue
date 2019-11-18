<template>
  <div class="bg-video-list">
    <h2>Video List</h2>
    <ul>
        <VideoListItem v-for="video in videos" :key="video.id.videoId" :video="video" @videoSelect="onVideoSelect" />
    </ul>
  </div>
</template>

<script>
import VideoListItem from './videoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
    },
  },
  methods: {
    onVideoSelect(video) {
      this.$emit('selectedVideo', video)
    }
  },
}
</script>

<style scoped>
  .bg-video-list {
    background-color: cadetblue;
}
</style>