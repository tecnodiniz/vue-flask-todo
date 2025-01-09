from bson import ObjectId
import jwt
from datetime import datetime, timedelta, timezone
from flask import jsonify, request, redirect, url_for
from functools import wraps
import app

SECRET_KEY = "@@l0ck3d0u7@@"

# Mock Test
users = {
    "user1":"password123",
    "user2":"password456",
}

#Create JWT Token
def create_token(user):
    expiration_time = datetime.now(timezone.utc) + timedelta(hours=1)
    payload = {
        'user_id': user['_id'],
        'username': user['name'],
        'exp': expiration_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return token


# Decorator to protect routes that require authentication
def token_require(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1] # Bearer <token>
        if not token:
            return redirect(url_for('login_page'))
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            
            # mongo = app.mongoConnect()
            
            if not ObjectId.is_valid(payload["user_id"]):
                return jsonify({'error': 'Invalid Id'}), 400
                
            
            user = app.mongo.db.usuario.find_one({'_id': ObjectId(payload["user_id"])})
                
            if user:
                current_user = payload['username'] 
            else:
                return jsonify({'msg': 'User not found in the database'}), 404


        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired! Please log in again."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message":"Invalid token! Please log in again."}), 401
        except Exception as e:
            return jsonify({"message": f'An error ocurred:{str(e)} '}), 500
        
        return f(current_user, *args, ** kwargs)
    return decorator

#Handle user login and return token if credentials are valid
def login(username,password):
    try:
        user = app.mongo.db.usuario.find_one({'user_login':username, 'pwd':password})
        if user:
            user["_id"] = str(user["_id"])
            token = create_token(user)
            return jsonify({'token':token}), 200
        # if username in users and users[username] == password:
        #     token = create_token(username)
        #     return jsonify({"token": token}), 200
        
        else:
            return jsonify({"message":"Invalid credentials"}), 401
    except TypeError as te:
        return jsonify({f'type error: {str(te)}'})
    except Exception as e:
        return jsonify({"message":f"An error ocurred during login: {str(e)}"}),500