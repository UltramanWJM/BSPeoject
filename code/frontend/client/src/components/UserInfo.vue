<template>
<div id="total">
    <el-row class="row">
        <el-col :span="5"><div class="label">ID</div></el-col>
        <el-col :span="12">
            <el-input type="text" placeholder="UserID" v-model="id" readonly class="input"></el-input>
        </el-col>
    </el-row>
    <el-row class="row">
        <el-col :span="5"><div class="label">用户昵称</div></el-col>
        <el-col :span="12">
            <el-input type="text" placeholder="username" v-model="username" class="input"></el-input>
        </el-col>
        <el-col :span="3" style="margin-left:25px"><el-button type="info" @click="modName"><span>确定</span></el-button></el-col>  
    </el-row>
    <el-row class="row">
        <el-col :span="5"><div class="label">手机号码</div></el-col>
        <el-col :span="12">
            <el-input type="text" placeholder="phone" v-model="phone" class="input"></el-input>
        </el-col>
        <el-col :span="3" style="margin-left:25px"><el-button type="info"><span>确定</span></el-button></el-col>
    </el-row>
    <el-row style="margin-top:60px">
        <el-col :span="5"><div class="label">用户密码</div></el-col>
        <el-col :span="12">
            <el-input type="text" placeholder="newPassword" v-model="newPassword" class="input"></el-input>
        </el-col>
    </el-row>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: "UserInfo",
    data() {
        return {
            id: '',
            username: '',
            newPassword: '',
            phone: ''

        }
    },
    methods: {
        updateLocal() {
            let url = 'http://localhost:5000/getuserinfo'
            let params = {
                id: this.id
            }
            axios.get(url,{params: params})
            .then((res) => {
                localStorage.setItem('id', this.id)
                localStorage.setItem('password', res.data.password)
                localStorage.setItem('username', res.data.name)
                localStorage.setItem('phone', res.data.phone)
                this.username = res.data.name
                this.phone = res.data.phone
            })
            .catch((err) => {
            console.log(err);
          });
            localStorage.setItem
        },
        modName() {
            console.log(this.username)
            let params = {
                id: this.id,
                name: this.username,
                type: 0 // 0 means modify username
            }
            let url = 'http://localhost:5000/modusr'
            axios.get(url, {params: params})
            .then((res) => {
                console.log(res)
                this.$message({
                message: res.data.msg,
                type: res.data.code == 1 ? 'success' : 'error'
            })
                // this.updateLocal()
            }).catch((err) => {
            console.log(err);
          });
        }
    },
    mounted:function() {
        this.id = localStorage.getItem('id')
        this.username = localStorage.getItem('username')
        this.phone = localStorage.getItem('phone')
    },
    updated:function() {
        console.log("flash!!!!!!!!!!!!!!")
        this.updateLocal()
    }
}
</script>

<style>
.label {
    font-size: 20px;
    margin-top: 5%;
    margin-left: 15%;
    color: aliceblue;
}

#total {
    background-color: #606060;
}

.el-input__inner{
    /* 使input框的背景变透明 */
    background-color: transparent;
    /* 使边框也变透明 */
    border-color: transparent;
    /* 给边框加阴影能够使其有立体感 */
    box-shadow: 2px 2px 0 0 rgba(0,0,0,0.2);
    /* 改变获取焦点后的竖线颜色 */
    caret-color: rgba(0, 255, 255,0.8);
    color:#FFFFFF;
}

.row {
    margin-top: 20px;
}
</style>