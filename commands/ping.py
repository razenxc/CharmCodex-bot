import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Надсилає затримку бота.")
    async def ping(self, ctx):
        await ctx.respond(f"Pong! Затримка {str(self.bot.latency)[:4]}ms.")

def setup(bot):
    bot.add_cog(Ping(bot))