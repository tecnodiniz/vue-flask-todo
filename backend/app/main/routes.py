from flask import Blueprint, render_template, send_from_directory, current_app

main_bp = Blueprint('main', __name__, template_folder='../templates', static_folder='static')


@main_bp.route('/')
def root():
    # Serves the index.html file inside the static_folder
    return send_from_directory(current_app.static_folder, 'index.html')


@main_bp.route('/<path:path>')
def serve_static_files(path):
    """
    Serves static files like CSS, JS, images, etc.
    If the requested file is not found, it redirects to index.html for Vue SPA routes.
    """
    try:
        return send_from_directory(current_app.static_folder, path)
    except:
        # Redirect to index.html for unrecognized routes (Vue handles them)
        return send_from_directory(current_app.static_folder, 'index.html')


@main_bp.errorhandler(404)
def page_not_found(e):
    """
    Redirect 404 errors to the Vue's index.html
    """
    return send_from_directory(current_app.static_folder, "index.html")
