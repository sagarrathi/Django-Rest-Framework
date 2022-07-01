<template>
  <li>
    <h2>{{ name }}</h2>
    <h6>Id:{{id}}</h6>
    <button @click="toggle_detail()"> {{detail_switch ? 'Hide': 'Show'}} Details</button>
    <ul v-if="detail_switch">
      <li>
        <strong>{{ phone }}</strong>
      </li>
      <li>
        <strong>{{ email }}</strong>
      </li>
    </ul>
  </li>
</template>

<script>
export default {
  props: [
    'id',
    'name',
    'phone',
    'email',
  ], 

  data() {
    return {
      detail_switch: false,
    };
  },

  methods: {
    toggle_detail() {
      this.detail_switch = !this.detail_switch;
    },
  },
};
</script>
