export default {
    login(context){
        context.commit('setAuth',  {isAuth: true});
    },
    login(context){
        context.commit('setAuth',{isAuth: false});
    },
}


