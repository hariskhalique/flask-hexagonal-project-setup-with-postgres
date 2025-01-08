import bcrypt
from flask_injector import inject

from app.adapters.out.database.entities.user_entity import User
from app.domain.interfaces.user_interface import IUserRepository
from app.domain.models.user_model import UserModel


class UserService:
    @inject
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def register(self, user: UserModel) -> UserModel:
        if self.repository.findOne(User.email == user.email):
            raise ValueError('Email already registered')

        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user = UserModel(
            id=None,
            email=user.email,
            password=hashed_password,
            firstname=user.firstname,
            lastname=user.lastname,
        )
        user = self.repository.insert(user)
        return user.to_dict()