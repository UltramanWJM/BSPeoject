<template>
    <div>
        <el-menu background-color="#404040" text-color="#ffffff" active-text-color="#ffd04b"
        default-active="1" @open="handleOpen" @close="handleClose" @select="handleSelect">
            <el-menu-item index="1">个人信息</el-menu-item>
            <el-menu-item index="2">家具管理</el-menu-item>
            <el-menu-item index="3">我是测试</el-menu-item>
            <el-submenu index="4">
                <template slot="title">多级菜单测试</template>
                <el-menu-item index="4-1">啊哈</el-menu-item>
                <el-menu-item index="4-2">我日</el-menu-item>
            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
export default {
    name: "UserInfo",
    methods: {
        handleOpen(key, keypath) {
            console.log("打开", key, keypath)
        },
        handleClose(key, keypath) {

        },
        handleSelect(key, keypath) {
            console.log("选择", key, keypath)
        }
    }
}
</script>

<style scoped>
</style>