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
            <v-col cols="12" md="4" sm="6">
              <v-text-field
                v-model="form.login"
                hint="User login"
                label="Login"
                required
                :rules="[form.rule.required]"
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4" sm="6">
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
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref } from 'vue'
const dialog = ref(false)
const loading = ref(false)
const submit = ref(false)

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
</script>
