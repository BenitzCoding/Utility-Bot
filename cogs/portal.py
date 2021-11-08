from imports import *
from utils import utils, default

class Portal(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")

	async def distribute_message(self, message, server):
		if server == "Senarc":

			senarc_srv = discord.utils.get(self.bot.guilds, id=886543799843688498)
			orion_srv = discord.utils.get(self.bot.guilds, id=881095332434440224)
			mta_srv = discord.utils.get(self.bot.guilds, id=849907771871854631)
			secure_srv = discord.utils.get(self.bot.guilds, id=864451138514452481)
			mittens_srv = discord.utils.get(self.bot.guilds, id=780278916173791232)

			for channel in orion_srv.text_channels:
				if channel.id == int(891555218939080714):
					orion = channel
					orion_webhook = discord.utils.get(await orion.webhooks(), name="Senarc Network Integration")
					await orion_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in mittens_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

			for channel in mta_srv.text_channels:
				if channel.id == int(891555527866331146):
					mta = channel
					mta_webhook = discord.utils.get(await mta.webhooks(), name="Senarc Network Integration")
					await mta_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in secure_srv.text_channels:
				if channel.id == int(891555715406262284):
					secure = channel
					secure_webhook = discord.utils.get(await secure.webhooks(), name="Senarc Network Integration")
					await secure_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in orion_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

		if server == "Orion":

			senarc_srv = discord.utils.get(self.bot.guilds, id=886543799843688498)
			mta_srv = discord.utils.get(self.bot.guilds, id=849907771871854631)
			secure_srv = discord.utils.get(self.bot.guilds, id=864451138514452481)
			mittens_srv = discord.utils.get(self.bot.guilds, id=780278916173791232)


			for channel in mta_srv.text_channels:
				if channel.id == int(891555527866331146):
					mta = channel
					mta_webhook = discord.utils.get(await mta.webhooks(), name="Senarc Network Integration")
					await mta_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in mittens_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

			for channel in secure_srv.text_channels:
				if channel.id == int(891555715406262284):
					secure = channel
					secure_webhook = discord.utils.get(await secure.webhooks(), name="Senarc Network Integration")
					await secure_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in senarc_srv.text_channels:
				if channel.id == int(890089098134585415):
					senarc = channel
					senarc_webhook = discord.utils.get(await senarc.webhooks(), name="Senarc Network Integration")
					await senarc_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

		if server == "Mittens":

			senarc_srv = discord.utils.get(self.bot.guilds, id=886543799843688498)
			orion_srv = discord.utils.get(self.bot.guilds, id=881095332434440224)
			mta_srv = discord.utils.get(self.bot.guilds, id=849907771871854631)
			secure_srv = discord.utils.get(self.bot.guilds, id=864451138514452481)
			mittens_srv = discord.utils.get(self.bot.guilds, id=780278916173791232)

			for channel in orion_srv.text_channels:
				if channel.id == int(891555218939080714):
					orion = channel
					orion_webhook = discord.utils.get(await orion.webhooks(), name="Senarc Network Integration")
					await orion_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in mta_srv.text_channels:
				if channel.id == int(891555527866331146):
					mta = channel
					mta_webhook = discord.utils.get(await mta.webhooks(), name="Senarc Network Integration")
					await mta_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in secure_srv.text_channels:
				if channel.id == int(891555715406262284):
					secure = channel
					secure_webhook = discord.utils.get(await secure.webhooks(), name="Senarc Network Integration")
					await secure_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in senarc_srv.text_channels:
				if channel.id == int(890089098134585415):
					senarc = channel
					senarc_webhook = discord.utils.get(await senarc.webhooks(), name="Senarc Network Integration")
					await senarc_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

		if server == "Secure":

			senarc_srv = discord.utils.get(self.bot.guilds, id=886543799843688498)
			orion_srv = discord.utils.get(self.bot.guilds, id=881095332434440224)
			mta_srv = discord.utils.get(self.bot.guilds, id=849907771871854631)
			secure_srv = discord.utils.get(self.bot.guilds, id=864451138514452481)
			mittens_srv = discord.utils.get(self.bot.guilds, id=780278916173791232)

			for channel in orion_srv.text_channels:
				if channel.id == int(891555218939080714):
					orion = channel
					orion_webhook = discord.utils.get(await orion.webhooks(), name="Senarc Network Integration")
					await orion_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in mta_srv.text_channels:
				if channel.id == int(891555527866331146):
					mta = channel
					mta_webhook = discord.utils.get(await mta.webhooks(), name="Senarc Network Integration")
					await mta_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in orion_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in mittens_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

			for channel in senarc_srv.text_channels:
				if channel.id == int(890089098134585415):
					senarc = channel
					senarc_webhook = discord.utils.get(await senarc.webhooks(), name="Senarc Network Integration")
					await senarc_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

		if server == "MTA":

			senarc_srv = discord.utils.get(self.bot.guilds, id=886543799843688498)
			orion_srv = discord.utils.get(self.bot.guilds, id=881095332434440224)
			mta_srv = discord.utils.get(self.bot.guilds, id=849907771871854631)
			secure_srv = discord.utils.get(self.bot.guilds, id=864451138514452481)
			mittens_srv = discord.utils.get(self.bot.guilds, id=780278916173791232)

			for channel in orion_srv.text_channels:
				if channel.id == int(891555218939080714):
					orion = channel
					orion_webhook = discord.utils.get(await orion.webhooks(), name="Senarc Network Integration")
					await orion_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in secure_srv.text_channels:
				if channel.id == int(891555715406262284):
					secure = channel
					secure_webhook = discord.utils.get(await secure.webhooks(), name="Senarc Network Integration")
					await secure_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in mittens_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in orion_srv.text_channels:
				if channel.id == int(891555957019119626):
					mittens = channel
					mittens_webhook = discord.utils.get(await mittens.webhooks(), name="Senarc Network Integration")
					await mittens_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

			for channel in senarc_srv.text_channels:
				if channel.id == int(890089098134585415):
					senarc = channel
					senarc_webhook = discord.utils.get(await senarc.webhooks(), name="Senarc Network Integration")
					await senarc_webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar)
					break

				else:
					continue

	@commands.Cog.listener()
	async def on_message(self, message):

		if message.author.bot:
			return

		if message.channel.id == int(890089098134585415):
			await self.distribute_message(message, "Senarc")

		elif message.channel.id == int(891555218939080714):
			await self.distribute_message(message, "Orion")

		elif message.channel.id == int(891555957019119626):
			await self.distribute_message(message, "Mittens")

		elif message.channel.id == int(891555715406262284):
			await self.distribute_message(message, "Secure")

		elif message.channel.id == int(891555527866331146):
			await self.distribute_message(message, "MTA")

def setup(bot):
	bot.add_cog(Portal(bot))
