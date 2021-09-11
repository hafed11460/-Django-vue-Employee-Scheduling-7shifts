// import axios from 'axios'
import jwtInterceptor from '../shared/jwtInterceptor'
const state = ()=>({
    offers:[]
})

const getters  = {
    allOffers(state){
        return state.offers
    }
}

const actions = {
    async getAllOffers ({commit}){
        await jwtInterceptor.get('/offers/')
        .then((res)=>{
            commit('SET_OFFERS',res.data)
        })
        .catch((err)=>{
            console.log('getOffers', err)
        })
    }
}

const mutations={
    SET_OFFERS(state,payload){
        state.offers = payload
    }
}

export default{
    namespaced:true,
    state,
    getters,
    actions,
    mutations,
}