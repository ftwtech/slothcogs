import discord
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from random import randint

class Supposedly:
    """Supposedly"""

    def __init__(self, bot):
        self.bot = bot
        default_guild = {"supposedly":False}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        author = message.author
        randomInt = randint(0, 250)
        if message.author.bot:
            return
        if randomInt == 1:
            if await self.config.guild(guild).supposedly():
                await channel.send("*Supposedly...*")

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def supposedly(self, ctx):
        """on/off"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).supposedly():
            await self.config.guild(guild).supposedly.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).supposedly.set(False)
            await ctx.send("off")