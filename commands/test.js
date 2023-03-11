const { SlashCommandBuilder, ActionRowBuilder, Events, ModalBuilder, TextInputBuilder, TextInputStyle } = require('discord.js');

const modal = new ModalBuilder()
    .setTitle('Title')
    .setCustomId('modal');

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

module.exports = {
    data: new SlashCommandBuilder()
        .setName('test')
        .setDescription('test'),
    async execute(interaction) {
        await interaction.showModal(modal);

        interaction.client.on(Events.InteractionCreate, async interaction => {
            if (!interaction.isModalSubmit()) return;
            const userName = interaction.fields.getTextInputValue('name');
            const userAbout = interaction.fields.getTextInputValue('about');
            await interaction.reply(`Username: ${userName}, About: ${userAbout}`);
        });
    }
};
