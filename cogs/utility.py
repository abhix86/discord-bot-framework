from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # example
    @commands.command() 
    async def working(self, ctx):
        await ctx.send("This cog is working!")

async def setup(bot):
    await bot.add_cog(Utility(bot))
