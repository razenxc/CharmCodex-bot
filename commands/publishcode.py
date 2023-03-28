import aiohttp
import disnake
from disnake.ext import commands
from disnake.http import Route
from disnake import ApplicationCommandInteraction as ACI
import os

class PublishCodeModal(disnake.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        components = [
            disnake.ui.TextInput(
                label="Введіть колір ембеду у форматі HEX (RRGGBB)",
                placeholder="ffffff",
                custom_id="color",
                required=True,
                style=disnake.TextInputStyle.short,
                min_length=6,
                max_length=6,
            ),
            disnake.ui.TextInput(
                label="Введіть мову програмувания",
                placeholder="c",
                custom_id="language",
                required=True,
                style=disnake.TextInputStyle.short,
                max_length=32,
            ),
            disnake.ui.TextInput(
                label="Введіть заголовок",
                placeholder="Hello, world!",
                custom_id="title",
                required=True,
                style=disnake.TextInputStyle.short,
                max_length=100,
            ),
            disnake.ui.TextInput(
                label="Введіть код",
                placeholder="#include <stdio.h>\n"
                            "int main(void)\n"
                            "{\n"
                            "    puts(\"Hello, world!\");\n"
                            "}\n",
                custom_id="code",
                required=True,
                style=disnake.TextInputStyle.paragraph,
            ),
            disnake.ui.TextInput(
                label="Введіть теги",
                placeholder="#javascript #python",
                custom_id="tags",
                required=True,
                style=disnake.TextInputStyle.short,
            ),
        ]
        super().__init__(
            title="Modal via Slash command",
            custom_id="publishcode",
            components=components,
        )
    async def callback(self, interaction: disnake.ModalInteraction):
        color = 0xFFFFFF
        try:
            color = int(interaction.text_values['color'], base=16)
        except:
            pass
        embed = disnake.Embed(
            color=color,
            title=interaction.text_values['title'],
            description=f"```{interaction.text_values['language']}\n"
                        f"{interaction.text_values['code']}\n"
                         "```",
        ).set_footer(
            text=interaction.text_values['tags'],
        ).set_author(
            name=interaction.user.name,
            icon_url=interaction.user.display_avatar,
        )
        async with aiohttp.ClientSession() as session:
            url = f"https://discord.com/api/webhooks/{os.getenv('WEBHOOK_ID')}/{os.getenv('WEBHOOK_TOKEN')}"
            webhook = disnake.Webhook.from_url(
                url=url,
                session=session,
            )
            await webhook.send(
                embeds=[
                    embed
                ]
            )
            await interaction.response.send_message(
                content="✅ Успішно надіслано код!",
                ephemeral=True,
            )

class PublishingUsefulCodes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="Надсилає ваш корисний або цікавий код до #useful-codes!")
    async def publishcode(self, ctx: ACI):
        await ctx.response.send_modal(
            PublishCodeModal(
                title="Modal via Slash Command"
            )
        ) 

def setup(bot):
    bot.add_cog(PublishingUsefulCodes(bot))
