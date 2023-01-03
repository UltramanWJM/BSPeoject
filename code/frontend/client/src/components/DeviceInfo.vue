<template>
    <div class="scenes">
        <h2 style="margin-top: -5px"><font color="white"> 设备管理界面 </font></h2>
        <el-row>
            <el-col :span="22" :push="0">
                <div>
                    <el-form :inline="true">
                        <el-form-item style="float: left" label="查询设备信息：" class="form">
                            <el-input v-model="searchSceneId" placeholder="查询设备ID"></el-input>
                        </el-form-item>
                        <el-form-item style="float: right">
                            <el-button type="primary" @click="handleAdd">创建设备</el-button>
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
                            label="设备ID"
                            align="center"
                            width="200"
                            prop="deviceId">
                        </el-table-column>
                        <el-table-column
                            label="设备名称"
                            align="center"
                            width="400"
                            prop="deviceName">
                        </el-table-column>
                        <el-table-column
                            label="设备类型"
                            width="400"
                            align="center"
                            prop="deviceType">
                        </el-table-column>
                        <el-table-column
                            label="所属场景ID"
                            align="center"
                            prop="sceneId">
                        </el-table-column>
                        <el-table-column fixed="right" label="操作" width="100">
                            <template slot-scope="scope">
                                <el-button type="text" size="small" @click="showScene(scope.$index, scope.row)">查看</el-button>
                                <el-button type="text" size="small" @click="deleteDevice(scope.$index, scope.row)">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-col>
        </el-row>
        <AddDevice :dialogAdd="dialogAdd" @update="getDevices"></AddDevice>
        <ShowScene :dialogShow="dialogShow" ref="DP"></ShowScene> 
    </div>
</template>

<script>
import axios from 'axios';
import AddDevice from './CreateDevice.vue'
import ShowScene from './ShowDevice.vue'
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
                show: false,
                scenes: []
            },
            dialogShow: {
                show: false,
                imgUrl: '',
                pX: '',
                pY: ''
            }
        }
    },
    components: {
        AddDevice,
        ShowScene
    },
    methods: {
        getDevices() {
            let url = 'http://127.0.0.1:5000/getdevices'
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
            this.getCreatedScenes();
            this.dialogAdd.show = true;
        },
        deleteDevice(index, row) {
            let params = {
                deviceId: row.deviceId
            };
            let url = "http://127.0.0.1:5000/deletedevice"
            axios.get(url, {params: params})
            .then((res) => {
                this.$message({
                message: res.data.msg,
                type: res.data.code == 1 ? 'success' : 'error'
                });
                this.getDevices()
            })
        },
        showScene(index, row) {
            this.getSceneImg(row.sceneId);
            this.dialogShow.show = true;
            this.getDevice(row.deviceId);
            // this.showDevPos(this.dialogShow.pX, this.dialogShow.pY)
            
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
        },
        getCreatedScenes() {
            let params = {
                userId: localStorage.getItem('id')
            };
            let url = 'http://127.0.0.1:5000/getcreatedscenes'
            axios.get(url, {params: params})
            .then((res) => {
                this.dialogAdd.scenes = res.data.data
            });
        },
        getDevice(deviceId) {
            let params = {
                deviceId: deviceId
            };
            let url = 'http://127.0.0.1:5000/getdevice'
            axios.get(url, {params: params})
            .then((res) => {
                this.dialogShow.pX = res.data.positionX;
                this.dialogShow.pY = res.data.positionY;
            })
        },
    //     showDevPos(x, y) {
    //         // var div = document.createElement('div');
    //         // div.className = 'marker';
    //         // div.id = 'marker0';
    //         let img = document.getElementById('devPos')
    //         let width = img.width;
    //         let height = img.height;

    //         var div = document.getElementById('mmark')
    //         x = x * width + document.getElementById('devPos').offsetLeft - 5;
    //         y = y * height + document.getElementById('devPos').offsetTop - 5;
    //         div.style.width = '10px';
    //         div.style.height = '10px';
    //         div.style.backgroundColor = 'red';
    //         div.style.left = x + 'px';
    //         div.style.top = y + 'px';
    //         // document.getElementById('biaozhuDiv').appendChild(div);
    //    }
    },
    mounted: function() {
        this.getDevices();
    }
}
</script>

<style>
.form .el-form-item__label{
    color: white;
}
/* .marker {
    position: absolute;
    z-index: 999;
    border-radius: 50%;
  } */
</style>