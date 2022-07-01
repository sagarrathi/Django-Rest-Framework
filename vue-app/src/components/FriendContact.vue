<template>
  <li>
    <h2>{{ friend.name }}</h2>
    <button @click="toggle_detail()"> {{detail_switch ? 'Hide': 'Show'}} Details</button>
    <ul v-if="detail_switch">
      <li>
        <strong>{{ friend.phone }}</strong>
      </li>
      <li>
        <strong>{{ friend.email }}</strong>
      </li>
    </ul>
  </li>
</template>

<script>
export default {
  data() {
    return {
      detail_switch: false,
      friend: {
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
};
</script>
