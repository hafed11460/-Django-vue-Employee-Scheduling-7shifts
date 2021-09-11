import axios from "axios";

const apiClient = axios.create({
    baseURL:'http://localhost:8000',
    withCredentials:false,
    headers:{
        Accept:'application/json',
        'Content-type':'application/json'
    }
})

export default{
    getEvents(){
        return apiClient.get('/events')
    },
    getEvent(id){
        return apiClient.get('/event/'+ id)
    }
}