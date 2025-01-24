<template>
  <v-layout>
    <v-app-bar prominent>
      <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Your Todo List</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      :location="$vuetify.display.mobile ? 'bottom' : undefined"
    >
      <v-list>
        <v-list-item v-if="!todos">
          <RouterLink to="/">Home</RouterLink>
        </v-list-item>

        <v-list-item v-if="todos">
          <RouterLink to="/user">Home</RouterLink>
        </v-list-item>

        <div v-if="todos">
          <v-list-item v-for="(i, index) in todos" :key="index">
            <RouterLink :to="`/todo/${i._id}`">{{ i.name }}</RouterLink>
          </v-list-item>
        </div>

        <v-list-item v-if="!todos">
          <RouterLink>Todo</RouterLink>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <RouterView />
    </v-main>
  </v-layout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { get_todos } from './services/api'
const token = ref('')
const todos = ref([])
const drawer = ref(false)
onMounted(() => {
  token.value = localStorage.getItem('token')

  if (token.value) getTodos()
})

const getTodos = async () => {
  try {
    const res = await get_todos()

    if (res && res.data) {
      todos.value.push(...res.data.todos)
    }
  } catch (erro) {
    console.log(erro)
  }
}
</script>
