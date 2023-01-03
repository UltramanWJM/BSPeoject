<template>
    <div class="addDevice">
      <el-dialog title="创建设备" :visible.sync="dialogAdd.show">
        <el-form :model="formData" ref="ruleF" label-width="100px" :rules="formRules">
          <el-form-item label="设备ID" prop="newDeviceId">
            <el-input v-model="formData.newDeviceId"></el-input>
          </el-form-item>
          <el-form-item label="设备名称" prop="newDeviceName">
            <el-input v-model="formData.newDeviceName"></el-input>
          </el-form-item>
          <el-form-item label="设备类型" prop="newDeviceType">
            <el-select
                v-model="formData.newDeviceType"
                placeholder="请选择"
                clearable
                filterable
                @blur="selectTypeBlur"
                @clear="selectTypeClear"
                @change="selectTypeChange"
                >
                <el-option
                    v-for="(item, index) in deviceTypes"
                    :key="index"
                    :label="item.label"
                    :value="item.value" />
            </el-select>
          </el-form-item>
          <el-form-item label="所在场景" prop="newDeviceScene">
            <el-select
                v-model="formData.newDeviceScene"
                placeholder="请选择"
                clearable
                filterable
                @blur="selectSceneBlur"
                @clear="selectSceneClear"
                @change="selectSceneChange"
                >
                <el-option
                    v-for="(item, index) in dialogAdd.scenes"
                    :key="index"
                    :label="item.label"
                    :value="item.value" />
            </el-select>
          </el-form-item>
          <el-form-item label="选择位置" prop="newDeviceP">
            <div id="biaozhuDiv">
                <el-image :src="imgUrl" style="width:100%" alt="" id="biaozhu" @mousedown="getXY" ></el-image>
                <h3>横向占比：{{formData.newDevicePX}}</h3>
                <h3>纵向占比：{{formData.newDevicePY}}</h3>
                <div id="mark"></div>
            </div>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogAdd.show = false">取 消</el-button>
          <el-button type="primary" @click="submitForm('ruleF')">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </template>
  
  <script>
import axios from 'axios'

  export default {
    name: 'AddDevice',
    props:{
      dialogAdd:Object
    },
    data () {
      return {
        formData:{
            newDeviceId: '',
            newDeviceName: '',
            newDeviceType: '',
            newDeviceScene: '',
            newDevicePX: '',
            newDevicePY: ''
        },
        formRules:{
            newDeviceId:[{required:true, message:"设备ID不能为空", trigger:"blur"}],
            newDeviceName:[{required:true, message:"设备名称不能为空", trigger:"blur"}],
            newDeviceType:[{required:true, message:"设备类型不能为空", trigger:"blur"}],
            newDeviceScene:[{required:true, message:"设备所属场景不能为空", trigger:"blur"}]
        },
        imgUrl: '',
        dialogVisible: false,
        deviceTypes: [
            {
                value: 0,
                label: '灯'
            },
            {
                value: 1,
                label: '开关'
            },
            {
                value: 2,
                label: '传感器'
            },
            {
                value: 3,
                label: '门锁'
            }
        ],
        scenes: [],
        pointColor: 'red',
        banma: [],
        pointSize: 10,
        canBiaoZhu: false
      }
    },
    methods:{
      submitForm(formName) {
        let formData = this.formData
        formData.userId = localStorage.getItem('id')
        this.$refs[formName].validate((valid) => {
            if (valid) {
                let url = 'http://localhost:5000/createdevice'
                axios.post(url, formData)
                .then((res) => {
                    this.$message({
                        message: res.data.msg,
                        type: res.data.code == 1 ? 'success' : 'error'
                    });
                    if (res.data.code == 1) {
                        this.dialogAdd.show = false;
                        this.resetForm(formName);
                        this.$emit('update');
                    }
                    
                })
            }
        })
        console.log(this.formData);
      },
      selectTypeBlur(e) {
        if (e.target.value !== '') {
        //   this.value = e.target.value + '(其他)';
          this.$forceUpdate()   // 强制更新
        }
      },
      selectTypeClear() {
        // this.value = '';
        this.$forceUpdate();
      },
      selectTypeChange(val) {
        // this.value = val;
        console.log(val)
        this.$forceUpdate();
      },
      selectSceneBlur(e) {
        if (e.target.value !== '') {
        //   this.value = e.target.value + '(其他)';
          this.$forceUpdate()   // 强制更新
        }
      },
      selectSceneClear() {
        // this.value = '';
        this.$forceUpdate();
      },
      selectSceneChange(val) {
        // this.value = val;
        this.getSceneImg(val);
        this.$forceUpdate();
      },
      getCreatedScenes() {
        let params = {
            userId: localStorage.getItem('id')
        };
        let url = 'http://127.0.0.1:5000/getcreatedscenes'
        axios.get(url, {params: params})
        .then((res) => {
            this.scenes = res.data.data
        });
        console.log(this.scenes)
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
                this.imgUrl = "data:image/jpeg;base64," + this.arrayBufferToBase64(res.data);
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
       getXY(event) {
            // console.log(event.offsetX, event.offsetY)
            this.formData.newDevicePX = event.offsetX;
            this.formData.newDevicePY = event.offsetY;
            var img = document.getElementById('biaozhu');
            let width = img.width;
            let height = img.height;
            console.log(width, height);
            this.formData.newDevicePX = event.offsetX / width;
            this.formData.newDevicePY = event.offsetY / height;
            console.log(this.formData.newDevicePX, this.formData.newDevicePY)
            this.createMarker(event.offsetX, event.offsetY);
       },
       createMarker(x, y) {
        // var div = document.createElement('div');
        // div.className = 'marker'
        // div.id = 'marker0'
        var div = document.getElementById('mark')
        x = x + document.getElementById('biaozhu').offsetLeft - this.pointSize/2;
        y = y + document.getElementById('biaozhu').offsetTop - this.pointSize/2;
        div.style.width = this.pointSize + 'px';
        div.style.height = this.pointSize + 'px';
        div.style.backgroundColor = this.pointColor;
        div.style.left = x + 'px';
        div.style.top = y + 'px';
        // document.getElementById('biaozhuDiv').appendChild(div);
       }
    },
    mounted: function() {
        
    }   
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style>
#mark {
    position: absolute;
    border-radius: 50%;
    z-index: 999;
}
  </style>