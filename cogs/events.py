import cool_utils
import discord
from imports import *
from utilities import default
from pymongo import MongoClient
from discord.ext import commands
from discord.ui import Button, button, View
from discord import ButtonStyle, Interaction

class Buttons(View):
	def __init__(self):
		super().__init__()
		self.value = None
		self.author = None
		self.message_id = None

	@button(label="Confirm", style=ButtonStyle.red)
	async def confirm(self, button: Button, interaction: Interaction):
		message = await interaction.response.send_message(f"Marked you as `Confirmed`!", ephemeral=True)
		self.message_id = message.id
		self.value = True
		self.author = interaction.user
		self.stop()

	@button(label="Cancel", style=ButtonStyle.grey)
	async def cancel(self, button: Button, interaction: Interaction):
		message = await interaction.response.send_message(f"Great! Your request has been revoked!", ephemeral=True)
		self.value = False
		self.message = message
		self.author = interaction.user
		self.stop()

class Events(commands.Cog):
    def __init__(self, senarc):
        self.senarc = senarc
        self.config = default.get("./config.json")

    @commands.Cog.listener('on_message')
    async def chrismas_special(self, message):
        if message.guild == None and message.author == self.senarc.me:
            view = Buttons()
            await message.edit(view=view)
            await view.wait()
            if view.value == None:
                return await message.author.send("Request timmed out, please re-submit the request.")

            if view.value:
                requests.post("https://api.senarc.org/confirm-contest", json={ "id": message.author.id, "type": "Confirmed", "auth": self.config.auth })
                return
            
            else:
                requests.post("https://api.senarc.org/confirm-contest", json={ "id": message.author.id, "type": "Cancelled", "auth": self.config.auth })
                return

def setup(bot):
    bot.add_cog(Events(bot))
