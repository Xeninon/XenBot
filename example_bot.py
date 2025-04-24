import discord
import logging
import os
from dotenv import load_dotenv
import bingus

load_dotenv()

token = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user = message.author
    content = message.content.lower()
    if content.startswith('$bingus'):
        await message.channel.send(bingus.handle_bingus(content, user))

    if content.startswith('$hello'):
        await message.channel.send('Hello World!')
    
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(token, log_handler=handler)
