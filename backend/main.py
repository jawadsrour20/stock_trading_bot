from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from requests import request
from sqlalchemy.orm import Session

from typing import Optional
from Stock_Market import Yfinance_Data_Fetcher
from Stock_Market.time_utils import Period, Interval
from bot import BotImplementation1, BotImplementation2, BotImplementation3, BotImplementation4, BotImplementation5

from cors import *
from http_status_codes import *
import crud, models, schemas
from database import SessionLocal, engine

# Create Database Tables
models.Base.metadata.create_all(bind=engine)


# Dependency: will create a new SQLAlchemy SessionLocal that will be used in a single request,
# and then close it once the request is finished.
async def get_db():
    db = SessionLocal()
    try:
        yield db
    # The code following the yield statement is executed after the response has been delivered:
    # we could've declared the function async instead of using yield
    finally:
        db.close()


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def index():
    return {"message": "Hello World"}

@app.post("/register", status_code=HTTP_STATUS_CODE_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    is_email_taken = bool(crud.get_user_by_email(db, user.email))
    is_username_taken = bool(crud.get_user_by_username(db, user.username))
    if is_email_taken:
        raise HTTPException(status_code=HTTP_STATUS_CODE_BAD_REQUEST, detail="Email already registered")
    if is_username_taken:
        raise HTTPException(status_code=HTTP_STATUS_CODE_BAD_REQUEST, detail="Username already taken")

    return crud.create_user(db=db, user=user)

@app.post("/login")
def login(username: str = Body(...), password: str = Body(...), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    does_user_exist = bool(user)
    is_password_correct = crud.auth_handler.verify_password(password, user.hashed_password)
    if not does_user_exist or not is_password_correct:
        raise HTTPException(status_code=HTTP_STATUS_CODE_UNAUTHORIZED, detail="Invalid credentials")
    JWT = crud.auth_handler.encode_token(user.username)
    return {"token": JWT}


@app.get("/home")
def home(username=Depends(crud.auth_handler.auth_wrapper)):
    return {"username": username}


@app.post("/bot1",  status_code=HTTP_STATUS_CODE_CREATED)
def recommender_bot1(ticker: str = Body(...), period: str = Body(...), interval: str = Body(...)):

    data = Yfinance_Data_Fetcher.get_history_by_period(ticker, period, interval)

    print(data)
    return {
        "decision": BotImplementation1.get_decision(market_data=data)
    }


@app.post("/bot2", status_code=HTTP_STATUS_CODE_OK)
def recommender_bot2(ticker: str = Body(...), period: str = Body(...), interval: str = Body(...)):
    data = Yfinance_Data_Fetcher.get_history_by_period(ticker, period, interval)
    print(data)
    return {
        "decision": BotImplementation2.get_decision(market_data=data)
    }

@app.post("/bot3", status_code=HTTP_STATUS_CODE_OK)
def recomender_bot3(ticker: str = Body(...), period: str = Body(...), interval: str = Body(...)):
    data = Yfinance_Data_Fetcher.get_history_by_period(ticker, period, interval)
    print(data)
    return {
        "decision": BotImplementation3.get_decision(market_data=data)
    }

@app.post("/bot4", status_code=HTTP_STATUS_CODE_OK)
def recommender_bot4(ticker: str = Body(...), period: str = Body(...), interval: str = Body(...)):
    data = Yfinance_Data_Fetcher.get_history_by_period(ticker, period, interval)
    print(data)
    return {
        "decision": BotImplementation4.get_decision(market_data=data)
    }

@app.post("/bot5", status_code=HTTP_STATUS_CODE_OK)
def recommender_bot5(ticker: str = Body(...), period: str = Body(...), interval: str = Body(...)):
    data = Yfinance_Data_Fetcher.get_history_by_period(ticker, period, interval)
    print(data)
    return {
        "decision": BotImplementation5.get_decision(market_data=data)
    }

@app.post("/tickerInfo", status_code=HTTP_STATUS_CODE_OK)
def ticker_info(ticker: str = Body(...)):
    data = Yfinance_Data_Fetcher.get_stock_info(ticker)
    #print(data)
    return {
        "info" : data
    }