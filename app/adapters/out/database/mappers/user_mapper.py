from datetime import datetime

from app.adapters.out.database.entities.user_entity import User
from app.domain.models.user_model import UserModel


def user_entity_to_model(user: User) -> UserModel:
    return UserModel(
        id=user.id,
        email=user.email,
        firstname=user.first_name,
        lastname=user.last_name,
        orders=user.orders,
        created_at=user.created_at,
        password=user.password,
    )

def user_model_to_entity(user: UserModel) -> User:
    return User(
        email=user.email,
        first_name=user.firstname,
        last_name=user.lastname,
        password=user.password.decode("utf8"),
        created_at= datetime.now(),
    )