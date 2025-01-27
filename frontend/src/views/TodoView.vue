<template>
  <v-container class="text-center">
    <TodoComponent
      :todos="todos"
      @add-item="addItem"
      @update-item="updateItem"
      @delete-item="deleteItem"
      @delete-all="deleteAll"
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
const loged = ref(false)
const route = useRoute()

onMounted(() => {
  if (localStorage.getItem('token')) {
    todos.splice(0, todos.length)
    loged.value = true
    username.value = localStorage.getItem('username')
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
const addItem = async (item) => {
  try {
    const task = { task: item, done: false, todo_id: route.params.id }
    const res = await new_task(task)
    if (res.data) {
      getTodos()
    }
  } catch (error) {
    handleError(error)
  }
}
const getTodos = async () => {
  try {
    const res = await get_tasks(route.params.id)
    if (res.data && res.data.tasks) {
      todos.splice(0, todos.length, ...res.data.tasks)
    } else throw new Error('Error fetching data')
  } catch (error) {
    handleError(error)
  }
}
const setTodos = () => {
  localStorage.setItem('task', JSON.stringify(todos))
}
const updateItem = async (task) => {
  if (localStorage.getItem('token')) {
    try {
      const res = await update_task(task._id, { done: task.done })
      if (res.data) {
        console.log(res.data.msg)
        getTodos()
      }
    } catch (error) {
      handleError(error)
    }
  } else setTodos()
}

const deleteItem = async (id) => {
  if (localStorage.getItem('token')) {
    try {
      const res = await delete_task(id)
      if (res.data) {
        console.log(res.data.msg)
        getTodos()
      }
    } catch (error) {
      handleError(error)
    }
  } else {
    const index = todos.findIndex((i) => i._id == id)
    todos.splice(index, 1)
    setTodos()
  }
}

const deleteAll = async (value) => {
  if (localStorage.getItem('token')) {
    try {
      const res = await delete_all(route.params.id)
      if (res.data) {
        getTodos()
      }
    } catch (error) {
      handleError(error)
    }
  } else if (value) {
    todos.splice(0, todos.length)
    setTodos()
  }
}

const exclude = async () => {
  const res = await delete_todo(route.params.id)

  try {
    if (res.data) {
      console.log(res.data.msg)
      location.href = '/'
    }
  } catch (error) {
    handleError(error)
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
