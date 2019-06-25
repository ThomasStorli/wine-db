<template>
  <div class="container pb-3">
    <form>
      <div class="form-group">
        <label for="typeSelect"> Alkohol Type </label>
        <select id="typeSelect" class="form-control">
            <option value="Alle typer alkohol" selected="selected">Alle typer alkohol</option>
            <option v-for="(type, index) in types" :key="index">{{type}}</option>
        </select>
      </div>
      <div class="form-row">
        <div class="col">
          <label for="minABV"> Minimum ABV </label>
          <input id="minABV" type="number" class="form-control" value="0" min="0" max="60" step="1"/>
        </div>
        <div class="col">
          <label for="maxABV"> Maks ABV </label>
          <input id="maxABV" type="number" class="form-control" value="60" min="0" max="60" step="1"/>
        </div>
        <div class="col">
          <label for="agelimit"> Aldersgrense </label>
          <select id="agelimit" class="form-control">
              <option value="18">18+</option>
              <option value="20" selected="selected">20+</option>
          </select>
        </div>
      </div>
    </form>
  </div>
</template>

<script>

export default {
  name: 'Footer',
  components: {
  },
  props: [
    'types'
  ]
}
</script>

<style scoped>
</style>
