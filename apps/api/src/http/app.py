from flask import Flask
from src.http.routes_health import health_bp
from src.http.responses import register_error_handlers

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["TESTING"] = testing
    register_error_handlers(app)
    app.register_blueprint(health_bp)
    return app