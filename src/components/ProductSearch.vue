<template>
  <div class="container pb-3">
    <form v-on:submit.prevent>
      <div class="form-group">
        <label for="search">Søk etter et produkt:</label>
        <input
          type="text"
          class="form-control"
          v-model="search"
          placeholder="Søk her..."
          @input="event => { $emit('input', event.target.value) }"
        />
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "ProductSearch",
  data() {
    return {
      search: ""
    };
  },
  methods: {
    update: function() {
      this.$emit("searchUpdate", this.search);
    }
  }
};
</script>

<style scoped>
</style>
