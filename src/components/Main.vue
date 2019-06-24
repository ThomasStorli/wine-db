<template>
  <div>
    <TopProduct v-bind:item ='items.items[0]' />
    <p> Welcome to WindeDB</p>
    <img src="https://www.wsjwine.com/images/us/wsj/homepage/sliders/2018/november/wsj_185off_Q2Digital_mobile_bottom.jpg"/>
  </div>
</template>

<script>
import TopProduct from './TopProduct.vue'
import axios from 'axios'

export default {
  name: 'Main',
  components: {
    TopProduct
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
