import json
import os
import telebot
import requests

from dotenv import load_dotenv

load_dotenv()

URL = "http://localhost:8000/"

API_KEY = os.getenv("API_KEY_TELEGRAM")
bot = telebot.TeleBot(API_KEY)

#TODO ADD HELP METHOD TO TELL USER ABOUT ALL COMMANDS

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

def stock_info(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "stock_info":
    return False
  else:
    return True

@bot.message_handler(commands=['start', 'help'])
def greet(message):
  bot.reply_to(message, "Welcome To Stock Trading Bot!\n=====\nCommand List:\n=====\n/Greet, /hello: Get greeted by our bot.\n=====\n/help, /start: get information about our bot and the commands supported by it.\n=====\nstock_info {ticker_symbol}: Get information on a specific stock.\n=====\nbot1 {ticker_symbol} {period} {interval}\n Activates our Stock Analysis Bot which uses the Moving Average Strategy on a specific stock. Period can be one of the following: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max. Interval can be one of the following: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo.\n=====\nbot2 {ticker_symbol} {period} {interval} \nActivates the second bot which uses the Turtle Trading System Strategy on a specific stock.\n=====\nbot3 {ticker_symbol} {period} {interval} \nActivates the third bot which uses the Mean Reversion Strategy on a specific stock.\n=====\nbot4 {ticker_symbol} {period} {interval} \nActivates the fourth Bot which uses the Piercing Pattern Strategy on a specific stock.\n=====\nbot5 {ticker_symbol} {period} {interval} \nActivates the fifth Bot which uses the Three White Soldiers Strategy on a specific stock.")

@bot.message_handler(func=stock_info)
def send_info(message):
  if len(message.text.split()) > 2:
    bot.reply_to(message, "Wrong Format.\nMessage format should be: stock_info {ticker_symbol}")
    return
  request = message.text.split()[1]
  r = requests.post(url = URL + "tickerInfo", json=str(request))
  data = r.json()
  for k, v in data["info"].items():
    bot.send_message(message.chat.id, str(k) + " : " + str(v))

#Bot 1
def bot_1(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot1":
    return False
  else:
    return True
 
@bot.message_handler(func=bot_1)
def send_info(message):
  if len(message.text.split()) > 4:
    bot.reply_to(message, "Wrong Format.\nMessage format should be: bot1 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot1", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    bot.reply_to(message, str(k) + " : " + str(v))

#Bot2
def bot_2(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot2":
    return False
  else:
    return True

@bot.message_handler(func=bot_2)
def send_info(message):
  if len(message.text.split()) > 4:
    bot.reply_to(message, "Wrong Format.\nMessage format should be: bot2 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot2", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    bot.reply_to(message, str(k) + " : " + str(v))

# Bot3
def bot_3(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot3":
    return False
  else:
    return True

@bot.message_handler(func=bot_3)
def send_info(message):
  if len(message.text.split()) > 4:
    bot.reply_to(message, "Wrong Format.\nMessage format should be: bot3 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot3", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    bot.reply_to(message, str(k) + " : " + str(v))

# Bot4
def bot_4(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot4":
    return False
  else:
    return True

@bot.message_handler(func=bot_4)
def send_info(message):
  if len(message.text.split()) > 4:
    bot.reply_to(message, "Wrong Format.\nMessage format should be: bot4 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot4", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    bot.reply_to(message, str(k) + " : " + str(v))

# Bot5
def bot_5(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "bot5":
    return False
  else:
    return True

@bot.message_handler(func=bot_5)
def send_info(message):
  if len(message.text.split()) > 4:
    bot.reply_to(message, "Wrong Format.\nMessage format should be: bot5 {ticker_symbol} {period} {interval}")
    return
  request = message.text.split()
  r = requests.post(url = URL + "bot5", json={"ticker": request[1], "period": request[2], "interval": request[3]})
  data = r.json()
  for k, v in data.items():
    bot.reply_to(message, str(k) + " : " + str(v))

#Keep the bot looking for new messages
bot.polling()