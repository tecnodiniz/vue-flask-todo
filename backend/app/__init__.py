from flask import Flask
from app.extensions import jwt, mongo
from app.routes import register_routes


def create_app():
    app = Flask(__name__)

    #Load Config
    app.config.from_object('app.config.Config')

    #Initialize Extensions
    jwt.init_app(app)
    mongo.init_app(app)

    #Register blueprints
    register_routes(app)
    
    return app

   
