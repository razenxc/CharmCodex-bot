require('dotenv').config();

const { EmbedBuilder } = require('@discordjs/builders');
const {
	Client,
	GatewayIntentBits,
	ActionRowBuilder,
	Events,
	ModalBuilder,
	TextInputBuilder,
	TextInputStyle,
	WebhookClient,
} = require('discord.js');

const client = new Client({
	intents: [
		GatewayIntentBits.Guilds
	]
});

client.on('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
});

client.on(Events.InteractionCreate, async interaction => {
	if (!interaction.isChatInputCommand()) return;
	switch (interaction.commandName) {
		case 'ping':
			await interaction.reply('Pong!');
			break;
		case 'profile':
			{
				const modal = new ModalBuilder()
					.setTitle('Title')
					.setCustomId('profile');
				const name = new TextInputBuilder()
					.setCustomId('name')
					.setRequired(true)
					.setLabel('Enter name')
					.setStyle(TextInputStyle.Short);
				const about = new TextInputBuilder()
					.setCustomId('about')
					.setRequired(true)
					.setLabel('Write about you')
					.setStyle(TextInputStyle.Paragraph);
				const firstActionRow = new ActionRowBuilder().addComponents(name);
				const secondActionRow = new ActionRowBuilder().addComponents(about);
				modal.addComponents(firstActionRow, secondActionRow);
				await interaction.showModal(modal);
			}
			break;
		case 'publishcode':
			{
				const modal = new ModalBuilder()
					.setCustomId('publishCode')
					.setTitle('Публікація корисного коду');
				const embedColorInput = new TextInputBuilder()
					.setCustomId('embedColorInput')
					.setLabel('Введіть колір ембеду в формати RRGGBB')
					.setMinLength(6)
					.setMaxLength(6)
					.setStyle(TextInputStyle.Short);
				const embedCodeTypeInput = new TextInputBuilder()
					.setCustomId('embedCodeTypeInput')
					.setLabel('Введіть тип код')
					.setMaxLength(4)
					.setStyle(TextInputStyle.Short);
				const embedTitleInput = new TextInputBuilder()
					.setCustomId('embedTitleInput')
					.setLabel('Введіть заголовок')
					.setStyle(TextInputStyle.Short);
				const embedDescriptionInput = new TextInputBuilder()
					.setCustomId('embedDescriptionInput')
					.setLabel('Введіть код')
					.setStyle(TextInputStyle.Paragraph);
				const embedFooterInput = new TextInputBuilder()
					.setCustomId('embedFooterInput')
					.setLabel('Введіть теги')
					.setStyle(TextInputStyle.Short);
				const firstRow = new ActionRowBuilder().addComponents(embedColorInput);
				const secondRow = new ActionRowBuilder().addComponents(embedCodeTypeInput);
				const thirdRow = new ActionRowBuilder().addComponents(embedTitleInput);
	    		const fourthRow = new ActionRowBuilder().addComponents(embedDescriptionInput);
				const fifthRow = new ActionRowBuilder().addComponents(embedFooterInput);
				modal.addComponents(firstRow, secondRow, thirdRow, fourthRow, fifthRow);
				await interaction.showModal(modal);
			}
			break;
	}
});

client.on(Events.InteractionCreate, async interaction => {
	if (!interaction.isModalSubmit()) return;
	switch (interaction.customId) {
		case 'profile':
			await interaction.reply({
				content: `Username: ${interaction.fields.getTextInputValue('name')}, About: ${interaction.fields.getTextInputValue('about')}`
			});
			break;
		case 'publishCode':
			{
				const codeDescription = interaction.fields.getTextInputValue('embedDescriptionInput')
				const codeType = interaction.fields.getTextInputValue('embedCodeTypeInput')
				const publishCodeEmbed = new EmbedBuilder()
					.setAuthor({ name: interaction.user.username, iconURL: 'https://i.imgur.com/AfFp7pu.png', url: 'https://discord.js.org' })
					.setColor(Number('0x' + interaction.fields.getTextInputValue('embedColorInput')))
					.setTitle(interaction.fields.getTextInputValue('embedTitleInput'))
					.setDescription(`\`\`\`${codeType}\n${codeDescription}\n\`\`\``)
					.setFooter({
						text: interaction.fields.getTextInputValue('embedFooterInput'),
					});
				const webhookId = process.env.GUILD_USEFUL_CODE_WEBHOOK_ID;
				const webhookToken = process.env.GUILD_USEFUL_CODE_WEBHOOK_TOKEN;
				await new WebhookClient({
					id: webhookId,
					token: webhookToken,
				}).send({
					embeds: [
						publishCodeEmbed
					],
				});
				await interaction.reply({
					content: '✅ Успіх',
					ephemeral: true,
				});
			}
			break;
		default:
			console.log(`Unknown modal ID: '${interaction.customId}'`);
	}
});

// Login client
client.login(process.env.DISCORD_BOT_TOKEN);
