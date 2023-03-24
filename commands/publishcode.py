import discord
from discord.ext import commands

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(
            label="Введіть колір ембеду у форматі HEX (RRGGBB)",
            style=discord.InputTextStyle.short,
            min_length=6, max_length=6
            ))
        self.add_item(discord.ui.InputText(
            label="Введіть тип коду. Наприклад js, py, cpp, c",
            style=discord.InputTextStyle.short,
            max_length=4
            ))
        self.add_item(discord.ui.InputText(
            label="Введіть заголовок",
            style=discord.InputTextStyle.long,
            max_length=100
            ))
        self.add_item(discord.ui.InputText(
            label="Введіть код",
            style=discord.InputTextStyle.paragraph
            ))
        self.add_item(discord.ui.InputText(
            label="Введіть теги. Наприклад #javascript #python",
            style=discord.InputTextStyle.short
            ))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            # color=f'0x{self.children[0].value}',
            title=self.children[2].value,
            description='```' + self.children[1].value + '\n' + self.children[3].value + '```',
            ).set_author(name=interaction.user.name, url=f'https://discord.com/users/{interaction.user.id}', icon_url=interaction.user.display_avatar)
        await interaction.response.send_message(embeds=[embed])

class PublishingUsefulCodes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Надсилає ваш корисний або цікавий код до #useful-codes!")
    async def publishcode(self, ctx: discord.ApplicationContext):
        modal = MyModal(title="Modal via Slash Command")
        await ctx.send_modal(modal) 
        

def setup(bot):
    bot.add_cog(PublishingUsefulCodes(bot))