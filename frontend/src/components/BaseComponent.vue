<template>
  <!-- @keyup.ctrl.delete="tasks=[]" -->
   <div v-if="!isUserLoggedIn">
    <LoginComponent @send-data="handleLogin"/>
   </div>
   <div v-if="isUserLoggedIn">
    <v-btn
        color="primary mb-4"
        @click="logout"
      >
        Logout
      </v-btn>
   </div>
 
    <div class="col-12" >
      <div class="card col-10 col-lg-3 col-md-6 col-sm-6">
        <div class="card-header">
          <h3><strong>TO-DO LIST</strong></h3>
          <p v-if="isUserLoggedIn">Usuário logado: {{ user.name }}</p>

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
import {delete_all, delete_task, new_task, update_task, get_task, user_login } from '@/services/api';
import InputGroup1 from './input-group-1/InputGroup1.vue';
import TodoItems from './todoItems/TodoItems.vue';
import LoginComponent from './loginComponent/LoginComponent.vue';  
  
  export default {
    name: 'BaseComponent',
    components: {
      InputGroup1,
      TodoItems,
      LoginComponent,
    },
    data(){
      return{
        tasks: [],
        itens: 0,
        user: JSON.parse(localStorage.getItem("user"))  || ""
      }
    }, 
    computed:{
      isUserLoggedIn(){
        return !!this.user
      }


    },
    mounted(){
      if(this.verifyToken()){
            get_task()
      .then((response) =>{
        this.tasks = response.data["data"]
      })
      .catch((error) =>{
        console.log("Error fetching tasks", error);
        localStorage.removeItem("token")
        localStorage.removeItem("user")
        location.reload()
      });

      }
      else{
        const data = localStorage.getItem('task');
        localStorage.removeItem("user")
        if(data){
          this.tasks = JSON.parse(data);
          this.itens = this.tasks.length;
        }
      }

    },
    methods:{
      createTask(task){
        if(this.verifyToken()){
          const data = {task: task, done:false};
          new_task(data)
          .then((response) =>{
            console.log("msg", response.data);
            this.getTask();
          }).catch((error) =>{
            console.log("error",error);
            localStorage.removeItem("token")
            localStorage.removeItem("user")
            location.reload()
          });

        }else{
            this.itens ++;
            const data = {_id:this.itens,task: task, done:false};
            this.tasks.push(data);
            localStorage.setItem('task',JSON.stringify(this.tasks));
        }
        
    
      },
      getTask(){
        if(this.verifyToken()){
            get_task()
      .then((response) =>{
        this.tasks = response.data["data"]
      })
      .catch((error) =>{
        console.log("Error fetching tasks", error);
        localStorage.removeItem("token")
        localStorage.removeItem("user")
        location.reload()
      });

      }
      else{
        const data = localStorage.getItem('task');
        localStorage.removeItem("user")
        if(data){
          this.tasks = JSON.parse(data);
          this.itens = this.tasks.length;
        }
      }
      },
      
      updateTask(obj){
         if(this.verifyToken()){
          update_task(obj.id, obj.update)
            .then((response) => {
              console.log("msg", response.data)
              this.getTask();
            }).catch((error) =>{
            console.log("error", error);
            localStorage.removeItem("token")
            localStorage.removeItem("user")
            location.reload()
            });

         }else
          localStorage.setItem('task',JSON.stringify(this.tasks));
  
      
      },
      deleteTask(id){
        if(this.verifyToken()){
          delete_task(id)
          .then((response) =>{
            console.log("msg", response.data);
            this.getTask();
          }).catch((error) =>{
            console.log("error", error);
            localStorage.removeItem("token")
            localStorage.removeItem("user")
            location.reload()
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
        
        if(this.verifyToken()){
          delete_all()
          .then((response) =>{
            console.log("msg", response.data);
            this.getTask();
          }).catch((error) => {
            console.log("error", error);
            localStorage.removeItem("token")
            localStorage.removeItem("user")
            location.reload()
          });
        }else{
          this.tasks = []
        }
      },
      getUser(data){
        return data
        // get_user(data)
        //   .then((response) =>{
        //     const { data } = response;
        //     localStorage.setItem("user", data.user.name)
        //     location.reload();
        //   }).catch((error) => {
        //     return error
        //   })
      },
      verifyToken(){
        return localStorage.getItem("token");
      },
      handleLogin(data){
        user_login(data)
        .then((response) => {
          const {token, user} = response.data
          localStorage.setItem("token", token)
          localStorage.setItem("user", JSON.stringify(user))
          location.reload()
          
       
        }).catch((error) => {
          alert(error.code)}
          
        );

      },
      logout(){
        localStorage.removeItem("token")
        localStorage.removeItem("user")
        location.reload();
      }
     
    }
  }
  </script>
  