import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt 
import yfinance as yf
yf.pdr_override()
import discord 
from discord import app_commands
from discord.ext import tasks
from discord.ext import commands
from discord import Embed
from discord_webhook import DiscordWebhook
from discord import Interaction
import re

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
activity = discord.Activity(name='Clusture Fires', type=discord.ActivityType.watching)
bot = commands.Bot(intents=intents, activity=activity, help_command=None, command_prefix="!")
invite_pattern = re.compile(r'(discord\.gg\/|discordapp\.com\/invite\/)([a-zA-Z0-9\-]+)')
guild_id = 988579939655778324



y_symbols = ['AAPL']

from datetime import datetime
startdate = dt.datetime(2020,1,1)
enddate = dt.datetime.now()


data = yf.download(y_symbols, start=startdate, end=enddate)

colors= mpf.make_marketcolors(up='#00ff00',down='#ff0000',
                              wick= "inherit",
                              edge="inherit",
                              volume="in")
mpf_style = mpf.make_mpf_style(base_mpf_style ='nightclouds', marketcolors=colors)

mpf.plot(data, style= "mpf_style")






@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check for invite links
    if invite_pattern.search(message.content):
        guild = bot.get_guild(guild_id)
        user = message.author

        # Check if the user is already banned
        if user in await guild.bans():
            # If already banned, don't kick again, just send a message
            embed = discord.Embed(
                title="Spam Prevention",
                description=f"{user.mention} has been banned for sharing invite links again.",
                color=discord.Color.red()
            )
            await message.channel.send(embed=embed)
            return

        # Delete the message containing the invite link
        await message.delete()

        # Check if the user has already been kicked
        if user in [kick.user for kick in await guild.audit_logs(action=discord.AuditLogAction.kick)]:
            # If already kicked, ban the user
            await guild.ban(user, reason="Repeatedly sharing invite links")
            
            # Send an embed message indicating the ban
            embed = discord.Embed(
                title="Spam Prevention",
                description=f"{user.mention} has been banned for sharing invite links multiple times.",
                color=discord.Color.red()
            )
            await message.channel.send(embed=embed)
        else:
            # Kick the user from the guild
            await guild.kick(user, reason="Sharing invite links")

            # Send an embed message indicating the kick
            embed = discord.Embed(
                title="Spam Prevention",
                description=f"{user.mention} has been kicked for sharing invite links.",
                color=discord.Color.red()
            )
            await message.channel.send(embed=embed)
