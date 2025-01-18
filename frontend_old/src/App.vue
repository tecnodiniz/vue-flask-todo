<template>
  <BaseComponent/>
</template>

<script>

import BaseComponent from './components/BaseComponent.vue';

export default {
  name:'App',
  components:{
    BaseComponent,
  }
}
</script>
<style>
body{
 background: linear-gradient(45deg, #002135, #4682B4);
    background-color: rgba(0, 0, 0, 0);
  height: 100vh;
;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

ul{
  padding: 15px;
}
.card{
  margin: 0 auto;
  padding: 25px;
}
.card .card-body{
  height: 200px;
  overflow: auto;
}
.card .card-footer .footer-content{
  display: flex;
  justify-content: space-between;
  
}
.card .card-footer .footer-content a{
  text-decoration: none;
  color: #6c757d;
}

</style>
