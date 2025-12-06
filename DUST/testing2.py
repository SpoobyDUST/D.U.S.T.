import openai
from openai import Completion
import discord
from discord import app_commands
from discord.ext import tasks
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

openai.api_key = "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"

intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(name='Clusture Fires', type=discord.ActivityType.watching)
bot = commands.Bot(intents=intents,activity=activity,command_prefix="!")


# Connecting to the Server
@bot.event
async def on_ready():
    # Initial message
    channel = bot.get_channel(1051227760326103080)
    await channel.send("D.U.S.T. TEST DOS is Operational!")



# Define a command named "openai"
@bot.command()
async def openai(ctx, prompt: str):
    max_tokens = 32
    temperature = 0.4
    completion = Completion.create(
        engine="text-davinci-003",
        prompt=prompt[3:],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    # Relaying to Discord
    debugchan = bot.get_channel(1051227760326103080)
    await ctx.send(completion["choices"][0]["text"])
    await debugchan.send(completion)

    
token = os.getenv("BOT_TOKEN")

bot.run(token)