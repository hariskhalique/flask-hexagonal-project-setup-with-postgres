from flask import Flask, jsonify
from app.config.config import appConfig
from app.config.exception.exception_handler import register_exception_handler
from app.config.logging.logging_config import setup_logging
from app.app_module import app_module

def create_app():
    app = Flask(__name__)

    # Register application modules
    app_module(app)

    # Register global exception handlers
    register_exception_handler(app)

    # Set up logging
    setup_logging()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=appConfig.FLASK_DEBUG)