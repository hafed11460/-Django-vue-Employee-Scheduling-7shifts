import { createStore } from "vuex";
import auth  from "./auth";
import offers from './offers'
import employees from './employees'
import shifts from './shifts'
import global from './global'

const store = createStore({
  modules: {
    auth,
    offers,
    employees,
    shifts,
    global,
  },
});

export default store;
