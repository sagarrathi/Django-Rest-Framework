<template>
  <button @click="run_code">Confirm</button>
  <button @click="save_changes">Save changes</button>
  <ul>
    <user-item
      v-for="user in users"
      :key="user.id"
      :name="user.fullName"
      :role="user.role"
    ></user-item>
  </ul>
</template>

<script>
import UserItem from './UserItem.vue';

export default {
  components: {
    UserItem,
  },
  inject: ['users'],
  data() {
    return { changes_saved: false };
  },

  methods: {
    run_code() {
      console.log('Doing something Doing something');
      this.$router.push('/teams');
    },
    save_changes() {
      this.changes_saved = true;
    },
  },

  beforeRouteEnter(to, from, next) {
    console.log('User list CMP beforeRouteEnter');
    console.log(to, from, next);
    next();
  },

  beforeRouteLeave(to, from, next) {
    console.log('before leaving page');
    console.log(to, from, next);

    if (this.changes_saved){
      next();
    } else {
      
      const user_want_to_leave= confirm("Are you share, yo got unsaved changes");
      next(user_want_to_leave);}

  },

  unmounted() {
    console.log('KIndly save data');
  },
};
</script>

<style scoped>
ul {
  list-style: none;
  margin: 2rem auto;
  max-width: 20rem;
  padding: 0;
}
</style>
