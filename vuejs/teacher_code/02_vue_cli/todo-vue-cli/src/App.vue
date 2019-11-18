<template>
  <div>
    <h1>John의 Todo 앱</h1>
    <TodoList category="취업준비" />
    <TodoList category="SSAFY" />
    <TodoList category="기타" />
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'

export default {
  components: {
    TodoList: TodoList
  }
}
</script>

<style lang="stylus" scoped>

</style>