<template>
  <div class='container text-center'>
    <h3> Billigste drikke </h3>
    <img v-bind:src="item.img" style="height: 150px;">
    <h1>
    {{item.name}}
    </h1>
    <div class="dropdown-divider"></div>
    <h3>
    {{item.price}},-
    </h3>
    <h3>
    {{item.volume}} cl
    </h3>
    <h3>
    {{item.ppa}},- per l/alcohol
    </h3>
    </div>
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
.centerText{
  display: block;
  margin: auto;
}
h3{
  font-size: 1.2em;
}
</style>
