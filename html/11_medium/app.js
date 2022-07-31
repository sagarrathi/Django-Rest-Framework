const app = Vue.createApp({
  data() {
    return {
      friends: [
        {
          id: "ram",
          name: "ram raghuvanshi",
          phone: "0214",
          email: "ram@bharat.in",
        },
        {
          id: "sita",
          name: "sita raghuvanshi",
          phone: "0214",
          email: "sita@janki.in",
        },
      ],
    };
  },
});


app.component('user-contact', {
  template: `
  <li>
  <h2>{{freind.name}}</h2>
    <button v-if="!detail_switch" @click="toggle_detail()">Show Details</button>
    <button v-if="detail_switch" @click="toggle_detail()">Hide Details</button>
  <ul v-if="detail_switch">
        <li><strong>Phone:</strong> {{freind.name}}</li>
        <li><strong>Email:</strong> {{freind.email}}</li>
    </ul>
  </li>
  `,

  data() {
    return {
      detail_switch: false,
      freind: {
        id: "ram",
        name: "ram raghuvanshi",
        phone: "0214",
        email: "ram@bharat.in",
      },
    };
  },

  methods: {
    toggle_detail() {
      this.detail_switch = !this.detail_switch;
    },
  },
});

app.mount('#app');

