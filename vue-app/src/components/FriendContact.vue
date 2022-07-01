<template>
  <li>
    <h2>{{ name }} {{ is_missing_f  ? "(missing)" : "" }}</h2>
    <h6>Id:{{ id }}</h6>
    <button @click="toggle_missing()">
      {{ is_missing_f  ? "Found" : "Missing" }}
    </button>

    <button @click="toggle_detail()">
      {{ detail_switch ? "Hide" : "Show" }} Details
    </button>

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
  // props: ["id", "name", "phone", "email", "is_missing"],

  props: {
    id: String,
    phone: { type: String, required: true },
    name: { type: String, required: true },
    email: String,
    is_missing: { 
      type: Boolean, 
      required: false, 
      default: false ,
    },
  },

  data() {
    return {
      detail_switch: false,
      is_missing_f: this.is_missing,
    };
  },

  methods: {
    toggle_detail() {
      this.detail_switch = !this.detail_switch;
    },
    toggle_missing() {
     this.is_missing_f = !this.is_missing_f 
    },
  },
};
</script>
