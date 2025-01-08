import bcrypt
from flask_jwt_extended import create_access_token
from flask_injector import inject
from pydantic import EmailStr

from app.adapters.out.database.entities.user_entity import User
from app.domain.interfaces.user_interface import IUserRepository


class AuthenticateService:
    @inject
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def authenticate(self, email: EmailStr, password: str) -> str:
        user = self.repository.findOne(User.email == email)
        print(user.password)
        if not user:
            raise ValueError('Invalid email or password')

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise ValueError('Invalid email or password')

        token = create_access_token(identity={"id": user.id, "email": user.email})
        return token

