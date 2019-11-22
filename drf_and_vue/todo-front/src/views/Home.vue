<template>
  <div class="home">
    <h1>Todo w/ Django & Vue</h1>
    <TodoInput />
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoList from '@/components/TodoList.vue'
import TodoInput from '@/components/TodoInput.vue'

export default {
  name: 'home',
  data() {
    return {
      todos: [
        {id: 1, title:'Django DRF로 로그인 구현'},
        {id: 1, title:'JWT활용 세션 구현'},
        {id: 1, title:'Todo관련 API 구현'},
        {id: 1, title:'vuex 활용한 Flux 아티택처 적용'},
      ]
    }
  },
  components: {
    TodoList,
    TodoInput,
  }
}
</script>
