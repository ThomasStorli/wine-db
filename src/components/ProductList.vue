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
      <div v-for="(item, index) in products" :key="index" class="row justify-content-center align-items-center border"> 
        <div class="col-1">
          {{index+1}}
        </div> 
        <div class="col-3">
           <a :href="item.url" target="_blank">
            <div class="col image-container">
              <img v-bind:src="item.picture"/>
            </div>
          </a>
        </div>      
        <div class="col-5 border-left border-right">
          <p v-if="type == ''"><small> {{item.type[0]}} </small></p>
          <a :href="item.url" target="_blank">
            <h1 style="text-decoration: underline; color:#343a40;">{{ item.name }} </h1>
          </a>
          <p> {{item.price }}kr {{item.cl}}cl {{item.alcohol}}%</p>
          <p><small>{{ item.price_per_alco }}kr per liter alkohol</small></p>
        </div>
        <div class="col-3">
          <span class="image-container age-limit">
            <img v-if="item.alcohol < 22" src="../assets/18.png" />
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
    'products',
    'type'
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

.td-image {
  vertical-align: middle;
}

.image-container img{
  display: block;
  margin:auto;
}
.age-limit img{
  width: 40px;
  height: 40px;
}
</style>
