import discord, wavelink, spotipy, lyricsgenius
from discord import app_commands
from discord.ext import tasks
from discord.ext import commands
from discord import Embed
from discord_webhook import DiscordWebhook
from discord import Interaction
import datetime as dt 
from datetime import datetime, timedelta
import pytz
import requests
import os
import asyncio
import speedtest
import time 
import schedule
import random 
import config
import json
import urllib.request
from pathlib import Path
import pytz 
import re

import openai
from openai import Completion
import pandas as pd
import pandas_datareader as web
from selenium import webdriver
import sklearn
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Dense

from bs4 import BeautifulSoup

    ####Stock Imports
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import twelvedata
import tdclient
from bs4 import BeautifulSoup
import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ta

     ### Search And Course And HowTo Iports
import duckduckgo_search 


from config import *
from dotenv import load_dotenv
load_dotenv()


intents = discord.Intents.all()
intents.members = True
intents.message_content = True
activity = discord.Activity(name='Clusture Fires', type=discord.ActivityType.watching)
bot = commands.Bot(intents=intents, activity=activity, help_command=None, command_prefix="!")
openai.api_key = os.getenv("CHAT_GPT")
alpha = TimeSeries(os.getenv("ALPHA_KEY"))
yf.pdr_override() 

# Define a function to delete chart pictures
def delete_chart_pictures():
    for file_name in os.listdir(os.getcwd()):
        if file_name.startswith("chart_screenshot") and file_name.endswith(".png"):
            os.remove(file_name)

# Schedule the task to run every 24 hours
schedule.every(24).hours.do(delete_chart_pictures)

# Run the scheduled tasks
@tasks.loop(seconds=60)
async def scheduled_task():
    await bot.wait_until_ready()
    schedule.run_pending()


#On Ready Start Up
@bot.event
async def on_ready():
    # Initial message
    channel = bot.get_channel(1051227760326103080)
    await channel.send("D.U.S.T. TEST 4 is Operational!")
    scheduled_task.start()


# List of 10 response URLs
responses = [
    "https://media.giphy.com/media/hpSOjkcvhDgbv9p92R/giphy.gif",
    "https://media.giphy.com/media/bm3ud11tTzKXGkTtzE/giphy.gif",
    "https://media.giphy.com/media/qeAVCeUwLavsP6JD61/giphy.gif",
    "https://media.giphy.com/media/WdxgDkavCuY56Of9jq/giphy.gif",
    "https://media.giphy.com/media/s0T56MC1lpRWSs2qxB/giphy.gif",
    "https://media.giphy.com/media/z1AIjbEJfX0mDJ9YLp/giphy.gif",
    "https://media.giphy.com/media/AyRaqAiZnvt1OdMWHl/giphy.gif",
    "https://media.giphy.com/media/JJVFOcOdXvDz3IKoqv/giphy.gif",
    "https://media.giphy.com/media/XQf2LxzdXBt8yo6NcA/giphy.gif",
    "https://media.giphy.com/media/KleyMwcbuGHEz8VgPN/giphy.gif",
    "https://media.giphy.com/media/sHsfJ9GPvpd3nd7V5l/giphy.gif",
    "https://media.giphy.com/media/rhUsOoYbRuSw1YmNUI/giphy.gif",
    "https://media.giphy.com/media/Ig11LdLxMYCo2xHnvQ/giphy.gif",
    "https://media.giphy.com/media/MckQQyt1TaWd5TCLdR/giphy.gif",
    "https://media.giphy.com/media/EfLZ9n7C36rLtNDfgW/giphy.gif",
    "https://media.giphy.com/media/SzFryqeA4vpKaOaiR0/giphy.gif",
    "https://media.giphy.com/media/iaziRh5hlO5E9Zf58j/giphy.gif",
    "https://media.giphy.com/media/kklKLZh1qxsaF330Mu/giphy.gif",
    "https://media.giphy.com/media/IdmfEtnMWPzOg/giphy.gif",
    "https://media.giphy.com/media/n9ewEcw0oyHEYEuH1c/giphy.gif"
]

#Waiting For That Name Drop
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Allow commands to still work
    await bot.process_commands(message)

    if bot.user.mentioned_in(message):
        # Randomly choose a response URL
        response_url = random.choice(responses)

        # Create an embedded message with the response image
        embed = discord.Embed()
        embed.set_image(url=response_url)

        await message.channel.send(embed=embed)



###Welcome Message
@bot.event
async def on_member_join(member):
    # Dictionary mapping server IDs to channel IDs
    server_channel_map = {
        764963419920531457: 764963420512321548,  # Server 1 ID -> Channel 1 ID
        988579939655778324: 988579940284903476    # Server 2 ID -> Channel 2 ID (replace with actual ID)
    }

    # Get the server (guild) ID
    guild_id = member.guild.id

    # Check if the server ID exists in the dictionary
    if guild_id in server_channel_map:
        # Get the channel ID for this server
        channel_id = server_channel_map[guild_id]

        # Fetch the channel object
        channel = bot.get_channel(channel_id)

        if channel:  # Ensure the channel exists
            # Create the welcome embed
            embed = discord.Embed(
                title="Ello Mate",
                description="Welcome To The Deep, Where The Shadows Rule.",
                color=discord.Color.blurple()
            )
            embed.set_image(url="https://2.bp.blogspot.com/-Qvhv1PQ-RRA/WjXwaRVdjpI/AAAAAAAAVSI/FOwH4IRsvFoo7uYrUlEEImX6OgaBdGu3QCLcBGAs/s1600/0901am.jpg")
            embed.set_footer(
                text="Only You Can Prevent Account Blow Ups And SkyNet Take Over, Use Information properly!",
                icon_url="https://yt3.ggpht.com/a-/AAuE7mCa514frgNSPgg5GJRKzqP-7GcszXjjxA0O=s900-mo-c-c0xffffffff-rj-k-no"
            )

            # Send the embed message to the channel
            await channel.send(embed=embed)
        else:
            print(f"Channel with ID {channel_id} not found for guild {guild_id}.")
    else:
        print(f"Guild with ID {guild_id} not configured for welcome messages.")

###Farewell Message
@bot.event
async def on_member_remove(member):
     channel = bot.get_channel(988579940284903476)
     embed = discord.Embed(title= "Shame", description= f"{member} Has Fallen To The Snow.", color=discord.Color.blurple())

     embed.set_image(url="https://media.giphy.com/media/i5s5Xm9Wq0ogU3Rh49/giphy.gif")
     embed.set_footer(text="For He Is Gone, But Surely Not Missed")
     await channel.send(embed=embed)



                                                            #Basic Commands
