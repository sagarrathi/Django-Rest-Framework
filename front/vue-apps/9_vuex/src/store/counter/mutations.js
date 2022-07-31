export default {
  increment(state) {
    state.counter += 1;
  },

  increase(state, payload) {
    console.log('state', state);
    state.counter += payload.value;
  },
};
