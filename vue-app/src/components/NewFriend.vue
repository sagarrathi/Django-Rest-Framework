<template>
  <form @submit.prevent="submit_data">
    <div>
      <label>Name</label>
      <input type="text" v-model="name" />
    </div>

    <div>
      <label>Phone</label>
      <input type="tel" v-model="phone" />
    </div>

    <div>
      <label>Email</label>
      <input type="email" v-model="email" />
    </div>
    <div>
    <button>Add Conatact</button>
    </div>
  </form>
</template>

<script>
export default {
  emits: ["add-contact"],

  data() {
    return {
      name: '',
      phone: '',
      email: '',
    };
  },

  methods: {
    submit_data() {
      this.$emit("add-contact", this.name, this.phone, this.email );
    },
  },
};
</script>
