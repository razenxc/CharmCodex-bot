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
    async def on_member_ban(self, guild, member):
        channel = self.bot.get_channel(1087424762885722192)
        embed = discord.Embed(
            color=0xff0000,
            title='Ban',
            description=f'Учасника {member.mention} було заблоковано на сервері!\nДетальна інформація нижче.\n**Про заблокованого учасника:**\n**Id** - {member.id}, **Name** - {member.name}#{member.discriminator}.\n**Детальна інформація про модератора:**\n**CHANGE ME**',
        )
        await channel.send(embeds=[embed])

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        channel = self.bot.get_channel(1087424762885722192)
        embed = discord.Embed(
            color=0x7CFC00,
            title='Unban',
            description=f'Учасника {member.mention} було разблоковано на сервері!\nДетальна інформація нижче.\n**Про разблокованого учасника:**\n**Id** - {member.id}, **Name** - {member.name}#{member.discriminator}.\n**Детальна інформація про модератора:**\n',
        )
        await channel.send(embeds=[embed])

def setup(bot):
    bot.add_cog(departedUsers(bot))
    bot.add_cog(moderationLogs(bot))