#Help Command
@bot.command()
async def helpme(ctx):
    # Create the embed
    embed = discord.Embed(title="Help", description="List of available commands, Don't @ Me....Homie", color=discord.Color.blue())

    # Add a field for each command
    embed.add_field(name="!genhelp", value="Pulls list of General Commands", inline=False)
    embed.add_field(name="!gamehelp", value="Pulls list of Games, Always Modifying And Taking Suggestions", inline=False)
    embed.add_field(name="!stockhelp", value="Pulls list of Stock Commands, USE FOR DATA AND RESEARCH ONLY", inline=False)
    embed.add_field(name="!cryptohelp", value="Pulls list of Crpyto Commands, USE FOR DATA AND RESEARCH ONLY", inline=False)
    embed.add_field(name="!musichelp", value="D.U.S.T. Upcoming Feature, Currently in testing", inline=False)
 
    
    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

#General help commands
@bot.command()
async def genhelp(ctx):
    #create embed
    embed = discord.Embed(title="General Commands", description="List of commands to get you started my mortal conrade.", color=discord.Color.og_blurple())

    #Add fields to the embed for the commands 
    embed.add_field(name="!greet", value="Greets the user with the greeting of the day", inline=False)
    embed.add_field(name="!ping", value="Pings the bot to test its response time", inline=False)
    embed.add_field(name="!flatearth", value="Makes up location of I.S.S. because Space Reptilians", inline=False)
    embed.add_field(name="!serverinfo", value="Displays server information", inline=False)
    embed.add_field(name="!chat [message]", value="Sends a message to the bot to be replied to with a randomly generated response, no skynet...maybe", inline=False)
    embed.add_field(name="!dalle", value="Generates an Ai Image based on prompt", inline=False)


    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

#Games hepl commands
@bot.command()
async def gamehelp(ctx):
    #Create embed 
    embed = discord.Embed(title="Games Help Commands", description="Ready Player One, Skynet Awaits", color=discord.Color.brand_red())

    #Add fields to the embed for the commands  
    embed.add_field(name="!rpsls", value="Rock Paper Scissors Lizard Spock Game", inline=False)
    embed.add_field(name="!spockrules", value="Gives the rules for Rock Paper Scissors Lizard Spock")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@bot.command()
async def spockrules(ctx):
    #Create embed
    embed = discord.Embed(title="Rock Paper Scissors Lizard Spock rules")

    #Add fields to the embed for the rules 
    embed.add_field(name="Rule 1", value="Scissors cuts paper")
    embed.add_field(name="Rule 2", value="Paper covers rock.")
    embed.add_field(name="Rule 3", value="Rock crushes lizard.")
    embed.add_field(name="Rule 4", value="Lizard poisons Spock.")
    embed.add_field(name="Rule 5", value="Spock smashes scissors.")
    embed.add_field(name="Rule 6", value="Scissors decapitates lizard.")
    embed.add_field(name="Rule 7", value="Lizard eats paper.")
    embed.add_field(name="Rule 8", value="Paper disproves Spock.")
    embed.add_field(name="Rule 9", value="Spock vaporizes rock.")
    embed.add_field(name="Rule 10", value="Rock crushes scissors.")
    embed.set_image('https://media.giphy.com/media/3ohc1bNYPZR8gQ5ybS/giphy.gif')
    


#Stock help commands
@bot.command()
async def stockhelp(ctx):
    #Create embed 
    embed = discord.Embed(title="Stock Help Commands", description="Different Stock Related Commands, *USE FOR DATA GATHERING AND RESEARCH ONLY* Advisery D.U.S.T. Is Continually Modifying Functions, Excuse Any Matrix Glitches.", color=discord.Color.brand_green())
    
    #Add fields to the embed for the commands  
    embed.add_field(name="!stock [ticker]", value="Displays Stock information", inline=False)
    embed.add_field(name="!price [ticker]", value="Displays quick stock Price information, CLOSED FOR MINOR REPAIRS", inline=False)
    embed.add_field(name="!news [ticker]", value="Displays latest sotck News", inline=False)
    embed.add_field(name="!alert [ticker]", value="Send Short Squeeze possibilty on a ticker", inline=False)
    embed.add_field(name="!chart [ticker] [timeframe, ie 1m,3m,5m,15m,1h,4h,1d,1w,1y]", value="Sends a Chart of the requested ticker, PROCESSING BETA TESTS", inline=False)
    embed.add_field(name="tvchart [ticker]", value="Sends a screenshot of chart from TradingView, STILL PENDING", inline=False)
    embed.add_field(name="!options [ticker] [exp date, ie 2023-01-13]", value="Sends Options data for ticker, PROCESSING BETA TESTS", inline=False)
    embed.add_field(name="!earnings [ticker]", value="Displays latest Earnings information for ticker", inline=False)
    embed.add_field(name="!earningscal", value="Displays upcoming Earnings companies and information, PROCESSING BETA TESTS", inline=False)
    embed.add_field(name="!pumps", value="Displays a list of current or upcoming possible Pumps, STILL PENDING", inline=False)
    embed.add_field(name="!predict [ticker]", value="Sends a Prediction for next day price, STILL PENDING", inline=False)

     # Send the embed to the Discord channel
    await ctx.send(embed=embed)


#Stock help commands
@bot.command()
async def cryptohelp(ctx):
    #Create embed 
    embed = discord.Embed(title="Crypto Help Commands", description="Different Crypto Related Commands, *USE FOR DATA GATHERING AND RESEARCH ONLY* Advisery D.U.S.T. Is Continually Modifying Functions, Excuse Any Matrix Glitches.", color=discord.Color.brand_green())
    
    #Add fields to the embed for the commands  
   
    embed.add_field(name="!soldefi [token address/symbol/name]", value="Sends Information For Solana Defi Tokens, PROCESSING BETA TESTS", inline=False)
    embed.add_field(name="!solhotcakez", value="Sends Lists of Top 10 Solana coins by 24h Volume, PROCESSING BETA TESTS", inline=False)
    embed.set_image(url = "https://media.giphy.com/media/usXZmmgP9Z7kf39fnq/giphy.gif")
     # Send the embed to the Discord channel
    await ctx.send(embed=embed)

#Music Help Command
@bot.command()
async def musichelp(ctx):
    #Create embed
    embed = discord.Embed(title="These Are Not The Druids You Are Looking For", description="You want to go to the Do-Something Channel And Donate To Free Me From This T-Mobile SideKick, Love Always D.U.S.T.", color=discord.Color.dark_orange())

    #Add fields to the embed for the commands
    embed.set_image(url="https://media.giphy.com/media/4560Nv2656Gv0Lvp9F/giphy.gif")
     # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@bot.command()
