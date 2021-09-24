from imports import *

class API_Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("./config.json")

	@commands.command(description="Finds a MTA Certificate.", aliases=["cert", "mta", "mod-cert"])
	async def certificate(self, ctx, method=None, token=None):
		BASE_API = "https://api.senarc.org/mta/v1/validate/"
		api_url = BASE_API + method + "/" + token

		if method == None:
			embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
			embed.set_author(name="MTA Validation", icon_url=ctx.author.avatar_url)
			embed.add_field("Methods:", value=f"{self.config.arrow} ID `n!certificate id <id>`\n{self.config.arrow} Guild Certificate Token `n!certificate guild <token>`\n{self.config.arrow} User Certificate Token `n!certificate user <token>`")
			embed.set_footer(text="Numix", icon_url=self.config.logo)
			return await ctx.send(embed=embed)

		elif token == None:
			embed = discord.Embed(timestamp=ctx.message.created_at, description="Please provide a ID/Token to search.", colour=242424)
			embed.set_author(name="MTA Validation", icon_url=ctx.author.avatar_url)
			embed.set_footer(text="Numix", icon_url=self.config.logo)
			return await ctx.send(embed=embed)

		elif method == "id":
			try:
				res = requests.get(api_url)
				if res.json() == {"found": False}:
					return await ctx.send(f"{self.config.forbidden} No Certificate with that ID.")

				elif res.json()['type'] == "Guild":
					json = res.json()
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.avatar_url)
					embed.add_field(name="Token:", value=f"{self.config.arrow} `{json['token']}`")
					embed.add_field(name="Type:", value=f"{self.config.arrow} `{json['type']}`")
					embed.add_field(name="ID:", value=f"{self.config.arrow} `{json['_id']}`")
					embed.add_field(name="Owner:", value=f"{self.config.arrow} {json['owner']}(`{json['owner-id']}`)")
					embed.add_field(name="Name:", value=f"{self.config.arrow} {json['name']}")
					embed.add_field(name="Status:", value=f"{self.config.arrow} `{json['status']}`")
					embed.set_footer(text="Numix", icon_url=self.config.logo)
					return await ctx.send(embed=embed)

				elif res.json()['type'] == "User":
					json = res.json()
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.avatar_url)
					embed.add_field(name="Token:", value=f"{self.config.arrow} `{json['token']}`")
					embed.add_field(name="Type:", value=f"{self.config.arrow} `{json['type']}`")
					embed.add_field(name="User:", value=f"{self.config.arrow} {json['discord']}(`{json['_id']}`)")
					embed.add_field(name="Registered Under Server:", value=f"{self.config.arrow} {json['srv-registered']}")
					embed.add_field(name="Server ID:", value=f"{self.config.arrow} {json['srv-id']}")
					embed.add_field(name="Status:", value=f"{self.config.arrow} `{json['status']}`")
					embed.set_footer(text="Numix", icon_url=self.config.logo)
					return await ctx.send(embed=embed)

			except:
				return await ctx.send(f"{self.config.forbidden} The API is currently Down.")

		elif method == "guild":
			try:
				res = requests.get(api_url)
				json = res.json()
				if res.json() == {"found": False}:
					return await ctx.send(f"{self.config.forbidden} No Certificate with that Token.")

				else:
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.add_field(name="Token:", value=f"{self.config.arrow} `{json['token']}`")
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.avatar_url)
					embed.add_field(name="ID:", value=f"{self.config.arrow} `{json['_id']}`")
					embed.add_field(name="Type:", value=f"{self.config.arrow} `{json['type']}`")
					embed.add_field(name="Owner:", value=f"{self.config.arrow} {json['owner']}(`{json['owner-id']}`)")
					embed.add_field(name="Name:", value=f"{self.config.arrow} {json['name']}")
					embed.add_field(name="Status:", value=f"{self.config.arrow} `{json['status']}`")
					embed.set_footer(text="Numix", icon_url=self.config.logo)
					return await ctx.send(embed=embed)

			except:
				return await ctx.send(f"{self.config.forbidden} The API is currently Down.")

		elif method == "user":
			try:
				res = requests.get(api_url)
				json = res.json()
				if res.json() == {"found": False}:
					return await ctx.send(f"{self.config.forbidden} No Certificate with that Token.")

				else:
					embed = discord.Embed(timestamp=ctx.message.created_at, colour=242424)
					embed.set_author(name="MTA Certificate Information", icon_url=ctx.author.avatar_url)
					embed.add_field(name="Token:", value=f"{self.config.arrow} `{json['token']}`")
					embed.add_field(name="Type:", value=f"{self.config.arrow} `{json['type']}`")
					embed.add_field(name="User:", value=f"{self.config.arrow} {json['discord']}(`{json['_id']}`)")
					embed.add_field(name="Registered Under Server:", value=f"{self.config.arrow} {json['srv-registered']}")
					embed.add_field(name="Server ID:", value=f"{self.config.arrow} {json['srv-id']}")
					embed.add_field(name="Status:", value=f"{self.config.arrow} `{json['status']}`")
					embed.set_footer(text="Numix", icon_url=self.config.logo)
					return await ctx.send(embed=embed)
			except:
				return await ctx.send(f"{self.config.forbidden} The API is currently Down.")
			
		else:
			await ctx.send(f"{self.config.forbidden} Invalid validation method.")