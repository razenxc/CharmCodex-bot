import discord
from discord.ext import commands

class departedUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1087415810445815880)
        await channel.send(f'Чмо {member.mention}, покинуло сервер. (id: {member.id}, tag: {member.name}#{member.discriminator})')

class moderationLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_ban(self, member):
        channel = self.bot.get_channel(1087424762885722192)
        await channel.send(f'Участника undefined було заблоковано...')

    @commands.Cog.listener()
    async def on_member_unban(self, member):
        channel = self.bot.get_channel(1087424762885722192)
        await channel.send(f'Участника undefined було разблоковано...')

def setup(bot):
    bot.add_cog(departedUsers(bot))
    bot.add_cog(moderationLogs(bot))