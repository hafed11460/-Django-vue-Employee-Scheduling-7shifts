<template>
  <div class="container my-5">
    <div v-for="restaurant in restaurants" :key="restaurant.id" class="my-5 border bg-light  p-3" >
      <h5 class="text-start mb-3 text-uppercase">{{ restaurant.name }}</h5>
        <div class="row row-cols-1 row-cols-md-3 g-4">

          <div v-for="location in restaurant.location" :key="location.id" class="col ">
            <div class="card">
              <div :class="getUserLocation== location.id?'bg-info text-white':'' " class="card-body ">
                <h5 class="card-title">{{location.name}}</h5>
                <p class="card-text">Restaurant : {{ restaurant.name}}</p>
              </div>
            </div>
          </div>


    </div>


    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import jwtInterceptor from '../shared/jwtInterceptor'
export default {
  data(){
    return{
      restaurants:{}
    }
  },
   computed: {
         ...mapGetters('auth',{
        isAuthenticated:'loggedIn',
        currentUser:'currentUser'
    }),
    getUserLocation(){
      return this.currentUser.location.id
    }
  },
  methods:{
    async getRestaurant(){
       await jwtInterceptor.get('/restaurants/')
            .then((res)=>{
               this.restaurants = res.data
            })
            .catch((err)=>{
                console.log('employees', err)
            })
    }
  },
  created(){
    this.getRestaurant()
  }
}
</script>

<style>

</style>