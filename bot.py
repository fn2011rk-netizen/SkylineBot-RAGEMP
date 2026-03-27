import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

# Set up bot with command prefix
intents = discord.Intents.none()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.reactions = True
if config.get('enable_welcome', False):
    intents.members = True  # For member join events

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

if config.get('enable_welcome', False):
    @bot.event
    async def on_member_join(member):
        channel = discord.utils.get(member.guild.channels, name=config['welcome_channel'])
        if channel:
            message = config['welcome_message'].format(user=member.mention)
            await channel.send(message)


print(f"intents.members: {intents.members}")
print(f"intents.presences: {intents.presences}")
if TOKEN and TOKEN != 'MTQ4NTc2NzMzMDM5ODIwODAzMQ.GuOnhf.Qqmfx6T5GbO6klJVbrHDRsiSbvn5JGfQh6qEng':
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN not found or not set in .env file. Please add your bot token.")