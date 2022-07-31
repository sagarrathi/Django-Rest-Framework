const app = Vue.createApp({
  data: function () {
    return {
      message1: "helow world",
      message2: "<h1>helow earth</h1>",
      some_link: "http://google.com"
    }; //  Always return a object}, // older method
  },
  methods: {
    out_goal: function() {
      const rand_num =Math.random();
      if (rand_num <0.5){
        return this.message1;
      } else {
        return this.message2;
      }
    }
  }
  //   data () {}  // is new method
}).mount("#user-goal");
