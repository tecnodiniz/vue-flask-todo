<template>


  <v-col class="ma-auto mt-15" cols="8">
        <div >
          <div class="text-h5 ma-5">
            Hey {{ username }}!! Welcome to Your Ultimate Todo List App!
          </div>

          <div class="text-body-1 text-justify">
            <p>
              Stay organized, focused, and on top of your goals with our powerful yet simple-to-use
              todo list app. Whether you're managing daily tasks, planning big projects, or keeping
              track of life's essentials, this app has everything you need to stay in control. Clean
              and intuitive design for a stress-free experience. Your productivity is about to hit a
              whole new level. Let's turn your plans into actions and your actions into
              achievements! Ready to get started? 🎯
            </p>

            <div class="ma-5">
              Click on <v-icon icon="mdi-dots-vertical"></v-icon> > <span class="green">Home</span> to get Start
            </div>
          </div>
        </div>
      </v-col>







</template>
<script setup>
import { onMounted, ref } from 'vue'

const username = ref('')

onMounted(() => {
  username.value = localStorage.getItem('username')
})
</script>


