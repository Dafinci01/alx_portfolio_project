from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register the 'home' blueprint or module
    from .home import app as home_app
    app.register_blueprint(home_app)

    return app
