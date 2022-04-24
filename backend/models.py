"""     Contains the models for the database used by sqlalchemy for ORM.    """
# Setup reference: https://fastapi.tiangolo.com/tutorial/sql-databases/
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    # name of the table in the database
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    photo = Column(String(255), index=True)
    balance = Column(Float, index=True)


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    amount = Column(Float, index=True, nullable=False)
    did_buy = Column(Boolean, index=True, nullable=False)
    timestamp = Column(DateTime, index=True, nullable=False)
    stock_name = Column(String(255), index=True, nullable=False)

class Stock(Base):

    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    stock_name = Column(String(255), index=True, nullable=False, unique=True)
    amount = Column(Float, index=True, nullable=False, default=0.0)