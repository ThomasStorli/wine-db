<template>
  <div class='container text-center border w-50 pt-1 alert alert-light'>
    <h3> Billigste drikke </h3>
    <img v-bind:src="item.img" style="height: 150px;">
    <h3>
    {{item.name}}
    </h3>
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
