import os
import telebot

from dotenv import dotenv_values, load_dotenv

load_dotenv()
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

@bot.message_handler(func=stock_info)
def send_info(message):
  request = message.text.split()[1]
  #use data fetchers file to get info on specific stock
  

#Keep the bot looking for new messages
bot.polling()