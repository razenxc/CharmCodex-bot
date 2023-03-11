require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { Client, Collection, Events, GatewayIntentBits, ClientPresence } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.commands = new Collection();

const eventsPath = path.join(__dirname, 'events');
const commandsPath = path.join(__dirname, 'commands');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));

for (const file of eventFiles) {
	const filePath = path.join(eventsPath, file);
	const event = require(filePath);
	if (event.once) {
		client.once(event.name, (...args) => event.execute(...args));
	} else {
		client.on(event.name, (...args) => event.execute(...args));
	}
}

// Interaction Modal Submit
client.on(Events.InteractionCreate, async interaction => {
	if(interaction.isModalSubmit()) return;
	if(interaction.customId === 'modal') {
		await interaction.reply({ content: "Form is submitted", ephemeral: true })
	}

	const name = interaction.fields.getTextInputValue('name');
	const about = interaction.fields.getTextInputValue('about');

	console.log(`Name is ${name} and About is: ${about}`)
})

client.login(process.env.DISCORD_BOT_TOKEN);