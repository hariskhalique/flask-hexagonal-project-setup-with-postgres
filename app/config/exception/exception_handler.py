from flask import jsonify
from app.config.exception.exception import AppException
from logging import getLogger

logger = getLogger(__name__)

def register_exception_handler(app):
    @app.errorhandler(AppException)
    def handle_app_exception(error):
        """
        Handle application-specific exceptions.
        """
        logger.warning(f"AppException: {error.message} | Details: {error.details}")
        response = {
            "error": {
                "message": error.message,
                "details": error.details
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(Exception)
    def handle_exception(error):
        """
        Handle all other uncaught exceptions.
        """
        logger.error(f"Unhandled Exception: {error}", exc_info=True)
        response = {
            "error": {
                "message": "An unexpected error occurred.",
                "details": str(error)
            }
        }
        return jsonify(response), 500

    @app.errorhandler(404)
    def handle_404_error(error):
        """
        Handle 404 Not Found errors.
        """
        logger.warning("404 Not Found: %s", error)
        return jsonify({
            "error": "Not Found",
            "message": "The requested resource does not exist."
        }), 404