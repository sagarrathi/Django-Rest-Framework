<template>
  <li>
    <h2>{{ name }} {{ is_missing  ? "(missing)" : "" }}</h2>
    <h6>Id:{{ id }}</h6>
    <button @click="toggle_missing()">
      {{ is_missing ? "Found" : "Missing" }}
    </button>

    <button @click="toggle_detail()">
      {{ detail_switch ? "Hide" : "Show" }} Details
    </button>

    <ul v-if="detail_switch">
      <li>
        <strong> Phone: </strong>
          {{ phone }}
      </li>
      <li>
        <strong>Email: </strong> 
          {{ email }}
      </li>
    </ul>      
    <button @click="$emit('delete-contact',id)">Delete</button>
  </li>
</template>

<script>
export default {
  // props: ["id", "name", "phone", "email", "is_missing"],

  props: {
    id: { type: String, required: true }, 
    phone: { type: String, required: true },
    name: { type: String, required: true },
    email: String,
    is_missing: { type: Boolean, },
  },

  emits:['toggle-missing-event', 'delete-contact'],
  
  // emits: {
  //   'toggle-missing-event': function(id){
  //     if (id){return true;} else {return false;}
  //   }
  // },

  data() {
    return {
      detail_switch: false,
    };
  },

  methods: {
    toggle_detail() {
      this.detail_switch = !this.detail_switch;
    },
    toggle_missing() {
     this.$emit('toggle-missing-event', this.id); 
    },

    
  },
};
</script>
