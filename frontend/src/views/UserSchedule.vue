<template>
    <div v-if="currentUser">
        <div class=" d-flex flex-row p-1 mt-3 justify-content-between">
            <div class="">
                <div class="btn-group border" role="group" aria-label="Basic mixed styles example">
                    <span v-if="currentUser.location" type="button" class="btn btn-light">
                        {{ currentUser.location['restaurant'].name }} -
                        {{ currentUser.location['name'] }}
                    </span>
                </div>
            </div>
            <div class="">
                <div class="btn-group border" role="group" aria-label="Basic mixed styles example">
                     <span @click="currentTab='UserDay'" type="button" :class="currentTabComponent=='UserDay'?'btn-primary':'btn-light'" class="btn ">Day</span>
                    <span @click="currentTab='UserWeek'" type="button" :class="currentTabComponent=='UserWeek'?'btn-primary':'btn-light'" class="btn ">Week</span>
                </div>
            </div>
        </div>
        <component v-bind:is="currentTabComponent" ></component>
    </div>
</template>

<script>
// import EventServices from '../services/EventServices'
import UserDay from '../components/dashboard/users/day/UserDay.vue'
import UserWeek from '../components/dashboard/users/week/UserWeek.vue'
import { mapGetters } from 'vuex'

export default {
    components:{
        UserDay,
        UserWeek,
    },
    data(){
        return{
            currentTab:'UserWeek'
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



}
</script>