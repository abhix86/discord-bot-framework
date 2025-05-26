from discord.ext import commands
import asyncio

class Extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # example
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


async def setup(bot):
    await bot.add_cog(Extra(bot))
