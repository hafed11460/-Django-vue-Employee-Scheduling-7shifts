<template>
    <div class="border-top pt-2 mt-3">
        <div class=" d-flex flex-row p-1 justify-content-between px-3">

            <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                <span @click="prevWeek" type="button" class="btn btn-outline-secondary">prev</span>
                 <input @change="dateChanged" type="date" id="birthday" readonly v-model="dateSelected"  class=" btn  btn-outline-secondary">
                <span @click="nextWeek" type="button" class="btn btn-outline-secondary">next</span>

            </div>
            <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                <span @click="restartToCurrentWeek()" type="button" class="btn btn-light border">This Week </span>
                <span @click="copyWeek()" type="button" class="btn btn-light border ">
                    <i class="far fa-copy text-success"></i> Copy Week </span>
                <span @click="cleareWeek()" type="button" class="btn btn-light border">
                    <i class="fas fa-trash-alt text-danger"></i> Clear week </span>

                <SendMail/>

            </div>

            <div class="">
                <div class="btn-group " role="group" aria-label="Basic mixed styles example">
                    <!-- <span @click="excelDownload()" type="button" class="btn btn-light border">
                        <i class="fas fa-file-excel text-success"></i>
                         Excel</span> -->
                    <span @click="CSVDownload()" type="button" class="btn btn-light border">
                        <i class="fas fa-file-csv text-secondary"></i> CSV
                    </span>
                </div>
            </div>

        </div>
        <div class="border m-2">
            <div class="d-flex flex-column" >
                <div class="d-flex flex-row">
                    <div class="col-employee border-bottom border-end">
                        <NewEmployee @pushNewEmployee="pushNewEmployee"/>
                    </div>
                    <div class="border-end border-bottom p-3 flex-grow-1 " style="width:14.28%;"
                        v-for="(day,index) in gettersGetWeekDaysHeader" :key="index">
                        {{ day }}
                    </div>
                </div>
            </div>

            <div class="d-flex flex-column" v-for="employee in gettersAllEmployees" :key="employee.id" >
                <div class="d-flex flex-row">
                    <div class="col-employee p-1 border-bottom border-end">
                        <router-link lass="p-0 m-0" :to="{ name: 'EmployeeProfile',params: { id: employee.id } }">
                            <div class="d-flex flex-row ps-1">
                                <img :src="employee.profile_image" alt="" width="40" height="40" class="rounded-circle">
                                <p class="ms-2 mt-2"> {{employee.first_name}} {{employee.last_name}}  </p>
                            </div>
                        </router-link>
                    </div>
                    <div class="d-flex flex-row w-100 row-day-cell" >
                        <WeekRowCell v-for="(day,index) in gettersGetWeekDaysDate"
                            :key="index" :employee_id="employee.id" :day="day"/>
                    </div>
                </div>
            </div>
            <WeekCreateShift/>

        </div>
        <router-view class="view"></router-view>
    </div>
</template>

