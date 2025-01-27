<template>
  <v-layout>
    <v-app-bar prominent>
      <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Your Todo List</v-toolbar-title>
      <v-spacer></v-spacer>

      <LoginComponent v-if="!loged" @user-login="userLogin">
        <template v-if="errorMessage"
          ><small class="text-caption text-red-lighten-1">{{ errorMessage }}</small>
        </template>
      </LoginComponent>

      <v-btn v-else @click="drawerR = !drawerR" icon="mdi-dots-vertical"></v-btn>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      :location="$vuetify.display.mobile ? 'bottom' : undefined"
    >
      <!-- Add New Todo -->

      <v-list>
        <div v-if="token">
          <TodoForm @new-todo="createTodo" />

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

    <v-navigation-drawer location="right" v-model="drawerR">
      <template v-slot:prepend>
        <v-list-item
          lines="two"
          prepend-avatar="https://thumbs.dreamstime.com/b/default-avatar-profile-icon-vector-social-media-user-portrait-176256935.jpg"
          subtitle="Logged in"
          :title="username"
        ></v-list-item>
      </template>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item prepend-icon="mdi-home-city" title="Home" value="home" to="/user">
        </v-list-item>

        <v-list-item prepend-icon="mdi-account" title="My Account" value="account"></v-list-item>
        <v-list-item
          prepend-icon="mdi-account-group-outline"
          title="Users"
          value="users"
        ></v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block append-icon="mdi-logout" @click="logout"> Logout </v-btn>
        </div>
      </template>
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
import {
  create_todo,
  get_todos,
  update_todo,
  user_logout,
  get_user,
  user_login,
} from './services/api'
import TodoForm from './components/TodoForm.vue'
import LoginComponent from './components/LoginComponent.vue'
const token = ref('')
const todos = ref([])
const drawer = ref(false)
const drawerR = ref(false)
const dialogTitle = ref('')
const dialogText = ref('')
const dialog = ref(false)
const editingIndex = ref(null)
const errorMessage = ref('')
const loged = ref(false)
const username = ref('')
onMounted(() => {
  token.value = localStorage.getItem('token')

  if (token.value) {
    getTodos()
    loged.value = true
    username.value = localStorage.getItem('username')
  }
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
