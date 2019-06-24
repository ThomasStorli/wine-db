<template>
  <div class="mx-2">
    <div class="container border">
      <div class="row justify-content-center align-items-center border">
          <div class="col-1">
            <small>#</small>
          </div> 
          <div class="col-3 text-center">
            <small>Bilde</small>
          </div>      
          <div class="col-5 border-left border-right">
            <small>Info</small>
          </div>
          <div class="col-3 text-center">
            <small>Aldersgrense</small>
          </div>
      </div>
      <div v-for="(item, index) in items" :key="index" class="row justify-content-center align-items-center border"> 
          <div class="col-1">
            {{index+1}}
          </div> 
          <div class="col-3">
            <div class="col image-container">
              <img v-bind:src="item.img"/>
            </div>
          </div>      
          <div class="col-5 border-left border-right">
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
  width: 40px;
  height: 40px;
}
.rank {
}
</style>
