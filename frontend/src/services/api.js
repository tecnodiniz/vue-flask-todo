import axios from "axios";

const api = axios.create({
    baseURL:"http://127.0.0.1:5000",
    timeout: 10000,
    headers:{
        "Content-Type":"application/json"
    }
});
// function checkConnection(){
//     api.get("").then((response) =>{
//         console.log(response.data);
//     }).catch((error) => {
//         const { code } = error;

//         if(code === "ERR_NETWORK")
//             alert("RODE A APLICAÇÃO BACKEND PRIMEIRO!")
        
//     })
// }

export const new_task = (data) => api.post("/tasks", data);
export const get_task = () => api.get("/tasks");
export const update_task = (id, data) => api.put(`/tasks/${id}`,data);
export const delete_task = (id) => api.delete(`/tasks/${id}`);
export const delete_all = () => api.get("/tasks/reset");

export default api;