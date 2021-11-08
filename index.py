from imports import *
from utils import utils, default
import aiohttp
import sys
from jishaku.flags import Flags

intents = discord.Intents.all()
#intents.members = True

class Senarc(commands.Bot):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

  async def start(self,*args, **kwargs):

    self.session = aiohttp.ClientSession()
    #doesn't intefer with the main bot's session as the bot uses http_session
    await super().start(*args, **kwargs)
    #super calls the discord.py start method of commands.Bot so just like bot.start which is called in bot.run.

  async def close(self):
    await self.session.close()
    await super().close()
    #closes aiohttp session

bot = Senarc(command_prefix="s!", slash_interactions=True, intents=intents)

config = default.get("./config.json")

@bot.event
async def on_ready():
    print("Bot initialized")

@bot.command(slash_interaction=True, name='e', aliases=["eval"])
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

@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, *, name: str):
	try:
		bot.load_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(default.traceback_maker(e))
	await ctx.send(f'"**{name}**" Cog loaded')

# Unload Cog

@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, *, name: str):
	try:
		bot.unload_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(default.traceback_maker(e))
	await ctx.send(f'"**{name}**" Cog unloaded')

# Reload Cog

@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx, *, name: str):
	if name == "all":
		await ctx.send("**All** Cogs are reloaded.")
		for file in os.listdir("./cogs"):
			if file.endswith(".py"):
				name = file[:-3]
				bot.reload_extension(f"cogs.{name}")
	try:
		bot.reload_extension(f"cogs.{name}")
	except Exception as e:
		return await ctx.send(default.traceback_maker(e))
	await ctx.send(f'Cog "**`{name}`**" has been reloaded.')

@bot.command(slash_interaction=True)
@commands.is_owner()
async def restart(ctx):
	await ctx.send(f"{config.success} Performing Complete Restart on Senarc Utilities.")
	os.system("ls -l; python3 main.py")
	await bot.logout()

@bot.command(slash_interaction=True)
@commands.is_owner()
async def fetch(ctx):
	os.system("ls -l; git pull Senarc main")
	await ctx.send(f"{config.success} Fetched Github updates, Restarting client now...")
	os.system("ls -l; python3 index.py")
	sys.exit()

def run():
	for file in os.listdir("./cogs"):
		try:
			if file.endswith(".py"):
				name = file[:-3]
				bot.load_extension(f"cogs.{name}")
				print(f"\"{name.capitalize()}\" cog loaded.")
		except Exception as e:
			print(e)
	try:
		# bot.load_extension("jishaku")
		null = None
	except Exception as e:
		print(e)
	Flags.HIDE = True
	try:
		bot.run(utils.get_env("TOKEN"), reconnect=True)
	except Exception as e:
		print(e)

run()
