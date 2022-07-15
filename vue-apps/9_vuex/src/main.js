import { createApp } from 'vue';
import { createStore } from 'vuex';

import App from './App.vue';

const store = createStore({
  state() {
    return {
      counter: 0,
    };
  },
  mutations: {
    increment(state) {
      setTimeout(() => {
        state.counter += 1;
      }, 2000);
    },

    increase(state, payload) {
      state.counter += payload.value;
    },
  },
  actions: {
    increment()
  },

  getters: {
    finalCounter(state) {
      return state.counter * 10;
    },
    noramlizedCounter(state, getters) {
      const finalCounter = getters.finalCounter;
      if (finalCounter < 0) {
        return 0;
      }
      if (finalCounter > 100) {
        return 100;
      }
      return finalCounter;
    },
  },
});

const app = createApp(App);

app.use(store);
app.mount('#app');
