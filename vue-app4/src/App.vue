<template>
  <the-header title="My demo app"></the-header>
  <ul>
    <stored-resources
    :resources="resources"
    ></stored-resources>
  </ul>
</template>

<script>
import StoredResources from './components/learning-resources/StoredResources.vue';
import TheHeader from './components/layout/TheHeader.vue';

export default {
  components: {
    'stored-resources': StoredResources,
    'the-header':TheHeader,
  },

  data() {
    return {
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
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

* {
  box-sizing: border-box;
}

html {
  font-family: 'Roboto', sans-serif;
}

body {
  margin: 0;
}
</style>
