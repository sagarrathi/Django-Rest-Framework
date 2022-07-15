<template>
 <button @click="inc">increment</button>
 <button @click="increase({value:10})">increase</button>
 
</template>

<script>
import {mapActions} from 'vuex';

export default {
    methods: {
        // ...mapActions(['increment', 'increase'])
        ...mapActions({
            inc: 'increment',
            increase: 'increase',
        })
        // addOne(){
        //     this.$store.dispatch('increment');
        // },

        // addTwo(){
        //     this.$store.dispatch('increase',{value:18})
        // }
    }
}
</script>
