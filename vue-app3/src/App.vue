<template>
  <div>
    <the-header></the-header>
    <base-card>
      <badge-list></badge-list>
    </base-card>
    <base-card>
      <user-info
        :full-name="activeUser.name"
        :info-text="activeUser.description"
        :role="activeUser.role"
      ></user-info>
    </base-card>
    <course-goals #default="slotProps">
      <!-- <template #default="slotProps"> -->
      <h2>{{ slotProps.item }}</h2>
      <p>{{slotProps['god']}}</p>
      <!-- </template> -->
      </course-goals>
  </div>
</template>

<script>
import TheHeader from "./components/TheHeader.vue";
import BadgeList from "./components/BadgeList.vue";
import UserInfo from "./components/UserInfo.vue";
import BaseCard from "./components/BaseCard.vue";
import CourseGoals from "./components/CourseGoals.vue";

export default {
  components: {
    TheHeader,
    BadgeList,
    UserInfo,
    BaseCard,
    CourseGoals,
  },

  data() {
    return {
      activeUser: {
        name: "Maximilian Schwarzmüller",
        description: "Site owner and admin",
        role: "admin",
      },
    };
  },
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
