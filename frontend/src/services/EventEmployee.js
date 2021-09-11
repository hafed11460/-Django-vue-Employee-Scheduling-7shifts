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
    getEmployees(){
        return apiClient.get('/employees')
    },
    async disableEmployee(id){
        return  await apiClient.put('/employees/'+ id)
    },
    disableEmployee(id){
        return apiClient.get('/employees/'+ id)
    },

}