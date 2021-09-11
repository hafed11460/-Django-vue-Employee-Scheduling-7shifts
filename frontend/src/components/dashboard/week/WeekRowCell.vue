<template>
    <div :class="{'today':todayDate === day}" class="day-cell border-end border-bottom  flex-fill" >

        <div @click="setCurrentShift({},day);showFormShiftModal();"
            class="new-shift my-1 border-bottom" role="button">
            <div class="d-block text-center " role="button">
                    <i class="fas fa-plus"></i>
            </div>
        </div>

        <div v-for="shift in getEmployeeShiftByDate" :key="shift.id"
            @click="setCurrentShift(shift,day);showFormShiftModal();"
            class="day-range d-flex flex-row my-1 " role="button">
            <RangeTitle :shift="shift"/>
        </div>
    </div>
</template>

<script>
import * as bootstrap from 'bootstrap'
import { mapGetters } from 'vuex'
import RangeTitle from './RangeTitle.vue'
export default {
    name:'WeekCell',
    props:{
        day:String,
        employee_id:Number,
    },
    components:{
        RangeTitle,
    },
    data(){
        return{
            shifts:'',
        }
    },
    computed:{
        ...mapGetters('global',{
            gettersGetFormShiftModal:'getFormShiftModal',
        }),
        ...mapGetters('employees',{
            gettersGetEmployeeByID:"getEmployeeById",
        }),

        todayDate(){
            const date = new Date();
            var day = date.toISOString().substr(0, 10)
            return day
        },
        getEmployeeShiftByDate(){
            var employee = this.gettersGetEmployeeByID(this.employee_id)
            return  employee.shifts.filter((shift) => shift.date === this.day)
        },
    },
    methods:{
        setCurrentShift(shift,date){
            try {
                const employee = this.gettersGetEmployeeByID(this.employee_id)
                // this.currentShift =  employee.shifts.some(shift => shift.date === date) ? employee.shifts.find(shift => shift.date === date):{}
                this.$store.dispatch("shifts/setCurrentShift",shift)
                this.$store.dispatch("global/setWeekSelectedDay",date)
                this.$store.dispatch('employees/setCurrentEmployee',employee)
            } catch (error) {
                console.log(error)
            }
        },
         showFormShiftModal(){
          if(this.gettersGetFormShiftModal === null){
            const modal = new bootstrap.Modal(document.getElementById('formShiftModel'))
            this.$store.dispatch("global/setFormShiftModal",modal)
          }
            this.gettersGetFormShiftModal.toggle()
        },
    },
    mounted(){
        this.shifts = this.getEmployeeShiftByDate
    }

}
</script>

<style scoped>
.today{
    background-color: rgb(244, 255, 183);
}
.day-cell{
    width:14.28%;
}
.day-cell:hover{
    /* background-color: cornflowerblue; */
    cursor: pointer;
}
.new-shift{
    visibility: hidden;
}
.day-cell:hover .new-shift{
    visibility: visible !important;
}

.day-range{
    box-sizing: border-box;
    width: 100%;
    border: 1px solid rgb(238, 236, 236);
    /* position: absolute; */
    transition: left 0.5s;
}
.day-range:hover{
    background-color: rgb(171, 202, 248);

}
</style>