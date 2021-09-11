import axios from 'axios'
import store from '../store/index';

const jwtInterceptor = axios.create({
  baseURL:'http://localhost:8000'
})

jwtInterceptor.interceptors.request.use((config) => {
    // const authData = store.getters["auth/getAuthData"];
    // config.headers.common["Authorization"] = `bearer ${authData.token}`;
    const accessToken = store.getters["auth/accessToken"];
    config.headers.common["Authorization"] = `Bearer ${accessToken}`;
    return config;
  });
  export default jwtInterceptor;
