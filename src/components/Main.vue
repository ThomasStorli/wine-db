<template>
  <div>
    <TopProduct v-bind:item ='items.items[0]' />
    <ProductChoose />
    <ProductList v-bind:items='items.items' />
  </div>
</template>

<script>
import TopProduct from './TopProduct.vue'
import ProductList from './ProductList.vue'
import ProductChoose from './ProductChoose.vue'

export default {
  name: 'Main',
  components: {
    TopProduct,
    ProductChoose,
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
