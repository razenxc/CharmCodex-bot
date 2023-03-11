const { Events } = require('discord.js');

module.exports = {
	name: Events.ClientReady,
	once: true,
	execute(client) {
		console.log(`Залогінений як ${client.user.tag}!`);
	    client.user.setPresence({ activities: [{ name: `Visual Studio Code` }] });
	},
};