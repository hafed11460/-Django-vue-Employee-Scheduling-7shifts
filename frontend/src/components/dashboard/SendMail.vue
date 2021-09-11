<template>
    <span @click="showEmailModal()" type="button" class="btn btn-success  border">
                    <i class="fas fa-mail-bulk"></i> publish week </span>
     <div class="modal fade" id="emailModel" tabindex="-1"
                aria-labelledby="hourCellLabel" data-bs-backdrop="static" aria-hidden="true">
            <div class="modal-dialog  modal-md">
                <div class="modal-content">
                <div class="modal-header">
                    <div class="d-flex flex-column text-start">
                       <p>publish this week </p>
                    </div>
                    <button @click="showEmailModal()" type="button" class="btn-close" ></button>
                </div>
                <div class="modal-body">
                   <form action="" @submit.prevent="sendMail">
                       <div v-if="error">
                           <p class="text-danger ">Error sending mail </p>
                       </div>
                        <!-- <div class="my-2 row">
                            <div class="col-sm-6 text-start">
                                <label for="startDate">Start date</label>
                               <input type="date" v-model="startDate" id="startDate" class="form-control" placeholder="Subject">
                            </div>
                            <div class="col-sm-6 text-start">
                                <label for="endDate">End date</label>
                                <input type="date" v-model="endDate" id="endDate" class="form-control" placeholder="Subject">
                            </div>
                        </div> -->
                        <div class="my-3 row">
                            <div class="col-sm-12">
                               <input v-model="subject"  class="form-control" placeholder="Subject">
                            </div>
                        </div>
                        <div class="mb-2 row">
                            <div class="col-sm-12">
                               <textarea v-model="message"  id="" cols="30" rows="4" class="form-control" placeholder="Message"></textarea>
                            </div>
                        </div>
                        <div class="my-2 border-top pt-2 d-flex justify-content-end" >
                            <button class="btn btn-success mx-1 btn-sm">Send</button>
                        </div>

                    </form>
                </div>

                </div>
            </div>
    </div>
</template>

<script>
import * as bootstrap from 'bootstrap'
import jwtInterceptor from '../../shared/jwtInterceptor'
import { mapGetters } from 'vuex'
export default {

    name:'CreateShift',
     data(){
        return{
            // startDate:'',
            // endDate:'',
           emailModal:null,
           subject:'Test ',
           message:'Hello world',
           error:'',
        }
    },
    computed:{
        ...mapGetters('global',{
              gettersGetSelecteddate:'getSelectedDate',
        })
    },

    methods:{
        async sendMail(){
            const data = {
                // startdate:this.startDate,
                // enddate:this.endDate,
                subject:this.subject,
                message:this.message
            }
            console.log(data)
            await jwtInterceptor.post('/employees/send-mail/?date='+this.gettersGetSelecteddate,data)
            .then(()=>{
                this.emailModal.toggle()
                this.showToast('mail are successfull send ','success')
            })
            .catch((err)=>{
                this.error = err.response.data
            })
        },
        showEmailModal(){
            if(this.emailModal === null){
                this.emailModal = new bootstrap.Modal(document.getElementById('emailModel'))
            }
                this.emailModal.toggle()
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