""" Contains the SQL Queries used by sqlalchemy for ORM. """
# Note: CRUD Stands for Create, Read, Update, and Delete.

from sqlalchemy.orm import Session

import models, schemas
from auth import AuthHandler
from http_status_codes import *


auth_handler = AuthHandler()

## Database READ functions START
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.User).offset(skip).limit(limit).all()
## Database READ functions END




## Database CREATE functions START
# function takes as input a Pydantic user object
# it then creates a sqlalchemy user object to be added to the database
def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = auth_handler.get_password_hash(user.password)
    # SQLAlchemy model instance
    db_user = models.User(email=user.email, username=user.username, hashed_password=hashed_password,
                          first_name=user.first_name, last_name=user.last_name, photo=user.photo,
                          balance=user.balance)
    db.add(db_user) # add the user to the database
    db.commit() # commit changes so they are saved
    db.refresh(db_user) # refresh instance so that it contains any new data from the database, like the generated ID
    return HTTP_STATUS_CODE_CREATED
## Database CREATE functions END