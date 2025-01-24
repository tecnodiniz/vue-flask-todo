from flask import Blueprint, jsonify, request
from bson import ObjectId
from app.extensions import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.utils import validadeUser


task_bp = Blueprint('task',__name__)

# New Task
@task_bp.route('/new', methods=['POST'])
@jwt_required()
def create_taks():
    try:
        if validadeUser(get_jwt_identity()):
            data = request.json
            data["todo_id"] = ObjectId(data["todo_id"])
            if data:
                result = mongo.db.list.insert_one(data)
                return jsonify({'msg': 'Taks adicionada', 'id': str(result.inserted_id)}), 201
            return jsonify({'msg':'O formato dos dados é inválido'}), 400
        return jsonify({'msg':'Inválid Token'}), 401
    except Exception as e:
        return jsonify({'error': str(e)})
    
# Get Tasks
@task_bp.route('', methods=['GET'])
@jwt_required()
def get_tasks():
    try:
        if validadeUser(get_jwt_identity()):
            todo_id = request.args.get('todo', default=None)
            cursor = mongo.db.list.find({"todo_id": ObjectId(todo_id)})
            tasks = list(cursor)

            if tasks:
                for task in tasks:
                    task['_id'] = str(task['_id'])
                    task['todo_id'] = str(task['todo_id'])
            
            return jsonify({'tasks':tasks}), 200
        return jsonify({'msg': 'Invalid Token'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET TASK
@task_bp.route('/<id>', methods=['GET'])
@jwt_required()
def get_task(id):
    try:
        if validadeUser(get_jwt_identity()):
            data = mongo.db.list.find_one({'_id': ObjectId(id)})

            if not data:
                return jsonify({'msg': 'Task não encontrada'}), 404
        
            data['_id'] = str(data['_id'])
          

            
            return jsonify({'task':data}), 200
        
        return jsonify({'msg': 'Invalid Token'}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)})

# UPDATE TASK
@task_bp.route('/<id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    try:
        data = request.json

        if not data:
            return jsonify({'msg':'Nenhum dado inserido para atualização'}),400

        if validadeUser(get_jwt_identity()):
            result = mongo.db.list.update_one({'_id': ObjectId(id)}, {'$set':data})

            if result.matched_count == 0:
                return jsonify({'msg':'Task não encontrada'}),404
        
            return jsonify({'msg':'Task atualizada'}), 201
        return jsonify({'msg': 'Invalid Token'}), 401

    except Exception as e:
        return jsonify({'error': str(e)})

# DELETE TASK
@task_bp.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    try: 
        if validadeUser(get_jwt_identity()):
            result = mongo.db.list.delete_one({'_id': ObjectId(id)})

            if result.deleted_count == 0:
                return jsonify({'msg': 'Taks não encontrada'}), 404
        
            return jsonify({'msg': 'Task excluida', 'id': id}),200
        return jsonify({'msg': 'Invalid token'}),401
        
    except Exception as e:
        return jsonify({'error': str(e)})

# DELETE ALL
@task_bp.route('/tasks/reset', methods=['GET'])
@jwt_required()
def delete_all():
    try:
        if validadeUser(get_jwt_identity()):
            todo_id =request.args.get('todo',default=None) 
            result = mongo.db.list.delete_many({"todo_id": ObjectId(todo_id)})

            if result.deleted_count == 0:
                return jsonify({'msg':'Nenhum item foi excluido'}),200
            return jsonify({'msg':'Todos os itens foram excluídos'}), 200
        return jsonify({'msg': 'Invalid Token'}), 401
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    