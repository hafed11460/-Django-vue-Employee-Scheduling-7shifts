<template>
  <div class="container">
      <div class="position-absolute top-50 start-50 translate-middle border p-5">
        <form @submit.prevent="login" >
            <p v-if="incorrectAuth" class="text-danger">Incorrect email or password entred</p>
            <div class="my-2">
                <select  v-model="email" class="form-control" >
                    <option value="admin@gmail.com">admin@gmail.com</option>
                    <option value="manager_a_1@gmail.com">manager_a_1@gmail.com</option>
                    <option value="manager_b_1@gmail.com">manager_b_1@gmail.com</option>
                    <option value="employee_a_1@gmail.com">employee_a_1@gmail.com</option>
                    <option value="employee2_a_1@gmail.com">employee2_a_1@gmail.com</option>
                    <option value="employee_b_1@gmail.com">employee1_b_1@gmail.com</option>
                </select>
                <!-- <input type="email" v-model="email" class="form-control"> -->
            </div>
            <div class="my-2">
                <select  v-model="password" class="form-control" >
                    <option value="123">123</option>
                    <option value="Azerty@123">Azerty@123</option>
                </select>
                <!-- <input type="password" v-model="password" class="form-control"> -->
            </div>
            <div class="my-2">
                <button class="btn btn-success btn-sm" >Login</button>
            </div>
        </form>
      </div>
  </div>
</template>

<script>
import {mapGetters,mapActions} from 'vuex'
export default {
    name:'Login',

    data(){
        return{
            API_URL:'http://localhost:8000',
            email:'admin@gmail.com',
            password:'',
            incorrectAuth:false,
            error:''
        }
    },

    computed: {
        ...mapGetters('auth',{

        }),
        loggedIn() {
        return false //this.$store.state.auth.status.loggedIn;
        },
    },
    created() {
        if (this.loggedIn) {
        this.$router.push("/offers");
        }
    },
    methods:{
        ...mapActions('auth',{
            actionLogin:'userLogin',
            actionSetUser:'setUser',
        }),
        async login(){
            await this.actionLogin({
                email:this.email,
                password:this.password,
            })
            .then(()=>{
                this.actionSetUser()
                this.$router.push('/')
            })
            .catch((err)=>{
                this.incorrectAuth =true
                console.log(err)
            })
        },
    }
}
</script>

<style>

</style>