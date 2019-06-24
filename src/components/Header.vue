<template>
  <div>
    <h1> WineDB </h1>
    <p> Last updated: {{updated}} </p>
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
h1 {
  font-size: 2.5em;
  text-align: center;
  color:brown;
}

p {
  font-size: 0.7em;
  text-align: center;
  color: grey;
}
</style>
