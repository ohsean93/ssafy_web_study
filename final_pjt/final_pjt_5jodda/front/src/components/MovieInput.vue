<template>
  <div class="5jodda-movieinput">
    <h2>영화 생성</h2>
    <!-- <div class="form-group">
      <label for="title">영화명</label>
      <input v-model="Info.title" type="text" id="title" class="form-control" placeholder="영화 제목을 입력하세요.">
      <br>
      <label for="audience">누적관객수</label>
      <input v-model="Info.audience" type="text" id="audience" class="form-control" placeholder="누적관객수를 입력하세요.">
      <br>
      <label for="posterUrl">포스터 URL</label>
      <input v-model="Info.posterUrl" type="text" id="posterUrl" class="form-control" placeholder="포스터 URL을 입력하세요.">
      <br>
      <label for="description">줄거리</label>
      <input v-model="Info.description" type="text" id="description" class="form-control" placeholder="줄거리를 입력하세요.">
      <br>
      <label for="genres">장르</label>
      <input v-model="Info.genres" type="text" id="genres" class="form-control" placeholder="장르들을 입력하세요.">
    </div> -->
    <!-- <button @click="createMovie()" class="btn btn-primary">등록하기</button> -->
  </div>
</template>

<script>
export default {
  name: 'MovieInput',
  Info: {
  }
}
</script>

<style>

</style>