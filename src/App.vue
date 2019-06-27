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
      link: "https://gist.githubusercontent.com/ThomasStorli/91432dde678216ecab41c31ae007f49b/raw/",
      test_link: "https://gist.githubusercontent.com/ThomasStorli/c36723fbc0ed7c2368f30eed186d53b4/raw/e55586abe9c3e71a0e8ded1d0686630b337d3287/gistfile1.json",
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
