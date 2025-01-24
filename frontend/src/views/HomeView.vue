<template>
  <v-container class="text-center">
    <LoginComponent v-if="!loged" @user-login="userLogin">
      <template v-if="errorMessage"
        ><small class="text-caption text-red-lighten-1">{{ errorMessage }}</small>
      </template>
    </LoginComponent>
    <v-btn v-if="loged" @click="logout"> Logout </v-btn>
    <TodoComponent
      :todos="todos"
      @add-item="addItem"
      @update-item="updateItem"
      @delete-item="deleteItem"
      @delete-all="deleteAll"
    />
  </v-container>

  <DialogComponent :msg="dialogTitle" :text="dialogText" :dialog="dialog" @close="logout" />
</template>

<script setup>
import LoginComponent from '@/components/LoginComponent.vue'
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'
import DialogComponent from '@/components/DialogComponent.vue'
import { user_login, get_user, user_logout } from '@/services/api'
import { onMounted, reactive, ref } from 'vue'

const dialog = ref(false)
const dialogTitle = ref('')
const dialogText = ref('')
const todos = reactive([])

const loged = ref(false)
const errorMessage = ref('')

onMounted(() => {
  if (localStorage.getItem('token')) loged.value = true
  if (localStorage.getItem('task'))
    todos.splice(0, todos.length, ...JSON.parse(localStorage.getItem('task')))
})
const addItem = async (item) => {
  const task = { _id: todos.length + 1, task: item, done: false }
  todos.push(task)
  localStorage.setItem('task', JSON.stringify(todos))
  setTodos()
}

const setTodos = () => {
  localStorage.setItem('task', JSON.stringify(todos))
}
const updateItem = async () => {
  setTodos()
}

const deleteItem = async (id) => {
  const index = todos.findIndex((i) => i._id == id)
  todos.splice(index, 1)
  setTodos()
}

const deleteAll = async (value) => {
  if (value) {
    todos.splice(0, todos.length)
    setTodos()
  }
}

const userLogin = async (user) => {
  try {
    const res = await user_login(user)

    if (res.data && res.data.token) {
      const token = res.data.token
      localStorage.setItem('token', JSON.stringify(token))
      getUser(user.username)
    } else throw new Error('Token not found')
    return user
  } catch (error) {
    const { response } = error
    if (error.response && error.response.status === 401) {
      console.warn('Error 401: UNAUTHORIZED')
      errorMessage.value = response.data.msg
    } else {
      console.log(error.message)
      dialogTitle.value = 'Something got wrong'
      dialog.value = true
    }
  }
}

const getUser = async (login) => {
  try {
    const res = await get_user(login)
    if (res.data && res.data.user) {
      localStorage.setItem('username', res.data.user)
      location.href = '/welcome'
    } else throw new Error('User not found')
  } catch (error) {
    dialogTitle.value = 'Something got wrong'
    dialog.value = true
    console.log(error.message)
  }
}

const logout = async () => {
  try {
    const res = await user_logout({})
    if (res.data) {
      console.log('logout')
    } else throw new Error('Erro')
  } catch (error) {
    console.log(error.message)
  }
  localStorage.removeItem('token')
  localStorage.removeItem('username')
  loged.value = false
  location.reload()
}
</script>
