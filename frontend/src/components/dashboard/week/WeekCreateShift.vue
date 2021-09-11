<template>
<div>
     <div class="modal fade" :id="'formShiftModel'" tabindex="-1"
                aria-labelledby="hourCellLabel" data-bs-backdrop="static" aria-hidden="true">
            <div class="modal-dialog  modal-md">
                <div class="modal-content">
                <div class="modal-header">
                    <div class="d-flex flex-column">
                        <div class="text-start"> Date : {{ gettersGetWeekSelectedDay }} </div>
                        <div class="text-start"> Employee : {{ gettersGetCurrentEmployee.first_name }} </div>
                    </div>
                    <button @click="closeModal()" type="button" class="btn-close" ></button>
                </div>
                <div class="modal-body">
                   <form action="" @submit.prevent="createShift">

                        <div v-if="err.message" class="mb-2 row">
                            <span class=" offset-4 col-sm-8 text-danger text-start is-invalid">
                                {{ err.message}}
                            </span>
                        </div>
                        <div class="mb-2 row">
                            <label for="startHour" class="col-sm-4 col-form-label">Jon Title</label>
                            <div class="col-sm-8">
                                <select  v-model.number="v$.job.$model"  id="startHour"
                                    :class="{'is-invalid':validationsStatus(v$.job),
                                    'is-valid':(validationsStatus(v$.job)!=null)}"
                                    class="form-select">
                                    <option selected>----------</option>
                                    <option v-for="item in gettersGetJobShiftChoices" :key="item.id"
                                        :value="item.id">{{ item.name }}</option>
                                </select>
                            </div>
                            <div v-if="v$.job.required.$invalid" class="invalid-feedback text-start">This field is required</div>
                        </div>

                        <div class="mb-2 row">
                            <label for="startHour" class="col-sm-4 col-form-label">Start Hour</label>
                            <div class="col-sm-8">
                                <input type="time" v-model="v$.startHour.$model"   min="00:00" max="23:00"
                                    class="form-control" required>
                            </div>
                            <!-- <div v-if="v$.startHour.startHour_between.$invalid" class="invalid-feedback text-start">Value must between 1 - 18 </div> -->
                            <div v-if="v$.startHour.required.$invalid" class="invalid-feedback text-start">This field is required</div>
                        </div>

                        <div class="mb-2 row">
                            <label for="endHour" class="col-sm-4 col-form-label">End Hour</label>
                            <div class="col-sm-8">
                                 <input type="time" v-model="v$.endHour.$model"   min="00:00" max="23:59"
                                 :class="{'is-invalid':validationsStatus(v$.endHour),'is-valid':(validationsStatus(v$.endHour)!=null)}"
                                   class="form-control" required>

                            <div v-if="v$.endHour.required.$invalid" class="invalid-feedback text-start">This field is required</div>
                            <div v-if="v$.endHour.endHour_greater_startHour.$invalid" class="invalid-feedback text-start">Must the end  hour be greater  than the start  hour </div>
                            <!-- <div v-if="v$.startHour.$model >= v$.endHour.$model  " class="invalid-feedback">Must the end  hour be greater  than the start  hour</div> -->
                            </div>
                        </div>

                        <div class="mb-2 row">
                            <div class="col-sm-12">
                               <textarea v-model.trim.lazy="v$.note.$model"  id="" cols="30" rows="4" class="form-control" placeholder="shift notes"></textarea>
                            </div>
                        </div>
                        <div class="my-2 border-top pt-2 d-flex justify-content-end" >
                            <button class="btn btn-success mx-1 btn-sm">save</button>
                            <button v-if="startHour" @click="deleteShift()" type="button" class="btn btn-outline-danger mx-1 btn-sm">delete</button>
                        </div>

                    </form>
                </div>

                </div>
            </div>
            </div>
    </div>
</template>

