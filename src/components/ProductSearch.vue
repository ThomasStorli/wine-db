<template>
  <div class="container pb-3">
    <form v-on:submit.prevent>
      <div class="form-group">
        <label for="search">Sök efter produkter</label>
        <input
          type="text"
          class="form-control"
          v-model="search"
          placeholder="Sök här..."
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
      this.$emit('input', this.search);
    },
    getSearch: function() {
        this.search = new URL(window.location).searchParams.get("id");
        this.update();
    }
  },
  mounted() {
    this.getSearch();
  }
};
</script>

<style scoped>
</style>
