from .shitpost import Shitpost
from redbot.core import data_manager

def setup(bot):
    n = Shitpost(bot)
    data_manager.load_bundled_data(n, __file__)
    bot.add_cog(n)