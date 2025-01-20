# Flask MongoDB API with Task Management

This project is a Flask-based RESTful API for managing tasks, utilizing MongoDB as the database. It supports operations to create, read, update, and delete tasks (CRUD operations). The project also includes features like CORS support, static file serving, and error handling.

---

## Features
- **Create Tasks**: Add new tasks to the MongoDB collection.
- **Retrieve Tasks**:
  - Fetch all tasks.
  - Fetch a specific task by its ID.
- **Update Tasks**: Modify the details of an existing task.
- **Delete Tasks**:
  - Delete a specific task by its ID.
  - Delete all tasks at once.
- **Error Handling**:
  - Custom 404 error page.
  - Proper error responses for invalid inputs and exceptions.
- **Static File Serving**: Serves static files like `index.html`.
- **CORS Support**: Allows cross-origin requests using Flask-CORS.

---

## Prerequisites
- Python 3.7+
- MongoDB instance (local or cloud)
- Node.js (optional for managing static files)

---

## Setup

### 1. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the project root directory and add the following:
```env
MONGO_URI=<your_mongodb_connection_string>
```
Replace `<your_mongodb_connection_string>` with your MongoDB URI.

### 3. Parse Users
You can create your users at database = {"name": "User Name", "user_login": "userlogin", "pwd":"***"} or, just run:
```
python parser.py
```
- Don't forget to check udata.json to see available users.

### 3.1. Run the Application
Start the Flask server:
```bash
python run.py
```
The application will run on `http://127.0.0.1:5000` by default.

---

## API Endpoints

### 1. **Home Route**
**`GET /`**
- Serves the `index.html` file from the `static` folder.

### 2. **Create Task**
**`POST /task/new`**
- Adds a new task.
- **Request Body**: JSON object with task details.
- **Response**: Task creation confirmation with the inserted ID.

### 3. **Retrieve All Tasks**
**`GET /task/`**
- Fetches all tasks in the database.
- **Response**: List of tasks.

### 4. **Retrieve a Specific Task**
**`GET /task/<id>`**
- Fetches a task by its ID.
- **Response**: Task details or 404 if not found.

### 5. **Update Task**
**`PUT /task/<id>`**
- Updates an existing task by its ID.
- **Request Body**: JSON object with updated task details.
- **Response**: Update confirmation or 404 if task not found.

### 6. **Delete Task**
**`DELETE /task/<id>`**
- Deletes a task by its ID.
- **Response**: Deletion confirmation or 404 if task not found.

### 7. **Delete All Tasks**
**`GET /task/tasks/reset`**
- Deletes all tasks in the database.
- **Response**: Confirmation of deletion.

---

## Error Handling
- **404 Page Not Found**: Custom HTML page for undefined routes.
- **Invalid Input**: Appropriate error messages for missing or invalid data.
- **Server Errors**: Catches unexpected exceptions and returns error details.

---

## Project Structure
```
/Backend
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
```
---

## Technologies Used
- **Flask**: Web framework for Python.
- **Flask-PyMongo**: MongoDB integration with Flask.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing.
- **MongoDB**: NoSQL database for storing tasks.
- **HTML**: For static file serving.
- **JWT**: For token auth

---

## Running Tests
You can use tools like Postman or cURL to test the API endpoints.

### Example with cURL
#### Create a Task:
```bash
curl -X POST http://127.0.0.1:5000/task/new \
-H "Content-Type: application/json" \
-d '{"title": "New Task", "description": "Details of the task"}'
```
#### Fetch All Tasks:
```bash
curl http://127.0.0.1:5000/task/
```
#### Update a Task:
```bash
curl -X PUT http://127.0.0.1:5000/task/<task_id> \
-H "Content-Type: application/json" \
-d '{"title": "Updated Task"}'
```
#### Delete a Task:
```bash
curl -X DELETE http://127.0.0.1:5000/task/<task_id>
```

---

## Acknowledgements
- Flask documentation: https://flask.palletsprojects.com/
- MongoDB documentation: https://www.mongodb.com/docs/

