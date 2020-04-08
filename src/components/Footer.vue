<template>
  <div>
    <footer class="border-top pt-3">
      <h3 class="text-center">AlkisKalkis.se är inte anslutet till Systembolaget på något sätt, och vi förbehåller om at fel kan uppstå</h3>
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
