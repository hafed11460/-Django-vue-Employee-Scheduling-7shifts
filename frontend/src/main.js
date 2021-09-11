import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VCalendar from 'v-calendar';
import DKToast from 'vue-dk-toast';
import Vuelidate from '@vuelidate/core'

createApp(App)
.use(router)
.use(store)
.use(VCalendar, {})
.use(Vuelidate)
.use(DKToast,{
    duration: 5000,
    positionY: 'bottom', // 'top' or 'bottom'
    positionX: 'right', // 'right' or 'left'
    styles: {
        color: '#000',
        backgroundColor: '#000',
        // Vendor prefixes also supported
    },
})
// .use(bootstrap)
// .component('DatePicker', DatePicker)
.mount('#app')
