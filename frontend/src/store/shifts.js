// import axios from 'axios'
// const baseURL = 'http://localhost:8000'
import jwtInterceptor from '../shared/jwtInterceptor'
const state = ()=>({
    currentShift:{},
    currentWeekStartDate:'',
    weekSelectedDay:'',


})

const getters  = {

    getCurrentWeekStartDate(state){
        return state.currentWeekStartDate
    },

    getCurrentShift(state){
        return state.currentShift
    },

}

const actions = {

    setCurrentWeekStartDate({commit},currentWeekStartdate){
        commit('SET_CURRENT_WEEK_START_DATE',currentWeekStartdate)
    },

    setCurrentShift({commit},currentShift){
        commit('SET_CURRENT_SHIFT',currentShift)
    },


    async createShift({commit},shift){
        await jwtInterceptor.post('/shifts/create/',shift)
        .then((res)=>{
            commit('SET_SHIFTS' ,res.data)
        })
        .catch((err)=>{
            console.log('shifts', err)
        })
    },
    async updateShift({commit},shift){
        if(shift){
            await jwtInterceptor.put('/shifts/'+shift.shift_id+'/update/',shift.shift)
            .then((res)=>{
                commit('SET_SHIFTS' ,res.data)
            })
            .catch((err)=>{
                console.log('shifts', err)
            })
        }
    },
    // Delete shift
    async deleteShift({commit},shift){
        if(shift){
            await jwtInterceptor.delete('/shifts/'+shift.id+'/delete/')
            .then((res)=>{
                commit('SET_SHIFTS' ,res.data)
            })
            .catch((err)=>{
                console.log('shifts', err)
            })
        }
    }

}

const mutations={

    SET_CURRENT_WEEK_START_DATE(state,currentWeekStartdate){
        state.currentWeekStartDate = currentWeekStartdate
    },
    SET_CURRENT_SHIFT(state,currentShift){
        state.currentShift = currentShift
    },
    SET_SHIFTS(){

    },
    DESTROY_STORE(state){
        state.currentShift = {}
        state.currentWeekStartDate = ''
        state.weekSelectedDay = ''
    }
}

export default{
    namespaced:true,
    state,
    getters,
    actions,
    mutations,
}