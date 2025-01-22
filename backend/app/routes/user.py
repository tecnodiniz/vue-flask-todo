from datetime import datetime, timezone
from flask import Blueprint, jsonify, request
from bson import ObjectId
from app.extensions import mongo, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from app.services.utils import validadeUser, check_token_in_blacklist

user_bp = Blueprint('user',__name__)

@user_bp.route('/auth', methods=['POST'])
def auth_user():
    try:
        data = request.get_json()
        userlogin = data.get('username')
        password = data.get('password')

        user = mongo.db.usuario.find_one({"user_login":userlogin, "pwd":password})

        if user:
            access_token = create_access_token(identity=str(user['_id']), )
            return jsonify({'token': access_token}),200
        
        return jsonify({'msg': 'Invalid credentials'}), 401
    except TypeError as te:
        return jsonify({f'Type error {str(te)}'})
    except Exception as e:
        return jsonify({f'An unexpected error occurred {str(e)}'})
    
@user_bp.route('/new', methods=['POST'])
def create_user():
    try:
        data = request.json
        if data:
            result = mongo.db.usuario.insert_one(data)
            return jsonify({'msg': 'user succefuly created!','id': str(result.inserted_id)}), 201
        return jsonify({'msg': 'Inválid format'}), 400
            
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@user_bp.route('', methods=['GET'])
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
    
@user_bp.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    mongo.db["blacklist"].insert_one({"jti":jti, "created_at": now})
    return jsonify({"msg": "Successfully signed out"})

@jwt.token_in_blocklist_loader
def blacklist_token(jwt_header, jwt_payload):
    return check_token_in_blacklist(jwt_header,jwt_payload)
