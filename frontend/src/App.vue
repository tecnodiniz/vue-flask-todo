<template>
  <v-layout>
    <v-app-bar prominent>
      <v-toolbar-title>Your Todo List</v-toolbar-title>
      <v-spacer></v-spacer>

      <LoginComponent v-if="!loged" @user-login="userLogin">
        <template v-if="errorMessage"
          ><small class="text-caption text-red-lighten-1">{{ errorMessage }}</small>
        </template>
      </LoginComponent>

      <v-btn v-else @click="drawerR = !drawerR" icon="mdi-dots-vertical"></v-btn>
    </v-app-bar>

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
        <v-list-item prepend-icon="mdi-home-city" title="Home" value="home" to="/user-info">
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block append-icon="mdi-logout" @click="logout"> Logout </v-btn>
        </div>

        <v-divider></v-divider>
        <v-spacer></v-spacer>

        <div class="text-center ma-2 pa-2">
          <span class="green">v 1.0.0</span>
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
import DialogComponent from './components/DialogComponent.vue'
import LoginComponent from './components/LoginComponent.vue'

import { ref, computed } from 'vue'
import { user_logout, get_user, user_login } from './services/api'

const token = ref(localStorage.getItem('token'))
const loged = computed(() => !!token.value)
const username = computed(() => localStorage.getItem('username') || '')

const drawerR = ref(false)

const dialogTitle = ref('')
const dialogText = ref('')
const dialog = ref(false)
const errorMessage = ref('')

const userLogin = (user) => {
  user_login(user)
    .then((resposne) => {
      localStorage.setItem('token', JSON.stringify(resposne.data.token))
      getUser(user.username)
    })
    .catch((error) => {
      console.log(error?.response.data.msg)
      errorMessage.value = 'Invalid credentials'
    })
}

const getUser = (login) => {
  get_user(login)
    .then((response) => {
      localStorage.setItem('username', response.data.user)
      location.href = '/welcome'
    })
    .catch((error) => {
      errorHandler(error)
      dialogTitle.value = 'Something got wrong'
      dialog.value = true
      console.log(error.message)
    })
}

const logout = () => {
  user_logout({})
    .then((response) => console.log(response.data))
    .catch((error) => errorHandler(error))
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

const errorHandler = (error) => {
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
