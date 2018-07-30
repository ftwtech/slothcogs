from .ayyy import Ayyy
from redbot.core import data_manager

def setup(bot):
    n = Ayyy(bot)
    data_manager.load_bundled_data(n, __file__)
    bot.add_cog(n)