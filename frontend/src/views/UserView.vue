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

    <div class="text-h6 ma-4">
      Welcome to your todo page <span class="green"> {{ username }}</span>
    </div>

    <div class="ma-4" v-if="!hasTodo">
      Tips: Click on blue
      <v-btn class="ma-4" icon="mdi-plus" color="indigo" size="40" @click="dialog = true"></v-btn>
      to create a todo list
    </div>
    <div class="ma-4" v-else>Tips: Double click on list name to edit</div>

    <TodoDataIteratorComponent
      :todos="userInfo.info.todo"
      @delete-confirm="deleteTodo"
      @update-todo="updateTodo"
    />
  </v-container>

  <DialogComponent :msg="dialogTitle" :text="dialogText" :dialog="erro" @close="logout" />
</template>

<script setup>
import TodoDataIteratorComponent from '@/components/TodoDataIteratorComponent.vue'
import DialogComponent from '@/components/DialogComponent.vue'
import TodoForm from '@/components/TodoForm.vue'

import { get_user_info, create_todo, delete_todo, update_todo, user_logout } from '@/services/api'
import { computed, onMounted, ref } from 'vue'

const userInfo = ref({ info: {} })
const username = computed(() => localStorage.getItem('username') || '')

const hasTodo = computed(() => !!userInfo.value.info.todo?.length)
const dialog = ref(false)
const erro = ref(false)
const dialogTitle = ref('')
const dialogText = ref('')
onMounted(() => handleAuth())

const getToken = () => localStorage.getItem('token')
const redirectToHome = () => (window.location.href = '/')

const handleAuth = () => {
  const token = getToken()
  return token ? getUserInfo() : redirectToHome()
}

const getUserInfo = () => {
  get_user_info()
    .then((response) => {
      userInfo.value = { ...response.data }
    })
    .catch((error) => handleError(error))
}

const createTodo = (todo) => {
  console.log(todo)
  create_todo(todo)
    .then(() => {
      getUserInfo()
      dialog.value = false
    })
    .catch((error) => handleError(error))
}

const updateTodo = (todo) => {
  update_todo(todo.id, { name: todo.name })
    .then(() => getUserInfo())
    .catch((error) => handleError(error))
}
const deleteTodo = (id) => {
  delete_todo(id)
    .then(() => getUserInfo())
    .catch((error) => handleError(error))
}

const sessionExpired = () => {
  console.warn('Error 401: UNAUTHORIZED')
  dialogTitle.value = 'Session Expired'
  dialogText.value = 'Your session has been expired, please login again'
  erro.value = true
}

const logout = () => {
  user_logout({})
  localStorage.removeItem('token')
  localStorage.removeItem('username')

  location.href = '/'
}

const handleError = (error) => {
  const { response } = error
  if (response && response.status === 401) {
    sessionExpired()
    console.log(response.data.msg)
  } else {
    console.log(error.message)
    dialogTitle.value = 'Something got wrong'
    erro.value = true
  }
}
</script>
