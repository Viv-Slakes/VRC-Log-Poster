import os
import discord
from discord.ext import tasks, commands

# Variables to be configured
TOKEN = 'YOURTOKEN' # Your Bot Token
GUILD_ID = YOURSERVERID  # The ID of your server (guild)
CHANNEL_ID = YOURCHANNELID  # The ID of the channel where bot will post files
COMMAND_CHANNEL_ID = YOURCOMMANDCHANNELID  # The ID of the channel where bot will respond to commands
INTERVAL_MINUTES = 20  # The interval in minutes at which the bot should post files
COMMAND_PREFIX = '/'  # The prefix for commands
COMMAND_NAME = 'vrclog'  # The name of the command to respond to
DIRECTORY_PATH = os.path.join(os.environ['USERPROFILE'], 'AppData\\LocalLow\\VRChat\\VRChat')  # The directory path to watch for files




intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, id=GUILD_ID)
    bot.channel = discord.utils.get(guild.channels, id=CHANNEL_ID)
    bot.command_channel = discord.utils.get(guild.channels, id=COMMAND_CHANNEL_ID)
    print(f'{bot.user} has connected to Discord!')
    send_latest_file.start()

# Sends log in response to someone using /vrclog in the COMMAND_CHANNEL_ID
@bot.command(name=COMMAND_NAME)
async def log(ctx):
    if ctx.channel.id == bot.command_channel.id:
        await send_file(bot.channel)
        await ctx.message.delete()

# Sends log every INTERVAL_MINUTES
@tasks.loop(minutes=INTERVAL_MINUTES)
async def send_latest_file():
    await send_file(bot.channel)

# Sends Log
async def send_file(channel):
    files = os.listdir(DIRECTORY_PATH)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(DIRECTORY_PATH, x)), reverse=True)
    newest_file = files[0]
    newest_file_path = os.path.join(DIRECTORY_PATH, newest_file)
    await channel.send(file=discord.File(newest_file_path))

bot.run(TOKEN)