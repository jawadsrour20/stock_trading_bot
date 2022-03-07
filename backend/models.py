"""     Contains the models for the database used by sqlalchemy for ORM.    """
# Setup reference: https://fastapi.tiangolo.com/tutorial/sql-databases/
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
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