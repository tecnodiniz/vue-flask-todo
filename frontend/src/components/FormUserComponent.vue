<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-account"
        text="Create Account"
        variant="plain"
        v-bind="activatorProps"
      ></v-btn>
    </template>

    <v-card prepend-icon="mdi-account" title="User Login">
      <v-card-text>
        <v-form v-model="form.valid">
          <v-row dense>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.username"
                hint="User Name"
                label="User Name*"
                required
                :rules="[form.rule.nameRules]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.login"
                hint="User login"
                label="Login*"
                required
                :rules="[form.rule.loginRules]"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.password"
                label="Password*"
                type="password"
                required
                :rules="[form.rule.pwdRules]"
                @keyup.enter="emitUser"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
        <slot></slot>

        <small class="text-caption text-medium-emphasis">*indicates required field</small>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

        <v-btn
          :disabled="!form.valid"
          color="primary"
          text="Sign in"
          variant="tonal"
          @click="emitUser"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref } from 'vue'
const dialog = ref(false)

const emit = defineEmits(['new-user'])
const form = ref({
  valid: false,
  username: '',
  login: '',
  password: '',
  rule: {
    nameRules: (value) => {
      if (!value) return 'Name is required'
      if (value?.length < 2) return 'Name must have at least 2 caracters'
      return true
    },
    loginRules: (value) => {
      if (!value) return 'Login is required'
      if (value?.length < 4) return 'Name must have at least 4 caracters'
      return true
    },
    pwdRules: (value) => {
      if (!value) return 'Password is required'
      if (value?.length < 6) return 'Name must have at least 6 caracters'
      return true
    },
    required: (v) => !!v || 'Field is required',
  },
})

const emitUser = () => {
  if (form.value.valid) {
    const payload = {
      name: form.value.username,
      user_login: form.value.login,
      pwd: form.value.password,
    }
    form.value.username = ''
    form.value.login = ''
    form.value.password = ''
    emit('new-user', payload)
  }
}
</script>
