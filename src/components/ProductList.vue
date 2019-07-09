<template>
  <div class="container">
    <table class="table">
      <thead>
        <tr>
          <th scope="col"><small>#</small></th>
          <th scope="col"><small>Bilde</small></th>
          <th scope="col"><small>Info</small></th>
          <th scope="col"><small>Aldersgrense</small></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in products" :key="index">
          <th scope="row">{{index+1}}</th>
          <td><img v-bind:src="item.picture"/></td>
          <td>
            <p v-if="type == ''"><small> {{item.type[0]}} </small></p>
            <a :href="item.url">
              <h1 style="text-decoration: underline; color:#343a40;">{{ item.name }} </h1>
            </a>
            <p> {{item.price }}kr {{item.cl}}cl {{item.alcohol}}%</p>
            <p><small>{{ item.price_per_alco }}kr per liter alkohol</small></p>
          </td>
          <td>
            <span class="image-container age-limit">
              <img v-if="item.alcohol < 22" src="../assets/18.png" />
              <img v-else src="../assets/20.png"/>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
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
