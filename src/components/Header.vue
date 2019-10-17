<template>
  <div class="container text-center header mb-3">
    <a href="AlkisKalkis.no">
      <img src="../assets/AlkisKalkisSmall.png" width="100px" />
    </a>
    <p>Alle varene på polet - sortert etter pris</p>
    <p v-if="getUpdated() == 1" class="updated">Sist oppdatert {{getUpdated()}} time siden</p>
    <p v-else class="updated">Sist oppdatert {{getUpdated()}} timer siden</p>
  </div>
</template>

<script>
export default {
  name: "Header",
  components: {},
  props: ["updated"],
  methods: {
    getUpdated: function(){
      var date = new Date();
      return Math.round((date.getTime() - this.updated)/(1000*60*60));
    }
  }
};
</script>

<style scoped>
.header {
  padding-top: 5px;
  background-color: #fff;
}

h1 {
  font-size: 2.2em;
  text-align: center;
  color: brown;
}

p {
  font-size: 0.8em;
  text-align: center;
  margin-bottom: 0px;
}

.updated {
  color: grey;
  margin-bottom: 10px;
}
</style>
