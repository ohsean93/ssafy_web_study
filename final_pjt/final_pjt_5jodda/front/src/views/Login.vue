<template>
  <div class="5jodda-login">
    <LoginForm />
    <Signup />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'
import Signup from '@/components/Signup'

export default {
    name: 'Login',
    components: {
        LoginForm,
        Signup,
    }
}
</script>

<style>

</style>