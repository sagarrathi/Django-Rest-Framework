<template>
  <section>
    <base-card>
      <h2>Submitted Experiences</h2>
      <div>
        <base-button @click="load_experiences"
          >Load Submitted Experiences</base-button
        >
      </div>
    
      <p v-if="is_loading">Loading....</p>
      <p v-else-if=" error">{{ error }}</p>
      <p v-else-if="(results.length === 0 || !results)">
        No strored Experice. Add survey
      </p>
      <ul v-else>
        <survey-result
          v-for="result in results"
          :key="result.id"
          :name="result.name"
          :rating="result.rating"
        ></survey-result>
      </ul>
    </base-card>
  </section>
</template>

<script>
import SurveyResult from './SurveyResult.vue';

export default {
  components: {
    SurveyResult,
  },

  data() {
    return {
      results: [],
      is_loading: true,
      error: null,
    };
  },

  methods: {
    load_experiences() {
      this.is_loading=true,
      this.error=null,
      fetch('https://vue-http-d534a-default-rtdb.firebaseio.com/survey.json')
        .then((response) => {
          if (response.ok) {
            return response.json();
          }
        })
        .then((data) => {
          this.is_loading = false;

          console.log(data);
          const results = [];
          for (const id in data) {
            results.push({
              id: id,
              name: data[id].name,
              rating: data[id].rating,
            });
          }
          this.results = results;
        })
        .catch((error) => {
          this.is_loading=false;
          console.log(error);
          this.error = 'Failed to fetch data -Try later';
        });
    },
  },
  mounted() {
    this.load_experiences();
  },
};
</script>

<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
</style>
