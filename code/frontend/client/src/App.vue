<template>
  <div id="app">
    <div>
      <myHeader></myHeader>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import myHeader from '@/components/myHeader'
export default {
  name: 'App',
  components: {
    'myHeader': myHeader
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
  height: 950px;
}
</style>
