from imports import *
from .utils.default import get

class Training(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = get("./config.json")
		self.actions = []
		self.strikes = []

	@commands.command(command_message=False, guild_whitelist=[886543799843688498], slash_interaction=True, brief="Create the correct moderation action for the training.")
	@commands.has_permissions(administrator=True)
	async def modaction(self, ctx, action):
		if action.lower() == "mute" or action.lower() == "warn" or action.lower() == "ban":
			self.actions.append(action.lower())
			await ctx.send(f"{self.config.success} Added \"{action}\" to possible moderation actions.", ephemeral=True)

		else:
			await ctx.send(f"{self.config.forbidden} That is not a valid moderation action.", ephemeral=True)

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Warns a user in training.")
	async def warn(self, ctx, user, *, message=None):
		if "warn" in self.actions:
			await ctx.send(f"{self.config.success} Warned {user} for `{message}`")
			self.actions.pop("warn")

		elif message == None:
			self.strikes.append("No valid reasoning.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Mute a user in training.")
	async def mute(self, ctx, user, *, message=None):
		if "mute" in self.actions:
			await ctx.send(f"{self.config.success} Muted {user} for `{message}`")
			self.actions.pop("mute")

		elif message == None:
			self.strikes.append("No valid reasoning.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Warns a user in training.")
	async def ban(self, ctx, user, *, message=None):
		if "ban" in self.actions:
			await ctx.send(f"{self.config.success} Banned {user} for `{message}`")
			self.actions.pop("ban")

		elif message == None:
			self.strikes.append("No valid reasoning.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			self.strikes.append("Wrong moderation action.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Shows the user's strikes.")
	async def strikes(self, ctx):
		await ctx.send(f"{len(self.strikes)} Strikes recorded.")

def setup(bot):
	bot.add_cog(Training(bot))
