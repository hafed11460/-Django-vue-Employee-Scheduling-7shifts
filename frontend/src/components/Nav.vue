<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
     <router-link class="navbar-brand"  :to="{name: 'Home'}">Home</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <!-- <li class="nav-item">
          <router-link class="nav-link active" to="/offers">Offers</router-link>
        </li> -->
        <li v-if="isManager" class="nav-item">
          <router-link class="nav-link active" :to="{name: 'Manager'}">Manager</router-link>
        </li>
        <li v-if="isManager" class="nav-item">
          <router-link class="nav-link active" :to="{name: 'EmployeesList'}">Employees List</router-link>
        </li>
        <li v-if="isUser" class="nav-item">
          <router-link class="nav-link active" :to="{name: 'UserSchedule'}">schedule </router-link>
        </li>

      </ul>
      <template v-if="currentUser">
        <ul class="navbar-nav mb-2 mb-lg-0 d-flex flex-row">
            <li class="nav-item mx-2">
              <router-link class="btn btn-success" to="/login">{{currentUser.first_name}}</router-link>
            </li>
            <li class="nav-item">
              <button  @click.prevent="logOut" class="btn btn-outline-success" >logout</button>
            </li>
        </ul>
      </template>
      <template v-else>
        <ul class="navbar-nav mb-2 mb-lg-0 d-flex flex-row">
            <li  class="nav-item mx-2">
              <router-link class="btn btn-success" :to="{name: 'Login'}">Login</router-link>
            </li>
            <li class="nav-item mx-2">
              <router-link class="btn btn-success" to="/login">register</router-link>
            </li>
        </ul>
      </template>
    </div>
  </div>
</nav>
</template>

<script>
import {mapGetters,mapActions} from 'vuex'
export default {
  computed:{
    ...mapGetters('auth',{
        isAuthenticated:'loggedIn',
        currentUser:'currentUser',
        gettersGetEmployeeRole:'getEmployeeRole',

    }),

    isManager(){
      if(this.currentUser){
        try {
              const {role} = this.currentUser
              var name = role['name']
              return role['name'] === 'Manager'
          } catch (error) {
            console.log(name)
          }
          return false
      }else{
            return false
      }
    },
    isUser(){
      if(this.currentUser){
        try {
              const {role} = this.currentUser
              var name = role['name']
              return role['name'] !== 'Manager'
          } catch (error) {
            console.log(name)
          }
          return false
      }else{
            return false
      }
    }

  },
  methods:{
    ...mapActions('auth',{
      actionLogout:'logout'
    }),
    logOut() {
        this.$store.dispatch('auth/logout')
        this.$router.push('/login')
        // .then(
        //   () => {
        //     // this.clearAll()
        //   }
        // )
      // this.actionLogout()
      // this.$router.push('/login');
    }
  }
}
</script>

<style>

</style>