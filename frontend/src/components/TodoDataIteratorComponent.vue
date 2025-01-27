<template>
  <v-data-iterator :items="todos" item-value="name">
    <template v-slot:default="{ items, isExpanded, toggleExpand }">
      <v-row>
        <v-col v-for="(item, index) in items" :key="item.raw._id" cols="12" md="6" sm="12">
          <v-card>
            <div class="d-flex align-center justify-space-between">
              <v-card-title class="d-flex align-center">
                <!-- <v-icon :color="item.raw.color" :icon="item.raw.icon" size="18" start></v-icon> -->

                <template v-if="editingIndex === index">
                  <v-text-field

                    v-model="item.raw.name"
                    @blur="saveItem(item.raw.name, item.raw._id)"
                    @keydown.enter="saveItem(item.raw.name, item.raw._id)"
                    label="Editar"
                    dense
                    width="200px"
                    autofocus
                    variant="plain"
                  ></v-text-field>
                </template>
                <h4 class="cursor-pointer" v-else @dblclick="editItem(index, item.raw.name)">{{ item.raw.name }}</h4>
              </v-card-title>

              <div class="text-center">
                <v-btn @click="dialog = true" icon="mdi-delete-circle" variant="plain"> </v-btn>

                <v-dialog v-model="dialog" width="auto">
                  <v-card
                    max-width="400"
                    prepend-icon="mdi-update"
                    text="Are you sure?"
                    title="Delete?"
                  >
                    <template v-slot:actions>
                      <v-btn class="ms-auto" text="Cancel" @click="dialog = false"></v-btn>
                      <v-btn
                        class="ms-auto"
                        text="Confirm"
                        @click="deleteTodo(item.raw._id)"
                      ></v-btn>
                    </template>
                  </v-card>
                </v-dialog>
              </div>
            </div>

            <v-card-text>
              {{ item.raw.description }}
            </v-card-text>

            <div class="px-4">
              <v-switch
                :label="`${isExpanded(item) ? 'Hide' : 'Show'} details`"
                :model-value="isExpanded(item)"
                density="compact"
                inset
                @click="() => toggleExpand(item)"
              ></v-switch>
            </div>

            <v-divider></v-divider>

            <v-expand-transition>
              <div v-if="isExpanded(item)">
                <v-list
                  :lines="false"
                  density="compact"
                  v-for="task in item.raw.tasks"
                  :key="task._id"
                >
                  <v-list-item :class="{ done: task.done }">{{ task.task }}</v-list-item>
                </v-list>
              </div>
            </v-expand-transition>

            <v-card-actions>
              <RouterLink :to="`/todo/${item.raw._id}`">View Todo</RouterLink>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </v-data-iterator>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['delete-confirm', 'update-todo'])
const dialog = ref(false)
const editingIndex = ref(null)
const previousName = ref('')
defineProps({
  todos: {
    type: Array,
    require: true,
  },
})

const saveItem = (name, id) => {
  const payload = { name: name, id: id }
  if (name.trim() != '') payload.name = name
  else payload.name = previousName.value

  emit('update-todo', payload)
  editingIndex.value = null
}
const editItem = (index, name) => {
  editingIndex.value = index
  previousName.value = name
}
const deleteTodo = (id) => {
  emit('delete-confirm', id)
  dialog.value = false
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
