import disnake
from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Надсилає затримку бота.")
    async def ping(self, ctx):
        await ctx.response.send_message(
            f"Pong! Затримка {round(self.bot.latency * 1000)}ms."
        )

def setup(bot):
    bot.add_cog(Ping(bot))
