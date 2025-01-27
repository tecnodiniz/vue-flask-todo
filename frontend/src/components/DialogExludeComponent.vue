<template>
  <div class="text-center pa-4">
    <v-btn @click="dialog = true"> Exclude </v-btn>

    <v-dialog v-model="dialog" width="auto">
      <v-card
        max-width="400"
        prepend-icon="mdi-update"
        text="Quer mesmo exluir a lista?"
        title="Deltar lista?"
      >
        <template v-slot:actions>
          <v-btn class="ms-auto" text="Cancel" @click="dialog = false"></v-btn>
          <v-btn class="ms-auto" text="Confirm" @click="$emit('delete-confirm')"></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const dialog = ref(false)
</script>
