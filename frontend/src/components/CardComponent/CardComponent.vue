<template>
  <v-container>
    <v-sheet color="dark" width="400" rounded>
      <div class="card">
        <div class="card-header d-flex">
          <v-text-field
            v-model="item"
            label="Task"
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
            v-model="i.done"
            :key="index"
            :label="i.task"
            class="ma-0"
            density="compact"
            hide-details
            :class="{ done: i.done }"
          >
          </v-checkbox>
        </div>

        <div class="card-footer d-flex justify-space-between align-center">
          <div>
            <span>Tasks: {{ itemsDone.length }}</span>
          </div>
          <v-btn :icon="IconGarbage" variant="plain" @click="items.splice(0, items.length)"></v-btn>
        </div>
      </div>
    </v-sheet>
  </v-container>
</template>

<script setup>
import IconAdd from '../icons/IconAdd.vue'
import { computed, reactive, ref } from 'vue'
import IconGarbage from '../icons/IconGarbage.vue'

const items = reactive([])
const item = ref('')
const rule = ref({ required: (value) => !!value || 'Field required' })

const itemsDone = computed(() => {
  return items.filter((item) => item.done == false)
})

const addItem = () => {
  if (item.value.trim()) {
    items.push({ task: item.value, done: false })
    item.value = ''
  }
}
</script>

<style scoped>
.card {
  padding: 1rem;
  border-radius: 16px;
}
.card-chips {
  overflow: auto;
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

.done {
  text-decoration: line-through;
}
</style>
