import discord
from .responses import responses
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from random import randint
from random import choice

class Respond:
    """Responding to random shit"""

    def __init__(self, bot):
        self.bot = bot
        default_guild = {"enabled":False, "frequency": 250}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        author = message.author
        msg = ' '
        max = await self.config.guild(guild).frequency()
        randomInt = randint(0, max)
        if message.author.bot:
            return
        if randomInt == 1:
            if await self.config.guild(guild).enabled():
                await channel.send(msg + choice(responses))

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def respondtoggle(self, ctx):
        """on/off"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).enabled():
            await self.config.guild(guild).enabled.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).enabled.set(False)
            await ctx.send("off")

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def respondfreq(self, ctx, frequency:int=250):
        """frequency"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).enabled():
            await ctx.send("I'm not setup on this guild!")
            return
        await self.config.guild(guild).frequency.set(frequency)
        await ctx.send("Frequency set to {}.".format(frequency))