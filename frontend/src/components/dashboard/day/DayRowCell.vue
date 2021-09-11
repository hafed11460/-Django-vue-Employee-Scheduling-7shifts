<template @click="setCurrentEmployee()">

    <!-- <Cell :employee_id="employee.id" v-for="(hour,index) in gettersGetHourShiftChoices" :key="index"/> -->
    <Cell :employee_id="employee.id" v-for="(hour,index) in 24 " :key="index"/>

    <template v-if="(shifts = isExistShifts())">
        <Range :employee_id="employee.id" :shift="shift" v-for="shift in shifts" :key="shift.id"/>
    </template>
</template>

<script>
import { mapGetters } from 'vuex';
// import * as bootstrap from 'bootstrap'
import useVuelidate from "@vuelidate/core";
import Range from './Range.vue'
import Cell from './Cell.vue'

export default {
    setup: () => ({ v$: useVuelidate() }),
    name:'RangeWork',
    props:{
        employee:Object,
    },
    components:{
        Cell,
        Range,
    },
    data(){
        return{
            shifts:{},
        }
    },
    computed:{
        ...mapGetters('global',{
        gettersGetHourShiftChoices:"getHourShiftChoices",
        gettersGetSelecteddate:'getSelectedDate',
        gettersGetFormShiftModal:'getFormShiftModal',
        gettersGetJobShiftChoices:"getJobShiftChoices",
         gettersGetHourHeader:"getHourHeader",
    }),

    getEmployeeByID(){
        const employee = this.$store.state.employees.employees.find(employee => employee.id === this.employee.id)
        return employee
    },


    },

    methods:{
        setCurrentEmployee(){
             this.$store.dispatch('employees/setCurrentEmployee',this.getEmployeeByID)
        },
        // showFormShiftModal(){
        //   if(this.gettersGetFormShiftModal === null){
        //     const modal = new bootstrap.Modal(document.getElementById('dayformShiftModel'))
        //     this.$store.dispatch("global/setFormShiftModal",modal)
        //   }
        //     this.gettersGetFormShiftModal.toggle()
        // },
        isExistShifts(){
            const employee = this.getEmployeeByID
            if('shifts' in employee){
                if (employee.shifts.length > 0){
                        this.shift = employee.shifts
                        return employee.shifts
                }
            }
        },
    },


}
</script>

<style>


</style>