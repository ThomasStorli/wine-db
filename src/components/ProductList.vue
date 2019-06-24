<template>
  <div class="container border">
    <div v-for="(item, index) in items" :key="index" class="row justify-content-center align-items-center border"> 
        <div class="col-2">
          <span class="image-container">
            <img v-bind:src="item.img"/>
          </span>
        </div>      
        <div class="col-7 border-left border-right">
          <p>{{ item.name }} </p>
          <p><small>{{ item.ppa }} ppa</small></p>
        </div>
        <div class="col-3">
          <span class="image-container">
            <img v-if="item.abv < 22" src="https://www.bingono.org/wp-content/uploads/2017/12/18plus.png" />
            <img v-else src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Norwegian-road-sign-362.6.svg/1200px-Norwegian-road-sign-362.6.svg.png"/>
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

.image-container img{
  display: block;
  margin:auto;
}
</style>
