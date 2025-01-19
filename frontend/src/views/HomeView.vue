<template>
  <TodoComponent
    :todos="todos"
    @add-item="addItem"
    @update-item="updateItem"
    @delete-item="deleteItem"
    @delete-all="deleteAll"
  />
</template>

<script setup>
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'
import { onMounted, reactive } from 'vue'

const todos = reactive([])

onMounted(() => {
  if (localStorage.getItem('task')) Object.assign(todos, JSON.parse(localStorage.getItem('task')))
})
const addItem = (item) => {
  const task = { _id: todos.length + 1, task: item, done: false }
  todos.push(task)
  localStorage.setItem('task', JSON.stringify(todos))
  setTodos()
}
// const getTodos = () => {
//   todos.splice(0, todos.length)
//   const data = localStorage.getItem('task')
//   Object.assign(todos, JSON.parse(data))
// }
const setTodos = () => {
  localStorage.setItem('task', JSON.stringify(todos))
}
const updateItem = (payload) => {
  console.log(payload)
  setTodos()
}

const deleteItem = (id) => {
  const index = todos.findIndex((i) => i._id == id)
  todos.splice(index, 1)
  setTodos()
}

const deleteAll = (value) => {
  if (value) {
    todos.splice(0, todos.length)
    setTodos()
  }
}
</script>
