from app.routes.user import user_bp
from app.routes.task import task_bp
from app.routes.todo import todo_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(task_bp, url_prefix='/task')
    app.register_blueprint(todo_bp, url_prefix='/todo')