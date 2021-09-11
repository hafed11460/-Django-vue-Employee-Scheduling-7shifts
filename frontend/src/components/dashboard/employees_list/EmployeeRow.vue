<template>
    <tr >
        <th scope="row">{{ employee.id}}</th>
        <td>{{ employee.first_name}}</td>
        <td>{{ employee.last_name}}</td>
        <td>{{ employee.email}}</td>
        <td>{{ employee.phone}}</td>
        <td>{{ employee.location.name}}</td>
        <td>{{ employee.employee_type}}</td>
        <td>
            <div class="form-check form-switch d-flex justify-content-center">
            <input @change="DisableEmployee()" class="form-check-input"
                type="checkbox" :id="'check'+ employee.id"  v-model="is_active">
            <label class="form-check-label ms-2" :for="'check'+employee.id">Active</label>
            </div>
        </td>
        <td>
            <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                <router-link class="btn btn-success"  :to="{ name: 'EmployeeProfile',params: { id: employee.id } }"><i class="far fa-edit"></i> </router-link>
                <button @click="DeleteEmployee(employee.id)"  class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
            </div>
        </td>
    </tr>
</template>

<script>
import { mapActions } from 'vuex'
import jwtInterceptor from '../../../shared/jwtInterceptor'
export default {
    name:'EmployeeRow',
    props:{
        employee:Object,
    },
    data(){
        return{
            is_active:this.employee.is_active
        }
    },
     methods:{
          ...mapActions('employees',{
            actionsSetEmployeeList:'setEmployeesList',
        }),

        async DisableEmployee(){
                const data = {
                    'is_active':this.is_active,
                }
                console.log(this.is_active)
                await jwtInterceptor.put('/employees/'+this.employee.id+'/disable/',data)
                .then(()=>{
                    if(this.employee.is_active){
                        this.showToast('Employee '+ this.employee.first_name +' enable successfully','success')
                    }else{
                        this.showToast('Employee '+ this.employee.first_name +' disabled successfully','error')
                    }
                })
                .catch((err)=>{
                     this.is_active = !this.is_active
                     alert('cannot change this employee')
                    this.err = err.response.data
                })
        },
        async DeleteEmployee(employee_id){
            var r = confirm("Are you sure to delete this employee.\n Press button yes to delete it .");
            if (r == true) {
                await jwtInterceptor.delete('/employees/'+employee_id+'/delete/')
                .then(()=>{
                    this.actionsSetEmployeeList()
                    this.showToast('Deleted Employee  successfully','error')
                })
                .catch((err)=>{
                    this.err = err.response.data
                })
            }
        },
        showToast(message,type='success'){
            this.$toast(message, {
                duration: 5000,
                type:type,
                // Position not yet supported
                styles: {
                    borderRadius: '25px',
                },
                slot: '<i class="fa fa-thumbs-up"></i>',
            });
         },
    },
}
</script>

<style>

</style>