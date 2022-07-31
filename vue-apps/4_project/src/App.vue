<template>
  <the-header title="My demo app"></the-header>
  <the-resources></the-resources>
</template>

<script>
import TheHeader from './components/layout/TheHeader.vue';
import TheResources from './components/learning-resources/TheResources.vue';

export default {
  components: {
    "the-header": TheHeader,
    "the-resources":TheResources,
},

  data() {
    return {
      
    };
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
  box-sizing: border-box;
}

html {
  font-family: 'Roboto', sans-serif;
}

body {
  margin: 0;
}
</style>
