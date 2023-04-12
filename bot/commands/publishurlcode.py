import aiohttp
import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction as ACI
import os

# Publishing to #codes-url
class PublishCodeUrlModal(disnake.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        components = [
            disnake.ui.TextInput(
                label="Введіть колір ембеду у форматі HEX (RRGGBB)",
                placeholder="ffffff",
                custom_id="color",
                required=False,
                style=disnake.TextInputStyle.short,
                min_length=6,
                max_length=6,
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
                label="Введіть посилання на код",
                placeholder="https://gist.github.com/razenxc/518a8c1ea9e8b094f14f7425ccf06bc6",
                custom_id="url",
                required=True,
                style=disnake.TextInputStyle.short,
                max_length=300,
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
            title="Публікація посилання коду до #codes-url",
            custom_id="publishurl",
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
            description=interaction.text_values['url']
        ).set_footer(
            text=interaction.text_values['tags'],
        ).set_author(
            name=interaction.user.name,
            icon_url=interaction.user.display_avatar,
        )
        async with aiohttp.ClientSession() as session:
            webhook = disnake.Webhook.from_url(
                url=("https://discord.com/api/webhooks"
                    f"/{os.getenv('PUBLISHCODEURL_WEBHOOK_ID')}"
                    f"/{os.getenv('PUBLISHCODEURL_WEBHOOK_TOKEN')}"),
                session=session,
            )
            await interaction.response.defer()
            message = interaction.client.get_message(
                (await webhook.send(
                    embeds=[
                        embed,
                    ],
                    wait=True,
                )).id
            )
            await message.add_reaction('👍')
            await message.add_reaction('👎')
            await interaction.followup.send(
                content="✅ Посилання успішно надіслане!",
                ephemeral=True,
            )


# Publishing to #codes-url
class PublishingCodesUrl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def can_publish(member: disnake.Member) -> bool:
        publish_roles = list(
            map(
                int,
                os.getenv('PUBLISHCODEURL_ROLES').split(',')
            )
        )
        return any(
            role.id in publish_roles
            for role in member.roles
        )
    
    @commands.slash_command(description="Надсилає посилання на ваш корисний або цікавий код до #codes-url!")
    async def publishurlcode(self, inner: ACI):
        if not self.can_publish(inner.author):
            await inner.response.send_message(
                content="❌ Відмовлено у доступі!",
                ephemeral=True,
            )
            return
        await inner.response.send_modal(
            PublishCodeUrlModal(
                title="Публікація коду до #codes-url"
            )
        ) 

def setup(bot):
    bot.add_cog(PublishingCodesUrl(bot))