<template>
    <el-dialog title="场景图片" :visible.sync="dialogShow.show" v-if="dialogShow.show">
        <div>
            <el-image :src="dialogShow.imgUrl" style="width: 100%;" id="devPos"/>
            <div id="mmark"></div>
            <el-button tyoe="success" @click="showDevPos">flash</el-button>
        </div>
    </el-dialog>    
</template>

<script>
import axios from 'axios'
export default {
    name: 'showScene',
    data() {
        return {
            imgUrl: ''
        }
    },
    props: {
        dialogShow: Object
    },
    methods: {
        showDevPos() {
            // var div = document.createElement('div');
            // div.className = 'marker'
            // div.id = 'marker0'
            let img = document.getElementById('devPos')
            let width = img.width;
            let height = img.height;
            console.log(width, height)
            var div = document.getElementById('mmark')
            let x = this.dialogShow.pX * width + document.getElementById('devPos').offsetLeft - 5;
            let y = this.dialogShow.pY * height + document.getElementById('devPos').offsetTop - 5;
            div.style.width = '10px';
            div.style.height = '10px';
            div.style.backgroundColor = 'red';
            div.style.left = x + 'px';
            div.style.top = y + 'px';
            // document.getElementById('biaozhuDiv').appendChild(div);
       }
    }
}
</script>

<style>
#mmark {
    position: absolute;
    border-radius: 50%;
    z-index: 999;
}
</style>