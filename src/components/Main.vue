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
  data() {
    return {
      // "link" is a public GitHub Gist for anyone to see
      link: "https://gist.githubusercontent.com/ThomasStorli/91432dde678216ecab41c31ae007f49b/raw/",
      items: null
    }
  },
  methods: {
    loadData(){
      axios.get(this.link).then(response =>{
        this.items = response.data
      })
    }
  },
  beforeMount() {
    this.loadData()
  }
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
