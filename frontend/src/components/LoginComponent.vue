<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        prepend-icon="mdi-account"
        text="Login"
        variant="tonal"
        v-bind="activatorProps"
      ></v-btn>
    </template>

    <v-card prepend-icon="mdi-account" title="User Login">
      <v-card-text>
        <v-form v-model="form.valid">
          <v-row dense>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.login"
                hint="User login"
                label="Login"
                required
                :rules="[form.rule.required]"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.password"
                label="Password"
                type="password"
                required
                :rules="[form.rule.required]"
                @keyup.enter="emitUser"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>

        <slot></slot>

        <!-- <small class="text-caption text-medium-emphasis">*indicates required field</small> -->
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

      <FormUserComponent @new-user="newUser">
        <template v-if="errorMessage"
          ><small class="text-caption text-red-lighten-1">{{ errorMessage }}</small>
        </template>
      </FormUserComponent>

      <DialogComponent
        :msg="dialogTitle"
        :text="dialogText"
        :dialog="formDone"
        @close="formDone = false"
      />
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref } from 'vue'
import FormUserComponent from './FormUserComponent.vue'
import DialogComponent from './DialogComponent.vue'
import { create_user } from '@/services/api'
const dialog = ref(false)
const loading = ref(false)
const submit = ref(false)
const formDone = ref(false)
const errorMessage = ref('')
const dialogTitle = ref('')
const dialogText = ref('')

const emit = defineEmits(['user-login'])
const form = ref({
  valid: false,
  login: '',
  password: '',
  rule: {
    required: (v) => !!v || 'Field is required',
  },
})

const emitUser = () => {
  if (form.value.valid) {
    loading.value = true
    submit.value = true
    const payload = { username: form.value.login, password: form.value.password }
    emit('user-login', payload)
  }
}

const newUser = async (data) => {
  try {
    console.log(data)
    const res = await create_user(data)
    if (res && res.data) {
      console.log(res.data)
      dialogTitle.value = 'User Created'
      dialogText.value = 'User successfully created, please, login into application'
      formDone.value = true
    }
  } catch (error) {
    const { response } = error
    if (response && response.status === 409) {
      console.log('conflito')
      errorMessage.value = response.data.msg
      return
    } else {
      console.log(error.message)
      dialogTitle.value = 'Something got wrong'
      formDone.value = true
    }
  }
}
</script>
