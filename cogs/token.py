import aiohttp

from typing import Literal
from country_list import countries_for_language

from discord import Embed
from discord.ext.commands import GroupCog
from discord.app_commands import Choice, command, describe, autocomplete

from functions import validate_user, get_env

country_dict = dict(countries_for_language("en"))

def get_country_name():
	return [
		Choice(name=country_name, value=country_code)
		for country_code, country_name in country_dict.items()
	]

class Tokens(
	GroupCog,
	name = "token"
):
	def __init__(self, bot):
		self.bot = bot
		self.BASE_API = "https://api.senarc.org/token/modify"
		self.HEADER_JSON = {
			"Authorisation": get_env("API_TOKEN")
		}

	@command(
		name = "firewall",
		description = "Toggle your API Token firewall."
	)
	@describe(toggle = "Enable or Disable your API Token Firewall.")
	async def firewall(self, interaction, toggle: Literal["enable", "disable"]):
		if not await validate_user(interaction.user.id):
			return await interaction.send(":no_entry_sign: You don't have an API token linked to your account..")

		if toggle == "enable":
			async with aiohttp.ClientSession() as session:
				data = {
					"discord_id": interaction.user.id,
					"firewall": True
				}
				async with session.patch(self.BASE_API, json=data) as response:
					if response.status == 200:
						return await interaction.send(":ballot_box_with_check: Firewall is now **enabled**.")
					else:
						return await interaction.send(":no_entry_sign: There was an error while trying to enable the firewall.")

		elif toggle == "disable":
			async with aiohttp.ClientSession() as session:
				data = {
					"discord_id": interaction.user.id,
					"firewall": False
				}
				async with session.patch(self.BASE_API, json=data) as response:
					if response.status == 200:
						return await interaction.send(":ballot_box_with_check: Firewall is now **disabled**.")
					else:
						return await interaction.send(":no_entry_sign: There was an error while trying to disable the firewall.")

	@command(
		name = "generate",
		description = "Generate a new API Token."
	)
	@describe(country_code = "The country code of your internet connection.")
	@autocomplete(country_code = get_country_name())
	async def generate(self, interaction, country: str):
		if await validate_user(interaction.user.id):
			return await interaction.send(":no_entry_sign: You already have an API token linked to your account.")

		async with aiohttp.ClientSession() as session:
			data = {
				"discord_id": interaction.user.id,
				"username": interaction.user.name,
				"country_code": country
			}
			async with session.post(self.BASE_API, json = data, headers = self.HEADER_JSON) as response:
				if response.status == 200:
					data = await response.json()
					embed = Embed(
						description = f"Your API Token is: ```{data['token']}```\nIn order for you to use your token, will need to activate it in https://api.senarc.org/activate.",
						colour = 0x1ED85F
					)
					embed.set_author(
						name = "Senarc API Token",
						icon_url = self.bot.user.avatar_url
					)
					return await interaction.send(
						embed = embed,
						ephemeral = True
					)
				else:
					return await interaction.send(":no_entry_sign: There was an error while trying to generate a new API Token.")

async def setup(bot):
	await bot.add_cog(Tokens(bot))