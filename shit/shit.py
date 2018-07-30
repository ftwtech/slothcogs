import discord
import glob
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from random import randint, choice
from redbot.core.data_manager import bundled_data_path

class Shit:
    """Shitpost"""

    def __init__(self, bot):
        self.bot = bot
        default_guild = {"shit":False}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        author = message.author
        randomInt = randint(0, 150)
        if message.author.bot:
            return
        if randomInt == 1:
            if await self.config.guild(guild).shit():
                directory = str(bundled_data_path(self))
                files = glob.glob(directory + "/*")
                file = discord.File(choice(files))
                await channel.send(file=file)

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def shit(self, ctx):
        """on/off """
        guild = ctx.message.guild
        if not await self.config.guild(guild).shit():
            await self.config.guild(guild).shit.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).shit.set(False)
            await ctx.send("off")
