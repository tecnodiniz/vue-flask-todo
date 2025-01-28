# PATH NOTES(v1.0.0)

- IF YOU ARE RUNNING THE OLD VERSION:
```
python updateDB.py
```

# To-Do List Application
This is a simple To-Do List Application built using Flask for the backend and Vue.js for the frontend. The frontend has been pre-built and is served through the Flask backend using the static directory.

## Project Structure

```
/To-do
├── backend
├── app
│   ├── config.py             - Server Config
│   ├── extensions.py         - Manage extensions like mongo and jwt
│   ├── __init__.py           - Initialize app
│   ├── main
│   │   └── routes.py         - Manage templates and static route
│   ├── routes                - Blueprint routes
│   │   ├── __init__.py
│   │   ├── task.py
│   │   └── user.py
│   ├── services              - Utilities methods
│   │   └── utils.py
│   ├── static                - Front end builded files
│   │   ├── assets
│   │   ├── favicon.ico
│   │   └── index.html
│   └── templates            
│       ├── 404.html
│       └── error.html
├── README.md
├── requiriments.txt
└── run.py                  - Run app
/frontend                   - Vue 
├── eslint.config.js
├── index.html
├── jsconfig.json
├── package.json
├── package-lock.json
├── public
│   └── favicon.ico
├── README.md
├── src
│   ├── App.vue
│   ├── assets
│   ├── components
│   ├── main.js
│   ├── router
│   ├── services
│   └── views
└── vite.config.js
```
## Requirements
- Python (version 3.8 or higher)
- MongoDB
- Node.js (if building the frontend yourself)

---

## Getting Started
### Backend (Flask)
1. Navigate to the backend directory:

```
cd backend  
```
2. Create a virtual environment (optional but recommended):

```
python -m venv venv  
```

3. Install dependences
```
pip install -r requirements.txt  
```
4.  START MONGODB SERVICE!!!

5. Run the Flask application:

```
python3 run.py 
```

# Frontend (Vue.js)
The frontend is already built and located in the static directory of the backend. If you need to rebuild it:

1. Navigate to the frontend directory:

```
cd frontend  
```
2. Install the frontend dependencies:
```
npm install  
```
3. Build the frontend for production:

```
npm run build  
```
4. Copy the built files to the static directory in the backend:
```
cp -r dist/* ../backend/app/static  
```
5. Accessing the Application

- Once the Flask server is running, open your browser and navigate to:

**http://localhost:5000**  

## Features
- Add new tasks to your to-do list
- Mark tasks as completed
- Delete tasks
- Persistent storage using Flask (you can configure the database)
