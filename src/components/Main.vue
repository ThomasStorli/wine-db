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
  data() {
    return {
      // "link" is a public GitHub Gist for anyone to see
      link: "https://gist.githubusercontent.com/ThomasStorli/91432dde678216ecab41c31ae007f49b/raw/3a0b8fde6c58c5ae5463c30ac7e0ccf45d9f48c4/wine-db-data.json",
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
