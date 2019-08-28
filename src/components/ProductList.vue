<template>
  <div class="wrapper table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">
            <small>#</small>
          </th>
          <th scope="col">
            <small>Bilde</small>
          </th>
          <th scope="col">
            <small>Info</small>
          </th>
          <th scope="col">
            <small>Aldersgrense</small>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in products" :key="index">
          <th scope="row">
            <p v-if="type == ''">{{item.IDa + 1}}</p>
            <p v-else>{{item.ID + 1}}</p>
          </th>

          <td>
            <a :href="item.url">
              <img class="productImage" v-bind:src="item.picture" />
            </a>
          </td>
          <td>
            <p>
              <small>{{item.type[0]}} - {{item.land}}</small>
            </p>
            <a :href="item.url">
              <p style="text-decoration: underline; color:#343a40;">{{ item.name }}</p>
            </a>
            <p>{{item.price }}kr {{item.cl}}cl {{item.alcohol}}%</p>
            <p>
              <small>{{ item.price_per_alco }}kr per liter alkohol</small>
            </p>
          </td>
          <td>
            <span class="image-container age-limit">
              <img v-if="item.alcohol < 22" src="../assets/18.png" />
              <img v-else src="../assets/20.png" />
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ProductList",
  props: ["products", "type", "search"]
};
</script>

<style scoped>
.wrapper {
  max-width: 60vw;
  margin: auto;
}
.age-limit img {
  width: 40px;
  height: 40px;
}

h1 {
  font-size: 1.2em;
}

.productImage {
  max-width: 50px;
  max-height: 100px;
}

@media all and (max-width: 499px) {
  .wrapper {
    max-width: 100vw;
  }
  .age-limit img {
    width: 30px;
    height: 30px;
  }

  .productImage {
    max-width: 10vw;
    max-height: 100px;
  }
  p {
    font-size: 4vw;
  }
  h1 {
    font-size: 4vw;
  }
}

small {
  color: grey;
}

p {
  padding: 0;
  margin: 0;
}

.td-image {
  vertical-align: middle;
}

.image-container img {
  display: block;
  margin: auto;
}
</style>
