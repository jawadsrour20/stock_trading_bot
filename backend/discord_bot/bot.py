import discord
import random
import os
from dotenv import load_dotenv
from messages import discord_messages, DiscordMessage

load_dotenv()
TOKEN = os.getenv("TOKEN")
ALLOWED_CHANNELS = ["stock_trading",]
client = discord.Client()

# Event handler called once the client connects to the server (once the bot is online)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the stock trading recommendation discord server!'
    )

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content).lower()
    channel = str(message.channel.name)
    print(f'{username} said: {user_message} in {channel}')

    # Avoid the bot responding to itself infinitely
    if message.author == client.user:
        return
    # Allow bot only to respond on certain channels
    if message.channel.name in ALLOWED_CHANNELS:
        if user_message == discord_messages.get(DiscordMessage.HELLO):
            response = f'Hello {username}!'
            await message.channel.send(response)
            return
        elif user_message == discord_messages.get(DiscordMessage.BYE):
            response = f'See you later {username}!'
            await message.channel.send(response)
            return

client.run(TOKEN)