import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const user_login = (data) => api.post('/user/auth', data)
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
export const get_tasks = () =>
  api.get('/task/', {
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

export const delete_all = () =>
  api.get('/task/tasks/reset', {
    headers: {
      Authorization: `Bearer ${JSON.parse(localStorage.getItem('token'))}`,
    },
  })
export default api
