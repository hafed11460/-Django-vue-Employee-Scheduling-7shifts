<template >

    <!-- <Cell :employee_id="employee.id" v-for="(hour,index) in gettersGetHourShiftChoices" :key="index"/> -->
    <Cell :employee_id="employee.id" v-for="(hour,index) in 24 " :key="index"/>


    <Range :employee_id="employee.id" :shift="shift" v-for="shift in shifts" :key="shift.id"/>

</template>

<script>
import Range from './Range.vue'
import Cell from './Cell.vue'

export default {
    name:'DayRowCell',
    props:{
        employee:Object,
        shifts:Object,
    },
    components:{
        Cell,
        Range,
    },
}
</script>

<style>


</style>