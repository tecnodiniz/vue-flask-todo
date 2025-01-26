from flask import Blueprint, jsonify, request
from bson import ObjectId
from app.extensions import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.utils import validadeUser

todo_bp = Blueprint('todo',__name__)

@todo_bp.route('/new', methods=['POST'])
@jwt_required()
def create_todo():
    try:
        data = request.json
        if validadeUser(get_jwt_identity()):
            data["user_id"] = ObjectId(get_jwt_identity())
            res = mongo.db.todos.insert_one(data)

            return jsonify({"msg": "Todo created", "id": str(ObjectId(res.inserted_id))}), 200

        return jsonify({"msg": "Invalid Token"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@todo_bp.route('/', methods=['GET'])
@jwt_required()
def get_todos():
    try:
        if(validadeUser(get_jwt_identity())):
            user_id = ObjectId(get_jwt_identity())
            cursor = mongo.db.todos.find({"user_id": user_id})
            todos = list(cursor)

            for todo in todos:
                todo["_id"] = str(todo["_id"])
                todo["user_id"] = str(todo["user_id"])
        
            return jsonify({"todos": todos}), 200
        return jsonify({"msg": "Invalid token"}),401
    except Exception as e:
        return jsonify({"error": str(e)})
    
@todo_bp.route('/<id>', methods=['PUT'])
@jwt_required()
def edit_todo(id):
    try:
        data = request.json

        if not data:
            return jsonify({'msg':'Nenhum dado inserido para atualização'}),400
        
        if(validadeUser(get_jwt_identity())):
            result = mongo.db.todos.update_one({"_id": ObjectId(id)}, {"$set": data})
            
            if result.matched_count == 0:
                return jsonify({'msg':'Todo não encontrado'}),404
        
            return jsonify({'msg':'Todo atualizado'}), 201
        return jsonify({'msg': 'Invalid Token'}), 401
        
    except Exception as e:
        return jsonify({"error": str(e)})