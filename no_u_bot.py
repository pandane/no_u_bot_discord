import discord
import random

from discord.ext import commands
from credentials import TOKEN, KEY, BOTID, OWNERID

client = discord.Client()

responses = ['no u', 'NO UU', 'NO U',
             'nO U', 'NO U!!', '\nNO U\nO\n\nU']

triggers = ['no u', 'no you']


@client.event
async def on_ready():
    print('logged in as: ' + str(client.user.name))


@client.event
async def on_message(message):
    strippedText = " ".join(message.content.split()).lower()
    if message.author.id != int(BOTID):
        for trigger in triggers:
            if trigger in strippedText:
                await message.channel.send(random.choice(responses))

client.run(TOKEN)
