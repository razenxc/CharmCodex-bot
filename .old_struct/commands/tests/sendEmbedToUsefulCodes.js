const { SlashCommandBuilder, EmbedBuilder } = require('discord.js');

const channelId = '1083839988447318056';

module.exports = {
    data: new SlashCommandBuilder()
        .setName('sendusefulcode')
        .setDescription('Відправляє ваш код до useful codes')
		.addStringOption(option => 
			option.setName('color')
				.setDescription('Введіть кольор в #RRGGBB')
				.setRequired(true))
        .addStringOption(option => 
            option.setName('title')
                .setDescription('Введіть заголовк')
                .setRequired(true))
		.addStringOption(option => 
			option.setName('code')
				.setDescription('Введіть код')
				.setRequired(true)),
		
			async execute(interaction) {
				const sendUsefulCodeEmd = new EmbedBuilder()
					.setAuthor({ name: interaction.user.username, iconURL: 'https://i.imgur.com/AfFp7pu.png', url: 'https://discord.js.org' })
					.setColor(interaction.options.getString('color'))
					.setTitle(interaction.options.getString('title'))
					.setDescription(interaction.options.getString('code'))
					.setFooter({ text: 'Some footer text here'});
					

				// channel.send({ embeds: [exampleEmbed] });
				await interaction.reply({ embeds: [sendUsefulCodeEmd] });
			},
};