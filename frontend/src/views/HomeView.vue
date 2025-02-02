<template>
  <v-container class="text-center">
    <TodoComponent
      :todos="todos"
      @add-item="addItem"
      @update-item="updateItem"
      @delete-item="deleteItem"
      @clearList="clear"
    />
  </v-container>
</template>

<script setup>
import TodoComponent from '@/components/CardComponent/TodoComponent.vue'

import { onMounted, ref } from 'vue'

const todos = ref([])

onMounted(() => {
  const storedTasks = localStorage.getItem('task')
  todos.value = storedTasks ? JSON.parse(storedTasks) : []
})

const updateTasks = (newTask) => {
  todos.value = newTask
  localStorage.setItem('task', JSON.stringify(newTask))
}
const updateItem = () => {
  updateTasks(todos.value)
}

const addItem = (item) => {
  const task = { _id: crypto.randomUUID(), task: item, done: false }
  updateTasks([...todos.value, task])
}

const deleteItem = (id) => updateTasks(todos.value.filter((i) => i._id !== id))

const clear = () => updateTasks([])
</script>
