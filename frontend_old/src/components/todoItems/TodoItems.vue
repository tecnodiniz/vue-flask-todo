<template>
    <li v-for="(item, index) in items" :key="index">
        <div class="item-box">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" :value="item._id" :id="'flexCheckChecked-'+index" v-model="item.done" @change="handleCheck" >
                <label class="form-check-label" :for="'flexCheckChecked-'+index">
                    <a :class="{active: item.done}" href="#">{{ item.task }}</a>
                </label>
            </div>
            <a href="#" @click="emitKey(item._id)"><i class="bi bi-x-lg"></i></a>

        </div>

        

    </li>
</template>

<script>
export default{
    emits:['delete-task', 'update-task'],
    props:{
        items: {
            type: Array,
            require: true
        }
    },
    methods:{
        emitKey(id){
            this.$emit('delete-task',id)
        },
        handleCheck(event){
           const obj = {id: event.target.value, update:{done: event.target.checked}}
            this.$emit('update-task',obj);
      
        }
    }
}
</script>

<style>
li{
    list-style: none;
    margin: 0;
    padding: 0;
    text-align: left;
}
.item-box{
    display: flex;
    justify-content: space-between;
}
label a{
    color: black;
    text-decoration: none;
}
label a.active{
    text-decoration: line-through;
}
</style>