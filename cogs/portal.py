from imports import *
from utils import utils

class Portal(commands.Cog):
	def __init__(self, bot):
		print("\"Portal\" cog loaded.")
		self.bot = bot
		self.config = default.get("./config.json")

	async def distribute_message(self, message, server):
		if server == "Senarc":
			orion = discord.utils.get(self.bot.channels, int(utils.get_env("ORION_SC_ID")))
			orion_webhook = discord.utils.get(orion, name="Senarc Network Integration")
			mittens = discord.utils.get(self.bot.channels, int(utils.get_env("MITTENS_SC_ID")))
			mittens_webhook = discord.utils.get(mittens, name="Senarc Network Integration")
			secure = discord.utils.get(self.bot.channels, int(utils.get_env("SECURE_SC_ID")))
			secure_webhook = discord.utils.get(secure, name="Senarc Network Integration")
			mta = discord.utils.get(self.bot.channels, int(utils.get_env("MTA_SC_ID")))
			mta_webhook = discord.utils.get(mta, name="Senarc Network Integration")

			await orion_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mittens_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await secure_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mta_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)

		if server == "Orion":
			senarc = discord.utils.get(self.bot.channels, int(utils.get_env("SENARC_SC_ID")))
			senarc_webhook = discord.utils.get(senarc, name="Senarc Network Integration")
			mittens = discord.utils.get(self.bot.channels, int(utils.get_env("MITTENS_SC_ID")))
			mittens_webhook = discord.utils.get(mittens, name="Senarc Network Integration")
			secure = discord.utils.get(self.bot.channels, int(utils.get_env("SECURE_SC_ID")))
			secure_webhook = discord.utils.get(secure, name="Senarc Network Integration")
			mta = discord.utils.get(self.bot.channels, int(utils.get_env("MTA_SC_ID")))
			mta_webhook = discord.utils.get(mta, name="Senarc Network Integration")

			await senarc_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mittens_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await secure_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mta_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)

		if server == "Mittens":
			orion = discord.utils.get(self.bot.channels, int(utils.get_env("ORION_SC_ID")))
			orion_webhook = discord.utils.get(orion, name="Senarc Network Integration")
			senarc = discord.utils.get(self.bot.channels, int(utils.get_env("SENARC_SC_ID")))
			senarc_webhook = discord.utils.get(senarc, name="Senarc Network Integration")
			secure = discord.utils.get(self.bot.channels, int(utils.get_env("SECURE_SC_ID")))
			secure_webhook = discord.utils.get(secure, name="Senarc Network Integration")
			mta = discord.utils.get(self.bot.channels, int(utils.get_env("MTA_SC_ID")))
			mta_webhook = discord.utils.get(mta, name="Senarc Network Integration")

			await orion_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await senarc_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await secure_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mta_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)

		if server == "Secure":
			orion = discord.utils.get(self.bot.channels, int(utils.get_env("ORION_SC_ID")))
			orion_webhook = discord.utils.get(orion, name="Senarc Network Integration")
			mittens = discord.utils.get(self.bot.channels, int(utils.get_env("MITTENS_SC_ID")))
			mittens_webhook = discord.utils.get(mittens, name="Senarc Network Integration")
			senarc = discord.utils.get(self.bot.channels, int(utils.get_env("SENARC_SC_ID")))
			senarc_webhook = discord.utils.get(senarc, name="Senarc Network Integration")
			mta = discord.utils.get(self.bot.channels, int(utils.get_env("MTA_SC_ID")))
			mta_webhook = discord.utils.get(mta, name="Senarc Network Integration")

			await orion_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mittens_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await senarc_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mta_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)

		if server == "MTA":
			orion = discord.utils.get(self.bot.channels, int(utils.get_env("ORION_SC_ID")))
			orion_webhook = discord.utils.get(orion, name="Senarc Network Integration")
			mittens = discord.utils.get(self.bot.channels, int(utils.get_env("MITTENS_SC_ID")))
			mittens_webhook = discord.utils.get(mittens, name="Senarc Network Integration")
			secure = discord.utils.get(self.bot.channels, int(utils.get_env("SECURE_SC_ID")))
			secure_webhook = discord.utils.get(secure, name="Senarc Network Integration")
			senarc = discord.utils.get(self.bot.channels, int(utils.get_env("SENARC_SC_ID")))
			senarc_webhook = discord.utils.get(senarc, name="Senarc Network Integration")

			await orion_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await mittens_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await secure_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
			await senarc_webhook.send(message, username=message.author.name, avatar_url=message.author.avatar_url)
		
	@commands.Cog.listener()
	async def on_message(self, message):

		if message.channel.id == int(utils.get_env("SENARC_SC_ID")):
			await self.distribute_message(message, "Senarc")

		elif message.channel.id == int(utils.get_env("ORION_SC_ID")):
			await self.distribute_message(message, "Orion")

		elif message.channel.id == int(utils.get_env("MITTENS_SC_ID")):
			await self.distribute_message(message, "Mittens")

		elif message.channel.id == int(utils.get_env("SECURE_SC_ID")):
			await self.distribute_message(message, "Secure")

		elif message.channel.id == int(utils.get_env("MTA_SC_ID")):
			await self.distribute_message(message, "MTA")

def setup(bot):
	bot.add_cog(Portal(bot))