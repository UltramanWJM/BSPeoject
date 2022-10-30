<template>
  <div class="page">
    <div class="nav">
      <div v-for="(item,index) in navList" :key="index" :class="index == active?'active':''" @mousemove="active = index" @mouseout="active = null" >
      {{ item.name }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.nav {
  width: 100%;
  display: flex;
  justify-content: space-around;
  z-index: 9;
  position: absolute;
  top: 20px;
  font-size: 20px;
  cursor: pointer;
}
.nav div {
  width: 150px;
  text-align: center;
  line-height: 50px;
}

.page {
  background-color: #606060;
}
</style>

<script>
export default {
  name: 'myHeader',
  data() {
    return {
      active: null,
      navList: [
        {name: '首页'},
        {name: '使用帮助'},
        {name: '联系我们'}
      ]
    }
  }
}
</script>
