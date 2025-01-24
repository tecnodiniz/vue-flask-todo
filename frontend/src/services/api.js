import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const get_todos = () =>
  api.get('/todo/', {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })
export const create_user = (data) => api.post('/user/new', data)
export const user_login = (data) => api.post('/user/auth', data)
export const user_logout = (data) =>
  api.post('/user/logout', data, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })
export const get_user = (user) =>
  api.get(`/user?login=${user}`, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })

export const new_task = (data) =>
  api.post('/task/new', data, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })
export const get_tasks = (id) =>
  api.get(`/task?todo=${id}`, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })

export const update_task = (id, data) =>
  api.put(`/task/${id}`, data, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })

export const delete_task = (id) =>
  api.delete(`/task/${id}`, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })

export const delete_all = (id) =>
  api.get(`/task/tasks/reset?todo=${id}`, {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })
export default api
