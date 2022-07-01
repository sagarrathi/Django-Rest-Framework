const app = Vue.createApp({
  data() {
    return {
      counter: 10,
      name:'',
      confirm_name:'',
    };
  },

  methods:{
    add_con(num){this.counter+=num},
    rem_con(num){this.counter+=-num},
    set_name(event, last_name){this.name=event.target.value + last_name},
    submit_form(event){
      // event.preventDefault();
      alert("!!!! Submitted !!!!");
    },
    confirm_input(){this.confirm_name=this.name}

  },
  
  
});

app.mount('#events');
