from typing import Literal

from discord import Object
from discord.ext.commands import Cog
from discord.app_commands import command, describe, default_permissions, guilds

from functions import get_env
from utilities.default import get

CORE_GUILD = Object(id = get_env("TRAINING_GUILD"))

class Training(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = get("./config.json")
		self.actions = []
		self.strikes = []

	@command(
		name = "modaction",
		description="Create the correct moderation action for the training."
	)
	@describe(action = "What's the action you want to create?")
	@guilds(CORE_GUILD)
	@default_permissions(administrator=True)
	async def modaction(self, interaction, action: Literal['warn', 'mute', 'kick', 'ban']):
		if action.lower() == "mute" or action.lower() == "warn" or action.lower() == "ban" or action.lower() == "kick":
			self.actions.append(action.lower())
			await interaction.response.send_message(f"{self.config.success} Added \"{action}\" to possible moderation actions.", ephemeral = True)

		else:
			await interaction.response.send_message(f"{self.config.forbidden} That is not a valid moderation action.", ephemeral = True)

	@command(
		name = "warn",
		description = "Warns a user in training."
	)
	@describe(user = "Who do you want to warn?")
	@describe(reason = "Why do you want to take this moderation action towards them?")
	@guilds(CORE_GUILD)
	async def warn(self, interaction, user: str, reason: str = None):
		if "warn" in self.actions:
			await interaction.resonse.send_message(f"{self.config.success} Warned {user} for `{reason}`")
			self.actions.remove("warn")

		elif reason == None:
			self.strikes.append("No valid reasoning.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@command(
		name = "mute",
		description = "Mutes a user in training."
	)
	@describe(user = "Who do you want to mute?")
	@describe(reason = "Why do you want to take this moderation action towards them?")
	@guilds(CORE_GUILD)
	async def mute(self, interaction, user: str, reason: str = None):
		if "mute" in self.actions:
			await interaction.response.send_message(f"{self.config.success} Muted {user} for `{reason}`")
			self.actions.remove("mute")

		elif reason == None:
			self.strikes.append("No valid reasoning.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@command(
		name = "ban",
		description = "Bans a user in training."
	)
	@describe(user = "Who do you want to ban?")
	@describe(reason = "Why do you want to take this moderation action towards them?")
	@guilds(CORE_GUILD)
	async def ban(self, interaction, user: str, reason: str = None):
		if "ban" in self.actions:
			await interaction.response.send_message(f"{self.config.success} Banned {user} for `{reason}`")
			self.actions.remove("ban")

		elif reason == None:
			self.strikes.append("No valid reasoning.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@command(
		name = "kick",
		description = "Kicks a user in training."
	)
	@describe(user = "Who do you want to kick?")
	@describe(reason = "Why do you want to take this moderation action towards them?")
	@guilds(CORE_GUILD)
	async def kick(self, interaction, user: str, reason: str = None):
		if "ban" in self.actions:
			await interaction.response.send_message(f"{self.config.success} Kicked {user} for `{reason}`")
			self.actions.remove("kick")

		elif reason == None:
			self.strikes.append("No valid reasoning.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await interaction.response.send_message(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@command(
		name = "strikes",
		description = "Shows the user's strikes."
	)
	@guilds(CORE_GUILD)
	async def strikes(self, interaction):
		await interaction.response.send_message(f"{len(self.strikes)} Strikes recorded.")

async def setup(bot):
	await bot.add_cog(Training(bot))
