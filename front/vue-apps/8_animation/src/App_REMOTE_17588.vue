<template>
  <div class="container">
    <router-view v-slot="slotProps">
      <transition name="fade-button" mode="out-in"> 
          <component :is="slotProps.Component"></component>
      </transition>
    </router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogIsVisible: false,
      animatedBlock: false,
      paraIsVisible: false,
      usersAreVisible: false,
    };
  },

  methods: {
    showDialog() {
      this.dialogIsVisible = true;
    },
    hideDialog() {
      this.dialogIsVisible = false;
    },

    animateBlock() {
      this.animatedBlock = true;
    },

    toggleParagraph() {
      this.paraIsVisible = !this.paraIsVisible;
    },

    showUsers() {
      this.usersAreVisible = true;
    },
    hideUsers() {
      this.usersAreVisible = false;
    },
    beforeEnter(el) {
      console.log(el);
      el.style.opacity = 0;
    },

    enter(el, done) {
      const interval = setInterval(function () {
        let round = 1;
        el.style.opacity = round * 0.1;
        round = round + 1;
        if (round > 10) {
          clearInterval(interval);
        }
        done;
      }, 20);
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}
html {
  font-family: sans-serif;
}
body {
  margin: 0;
}
button {
  font: inherit;
  padding: 0.5rem 2rem;
  border: 1px solid #810032;
  border-radius: 30px;
  background-color: #810032;
  color: white;
  cursor: pointer;
}
button:hover,
button:active {
  background-color: #a80b48;
  border-color: #a80b48;
}
.block {
  width: 8rem;
  height: 8rem;
  background-color: #290033;
  margin-bottom: 2rem;
  /* transition: transform 3s ease-out; */
}
.container {
  max-width: 40rem;
  margin: 2rem auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  border: 2px solid #ccc;
  border-radius: 12px;
}

/* .v-enter-from {
  opacity: 0;
  transform: translateY(-30px);
}
.v-enter-active {
transition: all 2s ease;
}
.v-leave-to {
  opacity: 1;
  transform: translateY(0px);
} */

@keyframes slide-fade {
  0% {
    transform: translateX(0) scale(1);
  }
  70% {
    transform: translateX(-120px) scale(1.1);
  }

  100% {
    transform: translateX(-150px) scale(1);
  }
}

/* .para-enter-active {
  animation: slide-fade 2s ease-out;
} */

.fade-button-enter-from,
.fade-button-leave-to {
  opacity: 0;
}

.fade-button-enter-active {
  transition: opacity 0.5s ease-out;
}

.fade-button-leave-active {
  transition: opacity 0.5s ease-in;
}

.fade-button-enter-to,
.fade-button-leave-from {
  opacity: 1;
}

.route-enter-from {
}
.route-enter-active {
  animation: slide-fade 2s ease-out;
}
.route-enter-to {
}

.route-leave-active {
  animation: slide-fade 2s ease-in;
}
</style>
