<template>
    <el-dialog title="场景图片" :visible.sync="dialogShow.show">
        <img :src="dialogShow.imgUrl" style="width: 100%;" />
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
        getSceneImg() {
            let url = 'http://127.0.0.1:5000/getsceneimg'
            let params = {
                sceneId: this.dialogShow.sceneId
            }
            axios.get(url, {params: params}, {responsetype: "arraybuffer"})
            .then((res) => {
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
        }
    }
}
</script>