<template>
  <div>
    <h1>Welcome! {{ username }}</h1>
  </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'

const username = ref('')

onMounted(() => {
  username.value = localStorage.getItem('username')
})
</script>
