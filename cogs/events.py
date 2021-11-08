from imports import *
from .utils.default import get

class Events(commands.Cog):
    def __init__(self, senarc):
        self.senarc = senarc
        self.config = get("./config.json")

def setup(bot):
    bot.add_cog(Events(bot))
