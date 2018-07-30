import discord
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from redbot.core.data_manager import bundled_data_path

class Ayyy:
    """Ayyy lmao"""

    def __init__(self, bot):
        self.bot = bot
        default_guild = {"ayyy":False}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        msg = message.content
        channel = message.channel
        if "ayyy" in msg.lower():
            if await self.config.guild(guild).ayyy():
                file = discord.File(str(bundled_data_path(self)) + "/lmao.jpg")
                await channel.send(file=file)

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def ayyy(self, ctx):
        """on/off"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).ayyy():
            await self.config.guild(guild).ayyy.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).ayyy.set(False)
            await ctx.send("off")