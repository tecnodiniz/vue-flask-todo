from datetime import timedelta

class Config:
    SECRET_KEY = 'SECRET'
    JWT_SECRET_KEY = 'SECRET'
    MONGO_URI = 'mongodb://localhost:27017/todo'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10);
