<template>
  <v-container>
    <div>Welcome to your info page {{ username }}</div>
  </v-container>
</template>

<script setup>
import { get_user_info } from '@/services/api'
import { onMounted, ref } from 'vue'
const userInfo = ref({
  info: {},
})

const username = ref('')

onMounted(() => {
  if (localStorage.getItem('token')) {
    getUserInfo()
    console.log(userInfo.value)
  } else location.href = '/'
})

const getUserInfo = async () => {
  try {
    const res = await get_user_info()
    if (res && res.data) {
      userInfo.value.info = res.data.info
      username.value = userInfo.value.info.user.name
    }
  } catch (erro) {
    console.log(erro.message)
  }
}
</script>
