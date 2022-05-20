import aiohttp

from imports import *
from utilities import default

class API_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")
		self.API_BASE = "https://api.senarc.org"

	@commands.command(description="Generates a API Token.")
	async def token(self, ctx, option, setting = None):
		if option == "firewall":
			if setting == None:
				return await ctx.send(f":no_entry_sign: You need to specify a setting for the firewall.")
			if setting == "enable":
				session = aiohttp.ClientSession()
				url = self.API_BASE + "/token/modify"
				headers = {
					"Authorisation": self.config.api_token
				}
				data = {
					"firewall": True
				}
				response = await session.post(url, headers=headers, json=data)
				return await ctx.send(f":ballot_box_with_check: Firewall is now **enabled**.")
			elif setting == "disable":
				self.config["firewall"] = False
				default.save("./config.json", self.config)
				return await ctx.send(f":ballot_box_with_check: Firewall is now **disabled**.")
			else:
				return await ctx.send(f":no_entry_sign: You need to specify a valid setting for the firewall.")

		if option == "generate":
			session = aiohttp.ClientSession()
			url = self.API_BASE + "/token/generate"
			headers = {
				"Authorisation": self.config.api_token
			}
			data = {
				"discord_id": ctx.author.id,
				"username": ctx.author.name,
				
			}
			response = await session.post(url, headers=headers)
			return await ctx.send(f":ballot_box_with_check: Your API Token has been generated.\n{response.json()['token']}")

	@commands.command(description="Finds a MTA Certificate.", aliases=["cert", "mta", "mod-cert"])
	async def certificate(self, ctx, method=None, token=None):
		BASE_API = "https://api.senarc.org/mta/v1/validate/"
		api_url = BASE_API + method + "/" + token

		if method == None:
			embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
			embed.set_author(name="MTA Validation", icon_url=ctx.author.display_avatar)
			embed.add_field("Methods:", value=f"ID `n!certificate id <id>`\nGuild Certificate Token `n!certificate guild <token>`\nUser Certificate Token `n!certificate user <token>`")
			return await ctx.send(embed=embed, ephemeral = True)

		elif token == None:
			embed = discord.Embed(timestamp=ctx.message.created_at, description="Please provide a ID/Token to search.", colour=242424)
			embed.set_author(name="MTA Validation", icon_url=ctx.author.display_avatar)
			return await ctx.send(embed=embed, ephemeral = True)

		elif method == "id":
			try:
				res = requests.get(api_url)
				if res.json() == {"found": False}:
					return await ctx.send(f"{self.config.forbidden} No Certificate with that ID.", ephemeral = True)

				elif res.json()['type'] == "Guild":
					json = res.json()
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.display_avatar)
					embed.add_field(name="Token:", value=f"`{json['token']}`", inline=False)
					embed.add_field(name="Type:", value=f"`{json['type']}`", inline=False)
					embed.add_field(name="ID:", value=f"`{json['_id']}`", inline=False)
					embed.add_field(name="Owner:", value=f"{json['owner']}(`{json['owner-id']}`)", inline=False)
					embed.add_field(name="Name:", value=f"{json['name']}", inline=False)
					embed.add_field(name="Status:", value=f"`{json['status']}`", inline=False)
					return await ctx.send(embed=embed)

				elif res.json()['type'] == "User":
					json = res.json()
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.display_avatar)
					embed.add_field(name="Token:", value=f"`{json['token']}`", inlin=False)
					embed.add_field(name="Type:", value=f"`{json['type']}`", inline=False)
					embed.add_field(name="User:", value=f"{json['discord']}(`{json['_id']}`)", inline=False)
					embed.add_field(name="Registered Under Server:", value=f"{json['srv-registered']}", inline=False)
					embed.add_field(name="Server ID:", value=f"{json['srv-id']}", inline=False)
					embed.add_field(name="Status:", value=f"`{json['status']}`", inline=False)
					return await ctx.send(embed=embed)

			except:
				return await ctx.send(f"{self.config.forbidden} The API is currently Down.", ephemeral = True)

		elif method == "guild":
			try:
				res = requests.get(api_url)
				json = res.json()
				if res.json() == {"found": False}:
					return await ctx.send(f"{self.config.forbidden} No Certificate with that Token.", ephemeral = True)

				else:
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.add_field(name="Token:", value=f"`{json['token']}`", inline=False)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.display_avatar)
					embed.add_field(name="ID:", value=f"`{json['_id']}`", inline=False)
					embed.add_field(name="Type:", value=f"`{json['type']}`", inline=False)
					embed.add_field(name="Owner:", value=f"{json['owner']}(`{json['owner-id']}`)", inline=False)
					embed.add_field(name="Name:", value=f"{json['name']}", inline=False)
					embed.add_field(name="Status:", value=f"`{json['status']}`", inline=False)
					return await ctx.send(embed=embed)

			except:
				return await ctx.send(f"{self.config.forbidden} The API is currently Down.", ephemeral = True)

		elif method == "user":
			try:
				res = requests.get(api_url)
				json = res.json()
				if res.json() == {"found": False}:
					return await ctx.send(f"{self.config.forbidden} No Certificate with that Token.", ephemeral = True)

				else:
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.display_avatar)
					embed.add_field(name="Token:", value=f"`{json['token']}`", inline=False)
					embed.add_field(name="Type:", value=f"`{json['type']}`", inline=False)
					embed.add_field(name="User:", value=f"{json['discord']}(`{json['_id']}`)", inline=False)
					embed.add_field(name="Registered Under Server:", value=f"{json['srv-registered']}", inline=False)
					embed.add_field(name="Server ID:", value=f"{json['srv-id']}", inline=False)
					embed.add_field(name="Status:", value=f"`{json['status']}`", inline=False)
					return await ctx.send(embed=embed)
			except:
				return await ctx.send(f"{self.config.forbidden} The API is currently Down.", ephemeral = True)

		else:
			await ctx.send(f"{self.config.forbidden} Invalid validation method.", ephemeral = True)

def setup(bot):
	bot.add_cog(API_Commands(bot))
