import cool_utils
import discord
import os

from utilities import default
from datetime import datetime
from pymongo import MongoClient
from discord.ext import commands


class Events(commands.Cog):
	def __init__(self, senarc):
		self.senarc = senarc
		self.config = default.get("./config.json")

	@commands.Cog.listener('on_message')
	async def welcome_message(self, member):
		if member.guild.id != 886543799843688498:
			return
		channel = await self.senarc.fetch_channel(886543799843688501)
		embed = discord.Embed(timestamp=int(datetime.now().timestamp()), description="Have a nice stay at **Senarc**. You should read <#886752366962040843> before getting started!", colour=0x90B4F8)
		embed.set_author(name=f"Welcome {member.name}!", icon_url=member.display_avatar)

		member_count = str(len(member.guild.members))
		if member_count.endswith("1"):
			member_count = member_count + "st"

		elif member_count.endswith("2"):
			member_count = member_count + "nd"

		elif member_count.endswith("3"):
			member_count = member_count + "rd"

		else:
			member_count = member_count + "th"

		embed.set_footer(text=f"You're the {member_count} member", icon_url=member.guild.icon)
		await channel.send(embed=embed)

def setup(bot):
	bot.add_cog(Events(bot))