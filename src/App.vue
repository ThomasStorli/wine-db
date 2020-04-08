<template>
  <div>
    <div v-if="items != null">
      <Header :updated="items.date"/>
      <Main :items="items.items"/>
      <Footer/>
    </div>
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
      link: "https://gist.githubusercontent.com/AlexanderDeBattista/65a1e9bc7280d77f89e655cc5f027225/raw/",
      items: null
    }
  },
  methods: {
    loadData(){
      axios.get(this.link).then(response =>{
        this.items = response.data;
      })
    }
  },
  beforeMount() {
    if (
      location.hostname !== "localhost" &&
      location.hostname !== "127.0.0.1"
    ) {
      if (location.protocol != "https:") {
        location.replace(
          "https:" +
            window.location.href.substring(window.location.protocol.length)
        );
      }
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
