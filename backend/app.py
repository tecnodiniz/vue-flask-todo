import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for, redirect
from bson import ObjectId
from flask_cors import CORS
from auth import login, token_require
from flask_pymongo import PyMongo
from pymongo.errors import ConnectionFailure


load_dotenv()

app = Flask('__name__', static_folder='static')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'

# app.config['MONGO_URI'] = os.getenv('MONGO_URI')

app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'

CORS(app)

mongo = PyMongo(app)


@app.route('/')
def index():
    try:
        mongo.db.command('ping')
        return send_from_directory(app.static_folder, 'index.html')
    except ConnectionFailure:
        return redirect(url_for('error'))
    

# Handle errors
@app.route('/error')
def error():
    return render_template('error.html', message='MongoDB connection failed! Please check the database server.')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# POST TASK
@app.route('/tasks', methods=['POST'])
def create_taks():
    try:
        data = request.json

        if data:
            result = mongo.db.list.insert_one(data)
            return jsonify({'msg': 'Taks adicionada', 'id': str(result.inserted_id)}), 201
        return jsonify({'erro':'O formato dos dados é inválido'}), 400
    except Exception as e:
        return jsonify({'error': str(e)})

# GET ALL
@app.route('/tasks')
def tasks():
    try:
        cursor = mongo.db.list.find({})
        tasks = list(cursor)

        if tasks:
            for task in tasks:
                task['_id'] = str(task['_id'])
        
        return jsonify({'data':tasks}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# GET TASK
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({'msg':'Id inválida'})
        
        data = mongo.db.list.find_one({'_id': ObjectId(id)})

        if not data:
            return jsonify({'msg': 'Task não encontrada'}), 404
        
        data['_id'] = str(data['_id'])
        return jsonify({'task':data}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)})
    

# UPDATE TASK
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({'error': 'Id inválida'}),400
        
        data = request.json
        if not data:
            return jsonify({'erro':'Nenhum dado inserido para atualização'}),400

        result = mongo.db.list.update_one({'_id': ObjectId(id)}, {'$set':data})

        if result.matched_count == 0:
            return jsonify({'erro':'Task não encontrada'}),404
        
        return jsonify({'msg':'Task atualizada'}), 201

    except Exception as e:
        return jsonify({'error': str(e)})

# DELETE TASK
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({'msg':'Id inválida'})
        
        result = mongo.db.list.delete_one({'_id': ObjectId(id)})

        if result.deleted_count == 0:
            return jsonify({'msg': 'Taks não encontrada'}), 404
        
        return jsonify({'msg': 'Task excluida', 'id': id}),200
        
    except Exception as e:
        return jsonify({'error': str(e)})


# DELETE ALL
@app.route('/tasks/reset', methods=['GET'])
@token_require
def delete_all():
    try:
        result = mongo.db.list.delete_many({})

        if result.deleted_count == 0:
            return jsonify({'msg':'Nenhum item foi excluido'}),200
        return jsonify({'msg':'Todos os itens foram excluídos'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    


# LOGIN PAGE
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# AUTH
@app.route('/auth', methods=['POST'])
def auth_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        return login(username,password)
    except TypeError as te:
        return jsonify({f'Type error {str(te)}'})
    except Exception as e:
        return jsonify({f'An unexpected error occurred {str(e)}'})


@app.route('/protected', methods=['GET'])
@token_require
def protected_route(current_user):
    return jsonify({'message':f'Hello, {current_user}! This is a protected route.'})

if __name__ == '__main__':
    app.run(debug=True)
