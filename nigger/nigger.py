import discord
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks

class Nigger:
    """nigger"""

    def __init__(self, bot):
        self.bot = bot
        default_guild = {"nigger":False}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        msg = message.content
        channel = message.channel
        if message.author.bot:
            return
        if "nigga" in msg.lower():
            if await self.config.guild(guild).nigger():
        	    await channel.send("*nigger")

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def nigger(self, ctx):
        """on/off"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).nigger():
            await self.config.guild(guild).nigger.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).nigger.set(False)
            await ctx.send("off")