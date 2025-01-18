<template>
   
      <v-btn
        color="primary mb-4"
        @click="overlay = !overlay"
      >
        Login
      </v-btn>

        <v-overlay class="align-center justify-center" v-model="overlay" contained>
            <v-sheet v-if="haveAccount" class="mx-auto" width="300">
                <v-form @submit.prevent>

                <v-text-field
                    v-model.trim="username"
                    :rules="rulesName"
                    label="User Login"
                ></v-text-field>

                <v-text-field
                    v-model.trim="password"
                    :rules="rulesPass"
                    label="Password"
                    type="password"
                ></v-text-field>

                <v-btn class="mt-2" type="submit" @click="emitLogin" block>Login</v-btn>
                </v-form>
                <v-btn class="mt-2" type="submit" variant="plain" @click="haveAccount = false" block>create account</v-btn>
                
            </v-sheet>

            <v-sheet v-if="!haveAccount" class="mx-auto" width="300">
                <v-form @submit.prevent>
                    <v-text-field
                    v-model.trim="name"
                    :rules="rules"
                    label="User Name"
                ></v-text-field>

                <v-text-field
                    v-model.trim="username"
                    :rules="rulesName"
                    label="User Login"
                    @focus="exist = false"
                ></v-text-field>

                <v-text-field
                    v-model.trim="password"
                    :rules="rulesPass"
                    label="Password"
                    type="password"
                ></v-text-field>

                <v-text-field
                    v-model.trim="r_password"
                    label="Repeat Password"
                    type="password"
                    @focus="pwdAlert=false"
                ></v-text-field>
                <span v-if="pwdAlert"><strong class="text-red-lighten-1">password not match</strong> </span>
                <span v-if="exist"><strong class="text-red-lighten-1">user already registered</strong> </span>

                <v-btn class="mt-2" type="submit" @click="emitData" block>Create account</v-btn>
                </v-form>
            </v-sheet>
        </v-overlay>


  </template>
<script>
import { create_user, get_user } from '@/services/api';

export default {
    emits:['send-data'],
    data: () => ({
        exist:false,
        pwdAlert: false,
        haveAccount:true,
        overlay: false,
        name: '',
        rules: [
            value => {
            if (value) return true

            return 'You must enter your user Name'
            },
        ],
        username: '',
        rulesName: [
            value => {
            if (value) return true

            return 'You must enter your user login'
            },
        ],
        r_password: '',
        password:'',
        rulesPass:[
            value =>{
                if(value) return true

                return 'You mus enter you password'
            }
        ],
    }),
    methods:{
        emitLogin(){
            if(this.username !== '' && this.password !== ''){
                const payload = {username: this.username, password: this.password}
                this.$emit('send-data', payload);
            }
               
        },
        emitData(){
            if(this.username !== '' && this.password !== ''){
                if(this.password !== this.r_password){
                    this.pwdAlert = true;
                }else{
                    const payload = {name: this.name, user_login: this.username, pwd: this.password}
                    get_user(payload.user_login)
                    .then((response) =>{
                        console.log(response.data)
                        if(response.data)
                            this.exist = true;
                      
                    }).catch((error) => {
                        if (error.response && error.response.status === 404) {
                                console.log("Usuário não encontrado. Prosseguindo com o cadastro...");
                                console.log(payload)
                                create_user(payload)
                                    .then((response) =>{
                                        console.log(response)
                                        alert('Usuário criado!')
                                        location.reload()
                                    })

                            } else {
                                console.error("Erro ao verificar usuário:", error);
                                return; // Interrompe o fluxo em caso de erro inesperado
                            }
                    })
                    // const payload = {username: this.username, password: this.password}
                    // this.$emit('send-data', payload);
                }
                    
            }
                
        }
    }
}
</script>
