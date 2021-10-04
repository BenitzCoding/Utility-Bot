from imports import *

class Developers(commands.Cog):
    def __init__(self, senarc):
        self.senarc = senarc
        self.config = default.get("./config.json")
        
    """Not Complete"""

def setup(senarc):
    senarc.add_cog(Developers(senarc))