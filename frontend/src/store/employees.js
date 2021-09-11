// import axios from 'axios'
const baseURL = 'http://localhost:8000'
import jwtInterceptor from '../shared/jwtInterceptor'
const state = ()=>({
    employees:[],
    currentEmployee:{},
    successCrateEmployee:false,
    employees_list:[],
})

const getters  = {
    /// this for component EmployeeList
    getEmployeesList(state){
        return state.employees_list
    },
    getSuccessCreateEmployee(state){
        return state.successCrateEmployee
    },
    getCurrentEmployee(state){
        return state.currentEmployee
    },

    allEmployees(state){
        return state.employees
    },

    // getEmployeeById(state,id){
    //     const employee  = state.employees.find(employee => employee.id === id)
    //     return employee
    // },
    getEmployeeById: (state) => (id) => {
        return state.employees.find(employee => employee.id === id)
    },
    getEmployeeShiftByDate: (state) => (id) => {
        return state.employees.find(employee => employee.id === id)
    }

}

const actions = {
    setSuccessCreateEmployee({commit},success){
        commit('SET_SUCCESS_CREATE_EMPLOYEE',success)
    },
    setCurrentEmployee({commit},currentEmployee){
        commit('SET_CURRENT_EMPLOYEE',currentEmployee)
    },

    getShifts(state){
        state.employees.indexOf(1).shifts
    },

    async setEmployeesList ({commit}){
        await jwtInterceptor.get('/employees/all/')
        .then((res)=>{
            commit('SET_EMPLOYEES_LIST',res.data)
        })
        .catch((err)=>{
            console.log('employees', err)
        })
    },
    async updateEmployee({commit},obj){
        await jwtInterceptor.get('/employees/'+obj.employee_id+'/?date='+obj.date)
        .then((res)=>{
            commit('UPDATE_EMPLOYEE',res.data)
        })
        .catch((err)=>{
            console.log('employees', err)
        })
    },

    async getAllEmployees ({commit},query_params){
        await jwtInterceptor.get('/employees/?date='+query_params)
        .then((res)=>{
            commit('SET_EMPLOYEES',res.data)
        })
        .catch((err)=>{
            console.log('employees', err)
        })
    },

    async weekUpdateEmployee({commit},obj){
        // const date = rootGetters.getWeekSelectedDay
        // const date = this.$store.getters['global/getWeekSelectedDay']
        await jwtInterceptor.get('/employees/'+obj.employee_id+'/week/?date='+ obj.date)
        .then((res)=>{
            commit('UPDATE_EMPLOYEE',res.data)
        })
        .catch((err)=>{
            console.log('employees', err)
        })
    },

    async getWeekAllEmployees ({commit},query_params){
        await jwtInterceptor.get('/employees/week/?date='+query_params)
        .then((res)=>{
            commit('SET_EMPLOYEES',res.data)
        })
        .catch((err)=>{
            console.log('employees', err)
        })
    },

    async createEmployee({commit,state}, employee){
        await jwtInterceptor.post('/employees/create/',employee)
        .then((res)=>{
            const newEmployee={
                id:res.data.id,
                location:res.data.location,
                first_name:res.data.first_name,
                last_name:res.data.last_name,
                email:res.data.email,
                profile_image:baseURL + res.data.profile_image,
                shifts:[]
            }
            state.successCrateEmployee = true
            commit('SET_NEW_EMPLOYEE',newEmployee)
        })
        .catch((err)=>{
            commit('global/SET_ERRORS',err.response.data,{ root: true })
            console.log('createEmployee error', err.response.data)
        })
    },



}

const mutations={
    SET_EMPLOYEES_LIST(state,employees_list){
        state.employees_list = employees_list
    },
    SET_SUCCESS_CREATE_EMPLOYEE(state,success){
        state.successCrateEmployee = success
    },
    SET_CURRENT_EMPLOYEE(state,currentEmployee){
        state.currentEmployee = currentEmployee
    },
    UPDATE_EMPLOYEE(state,up_employee){
        for (let index = 0; index < state.employees.length; index++) {
            const element = state.employees[index];
            if(element.id === up_employee.id){
                state.employees[index] = up_employee
            }
        }
    },


    SET_NEW_EMPLOYEE(state, newEmployee){
        state.employees.push(newEmployee)
    },
    SET_EMPLOYEES(state,payload){
        state.employees = payload
    },

    DESTROY_STORE(state){
        state.employees = []
        state.currentEmployee = {}
        state.successCrateEmployee = false
    }
}

export default{
    namespaced:true,
    state,
    getters,
    actions,
    mutations,
}