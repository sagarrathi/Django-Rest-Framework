<template>
  <ul>
    <li :class="{ active: active_option === 'poor' }">
      <button type="button" @click="activate('poor')">Poor</button>
    </li>
    <li :class="{ active: active_option === 'average' }">
      <button type="button" @click="activate('average')">Average</button>
    </li>
    <li :class="{ active: active_option === 'great' }">
      <button type="button" @click="activate('great')">Great</button>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['modelValue'],
  emits: ['update:modelValue'],

  // data(){
  //     return {
  //         active_option:this.modelValue
  //     }
  // },

  computed: {
    active_option() {
        return this.modelValue;
    }
  },

  methods: {
    activate(option) {
      this.active_option = option;
      this.$emit('update:modelValue', option);
    },
  },
};
</script>

<style scope>
.active {
  border-color: blueviolet;
}
.active button {
  color: blueviolet;
}

ul {
  list-style: none;
  margin: 0.5rem 0;
  padding: 0;
  display: flex;
}

li {
  margin: 0 2rem;
  border: 1px solid #ccc;
  padding: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  font: inherit;
  border: none;
  background-color: transparent;
  cursor: pointer;
}
</style>
