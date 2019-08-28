<template>
  <div>
    <footer>
      <h3
        class="text-center"
      >AlkisKalkis.no er ikke tilknyttet til Vinmonopolet på noen måte, og vi tar forbehold om at feil kan forekomme</h3>
      <h1>AlkisKalkis - {{ new Date().getFullYear() }}</h1>
    </footer>
  </div>
</template>

<script>
export default {
  name: "Footer",
  components: {}
};
</script>

<style scoped>
h1 {
  font-size: 1em;
  text-align: center;
}
h3 {
  font-size: 0.9em;
}

footer {
  margin-top: 15px;
  margin-bottom: 15px;
}
</style>
