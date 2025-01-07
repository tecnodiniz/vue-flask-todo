import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_from_directory
from bson import ObjectId
from flask_pymongo import PyMongo
from flask_cors import CORS

load_dotenv()

app = Flask('__name__', static_folder="static")

# app.config["MONGO_URI"] = os.getenv("MONGO_URI")

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo"

mongo = PyMongo(app)

CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# POST TASK
@app.route('/tasks', methods=["POST"])
def create_taks():
    try:
        data = request.json

        if data:
            result = mongo.db.list.insert_one(data)
            return jsonify({"msg": "Taks adicionada", "id": str(result.inserted_id)}), 201
        return jsonify({"erro":"O formato dos dados é inválido"}), 400
    except Exception as e:
        return jsonify({"error": str(e)})

# GET ALL
@app.route('/tasks')
def tasks():
    try:
        cursor = mongo.db.list.find({})
        tasks = list(cursor)

        if tasks:
            for task in tasks:
                task["_id"] = str(task["_id"])
        
        return jsonify({"data":tasks}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# GET TASK
@app.route('/tasks/<id>', methods=["GET"])
def get_task(id):
    try:
        if not ObjectId(id):
            return jsonify({"msg":"Id inválida"})
        
        data = mongo.db.list.find_one({"_id": ObjectId(id)})

        if not data:
            return jsonify({"msg": "Task não encontrada"}), 404
        
        data["_id"] = str(data["_id"])
        return jsonify({"task":data}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)})
    

# UPDATE TASK
@app.route('/tasks/<id>', methods=["PUT"])
def update_task(id):
    try:
        if not ObjectId(id):
            return jsonify({"error": "Id inválida"}),400
        
        data = request.json
        if not data:
            return jsonify({"erro":"Nenhum dado inserido para atualização"}),400

        result = mongo.db.list.update_one({"_id": ObjectId(id)}, {"$set":data})

        if result.matched_count == 0:
            return jsonify({"erro":"Task não encontrada"}),404
        
        return jsonify({"msg":"Task atualizada"}), 201

    except Exception as e:
        return jsonify({"error": str(e)})

# DELETE TASK
@app.route('/tasks/<id>', methods=["DELETE"])
def delete_task(id):
    try:
        if not ObjectId(id):
            return jsonify({"msg":"Id inválida"})
        
        result = mongo.db.list.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 0:
            return jsonify({"msg": "Taks não encontrada"}), 404
        
        return jsonify({"msg": "Task excluida", "id": id}),200
        
    except Exception as e:
        return jsonify({"error": str(e)})

# DELETE ALL
@app.route('/tasks/reset', methods=["GET"])
def delete_all():
    try:
        result = mongo.db.list.delete_many({})

        if result.deleted_count == 0:
            return jsonify({"msg":"Nenhum item foi excluido"}),200
        return jsonify({"msg":"Todos os itens foram excluídos"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
