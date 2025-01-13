<template>
   
      <v-btn
        color="primary mb-4"
        @click="overlay = !overlay"
      >
        Login
      </v-btn>

        <v-overlay class="align-center justify-center" v-model="overlay" contained>
            <v-sheet class="mx-auto" width="300">
                <v-form @submit.prevent>

                <v-text-field
                    v-model="username"
                    :rules="rulesName"
                    label="User Login"
                ></v-text-field>

                <v-text-field
                    v-model="password"
                    :rules="rulesPass"
                    label="Password"
                    type="password"
                ></v-text-field>

                <v-btn class="mt-2" type="submit" @click="emitLogin" block>Login</v-btn>
                </v-form>
            </v-sheet>
        </v-overlay>

  </template>
<script>
export default {
    emits:['send-data'],
    data: () => ({
        overlay: false,
        username: '',
        rulesName: [
            value => {
            if (value) return true

            return 'You must enter your user login'
            },
        ],
        password:'',
        rulesPass:[
            value =>{
                if(value) return true

                return 'You mus enter you password'
            }
        ]
    }),
    methods:{
        emitLogin(){
            const payload = {username: this.username, password: this.password}
            this.$emit('send-data', payload);
        }
    }
}
</script>
