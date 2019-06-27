<template>
  <div>
    <Header v-bind:updated="items.date"/>
    {{items.items[0].name}}
    <Main v-bind:items="items.items" :types="types" />
    <Footer/>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Main from "./components/Main.vue";
import Footer from "./components/Footer.vue";
import axios from 'axios'

export default {
  name: 'app',
  components: {
    Header,
    Main,
    Footer
  },
  data() {
    return {
      // "link" is a public GitHub Gist for anyone to see
      link: "https://gist.githubusercontent.com/ThomasStorli/91432dde678216ecab41c31ae007f49b/raw/",
      test_link: "https://gist.githubusercontent.com/ThomasStorli/c36723fbc0ed7c2368f30eed186d53b4/raw/134c5dba0da3ac113c07972502c1d50d7ed94d71/gistfile1.json",
      items: null,
      types: ["Vin"]
    }
  },
  methods: {
    loadData(){
      axios.get(this.test_link).then(response =>{
        this.items = response.data
      })
    },
    getTypes(){
      var l = new Array();
      for (var i = 0; i < this.items.items.length; i++){
        l.append(this.items.items[i].name);
      }
      return l;
    }
  },
  beforeMount() {
    this.loadData()
  }
}
</script>

<style>
body {
  font-family: 'Oswald', serif;
}
</style>
