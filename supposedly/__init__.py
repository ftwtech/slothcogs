from .supposedly import Supposedly

def setup(bot):
    n = Supposedly(bot)
    bot.add_cog(n)