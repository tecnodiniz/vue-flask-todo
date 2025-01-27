<template>
  <v-container>
    <v-sheet class="ma-10">
      <v-fab
        class="ms-4"
        color="indigo"
        icon="mdi-plus"
        location="top right"
        size="40"
        absolute
        offset
        @click="dialog = !dialog"
      ></v-fab>
    </v-sheet>

    <TodoForm v-model:dialog="dialog" @close="dialog = false" @new-todo="createTodo" />

    <div class="text-h6 ma-4">  Welcome to your todo page <span class="green"> {{ username }}</span> </div>

    {{  }}
    <div class="ma-4" v-if="count === 0">Tips: Click on blue  <v-btn class="ma-4" icon="mdi-plus" color="indigo" size="40" @click="dialog = !dialog"></v-btn> to create a todo list</div>
    <div class="ma-4" v-else>Tips: Double click on list name to edit  </div>


    <TodoDataIteratorComponent
      :todos="userInfo.info.todo"
      @delete-confirm="deleteTodo"
      @update-todo="updateTodo"
    />
  </v-container>
</template>

<script setup>
import TodoDataIteratorComponent from '@/components/TodoDataIteratorComponent.vue'
import TodoForm from '@/components/TodoForm.vue'

import { get_user_info, create_todo, delete_todo, update_todo } from '@/services/api'
import { onMounted, ref } from 'vue'
const userInfo = ref({
  info: {},
})

const count = ref(0)
const dialog = ref(false)
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
      count.value = userInfo.value.info.todo.length
    }
  } catch (erro) {
    console.log(erro.message)
  }
}

const createTodo = async (todo) => {
  try {
    const res = await create_todo(todo)
    if (res.data) {
      console.log(res.data)
      dialog.value = false
      getUserInfo()
    } else console.log(res.data)
  } catch (error) {
    console.log(error)
  }
}

const updateTodo = async (todo) => {
  try {
    console.log(todo)
    const res = await update_todo(todo.id, { name: todo.name })
    if (res.data) {
      console.log(res.data)
      getUserInfo()
    } else return
  } catch (error) {
    console.log(error)
  }
}
const deleteTodo = async (id) => {
  try {
    const res = await delete_todo(id)
    if (res.data) {
      console.log(res.data)
      getUserInfo()
    }
  } catch (error) {
    console.log(error)
  }
}
</script>