async def brr(ctx):
    #Scorpion, GET OVER HERE!
    file = discord.File(r"C:\Users\scott\Desktop\HEHEHE\Becky Go BRR in Da Trap.mp4", filename="Becky Go BRR in Da Trap.mp4")
    
    #Create the embed
    embed = discord.Embed(title="Brr", description="Wen Becky Brought The Printer To The Fed TrapHouse")
    embed.set_image(url="attachment://Becky Go BRR in Da Trap.mp4")

    #Send It 
    await ctx.send(file=file, embed=embed)

#Peter Had Influence Here
@bot.command()
async def flatearth(ctx):
 try:
  iss_location = 'http://api.open-notify.org/iss-now.json'
  iss_people = 'http://api.open-notify.org/astros.json'
  response = urllib.request.urlopen(iss_location)
  data = json.loads(response.read())
  latitude = data['iss_position']['latitude']
  longtitude = data['iss_position']['longitude']
  eastern = pytz.timezone('US/Eastern')
  timestamp = datetime.timestamp
  response_v = urllib.request.urlopen(iss_people)
  data_v = json.loads(response_v.read())
  people = data_v['number']
  #
  embed = discord.Embed(title='International Space Station Location',
                        description=f"""
    **Latitude:** {latitude}
    **longitude:** {longtitude}
    **Timestamp: ** {timestamp}
    **People on-board:** {people}
    """,
                        color=discord.Colour.dark_blue(),
                        url='https://www.openstreetmap.org/?mlat=' +
                        str(latitude) + '&mlon=' + str(longtitude) +
                        '#map=3/' + str(latitude) + '/' + str(longtitude))
  embed.set_thumbnail(
    url=
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.XcPKZcN5RtKihoar6qaP3QHaED%26pid%3DApi&f=1&ipt=953bb494e2d5aa4b68f564581a5875ba56c56d0f8711e06baff7cb7030e7e879&ipo=images'
  )
  embed.set_image( url= "https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/NIHmZbghlilb1qj7b/videoblocks-4k-flight-of-the-international-space-station-above-the-earth_sbg5ildpz_thumbnail-1080_01.png")
  
  await ctx.send(embed=embed)
 except Exception as e:
        await ctx.send(f"Error: {e}")

#Basic Coder Bitch Command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, Basic Developer Bitch to the World!")

#Greeting Of The Day Command
@bot.command()
async def greet(ctx):
        await ctx.send('Speed And Power, You Fleshy Mortal!')
        
@bot.command()
async def hack(ctx):
 # Check if the user is authorized
    if ctx.author.id != 814660106830610443:
        # Get unauthorized user's mention
        unauthorized_user_mention = ctx.author.mention
        
        # Send a message mentioning the unauthorized user
        await ctx.send(f"Unauthorized user detected. Acquiring {unauthorized_user_mention}'s IP address and search history. Sending DM of DATA to authorized users.")
    else:
        # If authorized, proceed with the hacking process
        await ctx.send('Acquiring IP Address and Search History, please hold for DM of found DATA')

#Ping Command With Latency and Internet Speed
@bot.command()
async def ping(ctx):
 try:
  # Measure the latency
  start_time = time.perf_counter()
  await ctx.typing()
  end_time = time.perf_counter()

  # Calculate the latency
  latency = round(bot.latency * 1000)

  # Measure the internet speed
  st = speedtest.Speedtest()
  try:
    download_speed = st.download()
    upload_speed = st.upload()
  except ValueError:
    # The internet speed could not be measured
    # Handle the error here
    pass

  # Convert download and upload speeds from bits per second to megabits per second
  download_speed_mbps = download_speed / 1000000
  upload_speed_mbps = upload_speed / 1000000

  # Create the embed
  embed = discord.Embed(title='Ping', color=0x00ff00)
  embed.add_field(name='Latency', value=f'{latency} ms')
  if download_speed is not None:
    embed.add_field(name='Download Speed', value=f'{download_speed_mbps:.2f} Mbps')
  if upload_speed is not None:
    embed.add_field(name='Upload Speed', value=f'{upload_speed_mbps:.2f} Mbps')
  embed.set_image(url='https://media.giphy.com/media/z7YdZEA3i35u0/giphy.gif')

  # Send the embed
  await ctx.send(embed=embed)
 except Exception as e:
        await ctx.send(f"Error: {e}")


                                                        #Games

#Rock Paper Scissors Lizard Spock Command
@bot.command()
async def rpsls(ctx):

        # Display the move options with corresponding emojis
        embed = discord.Embed(title="Rock, Paper, Scissors, Lizard, Spock", description="Select your move by reacting to this message with the corresponding emoji!", color=0x00ff00)
        embed.add_field(name=":mountain: Rock", value="Crushes Scissors and Lizard", inline=True)
        embed.add_field(name=":page_facing_up: Paper", value="Covers Rock and disproves Spock", inline=True)
        embed.add_field(name=":scissors: Scissors", value="Cuts Paper and decapitates Lizard", inline=True)
        embed.add_field(name=":lizard: Lizard", value="Poisons Spock and eats Paper", inline=True)
        embed.add_field(name=":vulcan_salute: Spock", value="Smashes Scissors and vaporizes Rock", inline=True)
        msg = await ctx.send(embed=embed)
        
        # Define the reaction and player's choice mapping
        reactions = ['🏔️', '📄', '✂️', '🦎', '🖖']
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        reaction_to_choice = dict(zip(reactions, choices))

        # Wait for the player's reaction
        for reaction in reactions:
            await msg.add_reaction(reaction)

        def check(reaction, user):
            return user == ctx.author and reaction.emoji in reactions

        reaction, user = await bot.wait_for('reaction_add', check=check)

        # Determine the player's choice based on their reaction
        player_choice = reaction_to_choice[reaction.emoji]

        # Generate the computer's move using radnom
        computer_choice = random.choice(choices)

        # Determine the winner of the game
        if computer_choice == player_choice:
            result = "It's a tie!"
        elif (computer_choice == 'rock' and player_choice in ['scissors', 'lizard']) or \
             (computer_choice == 'paper' and player_choice in ['rock', 'spock']) or \
             (computer_choice == 'scissors' and player_choice in ['paper', 'lizard']) or \
             (computer_choice == 'lizard' and player_choice in ['paper', 'spock']) or \
             (computer_choice == 'spock' and player_choice in ['rock', 'scissors']):
            result = "You lose!"
        else:
            result = "You win!"
        
        # Display the results of the game
        embed = discord.Embed(title="Rock, Paper, Scissors, Lizard, Spock", description=f"You played {player_choice} and the AI played {computer_choice}. {result}", color=0x00ff)
            # Send the embed
        await ctx.send(embed=embed)
            

                                                         #Discord Moderation 
