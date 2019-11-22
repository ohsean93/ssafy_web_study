<template>
  <div class="5jodda-movie">
    <MovieInfo />
    <ReviewInput />
    <ReviewList />
  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'
import ReviewInput from '@/components/ReviewInput'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'Movie',
  components: {
    MovieInfo,
    ReviewInput,
    ReviewList,
  }
}
</script>

<style>

</style>