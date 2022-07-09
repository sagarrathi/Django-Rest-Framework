<template>
  <section>
    <h2>{{ teamName }}</h2>
    <ul>
      <user-item
        v-for="member in members"
        :key="member.id"
        :name="member.fullName"
        :role="member.role"
      ></user-item>
    </ul>
    <router-link to="/teams/t2">Go to Team 2</router-link>
  </section>
</template>

<script>
import UserItem from '../users/UserItem.vue';

export default {
  inject: ['users', 'teams'],
  props:['teamId'],
  components: {
    UserItem,
  },

  data() {
    return {
      teamName: '',
      members: [],
    };
  },

  methods: {
    get_team_members(teamId) {
      //When all data is avaibale but not rendedered
      // if (this.teamId) {
      // const teamId = this.teamId;
      const selected_team = this.teams.find((team) => team.id === teamId);
      this.teamName = selected_team.name;
      const members = selected_team.members;
      for (const member of members) {
        const selected_user = this.users.find((user) => user.id === member);
        this.members.push(selected_user);
      }
      // }
    },
  },
  created() {
    this.get_team_members(this.teamId);
    },

  watch: {
    teamId(newId) {
      this.get_team_members(newId);},
  },
};
</script>

<style scoped>
section {
  margin: 2rem auto;
  max-width: 40rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  border-radius: 12px;
}

h2 {
  margin: 0.5rem 0;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
</style>
