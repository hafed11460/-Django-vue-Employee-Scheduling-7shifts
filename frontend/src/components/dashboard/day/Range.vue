<template>
    <div  @click="setCurrentShift();showFormShiftModal()"
        class="hour-range d-flex flex-row my-1" :style="getRangeCell()"
        role="button">
        <span @click="setCurrentShift();showFormShiftModal()" class="badge  bg-success rounded-0 " role="button" style="min-width:30px; padding:12px;">
            {{ shift.job.name.substring(0,1).toUpperCase()}}
        </span>
        <small
                class=" ms-2 rounded-0 py-2" role="button">
                {{shift.starthour.substring(0,5) }} {{ startType }} -
                {{shift.endhour.substring(0,5) }} {{ endType }}
        </small>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import * as bootstrap from 'bootstrap'
export default {
    name:'Range',
    props:{
        employee_id:Number,
        shift:Object,
    },
    data(){
        return{
            unity:4.16,
        }
    },
    computed:{
        ...mapGetters('global',{
            gettersGetHourShiftChoices:"getHourShiftChoices",
            gettersGetSelecteddate:'getSelectedDate',
            gettersGetFormShiftModal:'getFormShiftModal',
            gettersGetJobShiftChoices:"getJobShiftChoices",
        }),
        ...mapGetters('employees',{
            gettersGetEmployeeByID:"getEmployeeById",
        }),
        startType(){
            const time= parseInt(this.shift.starthour.substring(0,2))
            console.log(time)
            return time <  12 ? 'AM':'PM'
        },
        endType(){
            const time= parseInt(this.shift.endhour.substring(0,2))
            return time  <  12 ? 'AM':'PM'
        },
    },
    methods:{
        showFormShiftModal(){
          if(this.gettersGetFormShiftModal === null){
            const modal = new bootstrap.Modal(document.getElementById('dayformShiftModel'))
            this.$store.dispatch("global/setFormShiftModal",modal)
          }
            this.gettersGetFormShiftModal.toggle()
        },
        setCurrentShift(){
            this.$store.dispatch("shifts/setCurrentShift",this.shift)
            this.$store.dispatch('employees/setCurrentEmployee',this.gettersGetEmployeeByID(this.employee_id))
        },
         getRangeCell(){
            // const index = this.shifts.indexOf(shift)
            let width = this.DifferenceITime(this.shift.starthour,this.shift.endhour)

            // let width = (this.shift.endhour - this.shift.starthour);
            var style = 'width:'+ (width*this.unity) +'%;' ;
            const left = this.getLeft(this.shift.starthour,0)
            style += 'left:'+ (left * this.unity ) +'%;' ;
            // style += 'top:'+ (index * 50 ) +'px;' ;
            console.log(style)
            return style;
        },
        //  calcule left style
        getLeft(starthour , point0){
            console.log(point0)
            var  start  = starthour.split(':')
            var left = parseInt(start[0])
            // if(left < 7){ // 7 => 07:00
            //     left += 17
            // }else{
            //     left -= point0
            // }

            // console.log('start :' , start)
            // console.log('left :' , left)
            // console.log('left :' , left)


            var plus = parseInt(start[1]) // use this for time like 08:30 calcule minut
            plus = (plus * 100) / 60
            plus = Math.round(plus) // error 7.66.33
            // console.log('left :',left+'.'+plus)
            if(left < 0) return 0;
            // console.log('left :',left +'.'+ plus)
            return left +'.'+ plus;
        },
        // get deferent between start hour and en hour
        DifferenceITime(starthour, endhour){
            var end  = endhour.split(':');
            var start  = starthour.split(':');
            // console.log('end :' , end)
            // console.log('start :' , start)

            var hour = Math.abs(parseInt(end[0]) - parseInt(start[0]))
            var minut = Math.abs(parseInt(end[1]) - parseInt(start[1]))

            // console.log('hour :',hour)
            if(parseInt(end[0]) < 7 &&  parseInt(start[0]) > 7){
                hour -= 17 - (7-parseInt(end[0]))
            }
            // console.log('hour :',hour)

            // console.log('minut :',minut)

            minut = (minut * 100) / 60
            // console.log('minut :',minut)
            minut = Math.round(minut)
            // console.log('minut :',minut)
            // console.log('width :',hour+'.'+minut)
            const width = hour+'.'+minut
            return width
        },
    }
}
</script>

<style scoped>
.hour-range:hover .menu-option{
    visibility: visible !important;
}

.hour-range{
    left:5.5%;
    box-sizing: border-box;
    width: 100%;
    height: 40px;
    border: 1px solid #999;
    background-color: rgb(255, 255, 255);
    position: absolute;
    transform: 5.5%;
    transition: left 0.5s;
}
</style>