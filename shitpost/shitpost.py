import discord
import glob
import aiohttp
from .responses import responses
from redbot.core import Config
from redbot.core import checks
from random import randint, choice
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path

class Shitpost(getattr(commands, "Cog", object)):
    """Shitpost"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        default_guild = {"enabled":False, "frequency": 100}
        self.config = Config.get_conf(self, 18107945176)
        self.config.register_guild(**default_guild)

    async def on_message(self, message):
        guild = message.guild
        channel = message.channel
        author = message.author
        msg = ' '
        directory = str(bundled_data_path(self))
        files = glob.glob(directory + "/*")
        file = discord.File(choice(files))
        max = await self.config.guild(guild).frequency()
        randomInt = randint(0, max)
        if not await self.config.guild(guild).enabled():
            return
        if message.author.bot:
            return
        if randomInt == 0:
            await channel.send(msg + choice(responses))
        if randomInt == 1:
            await channel.send(file=file)

    @commands.group(hidden=True, pass_context=True, invoke_without_command=True)
    async def shitpost(self, ctx):
        """Shitpost for yout momma"""
        if ctx.invoked_subcommand is None:
            await ctx.send("Try adding a sub-command, you dumb homo")

    @shitpost.command(pass_context=True)
    @checks.is_owner()
    async def add(self, ctx):
        """Add an image to shitpost with"""
        channel = ctx.message.channel
        msg = ctx.message
        filename = "{}".format(msg.attachments[0].filename)
        directory = str(bundled_data_path(self))
        file_path = "{}/{}".format(str(directory), filename)
        async with self.session.get(msg.attachments[0].url) as resp:
            test = await resp.read()
            with open(file_path, "wb") as f:
                f.write(test)
        await ctx.send("added")
            
    @shitpost.command(pass_context=True)
    @checks.is_owner()
    async def toggle(self, ctx):
        """on/off"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).enabled():
            await self.config.guild(guild).enabled.set(True)
            await ctx.send("on")
        else:
            await self.config.guild(guild).enabled.set(False)
            await ctx.send("off")

    @shitpost.command(pass_context=True)
    @checks.is_owner()
    async def frequency(self, ctx, frequency:int=100):
        """frequency"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).enabled():
            await ctx.send("I'm not setup on this guild!")
            return
        await self.config.guild(guild).frequency.set(frequency)
        await ctx.send("Frequency set to {}.".format(frequency))