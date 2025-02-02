<template>
  <v-container class="text-center">
    <TodoComponent
      :todos="todos"
      @add-item="addItem"
      @update-item="updateItem"
      @delete-item="deleteItem"
      @clearList="deleteAll"
    />
    <DialogExludeComponent @delete-confirm="exclude" />
  </v-container>

  <DialogComponent :msg="dialogTitle" :text="dialogText" :dialog="dialog" @close="logout" />
</template>

<script setup>
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'
import DialogComponent from '@/components/DialogComponent.vue'
import DialogExludeComponent from '@/components/DialogExludeComponent.vue'
import {
  delete_all,
  delete_task,
  get_tasks,
  update_task,
  user_logout,
  new_task,
  delete_todo,
} from '@/services/api'
import { onMounted, onUpdated, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'

const dialog = ref(false)
const dialogTitle = ref('')
const dialogText = ref('')
const todos = reactive([])
const username = ref('')
const route = useRoute()

onMounted(() => {
  if (localStorage.getItem('token')) {
    todos.splice(0, todos.length)
    getTodos()
  } else {
    location.href = '/'
  }
})
onUpdated(() => {
  if (localStorage.getItem('token')) {
    todos.splice(0, todos.length)
    username.value = localStorage.getItem('username')
    getTodos()
  } else {
    location.href = '/'
  }
})
const addItem = (item) => {
  const task = { task: item, done: false, todo_id: route.params.id }
  new_task(task)
    .then(() => getTodos())
    .catch((error) => handleError(error))
}
const getTodos = () => {
  get_tasks(route.params.id)
    .then((response) => {
      todos.splice(0, todos.length, ...response.data.tasks)
    })
    .catch((error) => handleError(error))
}

const updateItem = (task) => {
  update_task(task._id, { done: task.done })
    .then(() => getTodos())
    .catch((error) => handleError(error))
}

const deleteItem = (id) => {
  delete_task(id)
    .then(() => getTodos())
    .catch((error) => handleError(error))
}

const deleteAll = () => {
  delete_all(route.params.id)
    .then(() => getTodos())
    .catch((error) => handleError(error))
}

const exclude = () => {
  delete_todo(route.params.id)
    .then(() => (window.location.href = '/user-info'))
    .catch((error) => handleError(error))
}

const logout = () => {
  user_logout({})
  localStorage.removeItem('token')
  localStorage.removeItem('username')

  location.href = '/'
}

const sessionExpired = () => {
  console.warn('Error 401: UNAUTHORIZED')
  dialogTitle.value = 'Session Expired'
  dialogText.value = 'Your session has been expired, please login again'
  dialog.value = true
}

const handleError = (error) => {
  const { response } = error
  if (response && response.status === 401) {
    sessionExpired()
    console.log(response.data.msg)
  } else {
    console.log(error.message)
    dialogTitle.value = 'Something got wrong'
    dialog.value = true
  }
}
</script>
