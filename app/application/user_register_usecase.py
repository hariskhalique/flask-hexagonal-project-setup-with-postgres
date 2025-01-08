from flask import jsonify
from injector import inject

from app.domain.models.user_model import UserModel
from app.domain.services.user_service import UserService


class UserRegisterUseCase:
    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, user: UserModel):
        user = self.user_service.register(user)
        return jsonify(user.__dict__)