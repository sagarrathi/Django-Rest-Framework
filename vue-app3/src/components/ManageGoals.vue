<template>
  <h2>Manage Goals</h2>
  <input type="text" ref="goal" />
  <button @click="set_goal">Set Goal</button>
  <error-alert v-if="input_is_invalid">
    <h2>Input Invalid</h2>
    <p>Please enetr data</p>
    <button @click="confirm_wrong">Ok</button>
  </error-alert>
</template>

<script>
import ErrorAlert from "../components/ErrorAlert.vue";

export default {
  components: {
    ErrorAlert,
  },

  data() {
    return {
      input_is_invalid: false,
    };
  },

  methods: {
    set_goal() {
      const entered_value = this.$refs.goal.value;
      if (entered_value === "") {
        this.input_is_invalid = true;
      }
    },

    confirm_wrong(){
        this.input_is_invalid=false;
    }
  },
};
</script>
