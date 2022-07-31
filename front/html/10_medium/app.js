const app = Vue.createApp({
  data() {
    return {
      currentUserInput: "",
      message: "Vue is great!",
    };
  },
  methods: {
    // saveInput(event) {
    //   this.currentUserInput = event.target.value;
    // },
    setText() {
      this.message = this.$refs.save_input.value;
      console.log(this.$refs.save_input)
      console.dir(this.$refs.save_input)
    },
  },
});

app.mount("#app");

// ..

const data = {
  message: "hello",
  long_message: "jdskdnjksndksjn",
};

const handler = {
  set(target, key, value) {
    console.log(target);
    console.log(key);
    console.log(value);
    if (key === 'message') {
      target.long_message = value + "long wala";
    } else {
      target.message=value
    }
  },
};

const proxy = new Proxy(data, handler);

proxy.message = "Hellooo...";

console.log(proxy.long_message)
