<template>
    <div class="scenes">
        <h2 style="margin-top: -5px"><font color="white"> 设备信息界面 —— 门锁 </font></h2>
        <el-row>
            <el-col :span="22" :push="0">
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
                            width="100"
                            prop="deviceId">
                        </el-table-column>
                        <el-table-column
                            label="设备名称"
                            align="center"
                            width="400"
                            prop="deviceName">
                        </el-table-column>
                        <el-table-column
                            label="设备状态"
                            align="center"
                            width="200"
                            prop="status">
                        </el-table-column>
                        <el-table-column
                            label="最近更新时间"
                            align="center"
                            width="400"
                            prop="updateTime">
                        </el-table-column>
                        <el-table-column fixed="right" label="操作" width="150">
                            <template slot-scope="scope">
                                <el-button type="text" size="small" @click="TrunOnorOff(scope.$index, scope.row)">开关</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </div>
            </el-col>
        </el-row>
        <!-- <LampInfo :dialogLampInfo="dialogLampInfo"></LampInfo>  -->
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'SceneInfo',
    data() {
        return {
            tableData: [],
            userId: '',
            username: '',
            phone: '',
            searchSceneId: '',
        }
    },
    methods: {
        getLockes() {
            let url = 'http://127.0.0.1:5000/getlockes'
            let params = {
                userId: localStorage.getItem('id')
            }
            axios.get(url, {params: params})
            .then((res) => {
                console.log(res.data)
                this.tableData = res.data.data
                console.log(this.tableData)
            });
        },
        TrunOnorOff(index, row) {
            let url = 'http://127.0.0.1:5000/modlockstatus'
            let params = {
                deviceId: row.deviceId
            }
            axios.get(url, {params: params})
            .then((res) => {
                this.$message({
                        message: res.data.msg,
                        type: res.data.code == 1 ? 'success' : 'error'
                    });
            })
        }
    },
    mounted: function() {
        this.getLockes();
    }
}
</script>

<style>
.form .el-form-item__label{
    color: white;
}
</style>