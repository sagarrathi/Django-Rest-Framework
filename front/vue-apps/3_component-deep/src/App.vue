<template>
  <div>
    <the-header></the-header>
    <button @click="set_selected_component('active-goals')">Active Goals</button>
    <button @click="set_selected_component('manage-goals')">Manage Goals</button>
    <keep-alive>
      <component :is="selected_component"></component>
    </keep-alive>

  </div>
</template>

<script>
import TheHeader from "./components/TheHeader.vue";
// import BadgeList from "./components/BadgeList.vue";
// import UserInfo from "./components/UserInfo.vue";
// import BaseCard from "./components/BaseCard.vue";
// import CourseGoals from "./components/CourseGoals.vue";
import ActiveGoals from "./components/ActiveGoals.vue";
import ManageGoals from "./components/ManageGoals.vue";

export default {
  components: {
    TheHeader,
    // BadgeList,
    // UserInfo,
    // BaseCard,
    // CourseGoals,
    ActiveGoals,
    ManageGoals,
  },

  data() {
    return {
      selected_component:'active-goals',
      activeUser: {
        name: "Maximilian Schwarzmüller",
        description: "Site owner and admin",
        role: "admin",
      },
    };
    
  },
  methods:{
    set_selected_component(cmp){
      this.selected_component=cmp;}
  }
};
</script>

<style>
html {
  font-family: sans-serif;
}

body {
  margin: 0;
}
</style>
