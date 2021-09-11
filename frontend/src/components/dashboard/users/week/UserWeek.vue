<template>
    <div class="border-top pt-2 mt-3">
        <div class=" d-flex flex-row p-1 justify-content-between px-3">

            <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                <span @click="prevWeek" type="button" class="btn btn-outline-secondary">prev</span>
                 <input @change="dateChanged" type="date" id="birthday" readonly v-model="dateSelected"  class=" btn  btn-outline-secondary">
                <span @click="nextWeek" type="button" class="btn btn-outline-secondary">next</span>

            </div>

            <div class="">
                <div class="btn-group " role="group" aria-label="Basic mixed styles example">
                    <!-- <span @click="excelDownload()" type="button" class="btn btn-light border">
                        <i class="fas fa-file-excel text-success"></i>
                         Excel</span> -->
                    <!-- <span @click="CSVDownload()" type="button" class="btn btn-light border">
                        <i class="fas fa-file-csv text-secondary"></i> CSV
                    </span> -->
                </div>
            </div>

        </div>
        <div class="border m-2">
            <div class="d-flex flex-column" >
                <div class="d-flex flex-row">
                    <div class="border-end border-bottom p-3 flex-grow-1 " style="width:14.28%;"
                        v-for="(day,index) in gettersGetWeekDaysHeader" :key="index">
                        {{ day }}
                    </div>
                </div>
            </div>

            <div class="d-flex flex-column" >
                <div class="d-flex flex-row">
                    <div class="d-flex flex-row w-100 row-day-cell" >
                        <WeekRowCell v-for="(day,index) in gettersGetWeekDaysDate"
                            :key="index" :shifts="employee.shifts" :day="day"/>

                    </div>
                </div>
            </div>

        </div>
        <router-view class="view"></router-view>
    </div>
</template>

<script>
import WeekRowCell from './WeekRowCell.vue'
import {mapGetters,mapActions} from 'vuex'
import jwtInterceptor from '../../../../shared/jwtInterceptor'
export default {
    components:{
        WeekRowCell,
        },
    data(){
        return{
            employee:'',
            dateSelected:'',
            date: new Date(),
            width:11.11,
        }
    },
    computed:{
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
            t.setDate(t.getDate() - t.getDay());
            return t;
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
            await this.getEmployeeWeek()
        },
        async getEmployeeWeek(){
            await jwtInterceptor.get('/employees/simple-user/week/?date='+this.dateSelected)
            .then((res)=>{
               this.employee = res.data.user
            })
            .catch((err)=>{
                console.log('employees', err)
            })
        },
    },
    created(){
        this.actionSetSlectedDate(this.weekStartDay())
        this.actionSetWeekDaysHeader()
        this.actionSetWeekDaysDate()
        this.actionGetHourShiftChoices()
        this.getEmployeeWeek()
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