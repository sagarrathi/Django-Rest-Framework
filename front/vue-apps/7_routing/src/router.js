import { createRouter, createWebHistory } from 'vue-router';

import TeamsList from './components/teams/TeamsList.vue';
import TeamMembers from './components/teams/TeamMembers.vue';

import UsersList from './components/users/UsersList.vue';

import TeamsFooter from './components/teams/TeamsFooter.vue';
import UsersFooter from './components/users/UsersFooter.vue';

import NotFound from './components/nav/NotFound.vue';


const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', redirect: '/teams' },
      {
        name: 'teams',
        path: '/teams',
        meta: {needsAuth: true},
        components: {
          default: TeamsList,
          footer: TeamsFooter,
        },
        children: [
          {
            name: 'team-members',
            path: ':teamId',
            component: TeamMembers,
            props: true,
          },
        ],
      },
  
      {
        path: '/users',
        components: {
          default: UsersList,
          footer: UsersFooter,
        },
        beforeEnter: (to, from, next) => {
          console.log('user beforeEnter', to, from);
          next();
        },
      },
      { path: '/:notFound(.*)', component: NotFound },
    ],
    linkActiveClass: 'active',
    scrollBehavior(to, from, savedPosition) {
      // console.log('to', to, 'from', from, 'saved', savedPosition);
      if (savedPosition) {
        return savedPosition;
      }
  
      return { left: 0, top: 0 };
    },
  });
  
  router.beforeEach((to, from, next) => {
    console.log("Gloabl beforeEach'");
    console.log('to', to, 'from', from);
    if(to.meta.needsAuth){
      alert("needs login");}
    // if (to.name=='team-members'){
    //   next();
    // } else {
    //   next(   {name:'team-members', params: {teamId: 't2'}});
    // }
    next();
  });
  
  router.afterEach((to, from, next) => {
    console.log("Send anaalytics data'");
    // console.log("to", to, "from", from);
    next();
  });


export default router;
  