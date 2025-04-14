from flask import Flask
from flask_cors import CORS
from .db import init_db
from .routes import task_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db()
    app.register_blueprint(task_routes)

    return app
