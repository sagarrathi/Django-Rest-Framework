<template>
  <h3>{{ finalCounter }}</h3>
</template>

<script>
import { mapGetters} from 'vuex'

export default {
  computed: {
    ...mapGetters('numbers', ['finalCounter'])
    // counter() {
    //   return this.$store.getters.finalCounter;
    // //   console.log(this.state)
    // },
  },
};
</script>

<style></style>
