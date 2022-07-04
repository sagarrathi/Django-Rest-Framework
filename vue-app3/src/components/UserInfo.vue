<template>
  <!-- <base-card> -->
  <section>
    <!-- <template v-slot:header> -->
    <h3>{{ fullName }}</h3> 
      <base-badge :type="role" :caption="role.toUpperCase()"></base-badge>
    <!-- </template> -->
    <p>{{ infoText }}</p>
  </section>
  <!-- </base-card> -->
</template>


<script>
export default {
  
  props: ['fullName', 'infoText', 'role'],
};
</script>


<style scoped>
section header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>