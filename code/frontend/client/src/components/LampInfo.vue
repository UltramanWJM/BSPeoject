<template>
    <div class="LampInfo">
      <el-dialog title="灯具详细信息" :visible.sync="dialogLampinfo.show">
        <el-form :model="formData" ref="ruleF" label-width="100px" :rules="formRules">
          <el-form-item label="设备ID" prop="newSceneId">
            <el-input v-model="dialogLampinfo.deviceId"></el-input>
          </el-form-item>
          <el-form-item label="设备名称" prop="newSceneName">
            <el-input v-model="dialogLampinfo.deviceName"></el-input>
          </el-form-item>
          <el-form-item label="亮度" prop="newSceneName">
            <el-input v-model="formData.newSceneName"></el-input>
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
    name: 'AddScene',
    props:{
      dialogAdd:Object
    },
    data () {
      return {
        formData:{
            newSceneId: '',
            newSceneName: '',
            image: ''
        },
        formRules:{
            newSceneId:[{required:true, message:"场景ID不能为空", trigger:"blur"}],
            newSceneName:[{required:true, message:"场景名称不能为空", trigger:"blur"}],
        },
        dialogImgUrl: '',
        dialogVisible: false,
        fileList: [],
      }
    },
    methods:{
      submitForm(formName) {
        let formData = this.formData
        formData.userId = localStorage.getItem('id')
        this.$refs[formName].validate((valid) => {
            if (valid) {
                let url = 'http://localhost:5000/createscene'
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
      },
      UploadImg(file, fileList) {
        let fd = new FormData()
        fd.append('file', file.raw)
        let url = 'http://localhost:5000/storeimg'
        axios.post(url, fd, {headers: {'Content-Type': 'multipart/form-data'}})
        .then((res) => {
            console.log("上传图片" + res.data)
            this.formData.image = res.data
        })
      },
      handleRemove(file, fileList) {
        console.log(file, fileList)
      },
      handleImgPreview(file) {
        console.log(file.url)
        this.dialogVisible = true
        this.dialogImgUrl = file.url
      },
      resetForm(formName) {
        this.$refs.upload.clearFiles()
        this.$refs[formName].resetFields()
      }

    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>