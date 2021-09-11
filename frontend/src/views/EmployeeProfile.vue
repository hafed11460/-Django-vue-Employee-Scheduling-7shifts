<template>
  <div class="container mt-5 text-start">

    <div class="d-flex flex-row border-bottom pb-3">
      <div >
         <img :src="employee.profile_image" width="100" height="100" class="rounded-circle">
      </div>
      <div class="align-self-center mx-2">
          <h1>
            {{ employee.first_name }}  {{ employee.last_name }}
          </h1>
      </div>
    </div>

    <div class="row my-3">
        <div class="col-md-3">
            <div class="list-group rounded-0" id="list-tab" role="tablist">
                <a  @click="currentTab='Personal'" :class="{ 'active':currentTab =='Personal'}" class="list-group-item list-group-item-action" >Personal</a>
                <!-- <a  @click="currentTab='Location'" :class="{ 'active':currentTab =='Location'}" class="list-group-item list-group-item-action" >Location</a>
                <a  @click="currentTab='Employment'" :class="{ 'active':currentTab =='Employment'}" class="list-group-item list-group-item-action" >Employment</a> -->
            </div>
        </div>
        <div class="col-md-9">
            <component v-bind:is="currentTabComponent" ></component>
        </div>
    </div>
  </div>
</template>

<script>
import jwtInterceptor from '../shared/jwtInterceptor'
import Personal from '../components/dashboard/employee/Personal.vue'
import Employment from '../components/dashboard/employee/Employment.vue'
import Location from '../components/dashboard/employee/Location.vue'
export default {
    name: 'Employee',
    components:{
        Personal,
        Employment,
        Location,
    },
    data(){
      return{
          currentTab:'Personal',
          employee:{},
        }
    },
    computed: {
            currentTabComponent() {
            return  this.currentTab
            }
        },
    methods:{
        async getEmployee(){
            await jwtInterceptor.get('/employees/'+this.$route.params.id+'/profile/')
            .then((res)=>{
                this.employee = res.data
            })
            .catch((err)=>{
                console.log('employees', err)
            })
        }
    },
    mounted() {
        this.getEmployee()
    }
    };
</script>

<style scoped>
    .active{
        background-color: rgb(239, 239, 243) !important;
        color: rgb(60, 61, 60);
        border:0px;
        border-left: 2px solid green;
        border-radius: 0px;
    }
</style>