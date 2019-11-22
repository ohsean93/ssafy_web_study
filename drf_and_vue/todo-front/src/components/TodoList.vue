<template>
  <div class="todo-list">
    <h2>todo 목록</h2>
    <div class="card col-12" v-for="todo in todos" :key="todo.id">
      <div class="card-body">
        <span>
          {{ todo.title }}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
    },
  },
}
</script>

<style>

</style>