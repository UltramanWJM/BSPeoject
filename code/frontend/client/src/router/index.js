import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import test from '../components/test.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import UserInfo from '../components/UserInfo.vue'
import User from '../components/User.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'Test',
      component: test
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/user',
      name: 'User',
      component: User,
      children:[
        {
          path: 'info',
          name: 'UserInfo',
          component: UserInfo
        }
      ]
    }
    
  ],
  mode: 'history'
})
