<template>
    <div class="login-wrap">
      <el-form class="login-container">
        <h1 class="title">用户登录</h1>
        <el-form-item>
          <el-input type="text" placeholder="用户ID" v-model="id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="password" placeholder="用户密码" v-model="password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="doLogin" style="width: 100%;">登录</el-button>
        </el-form-item>
        <el-row style="text-align: center;margin-top: -10px;">
          <el-link type="primary" @click="toRegister">用户注册</el-link>
          <el-link type="primary">忘记密码</el-link>
        </el-row>
      </el-form>
    </div>
  </template>
   
  <script>
import axios from 'axios';

    export default {
      name: 'Login',
      data: function() {
        return {
          id: '',
          password: ''
        }
      },
      methods: {
        doLogin:function(){
          let id=this.id;
          let password=this.password;
          console.log("id=%s,password=%s",id,password);
          let params = {
            id: id,
            password: password,
            method: 'Login'
          };
          const url = 'http://localhost:5000/login'
          axios.get(url, {params: params})
          .then((res) => {
            console.log(res);
            console.log(res.data);
            this.$message({
                message: res.data.msg,
                type: res.data.code == 1 ? 'success' : 'error'
            });
            if (res.data.code == 1) {
              localStorage.setItem('id', id)
              localStorage.setItem('password', password)
              localStorage.setItem('username', res.data.name)
              localStorage.setItem('phone', res.data.phone)
              this.$router.push('/user');
              // console.log(localStorage.getItem('username'))
            }
          })
          .catch((err) => {
            console.log(err);
          });
        },
        toRegister:function(){
          this.$router.push('/register');
        }
      }
    }
  </script>
   
  <style>
    .login-wrap {
      box-sizing: border-box;
      width: 100%;
      height: 100%;
      padding-top: 10%;
      background-color: #D3D3D3;
      background-repeat: no-repeat;
      background-position: center right;
      background-size: 100%;
    }
   
    .login-container {
      border-radius: 10px;
      margin: 0px auto;
      width: 350px;
      padding: 30px 35px 15px 35px;
      background: #fff;
      border: 1px solid #eaeaea;
      text-align: left;
      box-shadow: 0 0 20px 2px rgba(0, 0, 0, 0.1);
    }
   
    .title {
      margin: 0px auto 40px auto;
      text-align: center;
      color: #505458;
    }
  </style>
