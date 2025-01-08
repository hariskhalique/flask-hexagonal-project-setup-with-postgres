from flask_restx import Resource, Namespace
import logging
logger = logging.getLogger(__name__)
home_controller = Namespace('home', description="Root routes for the application")

@home_controller.route('/')
class Home(Resource):
    def get(self):
        """
        Root endpoint.
        Displays application information.
        """
        return {
            "message": "Welcome to the Flask application!",
            "status": "Running",
            "docs": "/api-docs"
        }