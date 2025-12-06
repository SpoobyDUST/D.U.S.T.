import openai
import discord
import os
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()

# Set your ChatGPT API key here
openai.api_key = "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"

# Create a new Discord client
intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(name='Clusture Fires', type=discord.ActivityType.watching)
client = discord.Client(intents=intents,activity=activity)
slash = app_commands.CommandTree(client)

@client.event
async def on_ready():
    # Initial message
    channel = client.get_channel(1051227760326103080)
    await channel.send("D.U.S.T. TESTING TRES is Operational!")


# Define the "!hello" command using the command tree
@slash.command(name="hello", description="Say hello")
async def hello_command(message):
    # Send the message "hello" to the Discord channel
    await message.channel.send("hello")

# Listen for messages in all channels that the bot has access to
@client.event
async def on_message(message):
    # Only respond to messages that start with the "!ai" command
    if message.content.startswith("!ai"):
        # Create a ChatGPT Completion object
        gpt_api = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message.content[3:]  # Use the rest of the message as the prompt
        )

        # Generate a response using the ChatGPT model
        response = gpt_api.generate()

        # Send the response to the Discord channel
        await message.channel.send(response.text)


# Register an event listener for the on_message event
@client.event
async def on_message(message):
    # This event handler will be called whenever a message is sent in any of the channels that the bot has access to

    # Add your logic to handle the message here
    pass

# Run the Discord client using your bot's token
token = os.getenv("BOT_TOKEN")

client.run(token)