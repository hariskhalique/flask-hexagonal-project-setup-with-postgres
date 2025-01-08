from flask import Flask, jsonify
from flask_injector import FlaskInjector
from flask_jwt_extended import JWTManager

from app.adapters.http.authenticate_controller import auth_controller
from app.adapters.http.home_controller import home_controller
from flask_restx import Api

from app.adapters.http.user_controller import user_controller
from app.adapters.out.database.db import db, database
from app.config.config import appConfig
from flask_migrate import Migrate

from app.config.services_registry import register_dependencies

api = Api(
    title="Flask Application API",
    version="1.0",
    description="API documentation for the Flask application",
)

def app_module(application: Flask):
    """
    Register application-level modules such as controllers, services, etc.
    """

    # Initialize JWT
    JWTManager(application)

    # Setting Up env variable
    application.config.from_object(appConfig)

    # Import models to register them
    import app.adapters.out.database.models

    # Initialize SQLAlchemy
    db.init_app(application)

    print("Registered Tables:", database.Base.metadata.tables.keys())
    print(application.config['SQLALCHEMY_DATABASE_URI'])

    # Initialize DB Migration with Base.metadata
    Migrate(application,
            db,
            directory="migrations",
            compare_type=True,
            render_as_batch=True
            )
    # Register controllers
    api.add_namespace(home_controller)
    api.add_namespace(auth_controller)
    api.add_namespace(user_controller)


    # Register API conditionally
    if appConfig.FLASK_ENV == "developments":
        # Attach API with Swagger documentation enabled
        api.init_app(application)
    else:
        # Attach API without Swagger documentation
        api.init_app(application, add_specs=False)


    # Integrate Flask-Injector
    FlaskInjector(app=application, modules=[register_dependencies])