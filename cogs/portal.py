from imports import *
from utils import utils

class Portal(commands.Cog):
	def __init__(self, bot):
		print("\"Portal\" cog loaded.")
		self.bot = bot
		self.config = default.get("./config.json")
		
	@commands.Cog.listener()
	async def on_message(self, message):
		senarc_sc_webhook = utils.get_env("SENARC_SC")
		orion_sc_webhook = utils.get_env("ORION_SC")
		mittens_sc_webhook = utils.get_env("MITTENS_SC")
		secure_sc_webhook = utils.get_env("SECURE_SC")
		mta_sc_webhook = utils.get_env("MTA_SC")

		if message.channel.id == utils.get_env("SENARC_SC_ID"):
			...

		elif message.channel.id == utils.get_env("ORION_SC_ID"):
			...

		elif message.channel.id == utils.get_env("MITTENS_SC_ID"):
			...

def setup(bot):
	bot.add_cog(Portal(bot))