<template>
  <div class="text-center pa-4">
    <v-dialog v-model="dialog" width="auto">
      <v-card
        max-width="400"
        prepend-icon="mdi-update"
        text="Unable to connect to the server. Please check your internet connection and try again. If the problem persists, contact server adminsitrator."
        :title="msg"
      >
        <template v-slot:actions>
          <v-btn class="ms-auto" text="Ok" @click="$emit('close')"></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import { toRef } from 'vue'

const props = defineProps(['dialog', 'msg'])

const dialog = toRef(props, 'dialog')
</script>
