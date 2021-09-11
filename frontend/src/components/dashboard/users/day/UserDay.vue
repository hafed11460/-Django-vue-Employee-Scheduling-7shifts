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
                    <div class="hour-cell border-end border-bottom py-2 px-1  flex-grow-1"
                     v-for="(hour,index) in gettersGetHourHeader" :key="index">
                        {{ hour }}
                    </div>
                </div>
            </div>
            <div class="d-flex flex-column">
                <div class="d-flex flex-row">
                    <div class="row-hour-cell d-flex flex-row flex-grow-1">

                        <DayRowCell :employee="employee" :shifts="employee.shifts" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapGetters,mapActions} from 'vuex'
import jwtInterceptor from '../../../../shared/jwtInterceptor'
import DayRowCell from './DayRowCell.vue'
export default {
    components:{
        DayRowCell,
        },
    data(){
        return{
            employee:{},
            dateSelected:new Date().toISOString().substr(0, 10),
            date: new Date(),

        }
    },
    computed:{
         ...mapGetters('auth',{
            isAuthenticated:'loggedIn',
            currentUser:'currentUser'
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
        async getEmployeeDayShift(){
            await jwtInterceptor.get('/employees/'+this.currentUser.id+'/simple-user/day/?date='+this.dateSelected)
            .then((res)=>{

                this.employee = res.data
            })
            .catch((err)=>{
                this.err = err.response.data
            })
        },
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
            this.getEmployeeDayShift()
        },


    },
    created(){
        this.actionGetHourShiftChoices()
        this.actionSetSlectedDate(this.dateSelected)
        this.getEmployeeDayShift()

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