const app = Vue.createApp({
  data() {
    return {
      boxA: false,
      boxB: false,
      boxC: false,
      counter:90,
    };
  },

  methods: {
    box_selected(box) {
      if (box === 'A') {
        this.boxA =! this.boxA;
      } else if (box === 'B') {
        this.boxB =! this.boxB;
      } else if (box === 'C') {
        this.boxC =! this.boxC;
      }
    },
  },

  computed: {
    boxAClasses(){ return {active: this.boxA};},
    boxBClasses(){ return {active: this.boxB};},
    boxCClasses(){ return {active: this.boxC};},
  },

  watch: {},
});

app.mount('#styling');


// const app2 = Vue.createApp({
//     data() {
//       return {
//         counter: 90,
//         name: '',
//         good_name: '',
//         full_good_name: '',
//       };
//     },
// });
  
// app2.mount('#styling');
  