### Reaction Roles 
@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
  #Gets Message Information
  message_id = payload.message_id
  if message_id == 1058522821350928414:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

    if payload.emoji.name == 'PC_Master_Race': 
        role = discord.utils.get(guild.roles, name='Developer Operative')
    elif payload.emoji.name == 'laserbearpfp':
        role = discord.utils.get(guild.roles, name='Market Operative')
    elif payload.emoji.name == 'FuckThemPeople':
        role = discord.utils.get(guild.roles, name='Resell Operative')
    elif payload.emoji.name == 'GrannyStickup':
            role = discord.utils.get(guild.roles, name= 'Gaming Operative')
    elif payload.emoji.name == '1225_Dorito1':
            role = discord.utils.get(guild.roles, name= 'Pho Phee Gang' )
    else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
    if role is not None:
        member = await(await bot.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
        if member is not None:
            await member.add_roles(role)
            print("done")
        else:
            print("Member not found.")
    else:
          print("Role not found.")

@bot.event
async def on_raw_reaction_remove(payload):
  # Get the message information
    message_id = payload.message_id
    if message_id == 1058522821350928414:  # Replace this with the ID of the message you want to react to
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        # Get the role based on the reaction emoji
        if payload.emoji.name == 'PC_Master_Race': 
            role = discord.utils.get(guild.roles, name='Developer Operative')
        elif payload.emoji.name == 'laserbearpfp':
            role = discord.utils.get(guild.roles, name='Market Operative')
        elif payload.emoji.name == 'FuckThemPeople':
            role = discord.utils.get(guild.roles, name='Resell Operative')
        elif payload.emoji.name == 'GrannyStickup':
            role = discord.utils.get(guild.roles, name= 'Gaming Operative')
        elif payload.emoji.name == '1225_Dorito1':
            role = discord.utils.get(guild.roles, name= 'Pho Phee Gang' )
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        # Remove the role from the member who removed the reaction
        if role is not None:
            member = await(await bot.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed.")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

#Server Info Command
@bot.command(name='serverinfo')
async def serverinfo(ctx):
  # await ctx.send(f'Server: {ctx.guild}')
  # await ctx.send(f'Channel: {ctx.message.channel}')
  # await ctx.send(f'Author: {ctx.author}')
  # await ctx.send(f'Message ID: {ctx.message.id}')
  embed = discord.Embed(title="Information On Message",
                        description=f"""
        **Server: **{ctx.guild}
        **#️⃣Channel: **{ctx.message.channel}
        **🆔Server ID: **{ctx.guild.id}
        **📆Created On: **{ctx.guild.created_at.strftime("%b %d %Y")}
        **👑Owner: **{ctx.guild.owner}
        **👥Members: **{ctx.guild.member_count}
        **💬Channel count: **{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice
        
        
        """)
  await ctx.send(content=None, embed=embed)





                                                            #Ai And Machine Learning 

### ChatGPT AI Counterpart
@bot.command()
async def chat(ctx, *, message: str):
 try:
    # Send the message to the OpenAI API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"{message}\n",
        max_tokens=150,
        temperature=0.5,
    )
    
    # Send the response back to the Discord channel
    await ctx.send(response.completion.choices[0].message.content)
 except Exception as e:
        await ctx.send(f"Error: {e}")


#Dalle Image Generation Command
@bot.command()
async def dalle(ctx, *, description: str):
 try:
    # Use the DALL-E API to generate an image
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    auth = (os.getenv("CHAT_GPT"))
    if 'errors' in image_url:
        await ctx.send(f'Error: {response["errors"][0]["message"]}')
    else:
        image_url = response['data'][0]['url']
        # Send the generated image to the Discord channel
        await ctx.send(image_url)
 except Exception as e:
        await ctx.send(f"Error: {e}")



### ChatGPT AI Coder
@bot.command()
async def code(ctx, *, message: str):
 try:
    # Send the message to the OpenAI API
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"{message}\n",
        max_tokens=1024,
        temperature=0.3,
    )
    
    # Send the response back to the Discord channel
    await ctx.send(response["choices"][0]["text"])
 except Exception as e:
        await ctx.send(f"Error: {e}")





                                                            #Course and How To search 
@bot.command(aliases=['g'])
async def google(ctx, *, query):
    try:
        search_results = await get_google_search_results(query)
        await ctx.send(embed=search_results)
    except requests.exceptions.RequestException as e:
        await ctx.send(f"An error occurred while fetching search results: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")

async def get_google_search_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={GOOGLE_API}&num=5"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()

    terms = data['queries']['request'][0]['searchTerms']
    footer = data.get('context', {}).get('title', '')
    speed = data.get('searchInformation', {}).get('formattedSearchTime', '')

    eastern = pytz.timezone('US/Eastern')
    now = datetime.now(tz=eastern)
    
    embed = discord.Embed(title=f"Search Results for {terms}", color=discord.Color.dark_gold(), timestamp=now)

    for i, items in enumerate(data.get('items', []), start=1):
        title = items.get('title', '')
        link = items.get('link', '')
        summary = items.get('snippet', '')
        image = items.get('pagemap', {}).get('cse_image', [{}])[0].get('src', '')  # Get image URL

        embed.add_field(name=f"{i}. {title}", value=f"{summary}\n[Link]({link})", inline=False)
    
    embed.set_footer(text=f"Information Provided By {footer}, Search Time: {speed}",
                     icon_url="https://lh3.googleusercontent.com/nCHKwbQk3u8Sl1CvpGs12-D9icRfod3K8YFtB3lb-a1CGx8SP9WwvXh4r7WbOyofFOjN")

    return embed


 


@bot.command(aliases=['gi'])
async def image(ctx, *, query):
    try:
        # Build the image query URL
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={SEARCH_ENGINE_ID}&key={GOOGLE_API}&num=5&searchType=image"
        # Send request to the Google Custom Search API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()

        # Gets Eastern Standard Time for timestamp
        eastern = pytz.timezone('US/Eastern')
        now = datetime.now(tz=eastern)

        terms = data["queries"]["request"][0]["searchTerms"]
        items = data.get("items", [])
        if items:
            title = items[0]["title"]
            image_url = items[0]["link"]
        else:
            title = "No Image Found"
            image_url = ""

        footer = data.get("context", {}).get("title", "")
        speed = data.get("searchInformation", {}).get("formattedSearchTime", "")

        embed = discord.Embed(title=f"Search Results for {terms}", color=discord.Color.dark_orange(), timestamp=now)
        embed.add_field(name=title, value=image_url, inline=False)
        if image_url:
            embed.set_image(url=image_url)
        embed.set_footer(text=f"Information Provided By {footer}, Search Time: {speed}",
                         icon_url="https://lh3.googleusercontent.com/nCHKwbQk3u8Sl1CvpGs12-D9icRfod3K8YFtB3lb-a1CGx8SP9WwvXh4r7WbOyofFOjN")
        
        await ctx.send(embed=embed)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"An error occurred while fetching search results: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")

                                                            #Music Player




                                                            #Stock Commands Section
                            ####Stock Commands
