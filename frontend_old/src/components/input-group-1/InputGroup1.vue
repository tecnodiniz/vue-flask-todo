<template>
   
    <div class="input-group mb-3">
        <input @keypress="onKeyPress" v-model.trim="value" type="text" class="form-control p-2" placeholder="Task item" aria-label="Task item" aria-describedby="button-addon2">
        <button @click="emitValue" class="btn btn-primary" type="button" id="button-addon2">Button</button>
    </div>

</template>

<script>
export default {
    emits:['create-task'],
    props:{
        
    },
    data(){
        return{
            value: ''
        }
        
    },
    methods:{
        emitValue(){
            if(this.value != "")
                this.$emit('create-task', this.value)
            this.value = ''
        },
        onKeyPress(event){
            if(event.key == "Enter")
                this.emitValue()
        }
    }
}
</script>