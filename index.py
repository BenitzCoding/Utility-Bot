import os
import io
import sys

import inspect
import textwrap
import traceback

from contextlib import redirect_stdout

from discord import Intents, Object, app_commands
from discord.ext.commands import Bot

from jishaku.flags import Flags

from utilities import utils, default

CORE_GUILD = Object(id = utils.get_env("CORE_GUILD"))
intents = Intents.all()

class Senarc(Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	async def start(self,*args, **kwargs):
		await super().start(*args, **kwargs)

	async def close(self):
		await super().close()

	async def setup_hook(self):
		for file in os.listdir("./cogs"):
			try:
				if file.endswith(".py"):
					name = file[:-3]
					await self.load_extension(f"cogs.{name}")
					print(f"\"{name.capitalize()}\" cog loaded.")
			except Exception as e:
				print(e)
			
		try:
			await self.load_extension("jishaku")
		except Exception as e:
			print(e)
		Flags.HIDE = True

bot = Senarc(command_prefix="s!", slash_commands=True, intents=intents)

config = default.get("./config.json")

@bot.listen("on_ready")
async def websocket_connect():
    print("Senarc Bot has established websocket connection.")

@bot.command(hidden = True, name = 'e', aliases = ["eval"])
async def _e(ctx, *, body=None):
	if ctx.author.id not in config.dev_ids:
		return await ctx.send(f"**`ERROR 401`**")
	env = {
		'ctx': ctx,
		'channel': ctx.channel,
		'author': ctx.author,
		'guild': ctx.guild,
		'message': ctx.message,
		'source': inspect.getsource
	}

	env.update(globals())

	body = cleanup_code(body)
	stdout = io.StringIO()
	err = out = None

	to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

	def paginate(text: str):
		'''Simple generator that paginates text.'''
		last = 0
		pages = []
		for curr in range(0, len(text)):
			if curr % 1980 == 0:
				pages.append(text[last:curr])
				last = curr
				appd_index = curr
		if appd_index != len(text)-1:
			pages.append(text[last:curr])
		return list(filter(lambda a: a != '', pages))

	try:
		exec(to_compile, env)
	except Exception as e:
		err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
		return await ctx.message.add_reaction('\u2049')

	func = env['func']
	try:
		with redirect_stdout(stdout):
			ret = await func()
	except Exception as e:
		value = stdout.getvalue()
		err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
	else:
		value = stdout.getvalue()
		if ret is None:
			if value:
				try:

					out = await ctx.send(f'```py\n{value}\n```')
				except:
					paginated_text = paginate(value)
					for page in paginated_text:
						if page == paginated_text[-1]:
							out = await ctx.send(f'```py\n{page}\n```')
							break
						await ctx.send(f'```py\n{page}\n```')
		else:
			bot._last_result = ret
			try:
				out = await ctx.send(f'```py\n{value}{ret}\n```')
			except:
				paginated_text = paginate(f"{value}{ret}")
				for page in paginated_text:
					if page == paginated_text[-1]:
						out = await ctx.send(f'```py\n{page}\n```')
						break
					await ctx.send(f'```py\n{page}\n```')

	if out:
		await ctx.message.add_reaction('\u2705')  # tick
	elif err:
		await ctx.message.add_reaction('\u2049')  # x
	else:
		await ctx.message.add_reaction('\u2705')

def cleanup_code(content):
	if content.startswith('```') and content.endswith('```'):
		return '\n'.join(content.split('\n')[1:-1])

	return content.strip('` \n')

def get_syntax_error(e):
	if e.text is None:
		return f'```py\n{e.__class__.__name__}: {e}\n```'
	return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

@bot.tree.command(
	name = "load",
	description = "Loads a Cog extension."
)
@app_commands.describe(extension = "The extension you'd like to load.")
@app_commands.guilds(CORE_GUILD)
async def load(interaction, *, extension: str):
	try:
		await bot.load_extension(f"cogs.{extension}")
	except Exception as e:
		return await interaction.response.send_message(default.traceback_maker(e))
	await interaction.response.send_message(f'"**{extension}**" Cog loaded')

# Unload Cog

@bot.tree.command(
	name = "unload",
	description = "Unloads a Cog extension."
)
@app_commands.describe(extension = "The extension you'd like to unload.")
@app_commands.guilds(CORE_GUILD)
async def unload(interaction, *, extension: str):
	try:
		await bot.unload_extension(f"cogs.{extension}")
	except Exception as e:
		return await interaction.response.send_message(default.traceback_maker(e))
	await interaction.response.send_message(f'"**{extension}**" Cog unloaded')

# Reload Cog

@bot.tree.command(
	name = "reload",
	description = "Reloads a Cog extension."
)
@app_commands.describe(extension = "The extension you'd like to reload.")
@app_commands.guilds(CORE_GUILD)
async def reload(interaction, *, extension: str):
	if extension == "all":
		await interaction.response.send_message("**All** Cogs are reloaded.")
		for file in os.listdir("./cogs"):
			if file.endswith(".py"):
				extension = file[:-3]
				bot.reload_extension(f"cogs.{extension}")
	try:
		await bot.reload_extension(f"cogs.{extension}")
	except Exception as e:
		return await interaction.response.send_message(default.traceback_maker(e))
	await interaction.response.send_message(f'Cog "**`{extension}`**" has been reloaded.')

@bot.tree.command(
	name = "restart",
	description = "Restarts the bot. (No furthur explanations required.)"
)
@app_commands.guilds(CORE_GUILD)
async def restart(ctx):
	await ctx.send(f"{config.success} Performing Complete Restart on Senarc Utilities.")
	os.system("ls -l; python3 main.py")
	await bot.close()

@bot.tree.command(
	name = "fetch",
	description = "Fetches updates from github."
)
@app_commands.guilds(CORE_GUILD)
async def fetch(ctx):
	os.system("ls -l; git pull")
	await ctx.send(f"{config.success} Fetched Github updates, Restarting client now...")
	os.system("ls -l; python3 index.py")
	sys.exit()

def main():
	try:
		bot.start(utils.get_env("TOKEN"), reconnect=True)
	except Exception as e:
		print(e)

main()
