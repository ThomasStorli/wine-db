<template>
  <div>
    <footer class="border-top pt-3">
      <h3 class="text-center">AlkisKalkis.no er ikke tilknyttet til Vinmonopolet på noen måte, og vi tar forbehold om at feil kan forekomme</h3>
      <div class="views-container container">
        Visninger:
        <a href="https://smallseotools.com/visitor-hit-counter/" target="_blank" rel="nofollow noopener"><img src="https://smallseotools.com/counterDisplay?code=37cd004a1113781d935e74d88578d154&style=0013&pad=8&type=page&initCount=248" border="0"></a>
      </div>
      <h1 class="pt-2">AlkisKalkis - {{ new Date().getFullYear() }}</h1>
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
.views-container {
  text-align: center;
  margin: auto;
}

.views-container a {
  height: 5px;
}

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
