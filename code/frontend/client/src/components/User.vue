<template>
    <div id="total">
        <el-container>
            <el-aside width="250px" background-color="#606060">
                <div>
            <el-menu background-color="#404040" text-color="#ffffff" active-text-color="#ffd04b"
            default-active="1" @open="handleOpen" @close="handleClose" @select="handleSelect">
                <el-menu-item index="/user/info">个人信息</el-menu-item>
                <el-menu-item index="/user/scene">场景管理</el-menu-item>
                <el-menu-item index="/user/device">设备管理</el-menu-item>
                <el-submenu index="4">
                    <template slot="title">设备信息详情</template>
                    <el-menu-item index="/device/lamp">灯</el-menu-item>
                    <el-menu-item index="/device/switch">开关</el-menu-item>
                    <el-menu-item index="/device/sensor">传感器</el-menu-item>
                    <el-menu-item index="/device/lock">门锁</el-menu-item>
                </el-submenu>
            </el-menu>
        </div>
            </el-aside>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </div>
</template>

<script>
export default {
    name: "User",
    methods: {
        handleOpen(key, keypath) {
            console.log("打开", key, keypath)
        },
        handleClose(key, keypath) {

        },
        handleSelect(key, keypath) {
            console.log("选择", key, keypath)
            this.$router.push(key)
        }
    }
}
</script>

<style scoped>
#total {
    background-color: #606060;
    height: 860px;
}
</style>