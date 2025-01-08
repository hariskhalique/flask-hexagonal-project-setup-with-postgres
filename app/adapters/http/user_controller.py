from logging import getLogger

from flask import request
from flask_restx import Namespace, fields, Resource
from injector import inject
from pydantic import ValidationError

from app.application.user_register_usecase import UserRegisterUseCase
from app.domain.dto.register_dto import RegisterDTO

logger = getLogger(__name__)
user_controller = Namespace('user', description='User related operations')

register_model = user_controller.model('Register', {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
})

@user_controller.route('/register', endpoint='register')
class Register(Resource):
    @inject
    def __init__(self, user_register: UserRegisterUseCase, *args, **kwargs):
        """
        Initialize the Login resource with injected dependencies.
        """
        super().__init__(*args, **kwargs)
        self.user_register = user_register

    @user_controller.expect(register_model)
    def post(self):
        """
        Register user and return user object with id, email, first_name, last_name
        """
        try:
            data = request.get_json()
            user = RegisterDTO(**data)
            return self.user_register.execute(user)
        except ValidationError as e:
            logger.error(e)
            return {'error': e.errors()}, 400
        except ValueError as e:
            logger.error(e)
            return {'error': str(e)}, 400
