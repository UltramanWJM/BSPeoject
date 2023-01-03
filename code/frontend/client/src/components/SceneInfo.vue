<template>
    <div class="scenes">
        <h2 style="margin-top: -5px"><font color="white"> 场景管理界面 </font></h2>
        <el-row>
            <el-col :span="22" :push="0">
                <div>
                    <el-form :inline="true">
                        <el-form-item style="float: left" label="查询设备信息：" class="form">
                            <el-input v-model="searchSceneId" placeholder="查询设备ID"></el-input>
                        </el-form-item>
                        <el-form-item style="float: right">
                            <el-button type="primary" @click="handleAdd">创建场景</el-button>
                        </el-form-item>
                    </el-form>
                </div>
                <div class="table">
                    <el-table :data="tableData" broder>
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
                                <el-button type="text" size="small" @click="showScene(scope.$index, scope.row)">查看</el-button>
                                <el-button type="text" size="small" @click="deleteScene(scope.$index, scope.row)">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-col>
        </el-row>
        <AddScene :dialogAdd="dialogAdd" @update="getScenes"></AddScene>
        <ShowScene :dialogShow="dialogShow"></ShowScene> 
    </div>
</template>

<script>
import axios from 'axios';
import AddScene from './CreateScene.vue'
import ShowScene from './ShowScene.vue'
export default {
    name: 'SceneInfo',
    data() {
        return {
            tableData: [],
            userId: '',
            username: '',
            phone: '',
            searchSceneId: '',
            dialogAdd: {
                show: false
            },
            dialogShow: {
                show: false,
                imgUrl: ''
            }
        }
    },
    components: {
        AddScene,
        ShowScene
    },
    methods: {
        getScenes() {
            let url = 'http://127.0.0.1:5000/getscenes'
            let params = {
                userId: localStorage.getItem('id')
            }
            axios.get(url, {params: params})
            .then((res) => {
                console.log(res.data)
                this.tableData = res.data.data
            });
        },
        handleAdd() {  //添加
            this.dialogAdd.show = true;
        },
        deleteScene(index, row) {
            let params = {
                sceneId: row.sceneId
            };
            let url = "http://127.0.0.1:5000/deletescene"
            axios.get(url, {params: params})
            .then((res) => {
                this.$message({
                message: res.data.msg,
                type: res.data.code == 1 ? 'success' : 'error'
                });
                this.getScenes()
            })
        },
        showScene(index, row) {
            this.getSceneImg(row.sceneId);
            this.dialogShow.show = true;
        },
        getSceneImg(sceneId) {
            let url = 'http://127.0.0.1:5000/getsceneimg'
            let params = {
                sceneId: sceneId
            }
            axios({
                method: 'post',
                url: url,
                data: params,
                responseType: "arraybuffer"
            })
            .then((res) => {
                console.log(res);
                this.dialogShow.imgUrl = "data:image/jpeg;base64," + this.arrayBufferToBase64(res.data);
            });
        },
        arrayBufferToBase64(buffer) {
            //第一步，将ArrayBuffer转为二进制字符串
            var binary = "";
            var bytes = new Uint8Array(buffer);
            var len = bytes.byteLength;
            for (var i = 0; i < len; i++) {
                binary += String.fromCharCode(bytes[i]);
            }
            //将二进制字符串转为base64字符串
            return window.btoa(binary);
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