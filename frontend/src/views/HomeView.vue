<template>
  <v-container class="text-center">
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
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'
import DialogComponent from '@/components/DialogComponent.vue'
import { user_logout } from '@/services/api'
import { onMounted, reactive, ref } from 'vue'

const dialog = ref(false)
const dialogTitle = ref('')
const dialogText = ref('')
const todos = reactive([])

const loged = ref(false)

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
