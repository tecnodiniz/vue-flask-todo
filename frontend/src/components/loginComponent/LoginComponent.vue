<template>
    <div>
        <form  @submit.prevent="emitLogin">
            <input type="text" id="username" v-model="username" placeholder="your user login">
            <input type="password" id="password" v-model="password" placeholder="your user password">

            <input type="submit" value="Log in">
        </form>

    </div>
</template>

<script>
export default {
    emits:['send-data'],
    data(){
        return{
            username:'',
            password:'',
        }
    },
    methods:{
        emitLogin(){
            const payload = {username: this.username, password: this.password}
            this.$emit('send-data', payload);
        }
    }
}
</script>