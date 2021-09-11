<template>
    <span :class="colorRange" class="badge   rounded-0 py-2" role="button">
        {{ shift.job.name.substring(0,1).toUpperCase()}}
    </span>
    <small  class=" rounded-0 px-1 py-2" role="button">
        {{shift.starthour.substring(0,5) }} {{ startType }} -
        {{shift.endhour.substring(0,5) }} {{ endType }}
    </small>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name:'RangeTitle',
    props:{
        shift:{
            type:Object,
            required:true,
        }
    },
    computed:{
        ...mapGetters('global',{
            gettersGetJobShiftChoices:"getJobShiftChoices",
        }),
        colorRange(){
            // var c = this.gettersGetJobShiftChoices [this.shift.job-1][1].substring(0,1).toUpperCase()
            try {

            const job = this.shift.job
            console.log(job)
            var c = job.name.substring(0,1).toUpperCase()

            if(c === 'M' || c==='m') {
                return 'bg-danger'
            }
            else if( c === 'F' || c==='f'){
                return 'bg-primary'
            }
            else if( c === 'C' || c==='c'){
                return 'bg-success'
            }
            else{
                return 'bg-secondary'
            }
            } catch (error) {
                 return 'bg-secondary'
            }
        },
        startType(){
            const time= parseInt(this.shift.starthour.substring(0,2))
            // console.log(time)
            return time <  12 ? 'AM':'PM'
        },
        endType(){
            const time= parseInt(this.shift.endhour.substring(0,2))
            return time  <  12 ? 'AM':'PM'
        },
    }
}
</script>

<style>

</style>