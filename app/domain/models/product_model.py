from typing import Optional, List, TYPE_CHECKING

from sqlalchemy import UUID
if TYPE_CHECKING:
    from app.domain.models.order_model import OrderModel


class ProductModel:
    def __init__(self, id: Optional[UUID],
                 name: str,
                 price: float,
                 amount: float,
                 is_available: bool,
                 created_at: Optional[str] = None):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount
        self.is_available = is_available
        self.created_at = created_at
        self.updated_at = None
        self.order = Optional[List[OrderModel]] or []