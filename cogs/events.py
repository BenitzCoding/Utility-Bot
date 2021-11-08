from imports import *
from utilities import default

class Events(commands.Cog):
    def __init__(self, senarc):
        self.senarc = senarc
        self.config = default.get("./config.json")

def setup(bot):
    bot.add_cog(Events(bot))
