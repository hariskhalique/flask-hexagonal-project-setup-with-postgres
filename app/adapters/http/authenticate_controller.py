from logging import getLogger

from flask import request
from flask_restx import Namespace, fields, Resource
from injector import inject
from pydantic import ValidationError

from app.application.user_login_usecase import UserLoginUseCase
from app.domain.dto.login_dto import LoginDto

logger = getLogger(__name__)
auth_controller = Namespace("auth", description="Authentication controller")
login_model = auth_controller.model("Login", {
    "email": fields.String(required=True, description="Email address"),
    "password": fields.String(required=True, description="Password"),
})

@auth_controller.route("/login", endpoint="login")
class Login(Resource):
    @inject
    def __init__(self, user_login_use_case: UserLoginUseCase, *args, **kwargs):
        """
        Initialize the Login resource with injected dependencies.
        """
        super().__init__(*args, **kwargs)
        self.user_login_use_case = user_login_use_case

    @auth_controller.expect(login_model)
    def post(self):  # Inject the dependency
        """
        Authenticate user and return JWT token.
        """
        try:
            data = request.get_json()
            login_dto = LoginDto(**data)
            # Use the injected instance
            return self.user_login_use_case.execute(
                email=login_dto.email,
                password=login_dto.password
            ), 200
        except ValidationError as e:
            logger.error(e)
            return {"errors": e.errors()}, 400
        except ValueError as e:
            logger.error(e)
            return {"errors": str(e)}, 401