<template>
<li>
    <img @click="onSelect" :src="url">
</li>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  computed: {
    url() {
      return this.video.snippet.thumbnails.default.url
    },
  },
  methods: {
    onSelect() {
      this.$emit('videoSelect', this.video)
    }
  }
}
</script>

<style>

</style>