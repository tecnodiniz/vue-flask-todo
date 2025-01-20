import json

from pymongo import MongoClient
from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    pwd: str
    user_login: str

def parse_user(data):
    return User(
        name=data["name"],
        user_login=data["user_login"],
        pwd=data["pwd"],
    )

def main():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["todo"]
    users_colletion = db["usuario"]

    #Read file
    with open("udata.json", "r") as file:
        data = json.load(file)["users"]

        #Parse data
        users = [parse_user(item) for item in data]
        users_dicts = [asdict(user) for user in users]

        users_colletion.insert_many(users_dicts)
    
    print("Users successfully importe")

if __name__ == '__main__':
    main()