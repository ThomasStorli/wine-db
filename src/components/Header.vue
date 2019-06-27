<template>
  <div class="container header border-bottom mb-3">
    <h1> Wine<span style="color: black;">DB</span></h1>
    <p> Sist Oppdatert: {{updated}} </p>
  </div>
</template>

<script>

export default {
  name: 'Header',
  components: {
  },
  props: [
    'updated'
  ]
}
</script>

<style scoped>
.header {
  padding-top:5px;
  background-color:#fff;
}

h1 {
  font-size: 2.2em;
  text-align: center;
  color:brown;
}

p {
  font-size: 0.7em;
  text-align: center;
  color: grey;
  margin-bottom: 10px;
}
</style>
