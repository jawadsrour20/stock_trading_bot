"""
    Here we define the schemas for the pydantic models.
    we need pydantic for the authentication process + object Models
    we will be re-defining a similar User class for sqlalchemy for ORM usage

"""
# Setup reference: https://fastapi.tiangolo.com/tutorial/sql-databases/

from pydantic import BaseModel
from typing import Optional
import datetime

# UserBase Pydantic model (or let's say "schema") to have common attributes while creating or reading data.
class UserBase(BaseModel):
    email: str # Required field
    username: str # Required field
    first_name: str # Required field
    last_name: str # Required field
    photo: Optional[str] = None # Optional field
    balance: Optional[float] = None # Optional field

# Used for Creating a user
class UserCreate(UserBase):
    password: str # Required field


# Before creating an item, we don't know what will be the ID assigned to it,
# but when reading it (when returning it from the API) we will already know its ID.

# Used for Reads when fetching a user
class User(UserBase):
    id: int # after the user is created, we know user id

    # in the Pydantic models for reading, add an internal Config class; used to provide configurations to Pydantic
    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    user_id: int
    amount: float
    did_buy: bool
    timestamp: datetime.datetime
    stock_name: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True

class StockBase(BaseModel):

    user_id: int 
    stock_name: str
    amount: float = 0.0

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True