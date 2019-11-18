<template>
  <div class="bg-color-search-bar">
    <input @change="onInput" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      // $emit 메소드는 자식 컴포넌트 -> 부모 컴포넌트 data를 올려줄때,
      this.$emit('inputChange', event.target.value)
    }
  }
}
</script>

<style scoped>
  .bg-color-search-bar {
    background-color: bisque;
  }

</style>