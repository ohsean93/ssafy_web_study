<template>
  <div class="5jodda-loginform">
    <h2>Log-in</h2>
      <div class="form-group">
        <label for="id">ID</label>
        <input v-model="credentials.username" type="text" id="id" class="form-control" placeholder="ID를 입력하세요.">
        <br>
        <label for="password">Password</label>
        <input v-model="credentials.password" type="password" id="password" class="form-control" placeholder="비밀번호를 입력하세요.">
      </div>
    <!-- <button @click="login()" class="btn btn-primary">Log-in</button> -->
  </div>
</template>

<script>
// import axios from 'axios'
// import router from '@/router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {}
    }
  },
  methods: {
    // login() {
    //   axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
    //   .then(res => {
    //     this.$session.start()
    //     this.$session.set('jwt', res.data.token)
    //     router.push('/')
    //   })
    // }
  },
}
</script>

<style>

</style>