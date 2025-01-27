<template>
  <v-data-iterator :items="todos" item-value="name">
    <template v-slot:default="{ items, isExpanded, toggleExpand }">
      <v-row>
        <v-col v-for="item in items" :key="item.raw._id" cols="12" md="6" sm="12">
          <v-card>
            <div class="d-flex align-center justify-space-between">
              <v-card-title class="d-flex align-center">
                <!-- <v-icon :color="item.raw.color" :icon="item.raw.icon" size="18" start></v-icon> -->

                <h4>{{ item.raw.name }}</h4>
              </v-card-title>

              <div class="text-center">
                <v-btn @click="dialog = true" icon="mdi-delete-circle" variant="plain"> </v-btn>

                <v-dialog v-model="dialog" width="auto">
                  <v-card
                    max-width="400"
                    prepend-icon="mdi-update"
                    text="Quer mesmo exluir a lista?"
                    title="Deltar lista?"
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

const emit = defineEmits(['delete-confirm'])
const dialog = ref(false)
defineProps({
  todos: {
    type: Array,
    require: true,
  },
})

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
