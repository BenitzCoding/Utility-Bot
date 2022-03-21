import discord

from pymongo import MongoClient
from discord.ext import commands

class Leveling(commands.Command):
	def __init__(self, bot):
		self.bot = bot
		self.MONGO = MongoClient("mongodb://Senarc:%2A%2A%2ASenarc%21%21%21@tea.ns.senarc.org:27017/senarc?authSource=admin")
		self.db = self.MONGO['Core']

	@commands.Cog.listener('on_message')
	async def update_xp(self, message):
		collection = self.db['senarc']['leveling']
		db_user = collection.find_one({"_id": message.author.id})
		user_xp = db_user["xp"]
		message_xp = len(message)
		user_level = db_user["level"]
		user_settings = db_user["settings"]
		leveling_formula = int((user_xp + message_xp) ** (1/4))

		if user_settings["disable"]:
			return
		
		if message.guild == None:
			return

		elif message.guild.id != 886543799843688498:
			return

		if message.author.id == self.bot.user.id:
			return       

		if collection.count_documents({ "_id": message.author.id }) == 0:
			payload = {
				"_id": message.author.id,
				"xp": 0,
				"level": 1,
				"settings": {
					"silence": False,
					"dm_alerts": False,
					"disable": False
				}
			}
			collection.insert_one(payload)
			return

		if leveling_formula > user_level:
			collection.update_one({
					"_id": message.author.id
				},
				{
					"$set": {
						"xp": message_xp + user_xp,
						"level": user_level + 1
				}
			})

			if (user_level + 1) == 5:
				ROLE_LEVEL_5 = discord.utils.get(message.guild.roles, id=954711256894418974)
				await message.author.add_roles(ROLE_LEVEL_5)

			elif (user_level + 1) == 10:
				ROLE_LEVEL_10 = discord.utils.get(message.guild.roles, id=954711378562805760)
				await message.author.add_roles(ROLE_LEVEL_10)

			elif (user_level + 1) == 15:
				ROLE_LEVEL_15 = discord.utils.get(message.guild.roles, id=954711574281605211)
				await message.author.add_roles(ROLE_LEVEL_15)

			elif (user_level + 1) == 50:
				ROLE_LEVEL_50 = discord.utils.get(message.guild.roles, id=954711756108869652)
				await message.author.add_roles(ROLE_LEVEL_50)

			if user_settings["silence_message"]:
				return
			elif user_settings["dm_alerts"]:
				await message.author.send(f"You've leveled up to level {user_level + 1} on **{message.guild.name}**!")
			else:
				await message.channel.send(f"{message.author.mention} You've leveled up to level {user_level + 1}!")

def setup(bot):
	bot.add_cog(Leveling(bot))