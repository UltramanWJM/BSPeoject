<template>
    <div class="scenes">
        <h2 style="margin-top: -5px"><font color="white"> 场景管理界面 </font></h2>
        <el-row>
            <el-col :span="22" :push="0">
                <div>
                    <el-form :inline="true">
                        <el-form-item style="float: left" label="查询场景信息：" class="form">
                            <el-input v-model="searchSceneId" placeholder="查询场景ID"></el-input>
                        </el-form-item>
                        <el-form-item style="float: right">
                            <el-button type="primary" @click="handleAdd">创建场景</el-button>
                        </el-form-item>
                    </el-form>
                </div>
                <div class="table">
                    <el-table :data="tableData" stripe broder>
                        <el-table-column
                        label="序号" 
                        type="index" 
                        width="100">
                        </el-table-column>
                        <el-table-column
                            label="场景ID"
                            align="center"
                            width="200"
                            prop="sceneId">
                        </el-table-column>
                        <el-table-column
                            label="场景名称"
                            align="center"
                            width="400"
                            prop="sceneName">
                        </el-table-column>
                        <el-table-column
                            label="设备数"
                            align="center"
                            prop="deviceNum">
                        </el-table-column>
                        <el-table-column fixed="right" label="操作" width="100">
                            <template slot-scope="scope">
                                <el-button type="text" size="small">查看</el-button>
                                <el-button type="text" size="small">编辑</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-col>
        </el-row>
        <AddScene :dialogAdd="dialogAdd" @update="getScenes"></AddScene>
    </div>
</template>

<script>
import axios from 'axios';
import AddScene from './CreateScene.vue'
export default {
    name: 'SceneInfo',
    data() {
        return {
            tableData: [],
            userId: '',
            username: '',
            phone: '',
            searchSceneId: '',
            dialogAdd:{
                show:false
            }
        }
    },
    components: {
        AddScene
    },
    methods: {
        getScenes() {
            let url = 'http://127.0.0.1:5000/getscenes'
            let params = {
                userId: localStorage.getItem('id')
            }
            axios.get(url, {params: params})
            .then((res) => {
                console.log(res)
                this.tableData = res.data
            });
        },
        handleAdd(){  //添加
            this.dialogAdd.show = true;
        }
    },
    mounted: function() {
        this.getScenes();
    }
}
</script>

<style>
.form .el-form-item__label{
    color: white;
}
</style>