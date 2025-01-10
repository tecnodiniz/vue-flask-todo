<template>
  <!-- @keyup.ctrl.delete="tasks=[]" -->
    <div class="col-12" >
      <div class="card col-10 col-lg-3 col-md-6 col-sm-6">
        <div class="card-header">
          <h3><strong>TO-DO LIST</strong></h3>
        </div>
        <InputGroup1 @create-task="createTask" />
        <div class="card-body">
          <ul>
          <TodoItems :items="tasks" @delete-task="deleteTask" @update-task="updateTask"/>
          
          </ul>
  
        </div>
       
        <div class="card-footer">
          <div class="footer-content">
            <div class="itens-count">
              <a href="#"> Tasks: {{ tasks.filter(i => i.done == false).length  }}</a>
  
            </div>
            <div class="delete-itens">
              <a href="#" @click="deleteAll"><i class="bi bi-trash3-fill"></i></a>
  
            </div>
            
          </div>
          
        </div>
        
    </div>
  
    </div>
  
  </template>
  
  <script>
import { delete_all, delete_task, update_task, get_task } from '@/services/api';
import InputGroup1 from './input-group-1/InputGroup1.vue';
import TodoItems from './todoItems/TodoItems.vue';
  
  
  export default {
    name: 'BaseComponent',
    components: {
      InputGroup1,
      TodoItems,
    },
    data(){
      return{
        tasks: [],
        token: '',
        itens: 0
      }
    }, 
    mounted(){
      const data = localStorage.getItem('task');
      if(data){
        this.tasks = JSON.parse(data);
        this.itens = this.tasks.length;
      }
      

      
      // get_task()
      //   .then((response) =>{
      //     this.tasks = response.data["data"];
      //   })
      //   .catch((error) =>{
      //     console.log("Error fetching tasks", error);
      //   });
    },
    methods:{
      createTask(task){
        this.itens ++;
       const data = {_id:this.itens,task: task, done:false};
       this.tasks.push(data);
       localStorage.setItem('task',JSON.stringify(this.tasks));
        // new_task(data)
        //   .then((response) =>{
        //     console.log("msg", response.data);
        //     this.getTask();
        //   }).catch((error) =>{
        //     console.log("error",error);
        //   });

      },
      getTask(){
        get_task()
        .then((response) =>{
          this.tasks = response.data["data"];
        })
        .catch((error) =>{
          console.log("Error fetching tasks", error);
        });
      },
      
      updateTask(obj){
        const token = localStorage.getItem("token")
        console.log(token)
        
         
         if(token){
          update_task(obj.id, obj.update)
            .then((response) => {
              console.log("msg", response.data)
              this.getTask();
            }).catch((error) =>{
              console.log("Erro ao atualizar task",error);
              this.getTask();
            });

         }else
          localStorage.setItem('task',JSON.stringify(this.tasks));
  
      
      },
      deleteTask(id){
        const data = localStorage.getItem("token");
        if(data){
          delete_task(id)
          .then((response) =>{
            console.log("msg", response.data);
            this.getTask();
          }).catch((error) =>{
            console.log("error", error);
          });
        }
        else{
          const index = this.tasks.findIndex(item => item._id == id)
          console.log(index)
          this.tasks.splice(index, 1);
          localStorage.setItem("task", JSON.stringify(this.tasks))
         
        }
       
      },
      deleteAll(){
        delete_all()
          .then((response) =>{
            console.log("msg", response.data);
            this.getTask();
          }).catch((error) => {
            console.log("error", error);
          });
      }
     
    }
  }
  </script>
  