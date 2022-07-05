<template>
  <base-card>
    <base-button @click="set_selected_tab('stored-resources')">Stored Resources</base-button>

    <base-button @click="set_selected_tab('add-resource')">Add Resource</base-button>
  </base-card>

  <component :is="selected_tab"></component>
</template>

<script>
import StoredResources from './StoredResources.vue';
import AddResource from './AddResource.vue';

export default {
  components: {
    StoredResources,
    AddResource,
  },

  data() 
  {
    return {
      selected_tab: 'stored-resources',
      resources: [
        {
          id: 'vuejs',
          title: 'Official Guide',
          description: 'The offcial Vues.js',
          link: 'https://vuejs.org',
        },

        {
          id: 'google',
          title: 'Google',
          description: 'The Search Engine',
          link: 'https://google.com',
        },
      ],
    };
  },

  provide(){
    return {
      resources: this.resources
    }
  },

  methods: {
    set_selected_tab(val) {
      this.selected_tab = val;
    },
  },
};
</script>

<style></style>
