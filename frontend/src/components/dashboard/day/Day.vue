<template>
    <div class="border-top pt-3 mt-3">
        <div class=" d-flex flex-row p-1  justify-content-between">
            <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                <span @click="prevDay" type="button" class="btn btn-outline-secondary">prev</span>
                 <input @change="dateChanged" type="date" id="birthday" v-model="dateSelected"  class=" btn  btn-outline-secondary">
                <span @click="nextDay" type="button" class="btn btn-outline-secondary">next</span>
            </div>
        </div>
        <div class="border m-2">
            <div class="d-flex flex-column" >
                <div class="d-flex flex-row">
                    <div class="col-employee border-bottom border-end">
                        <NewEmployee />
                    </div>
                    <!-- <div class="hour-cell border-end border-bottom p-2 flex-grow-1" v-for="(hour,index) in gettersGetHourShiftChoices" :key="index">
                        {{hour[1]}}
                    </div> -->
                    <div class="hour-cell border-end border-bottom py-2 px-1  flex-grow-1"
                     v-for="(hour,index) in gettersGetHourHeader" :key="index">
                        {{ hour }}
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
                    <div class="row-hour-cell d-flex flex-row flex-grow-1" >
                        <DayRowCell :employee="employee" />
                    </div>
                </div>
            </div>
            <DayCreateShift/>
        </div>
    </div>
</template>

<script>
import NewEmployee from '../NewEmployee.vue'
import DayCreateShift from './DayCreateShift.vue'
import DayRowCell from './DayRowCell.vue'
import {mapGetters,mapActions} from 'vuex'
export default {
    components:{
        NewEmployee,
        DayCreateShift,
        DayRowCell,
        // RowCell,
        },
    data(){
        return{
            dateSelected:new Date().toISOString().substr(0, 10),
            date: new Date(),
            // width:11.11,
        }
    },
    computed:{
        ...mapGetters('employees',{
          gettersAllEmployees:"allEmployees"
        }),
        ...mapGetters('global',{
          gettersGetHourShiftChoices:"getHourShiftChoices",
          gettersGetHourHeader:"getHourHeader",
        }),
    },
    watch:{
        dateSelected(){
            this.dateChanged()
        }
    },
    methods:{
            ...mapActions('employees',{
            actionGetAllEmployees:'getAllEmployees',
        }),
            ...mapActions('global',{
                actionGetHourShiftChoices:'getHourShiftChoices',
                actionSetSlectedDate:'setSelectedDate',
        }),
        nextDay(){
            var date = new Date(this.dateSelected);
            date.setDate(date.getDate() + 1);
            this.dateSelected = date.toISOString().substr(0, 10)
        },
        prevDay(){
            var date = new Date(this.dateSelected);
            date.setDate(date.getDate() - 1);
            this.dateSelected = date.toISOString().substr(0, 10)
        },
        async dateChanged(){
            await this.actionSetSlectedDate(this.dateSelected)
            await this.actionGetAllEmployees(this.dateSelected)
        },
        async getEmployee(){
            const date = new Date().toISOString().substr(0, 10)
            await this.actionGetAllEmployees(date)
        },

        deleteDate(){
            this.dateList.remove()
        },

    },
    created(){
        this.actionGetHourShiftChoices()
        this.actionSetSlectedDate(this.dateSelected)
        this.getEmployee()

    }

}
</script>

<style scoped>
.row-hour-cell{
    position: relative;
    box-sizing: content-box;
    /* height: 100px; */
}
.row-hour-cell:hover{
    background-color: lemonchiffon;
}

.hour-range:hover{
    left:5.55%;
}
.col-employee{
    /* padding: 20px 0px; */
    max-width: 250px;
    min-width: 250px;
    min-height: 50px;
}

.hour-cell{
    width:5.55%;
}

</style>