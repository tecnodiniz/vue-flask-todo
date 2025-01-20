from flask import Blueprint, render_template, send_from_directory, current_app

main_bp = Blueprint('main', __name__, template_folder='../templates', static_folder='static')

@main_bp.route('/')
def root():
# Serves the index.html file inside the static_folder
    return send_from_directory(current_app.static_folder, 'index.html')

@main_bp.route('/<path:path>')
def serve_static_files(path):
    
# Serves any file within the static_folder (CSS, JS, images, etc.)
    return send_from_directory(current_app.static_folder, path)


@main_bp.route('/error')
def error():
    return render_template('error.html', message='MongoDB connection failed! Please check the database server.')

@main_bp.errorhandler(404)
def page_not_found(e):
   return render_template('404.html')