import json
import os
import typer
import requests

## need to install typer before running
# pip install typer

from dotenv import load_dotenv
load_dotenv()

app = typer.Typer()

if __name__ == "__main__":
    app()

URL = "http://localhost:8000/"
# https://www.youtube.com/watch?v=we3907q1xz4
# if function name is put in typer --help it will display the argumneets the function takes automatically

#TODO ADD HELP METHOD TO TELL USER ABOUT ALL COMMANDS

@app.command()
def greet(message):
  print(message, "Hey! Hows it going?")

@app.command()
def hello(message):
  print(message.chat.id, "Hello!")

@app.command()
def stock_info(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "stock_info":
    return False
  else:
    return True

@app.command()
def greet(message):
  print(message, "Welcome To Stock Trading Bot!\n=====\nCommand List:\n=====\n/Greet, /hello: Get greeted by our bot.\n=====\n/help, /start: get information about our bot and the commands supported by it.\n=====\nstock_info {ticker_symbol}: Get information on a specific stock.\n=====\nbot1 {ticker_symbol} {period} {interval}: Activates our Stock Analysis Bot 1 on a specific stock. Period can be one of the following: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max. Interval can be one of the following: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo.\n=====\nbot2 {ticker_symbol} {period} {interval}.\n=====\nbot3 {ticker_symbol} {period} {interval}\n=====\nbot4 {ticker_symbol} {period} {interval}.\n=====\nbot5 {ticker_symbol} {period} {interval}")

@app.command()
def send_info1(message):
  if len(message.text.split()) > 2:
    print(message, "Wrong Format.\nMessage format should be: stock_info {ticker_symbol}")
    return
  request = message.text.split()[1]
  r = requests.post(url = URL + "tickerInfo", json=str(request))
  data = r.json()
  for k, v in data["info"].items():
    print(message.chat.id, str(k) + " : " + str(v))

#Bot 1
def bot_1(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot1":
    return False
  else:
    return True
 
@app.command()
def send_info2(message):
  if len(message.text.split()) > 4:
    print(message, "Wrong Format.\nMessage format should be: bot1 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot1", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    print(message, str(k) + " : " + str(v))

#Bot2
def bot_2(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot2":
    return False
  else:
    return True

@app.command()
def send_info3(message):
  if len(message.text.split()) > 4:
    print(message, "Wrong Format.\nMessage format should be: bot2 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot2", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    print(message, str(k) + " : " + str(v))

# Bot3
def bot_3(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot3":
    return False
  else:
    return True

@app.command()
def send_info4(message):
  if len(message.text.split()) > 4:
    print(message, "Wrong Format.\nMessage format should be: bot3 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot3", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    print(message, str(k) + " : " + str(v))

# Bot4
def bot_4(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot4":
    return False
  else:
    return True

@app.command()
def send_info5(message):
  if len(message.text.split()) > 4:
    print(message, "Wrong Format.\nMessage format should be: bot4 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot4", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    print(message, str(k) + " : " + str(v))

# Bot5
def bot_5(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot5":
    return False
  else:
    return True

@app.command()
def send_info6(message):
  if len(message.text.split()) > 4:
    print(message, "Wrong Format.\nMessage format should be: bot5 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot5", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    print(message, str(k) + " : " + str(v))
