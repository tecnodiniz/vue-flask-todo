<template>
  <v-data-iterator :items="todos" item-value="name">
    <template v-slot:default="{ items, isExpanded, toggleExpand }">
      <v-row>
        <v-col v-for="item in items" :key="item.raw.name" cols="12" md="6" sm="12">
          <v-card>
            <v-card-title class="d-flex align-center">
              <!-- <v-icon :color="item.raw.color" :icon="item.raw.icon" size="18" start></v-icon> -->

              <h4>{{ item.raw.name }}</h4>
            </v-card-title>

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
                  <v-list-item>{{ task.task }}</v-list-item>
                </v-list>
              </div>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </v-data-iterator>
</template>

<script setup>
defineProps({
  todos: {
    type: Array,
    require: true,
  },
})
</script>
