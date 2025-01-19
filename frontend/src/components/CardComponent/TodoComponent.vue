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
            v-for="(i, index) in todos"
            :key="index"
            v-model="i.done"
            :label="i.task"
            class="ma-0"
            density="compact"
            hide-details
            :class="{ done: i.done }"
            @change="() => updateItem(i)"
            :append-icon="IconCross"
            @click:append="deleteItem(i._id)"
          >
          </v-checkbox>
        </div>

        <div class="card-footer d-flex justify-space-between align-center">
          <div>
            <span>Tasks: {{ todos.filter((task) => task.done == false).length }}</span>
          </div>
          <v-btn :icon="IconGarbage" variant="plain"></v-btn>
        </div>
      </div>
    </v-sheet>
  </v-container>
</template>

<script setup>
import IconAdd from '../icons/IconAdd.vue'
import IconCross from '../icons/IconCross.vue'
import IconGarbage from '../icons/IconGarbage.vue'
import { ref } from 'vue'
const emit = defineEmits(['add-item', 'update-item', 'delete-item'])

defineProps({
  todos: {
    type: Array,
    required: true,
  },
})

const item = ref('')
const rule = ref({ required: (value) => !!value || 'Field required' })

const addItem = () => {
  if (item.value.trim()) {
    emit('add-item', item.value)
  }
}

const updateItem = (task) => {
  emit('update-item', task)
}

const deleteItem = (id) => {
  emit('delete-item', id)
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
