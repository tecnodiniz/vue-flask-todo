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

export const user_login = (data) => api.post("/auth", data);
export const get_user = (user) => api.get(`/users/${user}`);

export const new_task = (data) => api.post("/tasks", data, {
    headers:{
        Authorization: `Bearer ${JSON.parse(localStorage.getItem("token"))}`,
    }
});

export const get_task = () => api.get("/tasks", {
    headers:{
        Authorization: `Bearer ${JSON.parse(localStorage.getItem("token"))}`,
    }
});

export const update_task = (id, data) => api.put(`/tasks/${id}`,data, {
    headers:{
        Authorization: `Bearer ${JSON.parse(localStorage.getItem("token"))}`,
    }
});
export const delete_task = (id) => api.delete(`/tasks/${id}`, {
    headers:{
        Authorization: `Bearer ${JSON.parse(localStorage.getItem("token"))}`,
    }
});

export const delete_all = () => api.get("/tasks/reset", {
    headers:{
        Authorization: `Bearer ${JSON.parse(localStorage.getItem("token"))}`,
    }
});

export default api;