from typing import TypeVar, List, Optional
from app.domain.models.user_model import UserModel


class IUserRepository:
    def find(self) -> List[UserModel]:
        """
        Find all records.
        """
        raise NotImplementedError()
    def findOne(self, identifier) -> Optional[UserModel]:
        """
        Find a single record by identifier.
        """
        raise NotImplementedError()
    def update(self, identifier, model: UserModel) -> UserModel:
        """
        Add a new record.
        """
        raise NotImplementedError()
    def insert(self, user: UserModel) -> UserModel:
        """
        Update an existing record.
        """
        raise NotImplementedError()