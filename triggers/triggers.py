import discord
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from redbot.core.data_manager import bundled_data_path

class Triggers:
    """TRIGGERS"""

    def __init__(self, bot):
        self.bot = bot
        default_guild = {"enabled":False}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        author = message.author
        if not await self.config.guild(guild).enabled():
            return
        if message.author.bot:
            return
        if "nigga" in message.content.lower():
            await channel.send("*nigger")
        if "ayyy" in message.content.lower():
            react = discord.File(str(bundled_data_path(self)) + "/lmao.jpg")
            await channel.send(file=react)

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def triggers(self, ctx):
        """on/off"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).enabled():
            await self.config.guild(guild).enabled.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).enabled.set(False)
            await ctx.send("off")