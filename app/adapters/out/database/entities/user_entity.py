from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

from app.adapters.out.database.db import database
#database = Database()

class User(database.Base):
    __tablename__: str = 'user'
    __table_args__ = {'schema': 'public'}  # Explicit schema definition

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email: str = Column(String, index=True, unique=True, nullable=False)
    password: str = Column(String,  nullable=False)
    first_name: str = Column(String, index=True, nullable=False)
    last_name: str = Column(String, index=True, nullable=False)
    created_at: DateTime = Column(DateTime, nullable=False)
    updated_at: DateTime = Column(DateTime,  nullable=False, default=datetime.now(), onupdate=datetime.now())

    orders = relationship('Order', back_populates='user')