const { ActionRowBuilder, Events, ModalBuilder, TextInputBuilder, TextInputStyle, SlashCommandBuilder, EmbedBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('publishcode')
        .setDescription('Ця команда запускає процедуру створювання поста у useful codes'),
        async execute(interaction) {
            const modal = new ModalBuilder()
                .setCustomId('publishCode')
                .setTitle('Створіть публікацію для каналу useful codes');
            const embedColorInput = new TextInputBuilder()
                .setCustomId('embedColorInput')
                .setLabel("Введіть колір ембеду")
                .setMaxLength(6)
                .setMinLength(6)
                .setRequired(true)
                .setStyle(TextInputStyle.Short);
            const embedTitleInput = new TextInputBuilder()
            .setCustomId('embedTitleInput')
            .setLabel("Введіть заголовок")
            .setRequired(true)
            .setStyle(TextInputStyle.Paragraph);

            const firstActionRow = new ActionRowBuilder().addComponents(embedColorInput);
            const secondActionRow = new ActionRowBuilder().addComponents(embedTitleInput);
            modal.addComponents(firstActionRow);
            modal.addComponents(secondActionRow);

            await interaction.showModal(modal);

            const sendUsefulCodeEmd = new EmbedBuilder()
					.setAuthor({ name: interaction.user.username, iconURL: 'https://i.imgur.com/AfFp7pu.png', url: 'https://discord.js.org' })
					.setColor(interaction.fields.getTextInputValue('embedColorInput'))
					.setTitle(interaction.options.getString('title'))
					.setDescription(interaction.options.getString('code'))
					.setFooter({ text: 'Some footer text here'});
					

				// channel.send({ embeds: [exampleEmbed] });
                if (!interaction.isModalSubmit()) return;
				await interaction.reply({ embeds: [sendUsefulCodeEmd] });
        }
}