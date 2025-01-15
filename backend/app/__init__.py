from flask import Flask, send_from_directory
from app.extensions import jwt, mongo
from app.routes import register_routes
from app.main.routes import main_bp


def create_app():
    app = Flask('__name__')
    app.register_blueprint(main_bp)
    app.static_folder = 'app/static'

    #Load Config
    app.config.from_object('app.config.Config')

    #Initialize Extensions
    jwt.init_app(app)
    mongo.init_app(app)

    #Register blueprints
    register_routes(app)

   
    
    return app

   
