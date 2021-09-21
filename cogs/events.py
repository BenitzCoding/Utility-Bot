from imports import *

class Events(commands.Cog):
    def __init__(self, senarc):
        self.senarc = senarc
        self.config = default.get("./config.json")

    @commands.Cog.listener()
    async def on_reaction_add()