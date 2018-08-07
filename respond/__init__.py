from .respond import Respond

def setup(bot):
    n = Respond(bot)
    bot.add_cog(n)
