<template>
  <div class="container border">
    <div v-for="(item, index) in items" :key="index" class="row justify-content-center align-items-center border"> 
        <div class="col-2">
          <span class="rank">{{index+1}}</span>
          <span class="image-container">
            <img v-bind:src="item.img"/>
          </span>
        </div>      
        <div class="col-7 border-left border-right">
          <h1>{{ item.name }} </h1>
          <p> {{item.price }}kr {{item.volume}}cl</p>
          <p><small>{{ item.ppa }}kr per liter alkohol</small></p>
        </div>
        <div class="col-3">
          <span class="image-container age-limit">
            <img v-if="item.abv < 22" src="../assets/18.png" />
            <img v-else src="../assets/20.png"/>
          </span>
        </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ProductList',
  props: [
    'items'
  ]
}
</script>

<style scoped>
img {
  height: 60px;
}

small {
  color: grey;
}

p {
  padding: 0;
  margin: 0;
}

h1 {
  font-size: 1.2em;
}

.image-container img{
  display: block;
  margin:auto;
}
.age-limit img{
  height: 50px;
}
.rank {
  position: absolute;
}
</style>