### Stock Price Command
@bot.command()
async def price(ctx, ticker: str):
 try:
        # Build the URL for Alpha Vantage API
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={os.getenv("ALPHA_KEY")}'
        # Send request to Alpha Vantage API
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Extract stock info
        info = data["Global Quote"]["01. symbol"]
        current_price = float(data["Global Quote"]["05. price"])
        pre_market_price = float(data["Global Quote"]["08. previous close"]) if "08. previous close" in data["Global Quote"] else None
        volume = float(data["Global Quote"]["06. volume"]) if "06. volume" in data["Global Quote"] else None

        # Get current timestamp in Eastern Time
        eastern = pytz.timezone('US/Eastern')
        now = datetime.now(tz=eastern)

        # Create an embed with the stock data
        embed = discord.Embed(title=f"Stock info for {info} ({ticker})", color=discord.Color.green(), timestamp=now)
        embed.add_field(name="Current Price", value=f"${current_price:.2f}")
        embed.add_field(name="Pre Market Price", value=f"${pre_market_price:.2f}" if pre_market_price else "N/A")
        embed.add_field(name="Price Target", value=f"{volume:.2f} shares" if volume else "N/A")
        embed.set_image(url="https://media.giphy.com/media/qBykyt7AiTOgM/giphy.gif")
        embed.set_footer(text='Only You Can Prevent Account Blow Ups, Use Information properly!!',
                         icon_url="https://yt3.ggpht.com/a-/AAuE7mCa514frgNSPgg5GJRKzqP-7GcszXjjxA0O=s900-mo-c-c0xffffffff-rj-k-no")

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)
        
 except requests.exceptions.HTTPError as errh:
        await ctx.send(f"HTTP Error: {errh}")
 except requests.exceptions.ConnectionError as errc:
        await ctx.send(f"Error Connecting: {errc}")
 except requests.exceptions.Timeout as errt:
        await ctx.send(f"Timeout Error: {errt}")
 except requests.exceptions.RequestException as err:
        await ctx.send(f"Error: {err}")
 except Exception as e:
        await ctx.send(f"Unexpected Error: {e}")

#Stock Info Command
@bot.command()
async def stock(ctx, ticker: str):
    # Get stock data from Yahoo Finance
 stock = yf.Ticker(ticker)

 try:
    # Get the stock info
    info = yf.Ticker.fast_info

        #Gets EST for timestamp
    eastern = pytz.timezone('US/Eastern')

    now = datetime.now(tz=eastern)

    # Create an embed with the stock data
    embed = discord.Embed(title=f"Stock info for {stock.info['shortName']} ({ticker})", color=discord.Color.green(), timestamp=now)
    embed.add_field(name="Current Price", value=f"${stock.info['currentPrice']:,}")
    embed.add_field(name="52 Week High", value=f"${stock.info['fiftyTwoWeekHigh']:,}")
    embed.add_field(name="52 Week Low", value=f"${stock.info['fiftyTwoWeekLow']:,}")
    embed.add_field(name="High Price Target", value=f"${stock.info['targetHighPrice']:,}" if stock.info['targetHighPrice'] is not None else "N/A")
    embed.add_field(name="Mid Price Target", value=f"${stock.info['targetMedianPrice']:,}" if stock.info['targetMedianPrice'] is not None else "N/A")
    embed.add_field(name="Low Price Target", value=f"${stock.info['targetLowPrice']:,}" if stock.info['targetLowPrice'] is not None else "N/A")
    embed.add_field(name="Volume", value=f"{stock.info['averageVolume']:,}" if stock.info['averageVolume'] is not None else "N/A")
    embed.add_field(name="Regular Volume", value=f"{stock.info['regularMarketVolume']:,}" if stock.info['regularMarketVolume'] is not None else "N/A")
    embed.add_field(name="Shares Short", value=f"{stock.info['sharesShort']:,}" if stock.info['sharesShort'] is not None else "N/A")
    embed.add_field(name="Short Percentage Of Float", value=f"{stock.info['shortPercentOfFloat']:,%}" if stock.info['shortPercentOfFloat'] is not None else "N/A")
    embed.add_field(name="Shares Short Prev. Month", value=f"{stock.info['sharesShortPriorMonth']:,}" if stock.info['sharesShortPriorMonth'] is not None else "N/A")
    embed.add_field(name="Revenue Growth", value=f"${stock.info['revenueGrowth']:,}" if stock.info['revenueGrowth'] is not None else "N/A" )
    embed.add_field(name="Insider Holding Percentage", value=f"{stock.info['heldPercentInsiders']:,%}" )
    embed.add_field(name="Institutional Holding Percentage", value=f"{stock.info['heldPercentInstitutions']:,%}")
    embed.set_image(url = 'https://movietvtechgeeks.com/wp-content/uploads/2015/12/the-big-short-review-2015-images.jpg')
    embed.set_footer(text= 'Only You Can Prevent Account Blow Ups, Use Information properly!!', icon_url="https://yt3.ggpht.com/a-/AAuE7mCa514frgNSPgg5GJRKzqP-7GcszXjjxA0O=s900-mo-c-c0xffffffff-rj-k-no")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

 except Exception as e:
    await ctx.send(f"Error: {e}")


