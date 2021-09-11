
import axios from 'axios'
import store from '../store/index';

const excelJwtInterceptor = axios.create({
  baseURL:'http://localhost:8000'
})


excelJwtInterceptor.interceptors.request.use((config) => {
    // const authData = store.getters["auth/getAuthData"];
    // config.headers.common["Authorization"] = `bearer ${authData.token}`;
    const accessToken = store.getters["auth/accessToken"];
    config.headers.common["Authorization"] = `Bearer ${accessToken}`;
    config.responseType = 'blob'
    return config;
  });
  export default excelJwtInterceptor;
