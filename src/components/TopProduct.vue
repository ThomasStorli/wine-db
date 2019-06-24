<template>
  <div>
    <footer>
      <h1> {{item.name}} </h1>
      <!--<img src="{{item.name}}" />-->
    </footer>
  </div>
</template>

<script>

export default {
  name: 'TopProduct',
  props: [
    'item'
  ]
}
</script>

<style scoped>
h1 {
  font-size: 1em;
  text-align: center;
}

img {
  width: 50%;
}
</style>