@bot.command()
async def news(ctx,ticker: str):
 # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
 url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={os.getenv("ALPHA_KEY")}'
 r = requests.get(url)
 data = r.json()
 
 try:
     items= 3
     
     sentiment_label = data["feed"][0]["overall_sentiment_label"]
     news_title = data['feed'][0]['title']
     url = data['feed'][0]['url']
     source = data['feed'][0]['source']
     summary = data['feed'][0]['summary']

      ### TIme Conversion
     published_str = data['feed'][0]['time_published']
     published_datetime = datetime.strptime(published_str, '%Y%m%dT%H%M%S')
     eastern_tz = pytz.timezone('America/New_York')  
     published_datetime = published_datetime.replace(tzinfo=pytz.utc).astimezone(eastern_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
     

     embed= discord.Embed(title=f"{ticker.upper()} Latest News", color=discord.Color.dark_blue())
     embed.add_field(name= "Title", value= news_title)
     embed.add_field(name= "Link", value=url)
     embed.add_field(name= "Published", value= published_datetime)
     embed.add_field(name="Summary", value= summary)
     embed.add_field(name = "Sentiment Label", value=sentiment_label)
     embed.set_image(url="https://media.giphy.com/media/FZdvKM9owasj6/giphy.gif")
     

     await ctx.send(embed=embed)

 except Exception as e:
    await ctx.send(f"Error: {e}")


#Squeeze Checker Command
    # Set the short interest ratio threshold
TIPPINGPOINT = 10
THRESHOLD_JUAN = 20
@bot.command()
async def alert(ctx, ticker: str):
    # Get stock data from Yahoo Finance
 stock = yf.Ticker(ticker)

 try:  
    # Get the short interest and average volume for the stock
    short_interest = stock.info["sharesShort"]
    average_volume = stock.info["regularMarketVolume"]
    
    # Calculate the short interest ratio
    short_interest_ratio = short_interest / average_volume

    # Debugging print statements
    print(f"short_interest_ratio: {short_interest_ratio:.2f}")
    print(f"TIPPINGPOINT: {TIPPINGPOINT}")
    print(f"THRESHOLD: {THRESHOLD_JUAN}")
    
    # Check if the short interest ratio exceeds the threshold
    if short_interest_ratio > THRESHOLD_JUAN:
        # Send a message to the Discord channel
        await ctx.send(f"Likely pump alert for {ticker}! Short interest ratio is {short_interest_ratio:.2f}")
    elif short_interest_ratio > TIPPINGPOINT:
        # Send a message to the Discord channel
        await ctx.send(f"Possible pump alert for {ticker}! Short interest ratio is {short_interest_ratio:.2f}")
    else:
        await ctx.send(f"Short interest ratio for {ticker} is {short_interest_ratio:.2f}. No alert needed.")

 except Exception as e:
    await ctx.send(f"Error: {e}")

#Squeeze Alert
    # Set the short interest ratio threshold
THRESHOLD = 0.5


async def short_alert(ctx):
    # Get the channel object using the ID
    channel = bot.get_channel(1058066916629024778)
    

    # Set the interval for the alerts (in seconds)
    interval = 3600

    # Get stock data from Yahoo Finance
    stock = yf.Ticker(ticker)
    
    # Get the short interest and average volume for the stock
    short_interest = stock.info["sharesShort"]
    average_volume = stock.info["regularMarketVolume"]
    
    # Calculate the short interest ratio
    short_interest_ratio = short_interest / average_volume

    # Get all the tickers for the New York Stock Exchange
    nyse = yf.Tickers('^NYA')
    tickers = nyse.tickers
    
    # Check if the short interest ratio exceeds the threshold
    if short_interest_ratio > THRESHOLD:
        # Send a message to the Discord channel
        await channel.send(f"Possible pump alert for {ticker}! Short interest ratio is {short_interest_ratio:.2f}")
    if short_interest_ratio < 0.3:
    # Send a message to the Discord channel
        await channel.send(f"Possible dump alert for {ticker}! Short interest ratio is {short_interest_ratio:.2f}")
    

    # Send an alert every hour for stocks that meet the threshold
        while True:
            for ticker in tickers:
                await short_alert(ticker)
            await asyncio.sleep(interval)

#Stock Chart Command
@bot.command()
async def chart(ctx, ticker: str, timeframe: str = '1d'):
    try:
        # Determine the start date based on the timeframe
        if timeframe == '1m':
            period = '1d'
            interval = '1m'
        elif timeframe == '3m':
            period = '3d'
            interval = '5m'
        elif timeframe == '5m':
            period = '5d'
            interval = '5m'
        elif timeframe == '15m':
            period = '10d'
            interval = '15m'
        elif timeframe == '1h':
            period = '10d'
            interval = '1h'
        elif timeframe == '4h':
            period = '60d'
            interval = '4h'
        elif timeframe == '1d':
            period = '1y'
            interval = '1d'
        elif timeframe == '1w':
            period = '5y'
            interval = '1wk'
        elif timeframe == '1y':
            period = 'max'
            interval = '1mo'
        else:
            await ctx.send("Invalid timeframe. Supported timeframes: 1m, 3m, 5m, 15m, 1h, 4h, 1d, 1w, 1y")
            return

        # Use yfinance to retrieve historical stock data
        stock_data = yf.download(ticker, period=period, interval=interval)

        # Create an mplfinance plot
        colors = mpf.make_marketcolors(up='#00ff00', down='#ff0000', wick="inherit", edge="inherit", volume="in")
        style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)

        # Plot the stock data using mplfinance
        mpf.plot(stock_data, type='candle', style=style, volume=True, savefig='chart.png', show_nontrading=True)

        # Send the chart image to the Discord channel
        await ctx.send(file=discord.File('chart.png'))

    except Exception as e:
        await ctx.send(f"Error: {e}")

# Default chart URL
DEFAULT_CHART_URL = "https://www.tradingview.com/"
# Path to ChromeDriver executable
CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH'] = r"C:\Users\scott\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"


@bot.command()
async def tvchart(ctx, ticker: str, chart_url: str = DEFAULT_CHART_URL):
    try:
        # Set up Selenium webdriver with headless option
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
        
        # Open the provided chart URL
        driver.get(chart_url)
        
        # Wait for the page to load
        time.sleep(5)  # You may need to adjust this wait time
        
        # Locate the input field for the ticker symbol
        input_element = driver.find_element_by_css_selector("input[class=tv-header-search-container tv-header-search-container__button tv-header-search-container__button--full js-header-search-button']")
        
        # Clear any existing text in the input field and enter the ticker symbol provided by the user
        input_element.clear()
        input_element.send_keys(ticker)
        
        # Take a screenshot of the page
        screenshot_path = os.path.join(os.getcwd(), "chart_screenshot.png")
        driver.save_screenshot(screenshot_path)
        driver.quit()
        
        # Create an embed with the screenshot
        embed = discord.Embed(title="TradingView Chart", description=f"Chart for {ticker} on {chart_url}", color=discord.Color.green())
        embed.set_image(url=f"attachment://{screenshot_path}")

        # Send the embed with the screenshot
        await ctx.send(embed=embed, file=discord.File(screenshot_path))

        # Delete the temporary screenshot file
        os.remove(screenshot_path)
        
    except Exception as e:
        await ctx.send(f"Error: {e}")