<script>
import {mapGetters,mapActions} from 'vuex'
import useVuelidate from "@vuelidate/core";
import { required,  } from 'vuelidate/lib/validators';
import jwtInterceptor from '../../../shared/jwtInterceptor'
const endHour_greater_startHour = (value, vm) => (value > vm.startHour);
// const startHour_between = (value) => (value > 0 && value < 18)
// const endHour_between = (value) => (value > 1 && value < 19)
export default {
    setup: () => ({ v$: useVuelidate() }),
    name:'CreateShift',
     data(){
        return{
            note:'',
            job:'',
            startHour:'',
            endHour:'',
            err:{}
        }
    },
    validations() {
        return {
            note:{},
            job: { required},
            startHour: { required,
            // startHour_between
            },
            endHour: {
                required,
                endHour_greater_startHour,
                // endHour_between,
                },
        };
    },
    computed:{
        ...mapGetters('global',{
            gettersGetSelecteddate:'getSelectedDate',
            gettersGetFormShiftModal:'getFormShiftModal',
            gettersGetWeekSelectedDay:'getWeekSelectedDay',
            gettersGetHourShiftChoices:"getHourShiftChoices",
            gettersGetJobShiftChoices:"getJobShiftChoices",
        }),
        ...mapGetters('auth',{
            gettersGetLocation:'getLocation',
        }),
        ...mapGetters('shifts',{
            gettersGetCurrentShift:'getCurrentShift',
        }),
        ...mapGetters('employees',{
            gettersGetCurrentEmployee:'getCurrentEmployee',
        })
    },
    watch:{
        gettersGetCurrentShift:{
             handler(){
                 try {
                     if(this.gettersGetCurrentShift){
                        this.startHour = this.gettersGetCurrentShift.starthour
                        this.endHour = this.gettersGetCurrentShift.endhour
                        this.job = this.gettersGetCurrentShift.job.id
                        this.note = this.gettersGetCurrentShift.note
                     }

                } catch (error) {
                    console.log(error)
                }
            },
            deep:true
        }
    },
    methods:{
         ...mapActions('shifts',{
            actionsCreateShift:'createShift',
            actionsUpdateShift:'updateShift',
            actionsDeleteShift:'deleteShift',
        }),
         ...mapActions('employees',{
            actionsWeekUpdateEmployee:'weekUpdateEmployee',
        }),
         validationsStatus(validation){
          if(!validation.$dirty)   return null;
          return typeof validation !="undefined" ? validation.$error:false;
        },
        closeModal(){
             this.gettersGetFormShiftModal.toggle()
        },
        async deleteShift(){
            const shift = this.gettersGetCurrentShift
            await this.actionsDeleteShift(shift)
             .then(()=>{
                this.showToast(' shift deleted successfully','error')
                this.gettersGetFormShiftModal.toggle()
            })
            // await this.actionsUpdateEmployee(this.employee.id)
            await this.actionsWeekUpdateEmployee({employee_id:this.gettersGetCurrentEmployee.id,date:this.gettersGetSelecteddate})
        },
        async createShift(){
            this.v$.$touch();
            if (this.v$.$invalid ){
                return;
            }else{
                const data = {
                    location:this.gettersGetLocation.id,
                    job:this.job,
                    note:this.note,
                    starthour:this.startHour,
                    endhour:this.endHour,
                    date:this.gettersGetWeekSelectedDay,
                    employee:this.gettersGetCurrentEmployee.id
                }
                // console.log(data)

                if(Object.keys(this.gettersGetCurrentShift).length === 0 && this.gettersGetCurrentShift.constructor === Object){
                     await jwtInterceptor.post('/shifts/create/',data)
                    .then(()=>{
                        this.gettersGetFormShiftModal.toggle()
                        this.showToast(' shift created successfully','success')
                        this.err = {}
                    })
                    .catch((err)=>{
                        this.err = err.response.data
                    })
                }
                else{
                   await jwtInterceptor.put('/shifts/'+this.gettersGetCurrentShift.id+'/update/',data)
                    // await this.actionsUpdateShift({shift:data,shift_id:this.gettersGetCurrentShift.id})
                    .then(()=>{
                        this.gettersGetFormShiftModal.toggle()
                        this.showToast(' shift updated successfully','success')
                        this.err = {}
                    })
                    .catch((err)=>{
                        this.err = err.response.data
                    })
                }
                await this.actionsWeekUpdateEmployee({employee_id:this.gettersGetCurrentEmployee.id,date:this.gettersGetSelecteddate})
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
    }

}
</script>

<style>

</style>