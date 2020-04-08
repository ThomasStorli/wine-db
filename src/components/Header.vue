<template>
  <div class="container text-center header mb-3">
    <div>
      <span style="float:right; ">
        <img src="" alt="" />
      </span>
    </div>
    <div class="mt-2">
      <a href="AlkisKalkis.no">
      <img src="../assets/AlkisKalkisSmall.png" width="100px" />
    </a>
      <span v-on:click="gotoNO()" style="position:absolute; float:right; margin-left:20vw; cursor: pointer;">
        <img src="../assets/Flag_of_Norway.svg" width="40px" alt="" />
        <p> Norsk side </p>
      </span>
    <p>Allt på Systembolaget - Sorterat efter pris</p>
    <p v-if="getUpdated() == 1" class="updated">Senast uppdaterad för {{getUpdated()}} timme sedan</p>
    <p v-else class="updated">Sist oppdatert {{getUpdated()}} timmar sedan</p>
    
    </div>
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
    },
    gotoNO: function() {
      window.location.href = "https://www.alkiskalkis.no";
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
.stroke {
    -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: black;
  font-size:1.5em;
}
</style>
