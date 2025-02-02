<template>
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
      <v-form v-model="form.valid">
        <v-row dense>
          <v-col cols="12" sm="6">
            <v-text-field
              v-model="form.name"
              hint="Todo name"
              label="Todo name*"
              required
              :rules="[rules.required]"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6">
            <v-text-field v-model="form.description" label="Description"></v-text-field>
          </v-col>
        </v-row>
      </v-form>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="primary" variant="text" @click="$emit('close')"> Cancel </v-btn>
        <v-btn color="primary" variant="text" @click="emitTodo" :disabled="!form.valid">
          Submit
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, toRef } from 'vue'

const emit = defineEmits(['new-todo', 'close'])
const form = ref({
  valid: false,
  name: '',
  description: '',
})
const rules = ref({
  required: (v) => !!v || 'Field is required',
})

const createPayload = ({ name, description }) => ({
  name,
  description,
})

const defaultForm = () => ({
  name: '',
  description: '',
})

const resetForm = () => {
  form.value = defaultForm()
}
const emitTodo = () => {
  const payload = form.value.valid ? createPayload(form.value) : null
  emit('new-todo', payload)
  resetForm()
}

const props = defineProps(['dialog'])

const dialog = toRef(props, 'dialog')
</script>
