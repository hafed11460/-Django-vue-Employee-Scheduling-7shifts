
import axios from 'axios'
import jwtInterceptor from '../shared/jwtInterceptor'
// import { tokenAlive } from "../shared/jwtHelper";

const API_URL = 'http://localhost:8000'

const state = () => ({
    accessToken:null,
    refreshToken:null,
    user:{},

  });

  const getters = {

    accessToken(state){
        return state.accessToken
    },
    loggedIn(state){
        return (state.accessToken != null ? true : false )
    },
    currentUser(state){
        return state.user
    },
    getLocation(state){
        return state.user.location
    },

  };

  const actions = {
        refreshToken({ commit }, accessToken) {
            commit('refreshToken', accessToken);
        },
        userLogin(context, usercredentials){
            return new Promise((resolve,reject)=>{
            axios.post(API_URL +'/login/',{
                email:usercredentials.email,
                password:usercredentials.password
            })
            .then(response =>{
                context.commit('UPDATE_STORAGE',{access:response.data.access,refresh:response.data.refresh})
                resolve()
            })
            .catch(err=>{
                reject(err)
            })
            })
        },
        async setUser({commit}){
                await jwtInterceptor.get('/user/')
                .then(response =>{
                    commit('UPDATE_USER',{user:response.data.user })
                })
                .catch(err=>{
                    console.log(err)
                })
        },
        logout({commit}){
            if(getters.loggedIn){
            commit('DESTROY_TOKEN')
            commit('destroyUser')

            // global destroy store
            commit('global/DESTROY_STORE',{},{ root: true })
            commit('employees/DESTROY_STORE',{},{ root: true })
            commit('shifts/DESTROY_STORE',{},{ root: true })

            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            localStorage.removeItem("user");
            }
        }
  };

  const mutations = {
        refreshToken(state, accessToken) {
            state.status.loggedIn = true;
            state.user = { ...state.user, accessToken: accessToken };
        },
        UPDATE_STORAGE(state,{access,refresh}){
            state.accessToken = access
            state.refreshToken = refresh
            localStorage.setItem("access_token", access);
            localStorage.setItem("refresh_token", refresh);
        },
        DESTROY_TOKEN(state){
            state.accessToken = null
            state.refreshToken = null
            state.location = {}
            state.role = null
        },
        destroyUser(state){
            state.user = null
        },
        UPDATE_USER(state,{user}){
            state.user = user
            localStorage.setItem("user", user);
        },
}



  export default{
      namespaced:true,
      state,
      getters,
      actions,
      mutations
  }