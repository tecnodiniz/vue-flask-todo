<template>
  <TodoComponent
    @add-item="addItem"
    :todos="todos"
    @update-item="updateItem"
    @delete-item="deleteItem"
  />
</template>

<script setup>
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'
import { reactive } from 'vue'

const todos = reactive([])

const addItem = (item) => {
  const task = { _id: todos.length + 1, task: item, done: false }
  todos.push(task)
}

const updateItem = (payload) => {
  console.log(payload)
  console.log(todos)
}

const deleteItem = (id) => {
  const index = todos.findIndex((i) => i._id == id)
  todos.splice(index, 1)
}
</script>
