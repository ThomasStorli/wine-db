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
      // "link" is a public GitHub Gist for anyone to see
      link: "https://gist.githubusercontent.com/AlexanderDeBattista/c93e0407cfe939d0a77137cc8ad210f8/raw",
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
    this.loadData();
  }
}
</script>

<style>
body {
  font-family: 'Oswald', serif;
}
</style>
