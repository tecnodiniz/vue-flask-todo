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
      <!-- Add New Todo -->

      <v-list>
        <div v-if="token">
          <TodoForm @new-todo="createTodo" />
          <v-list-item>
            <RouterLink to="/user">Home</RouterLink>
          </v-list-item>

          <v-list-item v-for="(i, index) in todos" :key="i._id" @dblclick="editItem(index)">
            <template v-if="editingIndex === index">
              <v-text-field
                v-model="i.name"
                @blur="saveItem(i.name, i._id)"
                @keydown.enter="saveItem(i.name, i._id)"
                label="Editar"
                dense
                autofocus
              ></v-text-field>
            </template>

            <template v-else>
              <RouterLink :to="`/todo/${i._id}`">{{ i.name }}</RouterLink>
            </template>
          </v-list-item>
        </div>

        <v-list-item v-else> Todo </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <RouterView />
      <DialogComponent :msg="dialogTitle" :text="dialogText" :dialog="dialog" @close="logout" />
    </v-main>
  </v-layout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import DialogComponent from './components/DialogComponent.vue'
import { create_todo, get_todos, update_todo, user_logout } from './services/api'
import TodoForm from './components/TodoForm.vue'
const token = ref('')
const todos = ref([])
const drawer = ref(false)
const dialogTitle = ref('')
const dialogText = ref('')
const dialog = ref(false)
const editingIndex = ref(null)
onMounted(() => {
  token.value = localStorage.getItem('token')

  if (token.value) getTodos()
})

const getTodos = async () => {
  try {
    const res = await get_todos()

    if (res && res.data) {
      todos.value.splice(0, todos.value.length, ...res.data.todos)
    }
  } catch (error) {
    handleError(error)
  }
}

const createTodo = async (todo) => {
  try {
    const res = await create_todo(todo)
    if (res.data) {
      console.log(res.data)
      getTodos()
    } else console.log(res.data)
  } catch (error) {
    handleError(error)
  }
}

const editItem = (index) => {
  editingIndex.value = index
}

const saveItem = async (name, id) => {
  try {
    if (name.trim() !== '') {
      const payload = { name: name }
      const res = await update_todo(id, payload)
      if (res.data) {
        console.log(res.data)
        getTodos()
        editingIndex.value = null
      } else return
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
