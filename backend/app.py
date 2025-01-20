from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for, redirect
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from bson import ObjectId
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo.errors import ConnectionFailure
from datetime import timedelta

load_dotenv()

app = Flask('__name__', static_folder='static')

app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'
app.config["JWT_SECRET_KEY"] = "SECRET"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

jwt = JWTManager(app)
# app.config['MONGO_URI'] = os.getenv('MONGO_URI')

app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo'

CORS(app)

mongo = PyMongo(app)



@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_static_files(path):
    if path == "" or path == "index.html":
        mongo.db.command('ping')
        return send_from_directory(app.static_folder, "index.html")
    else:
        return send_from_directory(app.static_folder, path)

    
# Handle errors
@app.route('/error')
def error():
    return render_template('error.html', message='MongoDB connection failed! Please check the database server.')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# ---------------------------START TASKS-----------------------------------------------------------------
# POST TASK
@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_taks():
    try:
        if validadeUser(get_jwt_identity()):
            user_id = get_jwt_identity()
            data = request.json
            data["user_id"] = ObjectId(user_id)

            if data:
                result = mongo.db.list.insert_one(data)
                return jsonify({'msg': 'Taks adicionada', 'id': str(result.inserted_id)}), 201
            return jsonify({'erro':'O formato dos dados é inválido'}), 400
        return jsonify({'msg':'Inválid Token'}), 401
    except Exception as e:
        return jsonify({'error': str(e)})

# GET ALL
@app.route('/tasks')
@jwt_required()
def tasks():
    try:
        if validadeUser(get_jwt_identity()):
            user_id = get_jwt_identity()
            cursor = mongo.db.list.find({"user_id": ObjectId(user_id)})
            tasks = list(cursor)

            if tasks:
                for task in tasks:
                    task['_id'] = str(task['_id'])
                    task['user_id'] = str(task['user_id'])
            
            return jsonify({'tasks':tasks}), 200
        return jsonify({'msg': 'Invalid Token'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# GET TASK
@app.route('/tasks/<id>', methods=['GET'])
@jwt_required()
def get_task(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({'msg':'Id inválida'})
        
        data = mongo.db.list.find_one({'_id': ObjectId(id)})

        if not data:
            return jsonify({'msg': 'Task não encontrada'}), 404
        
        data['_id'] = str(data['_id'])
        data['user_id'] = str(data['user_id'])

        if validadeUser(get_jwt_identity()) and get_jwt_identity() == data["user_id"]:
            return jsonify({'task':data}), 200
        return jsonify({'msg': 'Invalid Token'}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)})
    

# UPDATE TASK
@app.route('/tasks/<id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({'error': 'Id inválida'}),400
    
        data = request.json
 
        if not data:
            return jsonify({'erro':'Nenhum dado inserido para atualização'}),400

        if validadeUser(get_jwt_identity()):
            result = mongo.db.list.update_one({'_id': ObjectId(id), 'user_id': ObjectId(get_jwt_identity())}, {'$set':data})

        if result.matched_count == 0:
            return jsonify({'erro':'Task não encontrada'}),404
        
        return jsonify({'msg':'Task atualizada'}), 201

    except Exception as e:
        return jsonify({'error': str(e)})

# DELETE TASK
@app.route('/tasks/<id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({'msg':'Id inválida'})
        
        if validadeUser(get_jwt_identity()):
            result = mongo.db.list.delete_one({'_id': ObjectId(id), 'user_id':ObjectId(get_jwt_identity())})

        if result.deleted_count == 0:
            return jsonify({'msg': 'Taks não encontrada'}), 404
        
        return jsonify({'msg': 'Task excluida', 'id': id}),200
        
    except Exception as e:
        return jsonify({'error': str(e)})


# DELETE ALL
@app.route('/tasks/reset', methods=['GET'])
@jwt_required()
def delete_all():
    try:
        result = mongo.db.list.delete_many({"user_id": ObjectId(get_jwt_identity())})

        if result.deleted_count == 0:
            return jsonify({'msg':'Nenhum item foi excluido'}),200
        return jsonify({'msg':'Todos os itens foram excluídos'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    
# ---------------------------END TASKS-----------------------------------------------------------------



# ---------------------------AUTHENTICATION-----------------------------------------------------------------


# AUTH
@app.route('/auth', methods=['POST'])
def auth_user():
    try:
        data = request.get_json()
        userlogin = data.get('username')
        password = data.get('password')

        user = mongo.db.usuario.find_one({"user_login":userlogin, "pwd":password})

        if user:
            access_token = create_access_token(identity=str(user['_id']), )
            return jsonify({'token': access_token}),200
        
        return jsonify({'error': 'Invalid credentials'}), 401
    except TypeError as te:
        return jsonify({f'Type error {str(te)}'})
    except Exception as e:
        return jsonify({f'An unexpected error occurred {str(e)}'})


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
   
    return jsonify({'message':f'Hello! This is a protected route.','user_id':current_user})

# Verify if token is assign to a user
def validadeUser(identity):
    return bool(mongo.db.usuario.find_one({"_id": ObjectId(identity)}))

# ---------------------------END AUTHENTICATION-----------------------------------------------------------------


# ---------------------------START USERS-----------------------------------------------------------------

@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        if data:
            result = mongo.db.usuario.insert_one(data)
            return jsonify({'msg': 'user succefuly created!','id': str(result.inserted_id)}), 201
        return jsonify({'msg': 'Inválid format'}), 400
            
    except Exception as e:
        return jsonify({'erro': str(e)}), 500



@app.route('/users', methods=['GET'])
@jwt_required()
def get_username():
    try:
        login = request.args.get('login', default=None)
        if(validadeUser(get_jwt_identity())):
            user = mongo.db.usuario.find_one({'user_login': login, '_id': ObjectId(get_jwt_identity())})
            if not user:
                return jsonify({'msg': 'User not found'}), 404
            
            user['_id'] = str(user['_id'])
            
            return jsonify({'user': user['name']})
        return jsonify({'msg': 'Inválid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        if not ObjectId(id):
            return jsonify({'msg': 'Invalid Id'}), 401
        
        data = request.json

        result = mongo.db.usuario.update_one({'_id': ObjectId(id)}, {'$set': data})

        if result.matched_count == 0:
            return jsonify({'msg': 'user not found'}), 404
        return jsonify({'msg': 'Password updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
