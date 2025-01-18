<template>
  <v-container>
    <v-sheet width="400" class="ma-4 pa-2" rounded>
      <v-form @submit.prevent="onSubmit" v-model="form">
        <v-text-field label="login" v-model="loginForm.userLogin" :rules="[rules.required]">
        </v-text-field>

        <v-text-field
          v-model="loginForm.userPassword"
          :append-inner-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show ? 'text' : 'password'"
          hint="At least 8 characters"
          label="Normal with hint text"
          name="input-10-1"
          counter
          aria-required="true"
          @click:append-inner="show = !show"
        ></v-text-field>

        <v-btn color="success" size="large" type="submit" variant="elevated" block> Sign In </v-btn>
      </v-form>
    </v-sheet>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
const loginForm = ref({
  userLogin: '',
  userPassword: '',
})

const rules = ref({
  required: (value) => !!value || 'Required.',
  min: (v) => v.length >= 8 || 'Min 8 characters',
  loginMatch: () => `The email and password you entered don't match`,
})

const show = ref(false)
const form = ref(false)

const onSubmit = () => {
  if (!form.value) return

  location.href = '/home'
}
</script>
