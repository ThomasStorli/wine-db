<template>
  <div>
    <TopProduct v-bind:item ='items.items[0]' />
    <ProductList v-bind:items='items.items' />
  </div>
</template>

<script>
import TopProduct from './TopProduct.vue'
import ProductList from './ProductList.vue'
import axios from 'axios'

export default {
  name: 'Main',
  components: {
    TopProduct,
    ProductList
  },
  props: [
    'items'
  ]
}
</script>

<style scoped>
p{
  text-align: center;
}

img {
  display: block;
  margin: auto;
  width: 50%;
}
</style>
