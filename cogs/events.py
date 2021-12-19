import cool_utils
import discord
import requests
import os
from imports import *
from utilities import default
from pymongo import MongoClient
from discord.ext import commands
from discord.ui import Button, button, View
from discord import ButtonStyle, Interaction


class Events(commands.Cog):
	def __init__(self, senarc):
		self.senarc = senarc
		self.config = default.get("./config.json")

	@commands.Cog.listener('on_message')
	async def chrismas_special(self, message):
		if message.guild == None and message.lower() == "confirm":
			data = {
				"id": message.author.id,
				"type": "Confirmed",
				"auth": ""
			}
			res = requests.post("https://api.senarc.org/confirm-contest", json=data)
			if res.status_code == 400:
				return await message.author.send("Your coding contest project has already been processed.")
			elif res.status_code == 401:
				return
			else:
				return await message.author.send("Marked as `confirmed`!")

		elif message.guild == None and message.lower() == "cancel":
			data = {
				"id": message.author.id,
				"type": "Cancelled",
				"auth": ""
			}
			res = requests.post("https://api.senarc.org/confirm-contest", json=data)
			if res.status_code == 400:
				return await message.author.send("Your coding contest project has already been processed.")
			elif res.status_code == 401:
				return
			else:
				return await message.author.send("Marked as `cancelled`!")

		else:
			return

def setup(bot):
	bot.add_cog(Events(bot))
