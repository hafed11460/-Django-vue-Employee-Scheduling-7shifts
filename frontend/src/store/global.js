// import axios from 'axios'
// const baseURL = 'http://localhost:8000'
import jwtInterceptor from '../shared/jwtInterceptor'
import excelJwtInterceptor from '../shared/excelJwtInterceptor'
const state = ()=>({
    HOUR_HEADER : [
        '00:00',
        '01:00 am',
        '02:00 am',
        '03:00 am',
        '04:00 am',
        '05:00 am',
        '06:00 am',
        '07:00 am',
        '08:00 am',
        '09:00 am',
        '10:00 am',
        '11:00 am',
        '12:00',
        '13:00 pm',
        '14:00 pm',
        '15:00 pm',
        '16:00 pm',
        '17:00 pm',
        '18:00 pm',
        '19:00 pm',
        '20:00 pm',
        '21:00 pm',
        '22:00 pm',
        '23:00 pm',
    ],

    HOUR_SHIFTS_CHOICES :{},
    JOB_SHIFTS_CHOICES :{},
    dateSelected:'',
    weekDaysHeader:'',
    weekDaysDate:'',
    formShiftModal:null,
    weekSelectedDay:'',
    errors:{}

})

const getters  = {
    getHourHeader(state){
        return state.HOUR_HEADER
    },
    getErrors(state){
        return state.errors
    },
    getWeekSelectedDay(state){
        return state.weekSelectedDay
    },
    getWeekDaysDate(state){
        return state.weekDaysDate
    },
    getWeekDaysHeader(state){
        return state.weekDaysHeader
    },
    getSelectedDate(state){
        return state.dateSelected;
    },
    getHourShiftChoices(state){
        return state.HOUR_SHIFTS_CHOICES
    },
    getJobShiftChoices(state){
        return state.JOB_SHIFTS_CHOICES
    },
    getFormShiftModal(state){
        return state.formShiftModal
    },

}

const actions = {
    setErrors({commit},errors){
        commit('SET_ERRORS',errors)
    },
    setWeekSelectedDay({commit},date){
        commit('SET_WEEK_SELECTED_DAY',date)
    },
    // set header days for current week
    setWeekDaysHeader({commit,state}){
        var weekDaysHeader= new Array();
        for (var i = 0; i < 7; i++) {
            var date = new Date(state.dateSelected);
            date.setDate(date.getDate() + i);
            var day = date.toDateString()
            weekDaysHeader.push(
                day
            );
        }
        commit('SET_WEEK_DAYS_HEADER',weekDaysHeader)
    },
    // set cell days
    setWeekDaysDate({commit,state}){
        var weekDaysDate= new Array();
        for (var i = 0; i < 7; i++) {
            var date = new Date(state.dateSelected);
            date.setDate(date.getDate() + i);
            var day = date.toISOString().substr(0, 10)
            weekDaysDate.push(
                day
            );
        }
        commit('SET_WEEK_DAYS_DATE',weekDaysDate)
    },
    setSelectedDate({commit},newDate){
        commit('SET_SELECTED_DATE',newDate)
    },
    // download excel file for current week
    async employeesExcelDownload({state}){
        await excelJwtInterceptor.get('/employees/excel/?date='+state.dateSelected)
        .then ((res) => {
            const url = window.URL.createObjectURL(new Blob([res.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'week-'+state.dateSelected+'.xlsx');
            document.body.appendChild(link);
            link.click();
        })
    },
    // download excel file for current week
    async employeesCSVDownload({state}){
        await excelJwtInterceptor.get('/employees/csv/?date='+state.dateSelected)
        .then ((res) => {
            const url = window.URL.createObjectURL(new Blob([res.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'week-'+state.dateSelected+'.csv');
            document.body.appendChild(link);
            link.click();
        })
    },
    // Create Shift
    async getHourShiftChoices({commit}){
        // await jwtInterceptor.get('/shifts/choices/')
        await jwtInterceptor.get('/employees/roles/')
        .then((res)=>{
            // commit('SET_HOUR_SHIFTS_CHOICES' ,res.data.HOUR_TYPE_CHOICES)
            commit('SET_JOB_SHIFTS_CHOICES' ,res.data)
        })
        .catch((err)=>{
            console.log('shifts', err)
        })
    },
    setFormShiftModal({commit},formShiftModal){
        commit('SET_FORM_SHIFT_MODAL',formShiftModal)
    },
}

const mutations={
    SET_ERRORS(state,errors){
        state.errors = errors
    },
    SET_WEEK_SELECTED_DAY(state,date){
        state.weekSelectedDay = date
    },
    SET_WEEK_DAYS_DATE(state, weekDaysDate){
        state.weekDaysDate = weekDaysDate
    },
    SET_WEEK_DAYS_HEADER(state, weekDaysHeader){
        state.weekDaysHeader = weekDaysHeader
    },
    SET_SELECTED_DATE(state,newDate){
        state.dateSelected = newDate
    },
    SET_HOUR_SHIFTS_CHOICES(state,hourShiftChoices){
        state.HOUR_SHIFTS_CHOICES = hourShiftChoices
    },
    SET_JOB_SHIFTS_CHOICES(state,jobShiftChoices){
        state.JOB_SHIFTS_CHOICES = jobShiftChoices
    },
    SET_FORM_SHIFT_MODAL(state,formShiftModal){
        state.formShiftModal = formShiftModal
    },

    DESTROY_STORE(state){
        state.HOUR_SHIFTS_CHOICES  ={}
        state.JOB_SHIFTS_CHOICES  ={}
        state.dateSelected =''
        state.weekDaysHeader =''
        state.weekDaysDate =''
        state.formShiftModal =null
        state.weekSelectedDay =''
        state.errors ={}
    }
}

export default{
    namespaced:true,
    state,
    getters,
    actions,
    mutations,
}