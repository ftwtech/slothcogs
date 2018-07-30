from .shit import Shit
from redbot.core import data_manager

def setup(bot):
    n = Shit(bot)
    data_manager.load_bundled_data(n, __file__)
    bot.add_cog(n)