<script>
import NewEmployee from '../NewEmployee.vue'
import WeekCreateShift from './WeekCreateShift.vue'
import WeekRowCell from './WeekRowCell.vue'
import SendMail from '../SendMail.vue'
import {mapGetters,mapActions} from 'vuex'
import jwtInterceptor from '../../../shared/jwtInterceptor'
export default {
    components:{
        SendMail,
        NewEmployee,
        WeekCreateShift,
        WeekRowCell,
        },
    data(){
        return{
            dateSelected:'',
            date: new Date(),
            width:11.11,
        }
    },
    computed:{
        ...mapGetters('employees',{
            gettersAllEmployees:"allEmployees",
        }),
        ...mapGetters('global',{
            gettersGetWeekDaysHeader:"getWeekDaysHeader",
            gettersGetSelecteddate:'getSelectedDate',
            gettersGetWeekDaysDate:'getWeekDaysDate',
        }),


    },
    watch:{
        dateSelected(){
            this.dateChanged()
        },
        gettersGetSelecteddate(){
            this.dateSelected = this.gettersGetSelecteddate
        }
    },
    methods:{
        ...mapActions('employees',{
            actionGetWeekAllEmployees:'getWeekAllEmployees',
        }),

        ...mapActions('global',{
            actionSetWeekDaysHeader:'setWeekDaysHeader',
            actionSetWeekDaysDate:'setWeekDaysDate',
            actionGetHourShiftChoices:'getHourShiftChoices',
            actionSetSlectedDate:'setSelectedDate',
            actionEmployeesExcelDownlod:'employeesExcelDownload',
            actionEmployeesCSVDownlod:'employeesCSVDownload',
        }),
        async excelDownload(){
            await this.actionEmployeesExcelDownlod()
        },
        async CSVDownload(){
            await this.actionEmployeesCSVDownlod()
            this.showToast('Start download CSV File','success')
        },
        restartToCurrentWeek(){
            this.dateSelected = this.weekStartDay()
        },
         weekStartDay(){
            const date =  this.getMonday(Date());
            return date.toISOString().substr(0, 10)
        },
        getMonday(d){
            var t = new Date(d);
            // console.log('new date ',t)
            // console.log('new date : ',t.getDate() ,'- ',t.getDay())
            t.setDate(t.getDate() - t.getDay());
            // t.setDate(t.getDate() - t.getDay(-1));
            // console.log('result date',t)
            return t;
        },

        setCurrentEmployee(employee){
            this.$store.dispatch('employees/setCurrentEmployee',employee)
        },
        nextWeek(){
            var date = new Date(this.gettersGetSelecteddate);
            date.setDate(date.getDate() + 7);
            this.$store.dispatch('global/setSelectedDate',date.toISOString().substr(0, 10))
            this.dateSelected = date.toISOString().substr(0, 10)
        },
        prevWeek(){
            var date = new Date(this.gettersGetSelecteddate);
            date.setDate(date.getDate() - 7);
            this.$store.dispatch('global/setSelectedDate',date.toISOString().substr(0, 10))
            this.dateSelected = date.toISOString().substr(0, 10)
        },

        async dateChanged(){
            await this.actionSetSlectedDate(this.dateSelected)
            this.actionSetWeekDaysHeader()
            this.actionSetWeekDaysDate()
            await this.actionGetWeekAllEmployees(this.dateSelected)
        },
        async getEmployee(){
            // const date = new Date().toISOString().substr(0, 10)
            await this.actionGetWeekAllEmployees(this.gettersGetSelecteddate)
        },

        pushNewEmployee(employee){
             this.lists.push(employee)
        },

        showToast(message,type='success'){
            this.$toast(message, {
                duration: 5000,
                type:type,
                // Position not yet supported
                styles: {
                    borderRadius: '25px',
                },
                slot: '<i class="fa fa-thumbs-up"></i>',
            });
        },
        async copyWeek(){
            var r = confirm("Are you sure to copy  this week << "+ this.gettersGetSelecteddate +" >> . \n Press button yes to cleare  it .");
            if (r == true) {
             await jwtInterceptor.get('/employees/copy-week/?date='+this.gettersGetSelecteddate)
                    .then(()=>{
                        this.showToast('the current week has been copied successfully ','success')
                    })
                    .catch((err)=>{
                        // this.err = err.response.data
                        alert(err.response.data.message)
                    })
            }
        },

        async cleareWeek(){
            var r = confirm("Are you sure to Cleare this week << "+ this.gettersGetSelecteddate +" >> . \n Press button yes to cleare  it .");
            if (r == true) {
                await jwtInterceptor.get('/employees/cleare-week/?date='+this.gettersGetSelecteddate)
                    .then(()=>{
                        this.showToast('the current week has been cleared successfully ','success')
                        this.dateChanged()
                    })
                    .catch((err)=>{
                        // this.err = err.response.data
                        alert(err.response.data.message)
                    })
            }
        },

    },
    created(){
        this.actionSetSlectedDate(this.weekStartDay())
        this.actionSetWeekDaysHeader()
        this.actionSetWeekDaysDate()
        this.actionGetHourShiftChoices()
        this.getEmployee()
        this.dateSelected = this.gettersGetSelecteddate

    }

}
</script>

<style scoped>
.row-day-cell{
    position: relative;
}
.row-day-cell:hover{
    background-color: lemonchiffon;
}


.col-employee{
    /* padding: 20px 0px; */
    max-width: 250px;
    min-width: 250px;
    min-height: 50px;
}



</style>