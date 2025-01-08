import uuid
from datetime import datetime

from sqlalchemy import Column, UUID, Float, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.adapters.out.database.db import database
#database = Database()
from app.adapters.out.database.entities.association_table import association_table


class Product(database.Base):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'public'}  # Explicit schema definition

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, unique=True, nullable=False)
    name: str = Column(String, nullable=False, index=True)
    price: float = Column(Float, nullable=False)
    amount: float = Column(Float, nullable=False)
    is_available: bool = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    orders = relationship('Order', secondary= association_table, back_populates='product')