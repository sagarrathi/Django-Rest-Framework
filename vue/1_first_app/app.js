// const button_el=document.querySelector('button');
// const input_el=document.querySelector('input');
// const list_el=document.querySelector('ul');

// function add_goal(){
//     const entered_value=input_el.value;
//     const list_item_el=document.createElement("li");
//     list_item_el.textContent=entered_value;
//     list_el.appendChild  (list_item_el);
// }

// button_el.addEventListener('click', add_goa

Vue.createApp({
  data() {
    return {
      goals: [],
      enteredValue: "",
    };
  },
  methods: {
    addGoal() {
      this.goals.push(this.enteredValue);
      this.enteredValue = "";
    },
  },
}).mount("#app");
