import { createRouter, createWebHistory } from 'vue-router'
import Manager from '../views/Manager.vue'
import Login from '../views/Login.vue'
import EmployeesList from '../views/EmployeesList.vue'
import EmployeeProfile from '../views/EmployeeProfile.vue'
import UserSchedule from '../views/UserSchedule.vue'
import Home from '../views/Home.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { authorize: ['Admin','Manager','User'] }
  },
  {
    path: '/manager',
    name: 'Manager',
    component: Manager,
    meta: { authorize: ['Admin','Manager'] }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { authorize: ['Admin','Manager','User'] }
  },

  {
    path: '/employees',
    name: 'EmployeesList',
    component: EmployeesList,
    meta: { authorize: ['Admin','Manager'] }
  },
  {
    path: '/employee/:id',
    name: 'EmployeeProfile',
    component: EmployeeProfile,
    meta: { authorize: ['Admin','Manager'] }
  },
  {
    path: '/user-schedule/',
    name: 'UserSchedule',
    component: UserSchedule,
    meta: { authorize: ['User'] }
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  const { authorize } = to.meta;

  const authPage = ['/login'];
  const isInAuthPage = authPage.includes(to.path);
  const isLoginPage = authPage.includes(from.path);
  const loggedIn = store.getters['auth/loggedIn']


  if(!store.getters["auth/accessToken"]){
    const access_token = localStorage.getItem("access_token");
    const refresh_token = localStorage.getItem("refresh_token");

    if(access_token){
        store.commit('auth/UPDATE_STORAGE',{access:access_token, refresh:refresh_token});
        store.dispatch('auth/setUser')
    }
  }
  var role = null
  try {
    const curentUser = store.getters['auth/currentUser']
    role = curentUser.role['name']
    if(role !=='Manager' && role !== 'Admin'){
      role = 'User'
    }
    console.log('roles ',role)
  } catch (error) {
    console.log(error)

  }
  var i = 0

  if(!loggedIn && !isInAuthPage && !isLoginPage){
    console.log('page login' ,i)
    console.log('from',from.path ,' to', to.path)
    next('/login')
  }else if(loggedIn && isInAuthPage) {
    console.log('page home',i)
    console.log('from',from.path ,' to', to.path)
    next('/')
  }else{
    console.log('from',from.path ,' to', to.path)
    console.log("authorize",authorize.includes(role))
    if(authorize.includes(role)){
      next()
    }else{
      next()
    }
  }

})

export default router
