<template>
  <div>
    <TopProduct v-bind:item ='items[0].prods[0]' />
    <ProductChoose v-bind:types='types'/>
    <ProductList v-bind:items='items.items[0].prods' />
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
    'items',
    'types'
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
