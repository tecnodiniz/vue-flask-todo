<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <template v-slot:activator="{ props: activatorProps }">
      <v-btn
        class="text-none font-weight-regular"
        text="New Todo"
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
                v-model="form.name"
                hint="Todo name"
                label="Todo name*"
                required
                :rules="[form.rule.required]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.description" label="Description"></v-text-field>
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
          text="Add"
          variant="tonal"
          @click="emitTodo"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref } from 'vue'
const dialog = ref(false)

const emit = defineEmits(['new-todo'])
const form = ref({
  valid: false,
  name: '',
  description: '',
  rule: {
    required: (v) => !!v || 'Field is required',
  },
})

const emitTodo = () => {
  if (form.value.valid) {
    const payload = {
      name: form.value.name,
      description: form.value.description,
    }
    form.value.name = ''
    form.value.description = ''
    emit('new-todo', payload)
    dialog.value = false
  }
}
</script>
