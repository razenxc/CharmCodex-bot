import disnake
from disnake.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1087407846108434522)
        await channel.send(f'🔆 Вітаємо , {member.mention} на {member.guild.name}.')

def setup(bot):
    bot.add_cog(Greetings(bot))
