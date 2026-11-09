"""
SQLAlchemy ORM models for database migration.
"""

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class DBItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, unique=True, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)