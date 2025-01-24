from pymongo import MongoClient
from bson import ObjectId

URI = "mongodb://localhost:27017/todo"
client = MongoClient(URI)
try:

    db = client["todo"]
    if not 'todos' in db.list_collection_names():
        cursor = db.usuario.find()
        users = list(cursor)

        if users:
            for user in users:
                res = db.todos.insert_one({"user_id": ObjectId(user["_id"]), "name": "Defaul List", "description": "Initial todo" })
                print(f"Todo created for: user: { user['user_login'] } - todo_id: {str(ObjectId(res.inserted_id))} \n")

                tasks = db.list.update_many({
                   "user_id": ObjectId(user["_id"])
                   },
                   {
                    "$set": {"todo_id": ObjectId(res.inserted_id)},
                    "$unset": {"user_id": ""}
                    })
                print(f"Documentos atualizados: {tasks.modified_count}")
            
            res = db.list.delete_many({"user_id": {"$exists": True}})
            print(f"Tasks sem usuários deletadas: {res.deleted_count}")
        else:
            print("Users not found")
    else: 
        print("A Atualização já foi feita")

except Exception as e:
    print(e)


