# Created by Chris2342

import discord
import asyncio
from discord.ext import commands
import safygiphy

client = discord.Client()

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('!hi'):
        msg = 'What is up {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDU3MjE1MzEzNjMzNjA3Njgx.DghAng.SL1tfO5eSCav2MBsmtD12NsEZaU')
