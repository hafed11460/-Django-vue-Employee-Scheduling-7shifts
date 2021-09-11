<template>
    <div :class="{'today':todayDate === day}" class="day-cell border-end border-bottom  flex-fill" >
        <div
            class="new-shift my-1 border-bottom" role="button">
            <div class="d-block text-center " role="button">

            </div>
        </div>
        <template v-if="shifts">
            <div v-for="shift in todayShifts" :key="shift.id"
                class="day-range d-flex flex-row my-1 " role="button">
                <RangeTitle v-if="shift.date == day" :shift="shift"/>
            </div>
        </template>
    </div>
</template>

<script>
import RangeTitle from './RangeTitle.vue'
export default {
    name:'WeekCell',
    props:{
        day:String,
        shifts:Object,
    },
    components:{
        RangeTitle,
    },
    data(){
        return{

        }
    },
    computed:{
        todayShifts(){
           return this.shifts.filter((shift) => shift.date === this.day)
        },
        todayDate(){
            const date = new Date();
            var day = date.toISOString().substr(0, 10)
            return day
        },
    },



}
</script>

<style scoped>
.today{
    background-color: rgb(244, 255, 183);
}
.day-cell{
    width:14.28%;
    min-height: 100px;
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