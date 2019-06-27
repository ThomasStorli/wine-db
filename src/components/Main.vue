<template>
  <div>
    <TopProduct v-bind:item ='currentItems.prods[0]' />
    <ProductChoose v-bind:types='types' v-model="currentType"/>
    <ProductList v-bind:products='currentItems.prods' v-bind:type="currentType"/>
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
  data() {
    return {
      types: [],
      currentType: "",
      currentItems: null
    }
  },
  props: [
    'items'
  ],
  methods: {
    getTypes: function(){  
      var l = [] 
      for (var i = 0; i < this.items.length; ++i){
        l.push(this.items[i].name);
      }
      this.types = l;
    },
    getCurrentItems: function(val){
      for (var i = 0; i < this.items.length; ++i){
        if (val == ""){
          this.currentItems = this.items[0]
          break;
        }
        if (this.items[i].name == val){
          this.currentItems = this.items[i]
          break;
        }
        this.currentItems = null
      }
    }
  },
  mounted() {
    this.getTypes();
    this.getCurrentItems(this.currentType);
  },
  watch: {
    currentType: function(val){
      this.getCurrentItems(val)
    }
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
