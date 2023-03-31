import disnake
from disnake.ext import commands

class UnauthorizedActivities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        channel = self.bot.get_channel(1079693252657172481)
        await channel.send(
            f'<@&1079696103903068240>\n'
            f'**❗UNAUTHORIZED ACTIVITIES IN GUILD❗**\n'
            f'**Server name:** Before - **{before}** , After - **{after}**'
            )

def setup(bot):
    bot.add_cog(UnauthorizedActivities(bot))