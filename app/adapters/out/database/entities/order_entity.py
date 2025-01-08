from datetime import datetime
import uuid
from sqlalchemy import Column, Integer, ForeignKey, DateTime, UUID
from sqlalchemy.orm import relationship

from app.adapters.out.database.db import database
#database = Database()

from app.adapters.out.database.entities.association_table import association_table


class Order(database.Base):
    __tablename__ = 'order'
    __table_args__ = {'schema': 'public'}  # Explicit schema definition

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), index=True, unique=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey('public.user.id'), index=True)
    created_at: DateTime = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at: DateTime = Column(DateTime, onupdate=datetime.now(), default=datetime.now)

    # Relationships
    user = relationship('User', back_populates='orders') # User bidirectional relation
    product = relationship('Product',
                           secondary= association_table ,
                           back_populates='orders') # Product bidirectional many to many