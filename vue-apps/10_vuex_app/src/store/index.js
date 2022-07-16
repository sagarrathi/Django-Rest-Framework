import {createStore} from 'vuex';

// import rootMutations from './mutation.js'
// import rootActions from './actions.js'
// import rootGetters from './actions.js'

import productModule from './modules/products.js'
import cartModule from './modules/cart.js'


const store = createStore({
    modules: {
        prods:productModule,
        cart:cartModule,
    },

    // state() {return {
    //     isLoggedIn: false,
    // }},
    
    // mutations:rootMutations,
    // actions:rootActions,
    // getters:rootGetters

});

export default store;




