<template>
  <div>
    <div class="form-group">
      <label for="id">아이디</label>
      <input type="text" id="id" class="form-control" placeholder="아이디를 입력해 주세요!">
    </div>
    <div class="form-group">
      <label for="password">비밀번호</label>
      <input type="password" id="password" class="form-control" placeholder="비밀번호를 입력해 주세요!">
    </div>
    <button class="btn btn-primary">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginFrom'
}
</script>

<style>

</style>