from app.extensions import mongo
from bson import ObjectId


def check_token_in_blacklist(jwt_header,jwt_payload):
     jti = jwt_payload["jti"]

     token = mongo.db["blacklist"].find_one({"jti":jti})

     return token is not None

def validadeUser(identity):
    if not ObjectId.is_valid(identity):
          return False
     
    return bool(mongo.db.usuario.find_one({"_id": ObjectId(identity)}))