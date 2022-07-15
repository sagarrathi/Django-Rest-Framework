<template>
  <h3>{{ counter }}</h3>
  <p> We do more than that</p>
</template>

<script>
export default {
    computed: {
    counter() {
      return this.$store.getters.noramlizedCounter;
    //   console.log(this.state)
    },
  },
  
};
</script>

<style></style>
