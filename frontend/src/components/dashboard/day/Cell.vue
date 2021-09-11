<template>
    <div class="hour-cell border-end border-bottom  flex-grow-1" @click="setCurrentShift();showFormShiftModal()" role="button">
        <span class="w-100 h-100  d-block " >
        </span>
    </div>
</template>

<script>
import * as bootstrap from 'bootstrap'
import { mapGetters } from 'vuex'
export default {
    name:'Cell',
    props:{
        employee_id:Number,
    },
    data(){
        return{

        }
    },
    computed:{
        ...mapGetters('global',{
            gettersGetSelecteddate:'getSelectedDate',
            gettersGetFormShiftModal:'getFormShiftModal',
            gettersGetJobShiftChoices:"getJobShiftChoices",
        }),
        ...mapGetters('employees',{
            gettersGetEmployeeByID:"getEmployeeById",
        }),
        getEmployeeByID(){
            const employee = this.$store.state.employees.employees.find(employee => employee.id === this.employee.id)
            return employee
        },
    },
    methods:{
        setCurrentShift(){
            this.$store.dispatch("shifts/setCurrentShift",{})
            this.$store.dispatch('employees/setCurrentEmployee',this.gettersGetEmployeeByID(this.employee_id))
            // this.$store.dispatch('employees/setCurrentEmployee',this.getEmployeeByID)
        },
        showFormShiftModal(){
          if(this.gettersGetFormShiftModal === null){
            const modal = new bootstrap.Modal(document.getElementById('dayformShiftModel'))
            this.$store.dispatch("global/setFormShiftModal",modal)
          }
            this.gettersGetFormShiftModal.toggle()
        },
    }
}
</script>

<style scoped>
.hour-cell{
    width:5%;
}

.hour-cell:hover{
    background-color: cornflowerblue;
    cursor: pointer;
}
</style>