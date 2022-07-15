export default {
  testAuth(state, getters, rootState, rootGetter) {
    console.log(state, getters, rootGetter);
    return rootState.isLoggedIn;
  },

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
};
