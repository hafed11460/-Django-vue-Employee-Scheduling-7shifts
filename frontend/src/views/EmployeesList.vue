<template>
    <div class="container mt-5">
        <div class="d-flex flex-row justify-content-between border-bottom my-2 py-2">
            <h5 class="text-start">Employees List</h5>
            <div>
                Location :
                <span v-if="currentUser.location" type="button" class="btn ">
                    {{ currentUser.location['name'] }} |
                    {{ currentUser.location['restaurant'].name }}
                </span>
            </div>
        </div>

        <div class="" >
            <table class="table table-striped table-hover">
                <thead>
                    <tr>
                    <th scope="col">Id</th>
                    <th scope="col">First</th>
                    <th scope="col">Last</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Location</th>
                    <th scope="col">Role</th>
                    <th scope="col">Status</th>
                    <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <EmployeeRow :employee="employee" v-for="employee in getterGetEmployeeList" :key="employee.id"/>
                </tbody>
                </table>
        </div>
    </div>
</template>

<script>
import jwtInterceptor from '../shared/jwtInterceptor'
import EmployeeRow from '../components/dashboard/employees_list/EmployeeRow.vue'
import { mapActions, mapGetters } from 'vuex'
export default {
    name:'EmployeesList',
    components:{
        EmployeeRow,
    },
    data(){
        return{
            employees:{}
        }
    },
    computed: {
         ...mapGetters('auth',{
        isAuthenticated:'loggedIn',
        currentUser:'currentUser'
    }),
         ...mapGetters('employees',{
        getterGetEmployeeList:'getEmployeesList',
    }),

    },
    methods:{
        ...mapActions('employees',{
            actionsSetEmployeeList:'setEmployeesList',
        }),
        async getAllEmployees(){
            await jwtInterceptor.get('/employees/all/')
            .then((res)=>{
                this.employees = res.data
            })
            .catch((err)=>{
                console.log('employees', err)
            })
        },
    },
    mounted(){
        this.actionsSetEmployeeList()
    }
}
</script>

<style>

</style>