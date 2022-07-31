const app = Vue.createApp({
  data() {
    return {
      counter: 0,
      name: "",
      good_name: "",
      full_good_name: "",
    };
  },

  // watch: {
  //   good_name(value){
  //     this.good_full_good_name=value+" "+"Good Name"
  //   },

  counter() {
    console.log("watcher running");
    if (this.counter > 50) {
      this.counter = 0;
    }
  },


  computed: {
    fullname() {
      console.log("running again");
      if (this.name === "") {
        return "";
      }

      return this.name + " Rathi";
    },

    counter_fun() {
      console.log("computed again");
      if (this.counter > 50) {
        this.counter = 0;
      }
      return this.counter;
    },
  },

  methods: {
    setName(event, lastName) {
      this.name = event.target.value;
    },
    add(num) {
      this.counter = this.counter + num;
    },
    reduce(num) {
      this.counter = this.counter - num;
      // this.counter--;
    },
    reset_input() {
      this.name = "";
    },

    output_fullname() {
      console.log("running again");
      if (this.name === "") {
        return "";
      }

      return this.name + " Rathi";
    },
  },
});

app.mount("#events");
