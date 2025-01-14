from app.extensions import mongo
from bson import ObjectId


def validadeUser(identity):
    if not ObjectId.is_valid(identity):
          return False
     
    return bool(mongo.db.usuario.find_one({"_id": ObjectId(identity)}))
