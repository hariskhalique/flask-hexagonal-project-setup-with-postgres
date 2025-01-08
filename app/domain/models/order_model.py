from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import UUID

if TYPE_CHECKING:
    from app.domain.models.product_model import ProductModel
    from app.domain.models.user_model import UserModel


class OrderModel:
    def __init__(self, id: Optional[UUID],
                 created_at: Optional[str] = None,
                 user: Optional[List[UserModel]] = None,
                 products: Optional[List[ProductModel]] = None,):
        self.id = id
        self.created_at = created_at
        self.updated_at = None
        self.user = user
        self.products = products or []