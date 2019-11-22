<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/movie">Movie</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/user">MyPage</router-link> |
      <router-link to="/adminmovie">Admin-Movie</router-link> |
      <router-link to="/adminuser">Admin-User</router-link>
    </div>
    <div>
      <router-view />
    </div>
  </div>
</template>

<script>

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
