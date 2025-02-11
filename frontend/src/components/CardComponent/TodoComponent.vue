<template>
  <v-col cols="12" md="12" sm="12" class="mx-auto">
    <v-sheet color="dark" rounded>
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
            @change="() => $emit('update-item', i)"
            :append-icon="IconCross"
            @click:append="$emit('delete-item', i._id)"
          >
          </v-checkbox>
        </div>

        <div class="card-footer d-flex justify-space-between align-center">
          <div>
            <span>Tasks: {{ todos.filter((task) => task.done == false).length }}</span>
          </div>
          <v-btn :icon="IconGarbage" variant="plain" @click="$emit('clearList')"></v-btn>
        </div>
      </div>
    </v-sheet>
  </v-col>
</template>

<script setup>
import IconAdd from '../icons/IconAdd.vue'
import IconCross from '../icons/IconCross.vue'
import IconGarbage from '../icons/IconGarbage.vue'
import { ref } from 'vue'
const emit = defineEmits(['add-item', 'update-item', 'delete-item', 'clearList'])

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
