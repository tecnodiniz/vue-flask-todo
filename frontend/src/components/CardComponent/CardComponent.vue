<template>
  <v-container>
    <v-sheet color="dark" width="400">
      <div class="card">
        <div class="card-header d-flex">
          <v-text-field
            v-model="item"
            label="Label"
            variant="underlined"
            clearable
            @keyup.enter="addItem"
            :rules="[rule.required]"
          ></v-text-field>
          <v-btn class="align-self-center" :icon="IconAdd" variant="plain" @click="addItem"></v-btn>
        </div>

        <div class="card-body">
          <v-checkbox
            v-for="(i, index) in items"
            :key="index"
            :label="i"
            class="ma-0"
            density="compact"
          >
          </v-checkbox>
        </div>

        <div class="card-footer d-flex">
          <v-btn :icon="IconGarbage" variant="plain"></v-btn>
        </div>
      </div>
    </v-sheet>
  </v-container>
</template>

<script setup>
import IconAdd from '../icons/IconAdd.vue'
import { ref } from 'vue'
import IconGarbage from '../icons/IconGarbage.vue'

const items = ref([])
const item = ref('')
const rule = ref({ required: (value) => !!value || 'Field required' })
// const rule = reactive({ required: (value) => !!value || 'Field required' })

const addItem = () => {
  if (item.value.trim()) {
    items.value.push(item.value.trim())
    item.value = ''
  }
}
</script>

<style scoped>
.card {
  padding: 1rem;
  border-radius: 16px;
}
.card-header {
  padding: 2rem;
}
.card-body {
  height: 200px;
  min-height: 300px;
  overflow: auto;
  padding: 2rem;
}
.card-footer {
  padding: 1rem;
}
</style>