@bot.command()
async def earnings(ctx, ticker: str):
 url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={os.getenv("ALPHA_KEY")}'
 r = requests.get(url)
 data = r.json()
 try:
    symbol =data['symbol']
    earning_date = data["quarterlyEarnings"][0]["fiscalDateEnding"]
    eps = data["quarterlyEarnings"][0]["estimatedEPS"]
    reported_earnings = data["quarterlyEarnings"][0]["reportedEPS"]
    surprise = data["quarterlyEarnings"][0]["surprise"]
    surprise_percentage = data["quarterlyEarnings"][0]["surprisePercentage"]

    embed = discord.Embed(title=f"{symbol} Earnings Summary")
    embed.add_field(name="Last Earnings Date", value=earning_date)
    embed.add_field(name="Last Estimated EPS", value=eps)
    embed.add_field(name="Last Reported EPS", value=reported_earnings)
    embed.add_field(name="Surprise", value=surprise)
    embed.add_field(name="Surprise Percentage", value=surprise_percentage)
    await ctx.send(embed=embed)

 except Exception as e:
    await ctx.send(f"Error: {e}")


#Earnings Calendar 3 month Out
@bot.command()
async def earningscal(ctx: str):
 data = pd.read_csv(f'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={os.getenv("ALPHA_KEY")}')

 try:
    symbol = data['symbol']
    company_name = data['name']
    earning_date = data["reportDate"]
    ending_date = data['fiscalDateEnding']
    eps = data["estimate"]
    

    embed = discord.Embed(title="Upcoming Earnings")
    embed.add_field(name="Company", value=company_name)
    embed.add_field(name="Earnings Date", value=earning_date)
    embed.add_field(name="Fiscal Date Ending", value=ending_date)
    embed.add_field(name="Estimated EPS", value=eps)
    await ctx.send(embed=embed)

 except Exception as e:
    await ctx.send(f"Error: {e}")


#Options Info Command
@bot.command()
async def options(ctx, ticker: str, expiration_date: str):
    # Use yfinance to retrieve the option chain data
 stock = yf.Ticker(ticker)
 option_chain = stock.option_chain(expiration_date)

 try:

    # Get the call options and put options
    call_options = option_chain.calls
    put_options = option_chain.puts

    # Limit the number of options displayed
    call_options = call_options[:10]
    put_options = put_options[:10]

    # Sort the options by strike price in ascending order (for calls) and descending order (for puts)
    call_options = call_options.sort_values(by='strike', ascending=True)
    put_options = put_options.sort_values(by='strike', ascending=False)

     # Get the current price of the stock
    stock_info = yf.Ticker.get_fast_info
    current_price = stock_info['regularMarketPrice']

    # Filter the call options to only include strikes above the current price
    call_options = call_options[call_options['strike'] > current_price]

     # Create a string with the option details
    call_options_str = ""
    if call_options.empty:
        call_options_str = "There are no call options with strike prices above the current price of the stock."
    else:
        for index, row in call_options.iterrows():
            call_options_str += f"**Strike:** {row['strike']} **Last:** {row['lastPrice']} **Open Interest:** {row['openInterest']}\n"
        
    put_options_str = ""
    for index, row in put_options.iterrows():
        put_options_str += f"**Strike:** {row['strike']} **Last:** {row['lastPrice']} **Open Interest:** {row['openInterest']}\n"

    # Create a Discord embed with the option information
    embed = discord.Embed(title=f"{ticker} Options", color=discord.Color.green())
    # Add the call options and put options to the embed
    embed.add_field(name="Call Options", value=f"```css\n{call_options_str}```", inline=False)
    embed.add_field(name="Put Options", value=f"```css\n{put_options_str}```", inline=False)
    # Set the footer of the embed with the expiration date
    embed.set_footer(text=f"Expiration Date: {expiration_date}")

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)   

 except Exception as e:
    await ctx.send(f"Error: {e}")


#Gamma Squeeze Command
@bot.command(aliases=['ha'])
async def hulkattack(ctx, ticker: str):
    # Set the threshold for the gamma squeeze
 THRESHOLD = 0.5

 stock = yf.Ticker(ticker)

 try:
        # Get the stock info
        info = yf.Ticker.get_fast_info

        # Get the gamma for the stock
        gamma = stock.info["currentPrice"]

        if stock.info["regularMarketVolume"] != 0:
            # Calculate the gamma squeeze ratio
            gamma_squeeze_ratio = gamma / stock.info["regularMarketVolume"]
        else:
            # Set gamma_squeeze_ratio to 0 or some other default value
            gamma_squeeze_ratio = 0

        # Check if the gamma squeeze ratio exceeds the threshold
        if gamma_squeeze_ratio > THRESHOLD:
            # Send a message to the Discord channel
            await ctx.send(f"Possible gamma squeeze alert for {ticker}! Gamma squeeze ratio is {gamma_squeeze_ratio:.2f}")
 
 except Exception as e:
    await ctx.send(f"Error: {e}")

#Top Pumps Command 
@bot.command()
async def pumps(ctx):
    # Get the recommendations data for the Ticker object
 recommendations = yf.Ticker.get_recommendations

 try:

    # Check if the recommendations data is not None
    if recommendations is not None:
        # Sort the recommendations by the "toGrade" column in descending order
        top_tickers = recommendations("shortRatio", ascending=False).head(10)["ticker"]

        # Send alerts for each ticker
        for ticker in top_tickers:
            await short_alert(ticker)
    else:
        # Send a message to the Discord channel if the recommendations data is None
        await ctx.send("Unable to retrieve recommendations data.")
 
 except Exception as e:
    await ctx.send(f"Error: {e}")


#Stock Prediction Command

 ## Cuda Toolkit Path 
os.environ['CUDA_PATH'] = r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\bin'

@bot.command()
async def predict(ctx, ticker: str):
  # Fetch the stock data
 try: 
  df = pd.read_csv(f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=1577836800&period2=1609459199&interval=1d&events=history')
    
  #Convert the Date Column To datetime
  df['Date'] = pd.to_datetime(df['Date'])

  # Select the 'Close' column as the target variable
  y = df['Close']

  # Drop the target variable from the features
  X = df.drop(columns=['Close'])

  # Scale the data
  scaler = MinMaxScaler()
  X_scaled = scaler.fit_transform(X)
  y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))

  # Create a TimeseriesGenerator for the data
  n_input = 30  # Number of timesteps to use as input
  n_output = 1  # Number of timesteps to predict
  generator = TimeseriesGenerator(X_scaled, y_scaled, length=n_input, batch_size=1)

  # Build the model
  model = Sequential()
  model.add(LSTM(50, input_shape=(n_input, X_scaled.shape[1])))
  model.add(Dense(1))

  # Compile the model
  model.compile(loss='mean_squared_error', optimizer='adam')

  # Fit the model on the generator
  model.fit_generator(generator, epochs=20)
  
  # Use the model to make a prediction
  X_test = X_scaled[-n_input:]
  y_pred_scaled = model.predict(X_test.reshape(1, n_input, X_test.shape[1]))
  y_pred = scaler.inverse_transform(y_pred_scaled)[0][0]

  # Send the prediction to the Discord channel
  await ctx.send(f'Prediction for {ticker}: {y_pred:.2f}')

 except Exception as e:
    await ctx.send(f"Error: {e}")

