<template>
    <div class='container text-center border w-50 pt-1 alert alert-light'>
      <a :href="item.url">
      <div>
        <h3> Billigste drikke </h3>
        <img v-bind:src="item.picture" style="height: 150px;">
        <h3>
          {{item.name}} 
          <img v-if="item.alcohol < 22" style="width:23px;" src="../assets/18.png" />
          <img v-else style="width:23px;" src="../assets/20.png" />
        </h3>
        <div class="dropdown-divider"></div>
          <h3>
            {{item.price}}kr
          </h3>
          <h3>
            {{item.cl}} cl
          </h3>
          <h3>
            {{item.alcohol}}%
          </h3>
          <h3>
            {{item.price_per_alco}}kr per liter rent alkohol
          </h3>
        </div>
      </a>
    </div>
</template>

<script>

export default {
  name: 'TopProduct',
  props: [
    'item'
  ]
}
</script>

<style scoped>
.centerText{
  display: block;
  margin: auto;
}
h3{
  font-size: 1.2em;
}

a {
  text-decoration: none;
  color: #343a40;
}

a:hover {
  text-decoration: none;
  color:#343a40;
}

a:visited {
  text-decoration: none;
  color:#343a40;
}

a:active {
  text-decoration: none;
  color:#343a40;
}

.border {
  /* 
  * NOTE: !important is needed in this case because Bootstrap 
  * also uses !important in many of the utility classes 
  * like border-*.
  */
  border-width: 3px !important;
}
.container{
  color: #343a40 !important;
}
</style>
