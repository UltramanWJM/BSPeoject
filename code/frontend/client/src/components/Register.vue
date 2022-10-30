<template>
    <div class="login-wrap">
      <el-form class="login-container">
        <h1 class="title">用户注册</h1>
        <el-form-item>
          <el-input type="text" placeholder="用户账号" v-model="id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="text" placeholder="用户昵称" v-model="username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="text" placeholder="手机号码" v-model="phone" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="password" placeholder="用户密码" v-model="password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="password" placeholder="确认密码" v-model="password1" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="doRegister" style="width: 48%;">注册</el-button>
          <el-button type="primary" @click="toLogin" style="width: 48%;">返回登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </template>
   
  <script>
  import axios from 'axios';
    export default {
      name: 'Login',
      data: function() {
        return {
          id:'',
          username: '',
          password: '',
          password1:'',
          phone:''
        }
      },
      methods: {
        doRegister:function(){
          let params = {
            id: this.id,
            username: this.username,
            phone: this.phone,
            password:this.password,
            method: 'Register'
          };
          console.log(params);
          const url = 'http://localhost:5000/register'
          axios.get(url, {params: params})
          .then((res) => {
            console.log(res);
            console.log(res.data);
            this.$message({
                message: res.data.msg,
                type: res.data.code == 1 ? 'success' : 'error'
            });
          })
          .catch((err) => {
            console.log(err);
          });
        },
        toLogin:function(){
          this.$router.push('/login');
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
