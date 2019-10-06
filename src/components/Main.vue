<template>
  <div>
    <div v-if="currentItems != null">
      <TopProduct v-bind:item="currentItems.products[0]" />
      <div
        id="adsgoeshere"
        style="background: #fff; padding-top:60px; text-align: center; padding:0px;"
        v-html="adsenseContent"
      ></div>
      <ProductChoose v-bind:types="types" v-model="currentType" />
      <ProductSearch v-model="search" />
      <ProductList
        v-bind:products="searchFilter(currentItems.products)"
        v-bind:type="currentType"
        v-bind:search="search"
      />
    </div>
  </div>
</template>

<script>
import TopProduct from "./TopProduct.vue";
import ProductList from "./ProductList.vue";
import ProductChoose from "./ProductChoose.vue";
import ProductSearch from "./ProductSearch.vue";

export default {
  name: "Main",
  components: {
    TopProduct,
    ProductChoose,
    ProductSearch,
    ProductList
  },
  data() {
    return {
      types: [],
      currentType: "",
      currentItems: null,
      adsenseContent: "",
      search: ""
    };
  },
  props: ["items"],
  methods: {
    searchFilter: function(lst) {
      let newList = [];
      for (let i = 0; i < lst.length; i++) {
        const el = lst[i];
        if (this.searchCheck(el.name)) {
          newList.push(el);
        }
      }
      return newList;
    },
    searchCheck: function(name) {
      if (name.toLowerCase().includes(this.search.toLowerCase())) {
        return true;
      } else if (this.search == "") {
        return true;
      }
      return false;
    },
    getTypes: function() {
      var l = [];
      for (var i = 0; i < this.items.length; ++i) {
        if (this.items[i].name != "top") {
          l.push(this.items[i].name);
        }
      }
      this.types = l;
    },
    getCurrentItems: function(val) {
      for (var i = 0; i < this.items.length; ++i) {
        if (val == "") {
          this.currentItems = this.items[0];
          break;
        }
        if (this.items[i].name == val) {
          this.currentItems = this.items[i];
          break;
        }
        this.currentItems = null;
      }
    }
  },
  mounted() {
    this.getTypes();
    this.getCurrentItems(this.currentType);
    this.adsenseContent = document.getElementById(
      "divadsensedisplaynone"
    ).innerHTML;
  },
  watch: {
    currentType: function(val) {
      this.getCurrentItems(val);
    }
  }
};
</script>

<style scoped>
p {
  text-align: center;
}

img {
  display: block;
  margin: auto;
  width: 50%;
}
</style>
