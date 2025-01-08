from typing import List

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.adapters.out.database.db import session
from app.adapters.out.database.entities.user_entity import User
from app.adapters.out.database.mappers.user_mapper import user_entity_to_model, user_model_to_entity
from app.domain.models.user_model import UserModel
from app.domain.interfaces.user_interface import IUserRepository
from logging import getLogger
logger = getLogger(__name__)

class UserRepository(IUserRepository):
    def __init__(self):
        self.session = session()

    def find(self) -> List[UserModel]:
        try:
            users = self.session.query(User).all()
            return [user_entity_to_model(user) for user in users]
        except Exception as e:
            logger.error(e)
            return []

    def findOne(self, where, fields=None) -> UserModel or None:
        try:
            stmt = select(*fields) if fields else select(User)
            stmt = stmt.where(where)
            result = self.session.execute(stmt).scalar()
            return user_entity_to_model(result)
        except Exception as e:
            logger.error(e)
            return None

    def insert(self, user: UserModel) -> UserModel or None:
        try:
            user_entity = user_model_to_entity(user)
            self.session.add(user_entity)
            self.session.commit()
            return user_entity_to_model(user_entity)
        except Exception as e:
            logger.error(e)
            return None

    def update(self, user_id: int, user: UserModel) -> UserModel or None:
        try:
            existing_user: User = self.session.query(User).filter(User.id == user_id).first()
            if not existing_user:
                raise ValueError("User not found")

            existing_user.first_name = user.firstname
            existing_user.last_name = user.lastname
            existing_user.email = user.email
            self.session.commit()
            return user_entity_to_model(existing_user)
        except Exception as e:
            logger.error(e)
            return None