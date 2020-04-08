<template>
  <div class="container pb-3">
    <form>
      <div class="form-group">
        <label for="typeSelect">Välj alkoholtyp:</label>
        <select
          id="typeSelect"
          class="form-control"
          v-model="currentType"
          @input="event => { $emit('input', event.target.value) }"
        >
          <option value selected="selected">Alla typer alkohol</option>
          <option v-for="(type, index) in types" :key="index" :value="type">{{type}}</option>
        </select>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "ProductChoose",
  data() {
    return {
      currentType: ""
    };
  },
  props: ["types"]
};
</script>

<style scoped>
</style>
