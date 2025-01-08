from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.order_model import OrderModel


class UserModel:
    def __init__(self, id: Optional[int],
                 email: str,
                 firstname: str,
                 lastname: str,
                 password: Optional[str] | Optional[bytes] = None,
                 orders: Optional[List["OrderModel"]] = None,
                 created_at: Optional[str] = None):
        self.id = id
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.Order = orders or []
        self.created_at = created_at or ""

    def to_dict(self):
        if self.password is not None:
            del self.password # Remove the password field

        return self