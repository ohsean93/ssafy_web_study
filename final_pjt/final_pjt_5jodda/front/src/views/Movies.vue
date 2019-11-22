<template>
  <div class="5jodda-movie">
    <MovieRec />
    <MovieList />
  </div>
</template>

<script>
import MovieRec from '@/components/MovieRec'
import MovieList from '@/components/MovieList'

export default {
  name: 'Movie',
  components: {
    MovieRec,
    MovieList,
  }
}
</script>

<style>

</style>