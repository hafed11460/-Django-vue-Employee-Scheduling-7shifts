<template>
    <div v-if="employee" class=" border-start my-3 ps-3 py-3 ">
        <h3 class="text-start  mb-3">Personal </h3>
        <form @submit.prevent="updateEmployee">
            <div class="row">
                <div class="row">
                    <div class="col-md-6 my-2">
                        <label class="fw-bold my-2"  for="email">Location</label>
                        <input id="email" type="email" v-model.trim="employee.location['name']"
                            :class="{'is-invalid':err.location != null}"
                            class="form-control" placeholder="Email" disabled>
                            <div v-if="err.location != null" class="invalid-feedback text-start"  v-html="err.location"></div>
                    </div>
                    <div class="col-md-6 my-2">
                        <label class="fw-bold my-2"  for="email">Restaurant</label>
                        <input id="email" type="email" v-model.trim="employee.location.restaurant['name']"
                            :class="{'is-invalid':err.location != null}"
                            class="form-control" placeholder="Email" disabled>
                            <div v-if="err.location != null" class="invalid-feedback text-start"  v-html="err.location"></div>
                    </div>
                </div>

                <div class="col  my-2">
                    <label class="fw-bold my-2"  for="first_name">First name</label>

                    <input id="first_name" type="text" v-model.trim="employee.first_name"
                    :class="{'is-invalid':err.first_name != null,}"
                        class="form-control" placeholder="First name">
                        <div v-if="err.first_name != null" class="invalid-feedback text-start"  v-html="err.first_name"></div>
                </div>
                <div class="col my-2">
                    <label class="fw-bold my-2"  for="last_name">Last name</label>
                    <input id="last_name" type="text" v-model.trim="employee.last_name"
                    :class="{'is-invalid':err.last_name != null,}"
                        class="form-control" placeholder="Last name">
                        <div v-if="err.last_name != null" class="invalid-feedback text-start"  v-html="err.last_name"></div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-6 my-2">
                    <label class="fw-bold my-2"  for="email">Email</label>
                    <input id="email" type="email" v-model.trim="employee.email"
                        :class="{'is-invalid':err.email != null}"
                        class="form-control" placeholder="Email">
                        <div v-if="err.email != null" class="invalid-feedback text-start"  v-html="err.email"></div>
                </div>
            </div>

             <div class="row">
                <div class="col  my-2">
                    <label class="fw-bold my-2" for="mobile_phone">Mobile phone</label>
                    <input id="mobile_phone" type="text" v-model.trim="employee.mobile_phone"
                    :class="{'is-invalid':err.mobile_phone != null,}"
                        class="form-control" placeholder="Mobile phone">
                        <div v-if="err.mobile_phone != null" class="invalid-feedback text-start"  v-html="err.mobile_phone"></div>
                </div>
                <div class="col my-2">
                    <label class="fw-bold my-2"  for="home_phone">Home phone</label>
                    <input id="home_phone" type="text" v-model.trim="employee.home_phone"
                    :class="{'is-invalid':err.home_phone != null,}"
                        class="form-control" placeholder="Home phone">
                        <div v-if="err.home_phone != null" class="invalid-feedback text-start"  v-html="err.home_phone"></div>
                </div>
            </div>
            <div class="d-flex flex-row mt-3">
                <button  class="btn btn-success">Save</button>
                <button v-if="!employee.is_active"  @click="DisableEmployee()"  type="button" class="btn btn-light border text-success mx-2">Enable Employee</button>
                <button v-else @click="DisableEmployee()"  type="button" class="btn btn-light border text-danger mx-2">Disable Employee</button>
                <button  @click="DeleteEmployee()"  type="button" class="btn btn-danger border  mx-2">Delete Employee</button>
            </div>
        </form>
    </div>
</template>

<script>
import jwtInterceptor from '../../../shared/jwtInterceptor'
export default {
    data(){
        return{
           employee:'',
            err:{
                // first_name:null,
                // last_name:null,
                // email:null,
                // password:null,
            }
        }
    },

    methods:{
        async updateEmployee(){
           const data = {
                'email':this.employee.email,
                'first_name':this.employee.first_name,
                'last_name':this.employee.last_name,
            }
            await jwtInterceptor.put('/employees/'+this.$route.params.id+'/update/',data)
            .then((res)=>{
                this.employee = res.data
                this.showToast('Update Employee Info successfully','success')
                this.err = {}
            })
            .catch((err)=>{
                this.err = err.response.data
            })
        },
        async DeleteEmployee(){
            var r = confirm("Are you sure to delete this employee.\n Press button yes to delete it .");
            if (r == true) {
                await jwtInterceptor.delete('/employees/'+this.$route.params.id+'/delete/')
                .then(()=>{
                    this.showToast('Deleted Employee  successfully','error')
                })
                .catch((err)=>{
                    this.err = err.response.data
                })
            }
        },
        async DisableEmployee(){
            var r = confirm("Are you sure to disable  this employee.\n Press button yes to delete it .");
            if (r == true) {
                const data = {
                    'is_active':false,
                }
                await jwtInterceptor.put('/employees/'+this.$route.params.id+'/disable/',data)
                .then(()=>{
                    this.showToast('Deleted Employee  successfully','error')
                    this.employee.is_active = !this.employee.is_active
                })
                .catch((err)=>{
                    this.err = err.response.data
                })
            }
        },

        async getEmployee(){
            await jwtInterceptor.get('/employees/'+this.$route.params.id+'/profile/')
            .then((res)=>{
                this.employee = res.data
            })
            .catch((err)=>{
                console.log('employees', err)
            })
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
    created() {
        this.getEmployee()

    }
}
</script>

<style scoped>

</style>