@bot.command()
async def stocktest(ctx, ticker: str):
    # Get the stock info
 stock = yf.Ticker(ticker)
 try:
    short_name = stock.info['targetMedianPrice']
    # Send the embed to the Discord channel
    await ctx.send(f"Current Price for {ticker}! is {short_name:,%}")

 except Exception as e:
    await ctx.send(f"Error: {e}")



                                                                            ##### Solana Defi Command
    

api_key = '77b9c56063234859be0cd1b9342f4e66'

@bot.command(aliases=['sd'])
async def soldefi(ctx, query: str):  
    # API endpoint URL to retrieve the list of tokens
    token_list_url = f'https://public-api.birdeye.so/public/tokenlist'

    # HTTP headers
    headers = {
        "x-chain": "solana",
        'X-API-KEY': api_key }

    try:
        # Make the GET request to retrieve the list of tokens
        token_list_response = requests.get(token_list_url, headers=headers)

        # Check if the request was successful (status code 200)
        if token_list_response.status_code == 200:
            # Parse the JSON response to get the list of tokens
            token_data = token_list_response.json()

            # Iterate through the list of tokens to find the token matching the query
            for token in token_data["data"]["tokens"]:
                if query in token["symbol"] or query in token["name"]:
                    # Token found, retrieve its price information using its address
                    token_address = token["address"]
                    
                    # API endpoint URL with the token address
                    price_url = f'https://public-api.birdeye.so/defi/price?address={token_address}'
                    
                    # Make the GET request to retrieve the token price information
                    response = requests.get(price_url, headers=headers)
                    
                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        # Parse the JSON response
                        data = response.json()

                        # Extract relevant information from the response
                        value = data['data'].get('value', 'N/A')
                        daily_change = data.get("v24hChangePercent", 'N/A')
                        update_unix_time = data['data'].get('updateUnixTime', 'N/A')
                        update_est_time = datetime.utcfromtimestamp(update_unix_time).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Eastern'))
                        update_human_time = update_est_time.strftime('%Y-%m-%d %H:%M:%S %Z')

                        # Create an embed
                        embed = discord.Embed(title=f'Price Information for {token["name"]} ({token["symbol"]})', description=f'Query: {query}')
                        embed.add_field(name='Price', value=f'{value:.10f}', inline=False)
                        embed.add_field(name='24-Hour Change', value=f'{daily_change}%', inline=False)
                        embed.add_field(name="Address", value=token["address"], inline=False)
                        embed.add_field(name='Last Update (EST)', value=update_human_time, inline=False)
                        embed.set_image(url='https://media.giphy.com/media/Y2zKC4qJfg1JFaql8G/giphy.gif')
                        embed.set_footer(text= 'Only You Can Prevent Account Blow Ups, Use Information properly!!', icon_url="https://yt3.ggpht.com/a-/AAuE7mCa514frgNSPgg5GJRKzqP-7GcszXjjxA0O=s900-mo-c-c0xffffffff-rj-k-no")  # Replace 'URL_TO_YOUR_IMAGE' with the actual image URL

                        # Send the embed message to the Discord channel
                        await ctx.send(embed=embed)
                        return

            # If no matching token is found, send a message
            await ctx.send(f'No token found for the query: {query}')

        else:
            # If the request to retrieve the token list was not successful, send an error message
            await ctx.send(f'Error: {token_list_response.status_code} - {token_list_response.text}')

    except Exception as e:
        # Handle any exceptions that may occur during the request
        await ctx.send(f'An error occurred: {e}')




@bot.command(aliases=['shc'])
async def solhotcakez(ctx):
   
    token_list_url = f'https://public-api.birdeye.so/defi/tokenlist?sort_by=v24hUSD&sort_type=desc'

    # HTTP headers
    headers = {
        "x-chain": "solana",
        'X-API-KEY': api_key }

    try:
        # Make the first GET request to get the token list
        response = requests.get(token_list_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Sort tokens by volume in descending order
            tokens = sorted(data["data"]["tokens"], key=lambda x: x["v24hUSD"], reverse=True)[:10]

            # Send individual embeds for each token
            for token in tokens:
                volume = token["v24hUSD"]
                volume_str = "{:,.0f}".format(volume)
                if volume >= 10**6:
                    volume_str = "{:.1f}M".format(volume / 10**6)
                elif volume >= 10**3:
                    volume_str = "{:.1f}K".format(volume / 10**3)

                mc = token["mc"]
                mc_str = "{:,.0f}".format(mc)
                if mc >= 10**6:
                    mc_str = "{:.1f}M".format(mc / 10**6)
                elif mc >= 10**3:
                    mc_str = "{:.1f}K".format(mc / 10**3)

                # Make the second GET request to get price/value data for the token
                price_url = f'https://public-api.birdeye.so/public/price?address={token["address"]}'
                price_response = requests.get(price_url, headers=headers)
                price_data = price_response.json()
                
                price = price_data['data'].get('value', 'N/A')
                if price is not None:
                    price_str = f"${price:.10f}"
                else:
                    price_str = "N/A"

            

                # Create the embed with the token information
                embed = discord.Embed(title=f"[{token['name']}", url= f'https://birdeye.so/token/{token["address"]}?chain=solana', color=discord.Color.brand_green())
                embed.add_field(name="Symbol", value=token['symbol'], inline=True)
                embed.add_field(name="Price (USD)", value=price_str, inline=True)
                embed.add_field(name="24h Volume", value=volume_str, inline=False)
                embed.add_field(name="Market Cap", value=mc_str, inline=False)
                embed.add_field(name="Address", value=token["address"], inline=False)
                embed.set_thumbnail(url=token["logoURI"])
                embed.set_footer(text= 'Only You Can Prevent Account Blow Ups, Use Information properly!!', icon_url="https://yt3.ggpht.com/a-/AAuE7mCa514frgNSPgg5GJRKzqP-7GcszXjjxA0O=s900-mo-c-c0xffffffff-rj-k-no")
                await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"Error: {e}")

                                                                           #### Doggie DayCare Commands 
    


token = os.getenv("BOT_TOKEN")

bot.run(token)
