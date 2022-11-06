import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import test from '../components/test.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import UserInfo from '../components/UserInfo.vue'
import User from '../components/User.vue'
import SceneInfo from '../components/SceneInfo.vue'
import DeviceInfo from '../components/DeviceInfo.vue'

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
        },
        {
          path: 'scene',
          name: 'SceneInfo',
          component: SceneInfo
        },
        {
          path:'device',
          name: 'DeviceInfo',
          component: DeviceInfo
        }
      ]
    }
    
  ],
  mode: 'history'
})
