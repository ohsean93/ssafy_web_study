<template>
  <div class="bg-detail">
    <h2>Video Detail</h2>
    <p>{{ video.snippet.title }}</p>
    <iframe :src="iframeURL" frameborder="0"></iframe>
    <h3>Detail</h3>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    iframeURL() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style scoped>
  .bg-detail {
    background-color: darkkhaki;
  }
</style>