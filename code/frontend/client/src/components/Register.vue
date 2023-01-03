<template>
    <div class="login-wrap">
      <el-form :model="formData" :rules="rules" class="login-container" >
        <h1 class="title">用户注册</h1>
        <el-form-item prop="id">
          <el-input type="text" placeholder="用户账号" v-model="formData.id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="username">
          <el-input type="text" placeholder="用户昵称" v-model="formData.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="phone">
          <el-input type="text" placeholder="手机号码" v-model="formData.phone" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" placeholder="用户密码" v-model="formData.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item prop="password1">
          <el-input type="password" placeholder="确认密码" v-model="formData.password1" autocomplete="off"></el-input>
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
        var checkId = (rule, value, callback) => {
          let idReg = /^[0][0-9]+$/
          if (!value) {
            callback()
          } else {
            if (idReg.test(value)) {
              callback(new Error("ID格式: 6-9位的纯数字，不得以0开头"))
            }
          }
        }
        var checkPassword = (rule, value, callback) => {
          if (value === '') {
            callback(new Error('请再次输入密码'))
          } else if (value !== this.formData.password) {
            callback(new Error('两次输入密码不一致！'))
          } else {
            callback()
          }
        }
        var checkPhone = (rule, value, callback) => {
          let phoneReg = /1[3|4|5|6|7|8|9][0-9]{9}$/
          if (!value) {
            callback()
          } else {
            if (phoneReg.test(value)) {
              callback()
            } else {
              callback(new Error("电话格式:13、14、15、17、18、19开头 + 9位阿拉伯数字"))
            }
          }
        }

        return {
          // id:'',
          // username: '',
          // password: '',
          // password1:'',
          // phone:'',

          formData:{
            id: '',
            username: '',
            password: '',
            password1: '',
            phone: ''
          },
          rules: {
            id: [
              {required: true, message: "请输入ID", trigger: "blur"},
              {min: 6, max: 9, message: "长度在6到9个字符", trigger: "blur"},
              {validator: checkId, trigger: "blur"}
            ],
            password: [
              {required: true, message: "请输入密码", trigger: "blur"},
              {min: 6, max: 30, message: "长度在6到30个字符", trigger: "blur"}
            ],
            password1: [
              {validator: checkPassword, trigger: "blur"}
            ],
            phone: [
              {required: true, message: "请输入电话号码", trigger: "blur"},
              {validator: checkPhone, trigger: "blur"}
            ],
            username: [
              {required: true, message: "请输入用户昵称", trigger: "blur"}
            ]
          }
        }
      },
      methods: {
        doRegister:function(){
          let params = {
            id: this.formData.id,
            username: this.formData.username,
            phone: this.formData.phone,
            password: this.formData.password,
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
