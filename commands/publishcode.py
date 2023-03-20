import discord
from discord.ext import commands

class PublishingUsefulCodes(discord.ui.Modal):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Надсилає ваш корисний або цікавий код до #useful-codes!")
    async def publishcode(self, ctx):
        modal = MyModal(title="Modal via Slash Command")
        await ctx.send_modal(modal)

        

def setup(bot):
    bot.add_cog(PublishingUsefulCodes(bot))