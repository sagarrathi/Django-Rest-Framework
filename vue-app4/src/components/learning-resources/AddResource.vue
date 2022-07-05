<template>
  <base-dialog v-if="input_is_invalid" title="Invlaid Input" @close="accept_wrong">
  <template #default>
    <p>Unfortunately atleastin one input is valid</p>
    <p>PLease check all input</p>
  </template>
  <template #actions>
    <base-button @click="accept_wrong">Okay</base-button>
  </template>
  
  </base-dialog>
  
  <base-card>
    <form @submit.prevent="submit_data">
      <div class="form-control">
        <label for="title">Title</label>
        <input id="title" name="title" type="text" ref="titleInput" />
      </div>

      <div class="form-control">
        <label for="description">Description</label>
        <textarea
          id="description"
          name="description"
          rows="3"
          ref="descriptionInput"
        />
      </div>

      <div class="form-control">
        <label for="link">Link</label>
        <input id="link" name="link" type="url" ref="linkInput" />
      </div>
      <div>
        <base-button type="submit">Add Resources</base-button>
      </div>
    </form>
  </base-card>
</template>

<script>
export default {
  inject: ['add_resource'],
  data() {
    return {
      input_is_invalid: false,
    };
  },
  methods: {
    accept_wrong() {this.input_is_invalid=false;},
    submit_data() {
      const resource = {
        title: this.$refs.titleInput.value,
        description: this.$refs.descriptionInput.value,
        link: this.$refs.linkInput.value,
      };

      if (
        resource.title.trim() === '' ||
        resource.description.trim() === '' ||
        resource.link.trim() === ''
      ) {
        this.input_is_invalid = true;
      }

      this.add_resource(resource);
    },
  },
};
</script>

<style scoped>
label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  font: inherit;
  padding: 0.15rem;
  border: 1px solid #ccc;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #3a0061;
  background-color: #f7ebff;
}

.form-control {
  margin: 1rem 0;
}
</style>
