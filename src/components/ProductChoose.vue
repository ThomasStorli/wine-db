<template>
  <form>
    <div class="container">
    <div class="row pb-2">
      <div class="col">
      <select class="form-control" id="exampleFormControlSelect1">
        <option>Alle typer alkohol</option>
        <option>Vin</option>
        <option>Brennevin</option>
        <option>Whiskey</option>
        <option>Øl</option>
      </select>
    </div>
    <div class="col">
      <input class="form-check-input" type="checkbox" id="gridCheck">
      <label class="form-check-label" for="gridCheck">
        18+
      </label>
    </div>
    </div>
    </div>
  </form>
</template>

<script>

export default {
  name: 'Footer',
  components: {
  }
}
</script>

<style scoped>
</style>
