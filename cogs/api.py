import aiohttp

from typing import Literal

from discord import Embed
from discord.ext.commands import Cog
from discord.app_commands import command, describe, guilds, autocomplete

from utilities import default

class API_Commands(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")
		self.API_BASE = "https://api.senarc.org"

	@command(
		name = "certificate",
		description = "Finds a MTA Certificate."
	)
	@describe(method = "Do you want to find certificate via token or id?")
	@describe(query = "Enter the method's finding argument. ('id' or 'token')")
	async def certificate(self, interaction, method: Literal['token', 'id'], query: str):
		BASE_API = "https://api.senarc.org/mta/v1/validate/"
		api_url = BASE_API + method + "/" + query

		if method == None:
			embed = Embed(timestamp=interaction.message.created_at, colour=242424)
			embed.set_author(
				name = "MTA Validation",
				icon_url = interaction.user.display_avatar
			)
			embed.add_field("Methods:", value = f"ID `n!certificate id <id>`\nGuild Certificate Token `n!certificate guild <token>`\nUser Certificate Token `n!certificate user <token>`")
			return await interaction.response.send_message(
				embed = embed,
				ephemeral = True
			)

		elif query == None:
			embed = Embed(timestamp=interaction.message.created_at, description="Please provide a ID/Token to search.", colour=242424)
			embed.set_author(name = "MTA Validation", icon_url = interaction.user.display_avatar)
			return await interaction.response.send_message(
				embed = embed,
				ephemeral = True
			)

		elif method == "id":
			async with aiohttp.ClientSession() as session:
				async with session.get(api_url) as resp:
					if resp.status == 200:
						data = await resp.json()
						if data['type'] == "Guild":
							embed = Embed(timestamp = interaction.message.created_at, colour = 242424)
							embed.set_author(name = "MTA Certificate Information", icon_url = interaction.user.display_avatar)
							embed.add_field(name = "Token:", value = f"`{data['token']}`", inline = False)
							embed.add_field(name = "Type:", value = f"`{data['type']}`", inline = False)
							embed.add_field(name = "ID:", value = f"`{data['_id']}`", inline = False)
							embed.add_field(name = "Owner:", value = f"{data['owner']}(`{data['owner-id']}`)", inline = False)
							embed.add_field(name = "Name:", value = f"{data['name']}", inline = False)
							embed.add_field(name = "Status:", value = f"`{data['status']}`", inline = False)
							return await interaction.response.send_message(embed=embed)

						elif data['type'] == "User":
							embed = Embed(timestamp = interaction.message.created_at, colour = 242424)
							embed.set_author(name = "MTA Certificate Information", icon_url = interaction.user.display_avatar)
							embed.add_field(name = "Token:", value = f"`{data['token']}`", inlin=False)
							embed.add_field(name = "Type:", value = f"`{data['type']}`", inline = False)
							embed.add_field(name = "User:", value = f"{data['discord']}(`{data['_id']}`)", inline = False)
							embed.add_field(name = "Registered Under Server:", value = f"{data['srv-registered']}", inline = False)
							embed.add_field(name = "Server ID:", value = f"{data['srv-id']}", inline = False)
							embed.add_field(name = "Status:", value = f"`{data['status']}`", inline = False)
							return await interaction.response.send_message(embed=embed)

						elif resp.status == 404:
							return await interaction.response.send_message(
								f"{self.config.forbidden} No certificate found with that ID.",
								ephemeral = True
							)

						elif resp.status == 500:
							return await interaction.response.send_message(
								":fire: An error occured while processing your request.",
								ephemeral = True
							)

		elif method == "guild":
			async with aiohttp.ClientSession() as session:
				async with session.get(api_url) as resp:
					if resp.status == 200:
						data = await resp.json()
						embed = Embed(timestamp = interaction.message.created_at, colour = 242424)
						embed.add_field(name = "Token:", value = f"`{data['token']}`", inline = False)
						embed.set_author(name = "MTA Certificate Information", icon_url = interaction.user.display_avatar)
						embed.add_field(name = "ID:", value = f"`{data['_id']}`", inline = False)
						embed.add_field(name = "Type:", value = f"`{data['type']}`", inline = False)
						embed.add_field(name = "Owner:", value = f"{data['owner']}(`{data['owner-id']}`)", inline = False)
						embed.add_field(name = "Name:", value = f"{data['name']}", inline = False)
						embed.add_field(name = "Status:", value = f"`{data['status']}`", inline = False)
						return await interaction.response.send_message(embed=embed)

					elif resp.status == 404:
						return await interaction.response.send_message(
							f"{self.config.forbidden} No certificate found with that ID.",
							ephemeral = True
						)

					elif resp.status == 500:
						return await interaction.response.send_message(
							":fire: An error occured while processing your request.",
							ephemeral = True
						)

		elif method == "user":
			async with aiohttp.ClientSession() as session:
				async with session.get(api_url) as resp:
					if resp.status == 200:
						data = await resp.json()
						embed = Embed(timestamp = interaction.message.created_at, colour = 242424)
						embed.set_author(name = "MTA Certificate Information", icon_url = interaction.user.display_avatar)
						embed.add_field(name = "Token:", value = f"`{data['token']}`", inline = False)
						embed.add_field(name = "Type:", value = f"`{data['type']}`", inline = False)
						embed.add_field(name = "User:", value = f"{data['discord']}(`{data['_id']}`)", inline = False)
						embed.add_field(name = "Registered Under Server:", value = f"{data['srv-registered']}", inline = False)
						embed.add_field(name = "Server ID:", value = f"{data['srv-id']}", inline = False)
						embed.add_field(name = "Status:", value = f"`{data['status']}`", inline = False)
						return await interaction.response.send_message(embed=embed)

					elif resp.status == 404:
						return await interaction.response.send_message(
							f"{self.config.forbidden} No certificate found with that ID.",
							ephemeral = True
						)

					elif resp.status == 500:
						return await interaction.response.send_message(
							":fire: An error occured while processing your request.",
							ephemeral = True
						)
		else:
			await interaction.response.send_message(f"{self.config.forbidden} Invalid validation method.", ephemeral = True)

def setup(bot):
	bot.add_cog(API_Commands(bot))
