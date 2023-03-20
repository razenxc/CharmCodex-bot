import discord
import os # default module
from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("with the Discord"))

events_list = [
    'onjoin',
    'logs',
]

commands_list = [
    'ping',
]

for cog in events_list:
    bot.load_extension(f'events.{cog}')
for cog in commands_list:
    bot.load_extension(f'commands.{cog}')

bot.run(os.getenv("DISCORD_TOKEN"))