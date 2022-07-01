const app = Vue.createApp({
  data() {
    return {
      goals: [],
      goal:""
    };
  },

  methods: {
    add_goal() {
      this.goals.push(this.goal)
    },
    rem_item(idx){
      this.goals.splice(idx, 1)

    },
  },


});

app.mount("#user-goals");
