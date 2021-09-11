<template>
    <div v-if="currentUser">
        <div class=" d-flex flex-row p-2 mt-3 justify-content-between  ">
            <div class="">
                <div class="btn-group " role="group" aria-label="Basic mixed styles example ">
                    <h5 v-if="currentUser.location" class="text-uppercase">
                        {{ currentUser.location['restaurant'].name }} -
                        {{ currentUser.location['name'] }}
                    </h5>
                </div>
            </div>
            <div class="">
                <div class="btn-group " role="group" aria-label="Basic mixed styles example">
                    <span @click="currentTab='Day'" type="button" :class="currentTabComponent=='Day'?'btn-primary':'btn-light'" class="btn ">Day</span>
                    <span @click="currentTab='Week'" type="button" :class="currentTabComponent=='Week'?'btn-primary':'btn-light'" class="btn ">Week</span>
                </div>
            </div>
        </div>
        <component v-bind:is="currentTabComponent" ></component>
    </div>
</template>

<script>
// import EventServices from '../services/EventServices'
import Day from '../components/dashboard/day/Day.vue'
import Week from '../components/dashboard/week/Week.vue'
import { mapGetters } from 'vuex'

export default {
    components:{
        Day,
        Week,
    },
    data(){
        return{
            currentTab:'Week'
        }
    },
    computed: {
         ...mapGetters('auth',{
        isAuthenticated:'loggedIn',
        currentUser:'currentUser'
    }),
        currentTabComponent() {
        return  this.currentTab
        }
    },
    watch:{
        currentTabComponent(){
            this.$store.dispatch("global/setFormShiftModal",null)
        }
    },

    created(){
        // EventServices.getEvent(10)
        // .then((res)=>{
        //     console.log(res.data)
        // })
        // .catch((err)=>{
        //     console.log(err)
        // })
    }

}
</script>