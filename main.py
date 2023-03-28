import disnake
from disnake.ext import commands
import os # default module
from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file
client = commands.Bot(
    intents=disnake.Intents.all(),
    command_prefix="/",
    help_command=None,
)

@client.event
async def on_ready():
    print(f"{client.user} is ready and online!")
    await client.change_presence(status=disnake.Status.dnd, activity=disnake.Game("with the Discord"))

events_list = [
    'onjoin',
    'logs',
]

commands_list = [
    'ping',
    'publishcode'
]

for cog in events_list:
    client.load_extension(f'events.{cog}')

for cog in commands_list:
    client.load_extension(f'commands.{cog}')

client.run(os.getenv("DISCORD_TOKEN"))
