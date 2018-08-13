from .addshit import AddShit

def setup(bot):
    n = AddShit(bot)
    bot.add_cog(n)