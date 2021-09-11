<template>
    <div>

        <button @click="showModalCreateEmployee()"  type="button" class="btn btn-light border  rounded-0 my-2">
            <i class="fas  fa-lg fa-plus-square text-success"></i>
            Add employee
        </button>
        <!-- Modal -->
        <div class="modal fade" id="newEmployee" tabindex="-1" aria-labelledby="newEmployeeLabel" data-bs-backdrop="static" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-sm">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="newEmployeeLabel">Add employee</h5>
                <button @click="showModalCreateEmployee()" type="button" class="btn-close" ></button>
            </div>
            <div class="modal-body">
                <form @submit.prevent="newEmployee">
                    <div class="row">
                        <div class="my-2">
                            <select type="text" v-model.trim="form.role"
                            :class="{'is-invalid':err.role != null,'is-valid':form.role != ''}"
                             class="form-select" placeholder="Role">
                                <option>----------</option>
                                <option v-for="job in gettersGetJobShiftChoices" :key="job.id"
                                    :value="job.id">{{ job.name }}</option>
                            </select>
                             <div v-if="err.role != null" class="invalid-feedback text-start"  v-html="err.role"></div>
                        </div>
                        <div class="my-2">
                            <input type="text" v-model.trim="form.first_name"
                            :class="{'is-invalid':err.first_name != null,'is-valid':form.first_name != ''}"
                             class="form-control" placeholder="First name">
                             <div v-if="err.first_name != null" class="invalid-feedback text-start"  v-html="err.first_name"></div>
                        </div>
                        <div class="my-2">
                            <input type="text" v-model.trim="form.last_name"
                            :class="{'is-invalid':err.last_name != null,'is-valid':form.last_name != ''}"
                             class="form-control" placeholder="Last name">
                             <div v-if="err.last_name != null" class="invalid-feedback text-start"  v-html="err.last_name"></div>
                        </div>
                        <div class="my-2">
                            <input type="email" v-model.trim="form.email"
                             :class="{'is-invalid':err.email != null,'is-valid':form.email != ''}"
                             class="form-control" placeholder="Email">
                             <div v-if="err.email != null" class="invalid-feedback text-start"  v-html="err.email"></div>
                        </div>
                        <div class="my-2">
                            <input type="password" v-model.trim="form.password"
                            :class="{'is-invalid':err.password != null,'is-valid':form.password != ''}"
                            class="form-control" placeholder="password">
                             <div v-if="err.password != null" class="invalid-feedback text-start"  v-html="err.password"></div>
                        </div>
                    </div>
                    <div class="d-flex flex-row-reverse mt-3">
                        <button  @click="showModalCreateEmployee()"  type="button" class="btn btn-secondary mx-2">Close</button>
                        <button   class="btn btn-primary">Create</button>
                    </div>
                </form>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import * as bootstrap from 'bootstrap'
export default {
    name:'NewEmployee',
    data(){
        return{
            myModal:null,
            form:{
                role:'',
                first_name:'',
                last_name:'',
                email:'',
                password:'',
            },
            err:{
                role:null,
                first_name:null,
                last_name:null,
                email:null,
                password:null,
            }
        }
    },
    computed:{
        ...mapGetters('auth',{
            gettersGetLocation:'getLocation',
        }),
        ...mapGetters('global',{
            gettersGetErrors:'getErrors',
             gettersGetJobShiftChoices:"getJobShiftChoices",
        }),
        ...mapGetters('employees',{
            gettersGetSuccessCreateEmployee:'getSuccessCreateEmployee',
        })
    },
    methods:{
        ...mapActions('employees',{
            actionsSetSuccessCreateEmployee:'setSuccessCreateEmployee',
             actionCreateEmployee:'createEmployee',
        }),
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
        showModalCreateEmployee(){
          if(this.myModal === null){
            this.myModal = new bootstrap.Modal(document.getElementById('newEmployee'))
          }
            this.myModal.toggle()
        },
        validationsStatus(validation){
            if(!validation.$dirty)   return null;
            return typeof validation !="undefined" ? validation.$error:false;
        },

        async newEmployee(){
            const data = {
                    role:this.form.role,
                    location:this.gettersGetLocation.id,
                    first_name:this.form.first_name,
                    last_name:this.form.last_name,
                    email:this.form.email,
                    password:this.form.password,
                }
                console.log(data)
            await this.actionCreateEmployee(data)
            if(this.gettersGetSuccessCreateEmployee){
                this.showModalCreateEmployee()
                this.showToast('New Employee add successfully','success')
                this.actionsSetSuccessCreateEmployee(false)
            }else{
                this.err = this.gettersGetErrors
            }
        },
    }
}
</script>

<style>

</style>