<template>
  <div>
    <Header v-bind:updated="items.date"/>
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
      // "link" is a public GitHub Gist for anyone to see.
      link: "https://gist.githubusercontent.com/ThomasStorli/91432dde678216ecab41c31ae007f49b/raw/",
      items: null
    }
  },
  methods: {
    loadData(){
      axios.get(this.link).then(response =>{
        this.items = response.data
      })
    }
  },
  beforeMount() {
    // Always go to https version of the page
    if (location.protocol == "http:"){
      // TODO: REMOVE COMMENT WHEN BUILDING FOR PRODUCTION
      //window.location.href = "https://www.alkiskalkis.no";
    }

    this.loadData();
  }
}
</script>

<style>
body {
  font-family: 'Oswald', serif;
}
</style>
