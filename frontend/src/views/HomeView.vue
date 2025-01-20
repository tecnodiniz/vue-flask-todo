<template>
  <v-container class="text-center">
    <h2>Welcome {{ username }}</h2>
    <LoginComponent v-if="!loged" @user-login="userLogin" />
    <v-btn v-if="loged" @click="logout"> Logout </v-btn>
    <TodoComponent
      :todos="todos"
      @add-item="addItem"
      @update-item="updateItem"
      @delete-item="deleteItem"
      @delete-all="deleteAll"
    />
  </v-container>

  <DialogComponent :msg="errorMessage" :dialog="dialog" @close="dialog = false" />
</template>

<script setup>
import LoginComponent from '@/components/LoginComponent.vue'
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'
import DialogComponent from '@/components/DialogComponent.vue'
import {
  delete_all,
  delete_task,
  get_tasks,
  get_user,
  new_task,
  update_task,
  user_login,
} from '@/services/api'
import { onMounted, reactive, ref } from 'vue'

const dialog = ref(false)
const todos = reactive([])
const username = ref('')
const loged = ref(false)
// const error = ref(false)
const errorMessage = ref('')

onMounted(() => {
  if (localStorage.getItem('token')) {
    loged.value = true
    username.value = localStorage.getItem('username')
    getTodos()
  } else if (localStorage.getItem('task'))
    todos.splice(0, todos.length, ...JSON.parse(localStorage.getItem('task')))
})
const addItem = (item) => {
  if (localStorage.getItem('token')) {
    const task = { task: item, done: false }
    new_task(task)
      .then((response) => {
        console.log(response.data)
        getTodos()
      })
      .catch((error) => {
        console.log(error)
      })
  } else {
    const task = { _id: todos.length + 1, task: item, done: false }
    todos.push(task)
    localStorage.setItem('task', JSON.stringify(todos))
    setTodos()
  }
}
const getTodos = () => {
  get_tasks()
    .then((response) => {
      todos.splice(0, todos.length, ...response.data.tasks)
    })
    .catch((error) => {
      console.log(error)
    })
}
const setTodos = () => {
  localStorage.setItem('task', JSON.stringify(todos))
}
const updateItem = (task) => {
  if (localStorage.getItem('token')) {
    update_task(task._id, { done: task.done })
      .then((response) => {
        console.log(response.data)
        getTodos()
      })
      .catch((error) => console.log(error))
  }
  setTodos()
}

const deleteItem = (id) => {
  if (localStorage.getItem('token')) {
    delete_task(id).then((response) => {
      console.log(response.data)
      getTodos()
    })
  } else {
    const index = todos.findIndex((i) => i._id == id)
    todos.splice(index, 1)
    setTodos()
  }
}

const deleteAll = (value) => {
  if (localStorage.getItem('token')) {
    delete_all()
      .then((response) => {
        console.log(response.data)
        getTodos()
      })
      .catch((error) => console.log(error))
  } else if (value) {
    todos.splice(0, todos.length)
    setTodos()
  }
}

const userLogin = (user) => {
  user_login(user)
    .then((response) => {
      const token = response.data.token
      localStorage.setItem('token', JSON.stringify(token))
      getUser(user.username)
    })
    .catch((error) => {
      if (error.message == 'Network Error') {
        errorMessage.value = error.message
        dialog.value = true
      } else console.log(error.message)
    })
}

const getUser = (login) => {
  get_user(login)
    .then((response) => {
      const username = response.data.user
      localStorage.setItem('username', username)
      location.reload()
    })
    .catch((error) => console.log(error.message))
}

const logout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('username')
  loged.value = false
  location.reload()
}
</script>
