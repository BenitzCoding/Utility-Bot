from imports import *

class Training(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")
		self.actions = []
		self.strikes = []

	@commands.command(command_message=False, guild_whitelist=[886543799843688498], slash_interaction=True, brief="Create the correct moderation action for the training.")
	@commands.has_permissions(administrator=True)
	async def modaction(self, ctx, action):
		if action.lower() == "mute" or action.lower() == "warn" or action.lower() == "ban":
			self.actions.append(action.lower())
			await ctx.send(f"{self.config.success} Added \"{action}\" to possible moderation actions.", ephemeral=True)

		else:
			await ctx.send(f"{self.config.forbidden} That is not a valid moderation action.")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Warns a user in training.")
	async def warn(self, ctx, user, *, message=None):
		if "warn" not in self.actions:
			self.strikes.append("Wrong moderation action.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

		elif message == None:
			self.strikes.insert({ "id" "reason": "No valid reasoning."})
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			await ctx.send(f"{self.config.success} Warned {user} for `{message}`")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Mute a user in training.")
	async def mute(self, ctx, user, *, message=None):
		if "mute" not in self.actions:
			self.strikes.append("Wrong moderation action.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

		elif message == None:
			self.strikes.append("No valid reasoning.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			await ctx.send(f"{self.config.success} Muted {user} for `{message}`")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Warns a user in training.")
	async def ban(self, ctx, user, *, message=None):
		if "ban" not in self.actions:
			self.strikes.append("Wrong moderation action.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, that's not the right moderation action.")

		elif message == None:
			self.strikes.append("No valid reasoning.")
			await ctx.send(f"{self.config.forbidden} Strike {len(self.strikes)}, you always provide valid reasoning while moderating.")

		else:
			await ctx.send(f"{self.config.success} Banned {user} for `{message}`")

	@commands.command(slash_interaction=True, guild_whitelist=[886543799843688498], brief="Shows the user's strikes.")
	async def strikes(self, ctx):
		await ctx.send(f"{len(self.strikes)} Strikes recorded.")

def setup(bot):
	bot.add_cog(Training(bot))