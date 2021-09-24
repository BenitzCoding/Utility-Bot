from imports import *
from utils import utils
from utils import default

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="s!", slash_interactions=True, intents=intents)
config = default.get("./config.json")

@bot.event
async def on_ready():
    print("Bot initialized")

@bot.command(name='e', hidden=True, aliases=["eval"])
async def _e(ctx, *, body=None):
	if ctx.author.id not in config.dev_ids:
		return await ctx.send(f"{config.forbidden} **`ERROR 401`**")
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

@bot.command(hidden=True)
@commands.is_owner()
async def restart(ctx):
	await ctx.send(f"{config.success} Performing Complete Restart on Numix.")
	os.system("ls -l; python3 main.py")
	await bot.logout()

def run():
	for file in os.listdir("./cogs"):
		try:
			if file.endswith(".py"):
				name = file[:-3]
				bot.load_extension(f"cogs.{name}")
		except Exception as e:
			print(e)
	bot.load_extension("jishaku")
	try:
		bot.run(utils.get_env("TOKEN"), reconnect=True)
	except Exception as e:
		print(e)

run()